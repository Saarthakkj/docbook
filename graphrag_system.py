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
    
    # print("🚀 Starting GraphRAG Implementation")
    # print("=" * 60)
    
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

    return  # Stop execution here

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

if __name__ == "__main__":
    asyncio.run(main())