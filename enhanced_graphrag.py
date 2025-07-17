"""
    TODO : 
        - i guess _expand_context function should return only important_relationships 
        - do I have relevant information on relationships for  _expand_context_with_graph ? 
        - delete useless commented code 
        - introduce cuGRAPh in networkx
        - any other score to add in find_relevant_url method?

"""


"""
    top_k =5  urls -> inside find_relevant_urls method and expand_context_with_graph method
"""


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
class EnhancedEntity:
    name: str
    type: str
    # description: str
    source_urls: List[str]
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
    # description: str
    # confidence: float
    source_urls: List[str]
    common_keywords: List[str]
    semantic_similarity: float
    # weight: float

class EnhancedGraphRAGSystem:
    def __init__(self, graph : Graph , gemini_api_key: str):
        self.entities: Dict[str, EnhancedEntity] = {}
        self.relationships: List[EnhancedRelationship] = []
        self.knowledge_graph = nx.DiGraph()
        self.url_content = {}  # Store full content by URL
        self.keyword_index = defaultdict(list)  # Keyword -> URLs that contain it
        self.graph = graph
        # self.kg_path = kg_path
        
        # Initialize models
        # print("🔧 Loading embedding model...")
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Initialize Gemini
        # genai.configure(api_key=gemini_api_key)
        client = genai.Client(api_key='GEMINI_API_KEY')
        chat = client.chats.create(model='gemini-2.0-flash')
        self.llm = chat
        # for chunk in chat.send_message_stream('tell me a story'):
        # print(chunk.text)

        # response = client.models.generate_content(
        #     model='gemini-2.0-flash-001',
        # )
        # self.llm = genai.GenerativeModel('gemini-2.5-flash')
        
    def load_from_kg_json(self):
        """ load knoweldge graph directly from graphNode"""
        
        
        print("🔍 Loading knowledge graph from graphNode...")
        
        
        for url, node in self.graph.nodes.items():
            for kw in node.keywords:
                self.keyword_index[kw.lower()].append(node.url)
    
        self._build_networkx_graph()
        self._create_entities_from_nodes(list(self.graph.nodes.values()))
        self._create_relationships_from_edges(self.graph.edges)
                
                
        
            
        
            
        
        
        
        
        
        
        # """Load knowledge graph directly from kg.json format"""
        # print("📥 Loading knowledge graph from kg.json format...")
        
        # # Store full content
        # for url, node_data in kg_data["nodes"].items():
        #     self.url_content[url] = node_data["content"]
            
        #     # Build keyword index
        #     for keyword in node_data.get("keywords", []):
        
        # # Create entities from nodes
        self._create_entities_from_nodes(self.graph.nodes)
        
        # # Create relationships from edges
        # self._create_relationships_from_edges(kg_data["edges"])
        
        # # Build NetworkX graph
        # self._build_networkx_graph()
        
        # print(f"✅ Loaded GraphRAG system:")
        # print(f"   - Entities: {len(self.entities)}")
        # print(f"   - Relationships: {len(self.relationships)}")
        # print(f"   - Unique keywords: {len(self.keyword_index)}")
        
    def _create_entities_from_nodes(self, all_nodes : List[GraphNode]):
        """Create entities from kg.json nodes"""
        print("🏗️  Creating entities from nodes...")
        
        for  node in all_nodes:

            entity = EnhancedEntity(
                name='',  # Placeholder, as original is commented
                type='',  # Placeholder
                description='',  # Placeholder
                source_urls=[node.url],
                keywords=node.keywords,
                content_snippet=node.content,
                depth=node.depth,
                score=node.score
            )
            
            self.entities[node.url] = entity
    
    def _create_relationships_from_edges(self, edges: List[Dict]):
        """Create relationships from kg.json edges"""
        print("🔗 Creating relationships from edges...")
        
        for edge in edges:
            relationship = EnhancedRelationship(
                source=edge["source"],
                target=edge["target"],
                relation_type=edge["relation_type"],
                # description=f"Navigation from {self._extract_entity_name(edge['source'])} to {self._extract_entity_name(edge['target'])}",
                source_urls=[edge["source"], edge["target"]],
                common_keywords=edge.get("common_keywords", []),
                semantic_similarity=edge.get("semantic_similarity", 0.0)
            )
            
            self.relationships.append(relationship)
    
    # def _extract_entity_name(self, url: str) -> str:
    #     """Extract a readable entity name from URL"""
    #     if url.endswith('/'):
    #         url = url[:-1]
        
    #     parts = url.split('/')
    #     if len(parts) >= 2:
    #         name = parts[-1].replace('-', ' ').replace('_', ' ').title()
    #         if name:
    #             return name
        
    #     return url.split('/')[-1] or "Home"
        
    # def load_enhanced_kg(self, enhanced_kg_path: str, original_kg_path: str = None):
    #     """Load enhanced knowledge graph from saved JSON file"""
    #     print(f"📥 Loading enhanced knowledge graph from {enhanced_kg_path}...")
        
    #     with open(enhanced_kg_path, 'r', encoding='utf-8') as f:
    #         enhanced_data = json.load(f)
        
    #     # Clear existing data
    #     self.entities.clear()
    #     self.relationships.clear()
    #     self.knowledge_graph.clear()
    #     self.keyword_index.clear()
    #     self.url_content.clear()
        
    #     # Load entities
    #     print("🏗️  Reconstructing entities...")
    #     for url, entity_data in enhanced_data["entities"].items():
    #         # Convert embedding back to numpy array if it exists
    #         embedding = None
    #         if entity_data["embedding"] is not None:
    #             embedding = np.array(entity_data["embedding"])
            
    #         entity = EnhancedEntity(
    #             name=entity_data["name"],
    #             type=entity_data["type"],
    #             description=entity_data["description"],
    #             source_urls=entity_data.get("source_urls", [url]),  # Fallback to URL if not saved
    #             keywords=entity_data["keywords"],
    #             content_snippet=entity_data["content_snippet"],
    #             depth=entity_data["depth"],
    #             score=entity_data["score"],
    #             embedding=embedding
    #         )
            
    #         self.entities[url] = entity
        
    #     # Load relationships
    #     print("🔗 Reconstructing relationships...")
    #     for rel_data in enhanced_data["relationships"]:
    #         relationship = EnhancedRelationship(
    #             source=rel_data["source"],
    #             target=rel_data["target"],
    #             relation_type=rel_data["relation_type"],
    #             description=rel_data.get("description", ""),
    #             # confidence=rel_data["pr"],
    #             source_urls=rel_data.get("source_urls", [rel_data["source"], rel_data["target"]]),
    #             common_keywords=rel_data["common_keywords"],
    #             semantic_similarity=rel_data["semantic_similarity"],
    #             # weight=rel_data["weight"]
    #         )
            
    #         self.relationships.append(relationship)
        
    #     # Load keyword index
    #     print("🏷️  Reconstructing keyword index...")
    #     for keyword, urls in enhanced_data["keyword_index"].items():
    #         self.keyword_index[keyword] = urls
        
    #     # Load url_content from original kg.json if path provided
    #     if original_kg_path and os.path.exists(original_kg_path):
    #         print("📄 Loading original content from kg.json...")
    #         with open(original_kg_path, 'r', encoding='utf-8') as f:
    #             kg_data = json.load(f)
            
    #         for url, node_data in kg_data["nodes"].items():
    #             self.url_content[url] = node_data["content"]
    #     else:
    #         # Use content snippets as fallback if original kg.json not available
    #         print("⚠️  Using content snippets as fallback (original kg.json not provided)")
    #         for url, entity in self.entities.items():
    #             self.url_content[url] = entity.content_snippet
        
    #     # Rebuild NetworkX graph
    #     self._build_networkx_graph()
        
    #     print(f"✅ Enhanced knowledge graph loaded:")
    #     print(f"   - Entities: {len(self.entities)}")
    #     print(f"   - Relationships: {len(self.relationships)}")
    #     print(f"   - Unique keywords: {len(self.keyword_index)}")
    # def _determine_entity_type(self, url: str) -> str:
    #     """Determine entity type based on URL structure"""
    #     if "/core/" in url:
    #         return "CORE_FEATURE"
    #     elif "/advanced/" in url:
    #         return "ADVANCED_FEATURE"
    #     elif "/extraction/" in url:
    #         return "EXTRACTION_STRATEGY"
    #     elif "/api/" in url:
    #         return "API_REFERENCE"
    #     elif "/blog/" in url:
    #         return "BLOG_POST"
    #     elif "docker" in url.lower():
    #         return "DEPLOYMENT"
    #     elif "installation" in url.lower():
    #         return "INSTALLATION"
    #     else:
    #         return "DOCUMENTATION_PAGE"
    
    def _build_networkx_graph(self):
        """Build NetworkX graph from entities and relationships"""
        print("🕸️  Building NetworkX graph...")
        
        # Add nodes
        for url, node in self.graph.nodes.items():
            self.knowledge_graph.add_node(
                url,
                keywords=node.keywords,
                depth=node.depth,
                score=node.score,
                embedding=node.embedding
            )
        
        # Add edges
        for rel in self.relationships:
            if rel.source in self.entities and rel.target in self.entities:
                self.knowledge_graph.add_edge(
                    rel.source,
                    rel.target,
                    relation_type=rel.relation_type,
                    # weight=rel.weight,
                    common_keywords=rel.common_keywords,
                    semantic_similarity=rel.semantic_similarity
                )
                
                
        
       
    async def retrieve_and_generate(self, query: str, top_k: int = 5) -> str:
        """Enhanced query processing using both keywords and embeddings"""
        
        print(f"Processing query: {query}")
        
        # Step 1: Find relevant URLs using multiple methods
        relevant_urls = await self._find_relevant_urls(query, top_k)
        
        # Step 2: Expand context using graph relationships
        expanded_context = self._expand_context_with_graph(relevant_urls , top_k)
        
        # Step 3: Retrieve and rank relevant content
        # relevant_content = self._retrieve_ranked_content(expanded_context, query)
        
        # Step 4: Generate answer using LLM
        answer = await self._generate_enhanced_answer(query, expanded_context, expanded_context)
        
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
        # if any(entity.embedding is not None for entity in self.entities.values()):
        query_embedding = self.embedding_model.encode(query)
        
        for url, entity in self.entities.items():
            similarity = cosine_similarity(
                query_embedding.reshape(1, -1),
                entity.embedding.reshape(1, -1)
            )[0][0]
            similarity_scores[url] = similarity
    
        # Method 3: Content-based fuzzy matching
        # content_scores = defaultdict(float)
        # for url, content in self.url_content.items():
        #     content_lower = content.lower()
        #     for word in query_words:
        #         if word in content_lower:
        #             # Count occurrences with diminishing returns
        #             count = content_lower.count(word)
        #             content_scores[url] += min(count * 0.1, 1.0)
        
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
        return [url for url, _ in sorted_urls[:top_k]]
    
    def _expand_context_with_graph(self, seed_urls: List[str] , k : int) -> Dict:
        """Expand context using graph relationships and high-value neighbors"""
        
        expanded_urls = set(seed_urls) # this seed_urls is top_k (here  , 5)
        important_relationships = []
        
        # Find neighbors and high-value connections
        for url in seed_urls:
            if url in self.knowledge_graph:
                # Get direct neighbors
                neighbors = list(self.knowledge_graph.neighbors(url))
                predecessors = list(self.knowledge_graph.predecessors(url))
                all_connected = neighbors + predecessors # 10 urls
                
                # Add top neighbors based on weight and similarity
                for neighbor in all_connected[:2]:  
                    expanded_urls.add(neighbor)
                    
                    # Collect relationship info
                    if self.knowledge_graph.has_edge(url, neighbor):
                        edge_data = self.knowledge_graph[url][neighbor]
                    else:
                        edge_data = self.knowledge_graph[neighbor][url]
                    
                    important_relationships.append({
                        "source": url,
                        "target": neighbor,
                        # "weight": edge_data.get("weight", 0.5),
                        "common_keywords": edge_data.get("common_keywords", []),
                        "semantic_similarity": edge_data.get("semantic_similarity", 0.0)
                    })
                    
        # seed_urls (5) x 2 =  10 urls 
        return {
            "urls" : expanded_urls , 
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
    
    # def _extract_relevant_snippets(self, content: str, query_words: Set[str], max_snippets: int = 3) -> List[str]:
    #     """Extract relevant snippets from content based on query words"""
        
    #     snippets = []
    #     sentences = content.split('\n')
        
    #     for sentence in sentences:
    #         sentence = sentence.strip()
    #         if len(sentence) < 50:  # Skip very short sentences
    #             continue
                
    #         sentence_lower = sentence.lower()
    #         word_matches = sum(1 for word in query_words if word in sentence_lower)
            
    #         if word_matches > 0:
    #             # Clean up the snippet
    #             if len(sentence) > 300:
    #                 sentence = sentence[:300] + "..."
    #             snippets.append(sentence)
                
    #             if len(snippets) >= max_snippets:
    #                 break
        
    #     return snippets
    
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
            response = await self.llm.send_message_stream(prompt)
            return response.text
        except Exception as e:
            return f"Error generating answer: {e}"
    
    # def save_enhanced_kg(self, filepath: str):
    #     """Save the enhanced knowledge graph"""
        
    #     enhanced_data = {
    #         "entities": {},
    #         "relationships": [],
    #         "keyword_index": dict(self.keyword_index),
    #         "metadata": {
    #             "total_entities": len(self.entities),
    #             "total_relationships": len(self.relationships),
    #             "unique_keywords": len(self.keyword_index)
    #         }
    #     }
        
    #     # Save entities
    #     for url, entity in self.entities.items():
    #         enhanced_data["entities"][url] = {
    #             "name": entity.name,
    #             "type": entity.type,
    #             "description": entity.description,
    #             "keywords": entity.keywords,
    #             "depth": entity.depth,
    #             "score": entity.score,
    #             "content_snippet": entity.content_snippet,
    #             "embedding": entity.embedding.tolist() if entity.embedding is not None else None
    #         }
        
    #     # Save relationships
    #     for rel in self.relationships:
    #         enhanced_data["relationships"].append({
    #             "source": rel.source,
    #             "target": rel.target,
    #             "relation_type": rel.relation_type,
    #             # "weight": rel.weight,
    #             "common_keywords": rel.common_keywords,
    #             "semantic_similarity": rel.semantic_similarity,
    #             # "confidence": rel.confidence
    #         })
        
    #     with open(filepath, 'w', encoding='utf-8') as f:
    #         json.dump(enhanced_data, f, indent=2, ensure_ascii=False)
        
    #     print(f"💾 Enhanced knowledge graph saved to {filepath}")

    #     # Stop further processing; the current workflow ends once the
    #     # enhanced knowledge graph is persisted.
    #     return


# Add this convenience function at the end of the file
# async def create_graphrag_from_enhanced_kg(enhanced_kg_path: str, gemini_api_key: str) -> EnhancedGraphRAGSystem:
#     """Create and initialize GraphRAG system from enhanced_kg.json file"""
    
#     # Create system instance
#     rag_system = EnhancedGraphRAGSystem( gemini_api_key)
    
#     # Load enhanced knowledge graph
#     rag_system.load_enhanced_kg(enhanced_kg_path)
    
#     print("✅ Enhanced GraphRAG system loaded and ready!")
#     return rag_system
        
    
# Convenience function for easy usage
async def create_graphrag_from_kg_json( graph : Graph ,  gemini_api_key: str) -> EnhancedGraphRAGSystem:
    """Create and initialize GraphRAG system from kg.json file"""
    
    # Load kg.json
    # with open(kg_json_path, 'r', encoding='utf-8') as f:
    #     kg_data = json.load(f)
    
    # Create and initialize system
    rag_system = EnhancedGraphRAGSystem(graph , gemini_api_key )
    rag_system.load_from_kg_json()
    
    # Create embeddings
    # await rag_system.create_embeddings()
    
    return rag_system 