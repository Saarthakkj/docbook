#!/usr/bin/env python3
"""
Enhanced GraphRAG System for Crawl4AI Documentation
Optimized to work directly with kg.json format from deepcrawl.py
"""

import asyncio
import json
import numpy as np
from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass
from sentence_transformers import SentenceTransformer
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
import os
from dotenv import load_dotenv
from collections import Counter, defaultdict

load_dotenv()

@dataclass
class EnhancedEntity:
    name: str
    type: str
    description: str
    source_urls: Set[str]
    keywords: List[str]
    content_snippet: str
    depth: int
    score: float
    embedding: Optional[np.ndarray] = None

@dataclass
class EnhancedRelationship:
    source: str
    target: str
    relation_type: str
    description: str
    confidence: float
    source_urls: Set[str]
    common_keywords: List[str]
    semantic_similarity: float
    weight: float

class EnhancedGraphRAGSystem:
    def __init__(self, gemini_api_key: str):
        self.entities: Dict[str, EnhancedEntity] = {}
        self.relationships: List[EnhancedRelationship] = []
        self.knowledge_graph = nx.DiGraph()
        self.url_content = {}  # Store full content by URL
        self.keyword_index = defaultdict(set)  # Keyword -> URLs that contain it
        
        # Initialize models
        print("🔧 Loading embedding model...")
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Initialize Gemini
        genai.configure(api_key=gemini_api_key)
        self.llm = genai.GenerativeModel('gemini-pro')
        
    def load_from_kg_json(self, kg_data: Dict):
        """Load knowledge graph directly from kg.json format"""
        print("📥 Loading knowledge graph from kg.json format...")
        
        # Store full content
        for url, node_data in kg_data["nodes"].items():
            self.url_content[url] = node_data["content"]
            
            # Build keyword index
            for keyword in node_data.get("keywords", []):
                self.keyword_index[keyword.lower()].add(url)
        
        # Create entities from nodes
        self._create_entities_from_nodes(kg_data["nodes"])
        
        # Create relationships from edges
        self._create_relationships_from_edges(kg_data["edges"])
        
        # Build NetworkX graph
        self._build_networkx_graph()
        
        print(f"✅ Loaded GraphRAG system:")
        print(f"   - Entities: {len(self.entities)}")
        print(f"   - Relationships: {len(self.relationships)}")
        print(f"   - Unique keywords: {len(self.keyword_index)}")
        
    def _create_entities_from_nodes(self, nodes: Dict):
        """Create entities from kg.json nodes"""
        print("🏗️  Creating entities from nodes...")
        
        for url, node_data in nodes.items():
            # Extract domain/page name as entity name
            entity_name = self._extract_entity_name(url)
            
            # Create content snippet (first 500 chars)
            content = node_data["content"]
            snippet = content[:500] + "..." if len(content) > 500 else content
            
            # Determine entity type based on URL structure
            entity_type = self._determine_entity_type(url)
            
            # Create entity
            entity = EnhancedEntity(
                name=entity_name,
                type=entity_type,
                description=f"Documentation page: {entity_name}",
                source_urls={url},
                keywords=node_data.get("keywords", []),
                content_snippet=snippet,
                depth=node_data.get("depth", 0),
                score=node_data.get("score", 1.0)
            )
            
            self.entities[url] = entity
    
    def _create_relationships_from_edges(self, edges: List[Dict]):
        """Create relationships from kg.json edges"""
        print("🔗 Creating relationships from edges...")
        
        for edge in edges:
            relationship = EnhancedRelationship(
                source=edge["source"],
                target=edge["target"],
                relation_type=edge["relation_type"],
                description=f"Navigation from {self._extract_entity_name(edge['source'])} to {self._extract_entity_name(edge['target'])}",
                confidence=edge["weight"],
                source_urls={edge["source"], edge["target"]},
                common_keywords=edge.get("common_keywords", []),
                semantic_similarity=edge.get("semantic_similarity", 0.0),
                weight=edge["weight"]
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
    
    def _determine_entity_type(self, url: str) -> str:
        """Determine entity type based on URL structure"""
        if "/core/" in url:
            return "CORE_FEATURE"
        elif "/advanced/" in url:
            return "ADVANCED_FEATURE"
        elif "/extraction/" in url:
            return "EXTRACTION_STRATEGY"
        elif "/api/" in url:
            return "API_REFERENCE"
        elif "/blog/" in url:
            return "BLOG_POST"
        elif "docker" in url.lower():
            return "DEPLOYMENT"
        elif "installation" in url.lower():
            return "INSTALLATION"
        else:
            return "DOCUMENTATION_PAGE"
    
    def _build_networkx_graph(self):
        """Build NetworkX graph from entities and relationships"""
        print("🕸️  Building NetworkX graph...")
        
        # Add nodes
        for url, entity in self.entities.items():
            self.knowledge_graph.add_node(
                url,
                name=entity.name,
                type=entity.type,
                keywords=entity.keywords,
                depth=entity.depth,
                score=entity.score,
                embedding=entity.embedding
            )
        
        # Add edges
        for rel in self.relationships:
            if rel.source in self.entities and rel.target in self.entities:
                self.knowledge_graph.add_edge(
                    rel.source,
                    rel.target,
                    relation_type=rel.relation_type,
                    weight=rel.weight,
                    common_keywords=rel.common_keywords,
                    semantic_similarity=rel.semantic_similarity
                )
    
    async def create_embeddings(self):
        """Create embeddings for all entities"""
        print("🔗 Creating embeddings for entities...")
        
        for url, entity in self.entities.items():
            # Combine name, keywords, and content snippet for embedding
            text_parts = [
                entity.name,
                entity.type,
                " ".join(entity.keywords[:10]),  # Top 10 keywords
                entity.content_snippet
            ]
            
            embedding_text = " ".join(text_parts)
            embedding = self.embedding_model.encode(embedding_text)
            entity.embedding = embedding
            
            # Update graph node
            if url in self.knowledge_graph:
                self.knowledge_graph.nodes[url]['embedding'] = embedding
    
    async def retrieve_and_generate(self, query: str, top_k: int = 5) -> str:
        """Enhanced query processing using both keywords and embeddings"""
        
        print(f"🔍 Processing query: {query}")
        
        # Step 1: Find relevant URLs using multiple methods
        relevant_urls = await self._find_relevant_urls(query, top_k)
        
        # Step 2: Expand context using graph relationships
        expanded_context = self._expand_context_with_graph(relevant_urls)
        
        # Step 3: Retrieve and rank relevant content
        relevant_content = self._retrieve_ranked_content(expanded_context, query)
        
        # Step 4: Generate answer using LLM
        answer = await self._generate_enhanced_answer(query, relevant_content, expanded_context)
        
        return answer
    
    async def _find_relevant_urls(self, query: str, top_k: int) -> List[str]:
        """Find relevant URLs using keyword matching and semantic similarity"""
        
        # Method 1: Keyword-based retrieval
        query_words = set(query.lower().split())
        keyword_scores = defaultdict(float)
        
        for word in query_words:
            if word in self.keyword_index:
                for url in self.keyword_index[word]:
                    keyword_scores[url] += 1.0
        
        # Method 2: Semantic similarity (if embeddings exist)
        similarity_scores = {}
        if any(entity.embedding is not None for entity in self.entities.values()):
            query_embedding = self.embedding_model.encode(query)
            
            for url, entity in self.entities.items():
                if entity.embedding is not None:
                    similarity = cosine_similarity(
                        query_embedding.reshape(1, -1),
                        entity.embedding.reshape(1, -1)
                    )[0][0]
                    similarity_scores[url] = similarity
        
        # Method 3: Content-based fuzzy matching
        content_scores = defaultdict(float)
        for url, content in self.url_content.items():
            content_lower = content.lower()
            for word in query_words:
                if word in content_lower:
                    # Count occurrences with diminishing returns
                    count = content_lower.count(word)
                    content_scores[url] += min(count * 0.1, 1.0)
        
        # Combine scores
        combined_scores = {}
        all_urls = set(keyword_scores.keys()) | set(similarity_scores.keys()) | set(content_scores.keys())
        
        for url in all_urls:
            score = (
                keyword_scores.get(url, 0) * 2.0 +  # Keyword match is most important
                similarity_scores.get(url, 0) * 1.5 +  # Semantic similarity
                content_scores.get(url, 0) * 1.0  # Content fuzzy match
            )
            combined_scores[url] = score
        
        # Sort and return top k
        sorted_urls = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
        return [url for url, _ in sorted_urls[:top_k]]
    
    def _expand_context_with_graph(self, seed_urls: List[str]) -> Dict:
        """Expand context using graph relationships and high-value neighbors"""
        
        expanded_urls = set(seed_urls)
        important_relationships = []
        
        # Find neighbors and high-value connections
        for url in seed_urls:
            if url in self.knowledge_graph:
                # Get direct neighbors
                neighbors = list(self.knowledge_graph.neighbors(url))
                predecessors = list(self.knowledge_graph.predecessors(url))
                all_connected = neighbors + predecessors
                
                # Add top neighbors based on weight and similarity
                for neighbor in all_connected[:3]:  # Limit to top 3
                    expanded_urls.add(neighbor)
                    
                    # Collect relationship info
                    if self.knowledge_graph.has_edge(url, neighbor):
                        edge_data = self.knowledge_graph[url][neighbor]
                    else:
                        edge_data = self.knowledge_graph[neighbor][url]
                    
                    important_relationships.append({
                        "source": url,
                        "target": neighbor,
                        "weight": edge_data.get("weight", 0.5),
                        "common_keywords": edge_data.get("common_keywords", []),
                        "semantic_similarity": edge_data.get("semantic_similarity", 0.0)
                    })
        
        return {
            "urls": list(expanded_urls),
            "relationships": important_relationships,
            "entities": [self.entities[url] for url in expanded_urls if url in self.entities]
        }
    
    def _retrieve_ranked_content(self, context: Dict, query: str) -> List[Dict]:
        """Retrieve and rank content based on relevance"""
        
        content_items = []
        query_words = set(query.lower().split())
        
        for url in context["urls"]:
            if url in self.url_content:
                content = self.url_content[url]
                entity = self.entities.get(url)
                
                # Calculate relevance score
                relevance_score = 0.0
                
                # Keyword relevance
                if entity:
                    keyword_overlap = len(set(kw.lower() for kw in entity.keywords) & query_words)
                    relevance_score += keyword_overlap * 0.3
                
                # Content relevance (simplified)
                content_lower = content.lower()
                for word in query_words:
                    if word in content_lower:
                        relevance_score += min(content_lower.count(word) * 0.1, 0.5)
                
                # Depth penalty (prefer shallower, more general pages)
                if entity:
                    depth_bonus = max(0, 1.0 - entity.depth * 0.1)
                    relevance_score *= depth_bonus
                
                # Extract relevant snippets
                snippets = self._extract_relevant_snippets(content, query_words)
                
                content_items.append({
                    "url": url,
                    "entity_name": entity.name if entity else self._extract_entity_name(url),
                    "entity_type": entity.type if entity else "UNKNOWN",
                    "relevance_score": relevance_score,
                    "snippets": snippets,
                    "keywords": entity.keywords if entity else []
                })
        
        # Sort by relevance and return top items
        content_items.sort(key=lambda x: x["relevance_score"], reverse=True)
        return content_items[:10]  # Limit to top 10 most relevant
    
    def _extract_relevant_snippets(self, content: str, query_words: Set[str], max_snippets: int = 3) -> List[str]:
        """Extract relevant snippets from content based on query words"""
        
        snippets = []
        sentences = content.split('\n')
        
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 50:  # Skip very short sentences
                continue
                
            sentence_lower = sentence.lower()
            word_matches = sum(1 for word in query_words if word in sentence_lower)
            
            if word_matches > 0:
                # Clean up the snippet
                if len(sentence) > 300:
                    sentence = sentence[:300] + "..."
                snippets.append(sentence)
                
                if len(snippets) >= max_snippets:
                    break
        
        return snippets
    
    async def _generate_enhanced_answer(self, query: str, content_items: List[Dict], context: Dict) -> str:
        """Generate enhanced answer using LLM with structured context"""
        
        # Prepare structured context
        context_sections = []
        
        # Add content from top relevant sources
        for item in content_items[:5]:  # Top 5 most relevant
            section = f"**{item['entity_name']} ({item['entity_type']})**\n"
            section += f"Source: {item['url']}\n"
            if item['keywords']:
                section += f"Keywords: {', '.join(item['keywords'][:8])}\n"
            section += "Content:\n"
            for snippet in item['snippets']:
                section += f"- {snippet}\n"
            context_sections.append(section)
        
        # Add relationship information
        relationships_text = ""
        if context['relationships']:
            relationships_text = "\n**Related Concepts:**\n"
            for rel in context['relationships'][:5]:
                source_name = self._extract_entity_name(rel['source'])
                target_name = self._extract_entity_name(rel['target'])
                relationships_text += f"- {source_name} → {target_name}"
                if rel['common_keywords']:
                    relationships_text += f" (shared: {', '.join(rel['common_keywords'][:3])})"
                relationships_text += "\n"
        
        # Construct prompt
        prompt = f"""
Based on the following Crawl4AI documentation content, answer the user's question comprehensively and accurately.

Question: {query}

Documentation Content:
{chr(10).join(context_sections)}

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
        
        try:
            response = await self.llm.generate_content_async(prompt)
            return response.text
        except Exception as e:
            return f"Error generating answer: {e}"
    
    def save_enhanced_kg(self, filepath: str):
        """Save the enhanced knowledge graph"""
        
        enhanced_data = {
            "entities": {},
            "relationships": [],
            "keyword_index": dict(self.keyword_index),
            "metadata": {
                "total_entities": len(self.entities),
                "total_relationships": len(self.relationships),
                "unique_keywords": len(self.keyword_index)
            }
        }
        
        # Save entities
        for url, entity in self.entities.items():
            enhanced_data["entities"][url] = {
                "name": entity.name,
                "type": entity.type,
                "description": entity.description,
                "keywords": entity.keywords,
                "depth": entity.depth,
                "score": entity.score,
                "content_snippet": entity.content_snippet,
                "embedding": entity.embedding.tolist() if entity.embedding is not None else None
            }
        
        # Save relationships
        for rel in self.relationships:
            enhanced_data["relationships"].append({
                "source": rel.source,
                "target": rel.target,
                "relation_type": rel.relation_type,
                "weight": rel.weight,
                "common_keywords": rel.common_keywords,
                "semantic_similarity": rel.semantic_similarity,
                "confidence": rel.confidence
            })
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(enhanced_data, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Enhanced knowledge graph saved to {filepath}")

# Convenience function for easy usage
async def create_graphrag_from_kg_json(kg_json_path: str, gemini_api_key: str) -> EnhancedGraphRAGSystem:
    """Create and initialize GraphRAG system from kg.json file"""
    
    # Load kg.json
    with open(kg_json_path, 'r', encoding='utf-8') as f:
        kg_data = json.load(f)
    
    # Create and initialize system
    rag_system = EnhancedGraphRAGSystem(gemini_api_key)
    rag_system.load_from_kg_json(kg_data)
    
    # Create embeddings
    await rag_system.create_embeddings()
    
    return rag_system 