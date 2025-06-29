#!/usr/bin/env python3
"""
GraphRAG Implementation for Crawl4AI Documentation
Integrates deepcrawl.py output with graphrag_system.py for intelligent querying
"""

import asyncio
import argparse
import sys
import subprocess
import os 
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
    parser.add_argument("--output_dir" , type = str  , required = True, help = "output dir")


    return parser.parse_args()


async def run_deepcrawl(url : str , max_depth : int , max_pages : int , output_dir : str = "kg.json"):
    """run deepcrawl.py with specified parameters"""
    
    
    print(f" URL : {url} ")
    print(f" Max depth : {max_depth}")
    print(f"output : {output_dir}")
    
    cmd = [sys.executable , "deepcrawl.py"] 
    
    if max_depth is not None : 
        cmd.extend(["--max_depth" , str(max_depth)])
    if max_pages is not None : 
        cmd.extend(["--max_pages" , str(max_pages)])
        
        
    cmd.extend(["--url" , url])
        
    cmd.extend(["--output_dir" , output_dir])
    
    
    
    # cmd = [
    #     sys.executable , "deepcrawl.py" , 
    #     "--url" , url , 
    #     '--max_depth' , str(max_depth) , 
    #     '--max_pages' , str(max_pages) , 
    #     '--output_dir' , output_dir
    # ] 
    
    
    try : 
        print(" executing deepcrawl.py .... ")
        
        # result = subprocess.run(cmd , check = True)
        
        process = subprocess.Popen(cmd , stdout = subprocess.PIPE , stderr = subprocess.PIPE ,  text = True , bufsize =1 , universal_newlines = True)
        # while True :
        #     output = process.stdout.readline()
        #     if output == '' and process.poll() is not None :
        #         break
        #     else: print(output.strip())
        # return_code = process.poll()
        
        output, errors = process.communicate()

        print(output)
        print(errors)


        
        # if return_code != 0:
        #     print(f"❌ Deepcrawl failed with return code: {return_code}")
        #     print(f" error : {process.stderr}")
        #     raise subprocess.CalledProcessError(return_code, cmd)
        
        # print("\nDeepcrawl completed successfully! ")
        
        
    except Exception as e : 
        print(f" Unexpected error : {e}")
        raise

async def main():
    """Main function to demonstrate GraphRAG implementation"""
    
    
    args = parse_arguments()
    # Check for required API key
    gemini_api_key = os.getenv("gemini_api_key")
    if not gemini_api_key:
        print("❌ Error: GEMINI_API_KEY environment variable not set")
        print("Please set your Gemini API key in the .env file")
        return
    
    print("🚀 Starting Docbook ")
    print("=" * 60)
    
    
    # Step 1: Load the knowledge graph from deepcrawl.py output
    print("📂 Loading knowledge graph from kg.json...")
    
    kg_path = os.path.join(args.output_dir , "kg.json")
    try:
        with open(kg_path ,  "r", encoding="utf-8") as f:
            kg_data = json.load(f)
        
        print(f"✅ Loaded knowledge graph:")
        print(f"   - Nodes: {len(kg_data['nodes'])}")
        print(f"   - Edges: {len(kg_data['edges'])}")
        print(f"   - Root URL: {kg_data['metadata']['root_url']}")
        
    except Exception as e:
        print(f"❌ Error loading kg.json. Running deepcrawl.py")
        await run_deepcrawl(args.url , args.max_depth , args.max_pages , args.output_dir)
        
    # except json.JSONDecodeError as e:
    #     print(f"❌ Error loading kg.json: {e}")
    #     return
    
    rag_system = None
    
    # Check if enhanced_kg.json exists
    enhanced_kg_path = os.path.join(args.output_dir  , "enhanced_kg.json")
    
    
    # Replace the problematic section in main() with:
    if os.path.exists(enhanced_kg_path):
        print(f"✅ Found existing enhanced knowledge graph: {enhanced_kg_path}")
        print("Loading existing enhanced GraphRAG system...")
        
        # Load from enhanced_kg.json with fallback to original kg.json for content
        rag_system = await create_graphrag_from_enhanced_kg(
            enhanced_kg_path, 
            gemini_api_key, 
            original_kg_path=kg_path
        )
    else:
        # Step 2: Initialize Enhanced GraphRAG system directly from kg.json
        print("\n🧠 Initializing Enhanced GraphRAG system...")
        rag_system = await create_graphrag_from_kg_json(kg_path, gemini_api_key)
        
        # Step 3: Save the enhanced knowledge graph
        print("💾 Saving enhanced knowledge graph...")
        rag_system.save_enhanced_kg(enhanced_kg_path)
        
    

# def convert_kg_to_url_graph(kg_data):
#     """
#     Convert kg.json format to the format expected by GraphRAG system
    
#     Args:
#         kg_data: The loaded kg.json data
        
#     Returns:
#         dict: URL graph in GraphRAG format
#     """
#     url_graph = {}
    
#     # Convert nodes to the expected format
#     for url, node_data in kg_data["nodes"].items():
#         url_graph[url] = {
#             "content": node_data["content"],
#             "keywords": node_data.get("keywords", []),
#             "depth": node_data.get("depth", 0),
#             "score": node_data.get("score", 1.0),
#             # Additional metadata that might be useful
#             "metadata": {
#                 "source_url": node_data["source_url"],
#                 "embedding": node_data.get("embedding")
#             }
#         }
    
#     return url_graph


if __name__ == "__main__":
    asyncio.run(main())
