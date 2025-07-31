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
from deepcrawl import save_graph

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
    
    kg_path = os.path.join(args.output_dir, f"{args.name}_kg.json")

    if os.path.exists(kg_path):
        print(f"Found existing knowledge graph at {kg_path}")
        with open(kg_path, 'r', encoding='utf-8') as f:
            raw = f.read()
            #print(f" raw : {raw} and len : {len(raw)}")
            kg_data = json.load(f)
        graph = Graph()
        graph.metadata = kg_data['metadata']
        node_map = {}
        for url, data in kg_data['nodes'].items():
            node = GraphNode(
                url=data['source_url'],
                content=data['content'],
                depth=data['depth'],
                score=data['score'],
                keywords=data['keywords'],
                embedding=['embedding'],
                children=['children']
            )
            node_map[url] = node
            graph.nodes[url] = node
        for edge_data in kg_data['edges']:
            source = edge_data['source']
            target = edge_data['target']
            if source in node_map and target in node_map:
                node_map[source].add_child(node_map[target])
            graph.edges.append(edge_data)
    else:
        print(f"No existing graph found, running deepcrawl...")
        graph = await run_deepcrawl(args.url, args.max_depth, args.max_pages)
        root = graph.nodes[args.url]
        save_graph(root, kg_path)
        print(f"Knowledge graph saved to {kg_path}")

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

    
    

    



if __name__ == "__main__":
    asyncio.run(main())
