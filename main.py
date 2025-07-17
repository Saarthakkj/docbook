#!/usr/bin/env python3


'''
TODO : 
    1. check for existing json file for this
    2. save graph dataclasss file as args.name in the same directory
'''

"""
GraphRAG Implementation for Crawl4AI Documentation
Integrates deepcrawl.py output with graphrag_system.py for intelligent querying
"""
from deepcrawl import GraphNode , Graph
import deepcrawl
import asyncio
import argparse
import sys
import subprocess
import os 
import json
import os
from dotenv import load_dotenv
from enhanced_graphrag import EnhancedGraphRAGSystem, create_graphrag_from_kg_json 

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
    parser.add_argument("--output_dir" , type = str  , required = True, help = "output directory")

    parser.add_argument("--name" , type = str  , required = True, help = "name of your documentation")


    return parser.parse_args()


async def run_deepcrawl(url : str , max_depth : int , max_pages : int ) -> Graph:
    """run deepcrawl.py with specified parameters"""
    
    
    return await deepcrawl.main(url , max_depth , max_pages )
    
    
    # print(f" URL : {url} ")
    # print(f" Max depth : {max_depth}")
    # print(f"output : {output_dir}")
    
    # cmd = [sys.executable , "deepcrawl.py"] 
    
    # if max_depth is not None : 
    #     cmd.extend(["--max_depth" , str(max_depth)])
    # if max_pages is not None : 
    #     cmd.extend(["--max_pages" , str(max_pages)])
        
        
    # cmd.extend(["--url" , url])
        
    # cmd.extend(["--output_dir" , output_dir])
    
    
    
    # # cmd = [
    # #     sys.executable , "deepcrawl.py" , 
    # #     "--url" , url , 
    # #     '--max_depth' , str(max_depth) , 
    # #     '--max_pages' , str(max_pages) , 
    # #     '--output_dir' , output_dir
    # # ] 
    
    
    # try : 
    #     print(" executing deepcrawl.py .... ")
        
    #     # result = subprocess.run(cmd , check = True)
        
    #     process = subprocess.Popen(cmd , stdout = subprocess.PIPE , stderr = subprocess.PIPE ,  text = True , bufsize =1 , universal_newlines = True)
    #     # while True :
    #     #     output = process.stdout.readline()
    #     #     if output == '' and process.poll() is not None :
    #     #         break
    #     #     else: print(output.strip())
    #     # return_code = process.poll()
        
    #     output, errors = process.communicate()

    #     print(output)
    #     print(errors)


        
    #     # if return_code != 0:
    #     #     print(f"❌ Deepcrawl failed with return code: {return_code}")
    #     #     print(f" error : {process.stderr}")
    #     #     raise subprocess.CalledProcessError(return_code, cmd)
        
    #     # print("\nDeepcrawl completed successfully! ")
        
        
    # except Exception as e : 
    #     print(f" Unexpected error : {e}")
    #     raise

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
    print("📂 Loading graphRG system.....")
    
    rag_system = None
    
    #check for existing json file for this
    
    # kg_path = os.path.join(sys.path , args.name)
    # if os.path.exists(kg_path):
    #     print(f"Found existing file for the given name {args.name}")
    #     # if exists -> then just call the graphRAG implementation
    # else:
    #     raise FileNotFoundError
    graph = await run_deepcrawl(args.url , args.max_depth , args.max_pages)
    rag_system = await create_graphrag_from_kg_json(
        graph, 
        gemini_api_key
    )
    print("🤖 GraphRAG Query Interface Ready!")
    print(f"Ask questions about {args.name} documentation.")
    print("Type 'quit' to exit.")
    print("=" * 60)
    
    
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
