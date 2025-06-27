#!/usr/bin/env python3
"""
Test script for GraphRAG implementation
"""

import asyncio
import os
from dotenv import load_dotenv
from enhanced_graphrag import create_graphrag_from_kg_json

load_dotenv()

async def test_graphrag():
    """Test the GraphRAG system with sample queries"""
    
    # Check for API key
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        print("❌ Error: GEMINI_API_KEY not set")
        return
    
    print("🧪 Testing GraphRAG Implementation")
    print("=" * 50)
    
    try:
        # Initialize the system
        print("🚀 Initializing GraphRAG system...")
        rag_system = await create_graphrag_from_kg_json("kg.json", gemini_api_key)
        
        # Test queries
        test_queries = [
            "How do I install Crawl4AI?",
            "What is deep crawling?",
            "How do I use Docker with Crawl4AI?",
            "What are the different extraction strategies?",
            "How do I use the CLI?"
        ]
        
        print(f"\n🔍 Testing {len(test_queries)} sample queries...")
        
        for i, query in enumerate(test_queries, 1):
            print(f"\n{'='*60}")
            print(f"🔍 Query {i}: {query}")
            print(f"{'='*60}")
            
            try:
                answer = await rag_system.retrieve_and_generate(query)
                print("📝 Answer:")
                print("-" * 40)
                print(answer)
                print("-" * 40)
                
            except Exception as e:
                print(f"❌ Error processing query: {e}")
                
            # Add a small delay between queries
            await asyncio.sleep(1)
        
        print("\n✅ GraphRAG testing completed!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")

if __name__ == "__main__":
    asyncio.run(test_graphrag()) 