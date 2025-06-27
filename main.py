#!/usr/bin/env python3
"""
GraphRAG Implementation for Crawl4AI Documentation
Integrates deepcrawl.py output with graphrag_system.py for intelligent querying
"""

import asyncio
import argparse
import sys
import subprocess
import json
import os
from dotenv import load_dotenv
from enhanced_graphrag import EnhancedGraphRAGSystem, create_graphrag_from_kg_json , create_graphrag_from_enhanced_kg

load_dotenv()


def parse_arguments(): 
    '''parse command line arguments'''
    
    parser = argparse.ArgumentParser(
        description= "GraphRAG implementation using Crawl4AI" , 
        formatter_class = argparse.RawDescriptionHelpFormatter , 
        epilog="""
Examples : 
    # Quick start with default settings 
    python main.py --url https://docs.crawl4ai.com/
    
    #Custom crawling parameters 
    python main.py --url https://crawl4ai.com/ --max_depth 3 max_pages 50
        """
    )
    
    
    parser = argparse.ArgumentParser(description = "pass multiple varirables")
    parser.add_argument("--max_depth"  , type = int  , help = "maximum depth of pages")
    parser.add_argument ("--max_pages" , type = int ,  help = "maximum number of pages")

    parser.add_argument("--url" , type = str  , required = True, help = "doc url")


    return parser.parse_args()


async def run_deepcrawl(url : str , max_depth : int , max_pages : int , output_file : str = "kg.json"):
    """run deepcrawl.py with specified parameters"""
    
    
    print(f" URL : {url} ")
    print(f" Max depth : {max_depth}")
    print(f"output : {output_file}")
    
    cmd = [sys.executable , "deepcrawl.py" , "--url" , url] 
    
    if max_depth is not None : 
        cmd.extend(["--max_depth" , str(max_depth)])
    if max_pages is not None : 
        cmd.extend(["--max_pages" , str(max_pages)])
    
    
    
    # cmd = [
    #     sys.executable , "deepcrawl.py" , 
    #     "--url" , url , 
    #     "--max_depth"  , str(max_depth) , 
    #     "--max_pages" , str(max_pages)
    # ] 
    
    
    try : 
        print(" executing deepcrawl.py .... ")
        
        result = subprocess.run(cmd , check = True)
        
        # process = subprocess.Popen(cmd , stdout = subprocess.PIPE , stderr = subprocess.STDOUT , text = True , bufsize =1 , universal_newlines = True)
        # while True :
        #     output = process.stdout.readline()
        #     if output == '' and process.poll() is not None :
        #         break
        #     else: print(output.strip())
            
        # return_code = process.poll()
        
        print("\nDeepcrawl completed successfully! ")
        
        
    except Exception as e : 
        print(f" Unexpected error : {e}")
        raise

async def main():
    """Main function to demonstrate GraphRAG implementation"""
    
    # Check for required API key
    gemini_api_key = os.getenv("gemini_api_key")
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
            
        args = parse_arguments()
        await run_deepcrawl(args.url , args.max_depth , args.max_pages , "kg.json")
        
    except json.JSONDecodeError as e:
        print(f"❌ Error loading kg.json: {e}")
        return
    
    rag_system = None
    
    # Check if enhanced_kg.json exists
    enhanced_kg_path = "enhanced_kg.json"
    
    # Replace the problematic section in main() with:
    if os.path.exists(enhanced_kg_path):
        print(f"✅ Found existing enhanced knowledge graph: {enhanced_kg_path}")
        print("Loading existing enhanced GraphRAG system...")
        
        # Load from enhanced_kg.json with fallback to original kg.json for content
        rag_system = await create_graphrag_from_enhanced_kg(
            enhanced_kg_path, 
            gemini_api_key, 
            original_kg_path="kg.json"
        )
    else:
        # Step 2: Initialize Enhanced GraphRAG system directly from kg.json
        print("\n🧠 Initializing Enhanced GraphRAG system...")
        rag_system = await create_graphrag_from_kg_json("kg.json", gemini_api_key)
        
        # Step 3: Save the enhanced knowledge graph
        print("💾 Saving enhanced knowledge graph...")
        rag_system.save_enhanced_kg("enhanced_kg.json")
        
    
    # Step 4: Interactive query session
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
    # weights = [edge["weight"] for edge in edges]
    # similarities = [edge["semantic_similarity"] for edge in edges]
    
    # print(f"🔗 Edges: {len(edges)}")
    # print(f"   - Avg weight: {sum(weights) / len(weights):.3f}")
    # print(f"   - Avg semantic similarity: {sum(similarities) / len(similarities):.3f}")
    
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
