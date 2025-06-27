#!/usr/bin/env python3
"""
GraphRAG Implementation for Crawl4AI Documentation
Integrates deepcrawl.py output with graphrag_system.py for intelligent querying
"""

import asyncio
import json
import os
from dotenv import load_dotenv
from graphrag_system import GraphRAGSystem

load_dotenv()

async def main():
    """Main function to demonstrate GraphRAG implementation"""
    
    # Check for required API key
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        print("❌ Error: GEMINI_API_KEY environment variable not set")
        print("Please set your Gemini API key in the .env file")
        return
    
    print("🚀 Starting GraphRAG Implementation")
    print("=" * 60)
    
    # Step 1: Load the knowledge graph from deepcrawl.py output
    print("📂 Loading knowledge graph from kg.json...")
    try:
        with open("kg.json", "r", encoding="utf-8") as f:
            kg_data = json.load(f)
        
        print(f"✅ Loaded knowledge graph:")
        print(f"   - Nodes: {len(kg_data['nodes'])}")
        print(f"   - Edges: {len(kg_data['edges'])}")
        print(f"   - Root URL: {kg_data['metadata']['root_url']}")
        
    except FileNotFoundError:
        print("❌ Error: kg.json not found. Please run deepcrawl.py first.")
        return
    except json.JSONDecodeError as e:
        print(f"❌ Error loading kg.json: {e}")
        return
    
    # Step 2: Convert kg.json format to GraphRAG system format
    print("\n🔄 Converting to GraphRAG format...")
    url_graph = convert_kg_to_url_graph(kg_data)
    
    # Step 3: Initialize GraphRAG system
    print("🧠 Initializing GraphRAG system...")
    rag_system = GraphRAGSystem(gemini_api_key)
    
    # Step 4: Build the knowledge graph
    print("🏗️  Building knowledge graph...")
    await rag_system.build_knowledge_graph(url_graph)
    
    # Step 5: Save the enhanced knowledge graph
    print("💾 Saving enhanced knowledge graph...")
    rag_system.save_knowledge_graph("enhanced_kg.json")
    
    # Step 6: Interactive query session
    print("\n" + "=" * 60)
    print("🤖 GraphRAG Query Interface Ready!")
    print("Ask questions about the Crawl4AI documentation.")
    print("Type 'quit' to exit.")
    print("=" * 60)
    
    # Example queries to demonstrate capabilities
    example_queries = [
        "What is deep crawling in Crawl4AI and how does it work?",
        "How do I install and set up Crawl4AI?",
        "What are the different extraction strategies available?",
        "How can I use Docker with Crawl4AI?",
        "What's new in the latest version of Crawl4AI?"
    ]
    
    print("\n💡 Example queries you can try:")
    for i, query in enumerate(example_queries, 1):
        print(f"   {i}. {query}")
    
    while True:
        print("\n" + "-" * 40)
        user_query = input("🔍 Enter your question: ").strip()
        
        if user_query.lower() in ['quit', 'exit', 'q']:
            print("👋 Thanks for using GraphRAG! Goodbye!")
            break
        
        if not user_query:
            continue
        
        try:
            print("\n🔎 Processing your query...")
            answer = await rag_system.retrieve_and_generate(user_query)
            print("\n📝 Answer:")
            print("=" * 50)
            print(answer)
            print("=" * 50)
            
        except Exception as e:
            print(f"❌ Error processing query: {e}")
            print("Please try a different question.")

def convert_kg_to_url_graph(kg_data):
    """
    Convert kg.json format to the format expected by GraphRAG system
    
    Args:
        kg_data: The loaded kg.json data
        
    Returns:
        dict: URL graph in GraphRAG format
    """
    url_graph = {}
    
    # Convert nodes to the expected format
    for url, node_data in kg_data["nodes"].items():
        url_graph[url] = {
            "content": node_data["content"],
            "keywords": node_data.get("keywords", []),
            "depth": node_data.get("depth", 0),
            "score": node_data.get("score", 1.0),
            # Additional metadata that might be useful
            "metadata": {
                "source_url": node_data["source_url"],
                "embedding": node_data.get("embedding")
            }
        }
    
    return url_graph

def print_statistics(kg_data):
    """Print detailed statistics about the knowledge graph"""
    nodes = kg_data["nodes"]
    edges = kg_data["edges"]
    
    print("\n📊 Knowledge Graph Statistics:")
    print("-" * 40)
    
    # Node statistics
    depths = [node["depth"] for node in nodes.values()]
    keyword_counts = [len(node.get("keywords", [])) for node in nodes.values()]
    content_lengths = [len(node["content"]) for node in nodes.values()]
    
    print(f"📈 Nodes: {len(nodes)}")
    print(f"   - Max depth: {max(depths) if depths else 0}")
    print(f"   - Avg keywords per node: {sum(keyword_counts) / len(keyword_counts):.1f}")
    print(f"   - Avg content length: {sum(content_lengths) / len(content_lengths):.0f} chars")
    
    # Edge statistics  
    weights = [edge["weight"] for edge in edges]
    similarities = [edge["semantic_similarity"] for edge in edges]
    
    print(f"🔗 Edges: {len(edges)}")
    print(f"   - Avg weight: {sum(weights) / len(weights):.3f}")
    print(f"   - Avg semantic similarity: {sum(similarities) / len(similarities):.3f}")
    
    # Top keywords across all nodes
    all_keywords = []
    for node in nodes.values():
        all_keywords.extend(node.get("keywords", []))
    
    from collections import Counter
    top_keywords = Counter(all_keywords).most_common(10)
    
    print(f"🏷️  Top Keywords:")
    for keyword, count in top_keywords:
        print(f"   - {keyword}: {count}")

if __name__ == "__main__":
    asyncio.run(main())