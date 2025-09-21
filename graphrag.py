"""
    TODO : 
        - introduce cuGRAPh in networkx
        - any other score to add in find_relevant_url method?
"""

#!/usr/bin/env python3
"""
GraphRAG System for Documentation Crawling
Optimized to work directly with hd5py format from deepcrawl.py
"""

import asyncio
import json
import numpy as np
from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass
# pip install sentence-transformers
from sentence_transformers import SentenceTransformer
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv
from collections import Counter, defaultdict
from google import genai
from google.genai import types
from deepcrawl import GraphNode , Graph

load_dotenv()

@dataclass
class Entity:
    source_urls: List[str]
    keywords: List[str]
    content_snippet: str
    depth: int
    embedding: List[float]

@dataclass
class Relationship:
    source: str
    target: str
    source_urls: List[str]
    common_keywords: List[str]
    semantic_similarity: float

class GraphRAGSystem:
    def __init__(self, graph : Graph , gemini_api_key: str, token_budget: Optional[int] = None):
        self.entities: Dict[str, Entity] = {}
        self.relationships: List[Relationship] = []
        self.knowledge_graph = nx.DiGraph()
        self.keyword_index = defaultdict(list)  # Keyword -> URLs that contain it
        self.graph = graph
        self.token_budget: Optional[int] = token_budget
        
        # Initialize models
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Initialize Gemini
        client = genai.Client(api_key=os.environ['gemini_api_key'])
        chat = client.chats.create(model='gemini-2.0-flash')
        self.llm = chat
        
    def _estimate_tokens_text(self, text: str) -> int:
        """Rough token estimator: ~1 token per 4 characters as a safe upper bound."""
        if not text:
            return 0
        # Use characters/4 to avoid underestimating for long words; clamp at >= 1 for non-empty
        return max(1, len(text) // 4)

    def _estimate_entity_tokens(self, entity: Entity) -> int:
        """Estimate tokens contributed by an entity block in the prompt."""
        url = entity.source_urls[0] if entity.source_urls else ""
        header = self._extract_entity_name(url)
        meta = ", ".join((entity.keywords or [])[:5])
        overhead = len(header) + len(url) + len(meta) + 32  # headings + labels
        return (overhead // 4) + self._estimate_tokens_text(entity.content_snippet or "")

    def _normalize_keyword(self, kw) -> str:
        """Convert keyword-like values (bytes, numpy scalars) to normalized lowercase str."""
        try:
            import numpy as _np  # local import to avoid top-level alias issues
            if isinstance(kw, (_np.bytes_, bytes)):
                kw = kw.decode('utf-8', errors='ignore')
        except Exception:
            # If numpy is not available or decode fails, fall back to str
            pass
        if isinstance(kw, bytes):
            kw = kw.decode('utf-8', errors='ignore')
        return str(kw).strip().lower()

    def load_from_kg_json(self):
        """ load knoweldge graph directly from graphNode"""
        
        
        print("🔍 Loading knowledge graph from graphNode...")
        
        
        # Normalize keywords and build keyword index
        for url, node in self.graph.nodes.items():
            normalized_keywords = []
            try:
                iterable_keywords = node.keywords or []
            except Exception:
                iterable_keywords = []
            for kw in iterable_keywords:
                if kw is None:
                    continue
                norm_kw = self._normalize_keyword(kw)
                if not norm_kw:
                    continue
                normalized_keywords.append(norm_kw)
                self.keyword_index[norm_kw].append(node.url)
            node.keywords = normalized_keywords

        # Create entities and relationships before building the NetworkX graph
        nodes_list = [self.graph.nodes[_] for _ in self.graph.nodes]
        self._create_entities_from_nodes(nodes_list)
        self._create_relationships_from_edges(self.graph.edges)

        # Now build the NetworkX graph with nodes and edges available
        self._build_networkx_graph()
        
    def _create_entities_from_nodes(self, all_nodes : List[GraphNode]):
        """Create entities from kg.json nodes"""
        print("🏗️  Creating entities from nodes...")
        
        for  node in all_nodes:
            entity = Entity(
                source_urls=[node.url],
                keywords=node.keywords,
                content_snippet=node.content,
                embedding = node.embedding ,  
                depth=node.depth,
            )
            
            self.entities[node.url] = entity
    
    def _create_relationships_from_edges(self, edges: List[Dict]):
        """Create relationships from kg.json edges"""
        print("🔗 Creating relationships from edges...")
        
        for edge in edges:
            relationship = Relationship(
                source=edge["source"],
                target=edge["target"],
                source_urls=[edge["source"], edge["target"]],
                common_keywords=edge.get("common_keywords", []),
                semantic_similarity=edge.get("semantic_similarity", 0.0)
            )
            
            self.relationships.append(relationship)
    
    def _extract_entity_name(self, url: str) -> str:
        """Extract a readable entity name from URL"""
        if url.endswith('/'):
            url = url[:-1]
        
        parts = url.split('/')
        if len(parts) >= 2:
            name = parts[-1].replace('-', ' ').replace('_', ' ').title()
            if name:
                return name
        
        return url.split('/')[-1] or "Home"
            
    def _build_networkx_graph(self):
        """Build NetworkX graph from entities and relationships"""
        print("🕸️  Building NetworkX graph...")
        
        # Add nodes
        for url, node in self.graph.nodes.items():
            self.knowledge_graph.add_node(
                url,
                keywords=node.keywords,
                depth=node.depth,
                embedding=node.embedding
            )
        
        # Add edges
        for rel in self.relationships:
            if rel.source in self.entities and rel.target in self.entities:
                self.knowledge_graph.add_edge(
                    rel.source,
                    rel.target,
                    common_keywords=rel.common_keywords,
                    semantic_similarity=rel.semantic_similarity
                )
                
    async def retrieve_and_generate(self, query: str, top_k: int = 10) -> str:
        """Enhanced query processing using both keywords and embeddings"""
        
        if self.token_budget is not None:
            print(f"[Budget] Token budget for this query: {self.token_budget} tokens")

        # Step 1: Find relevant URLs using multiple methods
        relevant_urls = await self._find_relevant_urls(query, top_k)
        
        # Step 2: Expand context using graph relationships
        expanded_context = self._expand_context_with_graph(relevant_urls)
                
        # Step 4: Generate answer using LLM
        answer = await self._generate_enhanced_answer(query, expanded_context)
        
        return answer
    
    async def _find_relevant_urls(self, query: str, top_k: int) -> List[str]:
        """Find relevant top k URLs using keyword matching and semantic similarity"""
        # Method 1: Keyword-based retrieval
        query_words = set(query.lower().split())
        keyword_scores = defaultdict(float)
        
        for word in query_words:
            if word in self.keyword_index:
                for url in self.keyword_index[word]:
                    keyword_scores[url] += 1.0
        
        # Method 2: Semantic similarity (if embeddings exist)
        similarity_scores = {}
        query_embedding = self.embedding_model.encode(query)
        
        for url, entity in self.entities.items():
            if entity.embedding is None : 
                continue
            
            # Convert entity embedding to numpy array if needed
            entity_embedding = np.array(entity.embedding, dtype=np.float32)
            
            # Ensure both embeddings are 1D vectors for cosine similarity
            if query_embedding.ndim > 1:
                query_embedding = query_embedding.flatten()
            if entity_embedding.ndim > 1:
                entity_embedding = entity_embedding.flatten()
            
            # Calculate cosine similarity between 1D vectors
            similarity = np.dot(query_embedding, entity_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(entity_embedding)
            )
            similarity_scores[url] = similarity
    
        # Combine scores
        combined_scores = {}
        all_urls = set(keyword_scores.keys()) | set(similarity_scores.keys())
        
        for url in all_urls:
            score = (
                keyword_scores.get(url, 0) * 2.0 +  # Keyword match is most important
                similarity_scores.get(url, 0) * 1.5   # Semantic similarity
            )
            combined_scores[url] = score
        
        # Sort and return top k
        sorted_urls = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
        top_urls = [url for url, _ in sorted_urls[:top_k]]

        # Fallback: if nothing scored (e.g., no embeddings and no keyword matches), return first k nodes
        if not top_urls:
            try:
                return list(self.graph.nodes.keys())[:top_k]
            except Exception:
                return []
            
            
        return top_urls
    
    def _expand_context_with_graph(self, seed_urls: List[str]) -> Dict:
        """Expand context using graph relationships and high-value neighbors with optional token budget."""
        expanded_urls: Set[str] = set()
        important_relationships: List[Dict] = []

        # Helper to try-include a URL respecting budget
        used_tokens = 0
        limit = self.token_budget if self.token_budget is not None else None
        included_count_seeds = 0
        included_count_neighbors = 0

        def try_include(url: str) -> bool:
            nonlocal used_tokens
            if url not in self.entities:
                return False
            if url in expanded_urls:
                return False
            est = self._estimate_entity_tokens(self.entities[url])
            if limit is not None and used_tokens + est > limit:
                return False
            expanded_urls.add(url)
            used_tokens += est
            return True

        # Include seeds first
        for url in seed_urls:
            if try_include(url):
                included_count_seeds += 1

        if limit is not None:
            print(f"[Budget] After seeds: included={included_count_seeds}, used={used_tokens}/{limit}")

        # Then include up to 5 neighbors per seed
        for url in seed_urls:
            if url in self.knowledge_graph:
                neighbors = list(self.knowledge_graph.neighbors(url))[:5]
                for neighbor in neighbors:
                    if try_include(neighbor):
                        included_count_neighbors += 1
                        # Record relationship if present
                        if self.knowledge_graph.has_edge(url, neighbor):
                            edge_data = self.knowledge_graph[url][neighbor]
                        elif self.knowledge_graph.has_edge(neighbor, url):
                            edge_data = self.knowledge_graph[neighbor][url]
                        else:
                            edge_data = {}
                        important_relationships.append({
                            "source": url,
                            "target": neighbor,
                            "common_keywords": edge_data.get("common_keywords", []),
                            "semantic_similarity": edge_data.get("semantic_similarity", 0.0)
                        })
                if limit is not None and used_tokens >= limit:
                    break

        if limit is not None:
            print(f"[Budget] After neighbors: added={included_count_neighbors}, used={used_tokens}/{limit}")

        # Build final entities list
        entities = [self.entities[url] for url in expanded_urls if url in self.entities]
        return {"relationships": important_relationships, "entities": entities}


    async def _generate_enhanced_answer(self, query: str, context: Dict) -> str:
        """Generate enhanced answer using LLM with structured context"""
        
        # Prepare structured context
        context_text = "\n**Documentation Context:**\n"
        for entity in context.get('entities', []):
            url = entity.source_urls[0] if entity.source_urls else "Unknown"
            name = self._extract_entity_name(url)
            context_text += f"**{name}**\n"
            context_text += f"URL: {url}\n"
            if entity.keywords:
                context_text += f"Keywords: {', '.join(entity.keywords[:5])}\n"
            content_snippet = entity.content_snippet 
            context_text += f"Content: {content_snippet}\n\n"
        
        # Add relationship information
        relationships_text = ""
        if context.get('relationships'):
            relationships_text = "\n**Related Concepts:**\n"
            for rel in context['relationships']:
                source_name = self._extract_entity_name(rel['source'])
                target_name = self._extract_entity_name(rel['target'])
                relationships_text += f"- {source_name} → {target_name}"
                
                # Add content snippets from related entities
                source_entity = self.entities.get(rel['source'])
                target_entity = self.entities.get(rel['target'])
                
                if source_entity and target_entity:
                    # Get brief content snippets (first 100 chars)
                    source_snippet = source_entity.content_snippet   
                    target_snippet = target_entity.content_snippet 
                    relationships_text += f"\n  Source: {source_snippet}\n  Target: {target_snippet}"
                
                if rel.get('common_keywords'):
                    relationships_text += f"\n  Shared keywords: {', '.join(rel['common_keywords'][:3])}"
                relationships_text += "\n\n"
        
        # Construct prompt
        prompt = f"""
        Based on the following documentation context, answer the user's question comprehensively and accurately.

        Question: {query}

        {context_text}
        {relationships_text}

        Instructions:
        1. Provide a clear, comprehensive answer to the question
        2. Use specific information from the documentation
        3. Include relevant code examples or commands when applicable
        4. Mention specific URLs when referencing particular features
        5. If the question asks about multiple topics, organize your answer with clear sections
        6. Be practical and actionable in your recommendations

        Answer:
        """
        
        if self.token_budget is not None:
            est_ctx_tokens = self._estimate_tokens_text(context_text + relationships_text)
            overhead = self._estimate_tokens_text(prompt.replace(context_text, '').replace(relationships_text, ''))
            print(f"[Budget] Prompt context tokens≈{est_ctx_tokens}, overhead≈{overhead}. Total≈{est_ctx_tokens + overhead} / limit={self.token_budget}")

        try:
            response = self.llm.send_message(prompt)
            return response.text
        except Exception as e:
            return f"Error generating answer: {e}"
    



# Convenience function for easy usage
async def create_graphrag( graph : Graph ,  gemini_api_key: str, token_budget: Optional[int] = None) -> GraphRAGSystem:
    """Create and initialize GraphRAG system from kg.json file"""
    
    # Create and initialize system
    rag_system = GraphRAGSystem(graph , gemini_api_key, token_budget=token_budget)
    rag_system.load_from_kg_json()
    
    return rag_system 
