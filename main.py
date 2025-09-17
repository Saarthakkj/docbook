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
from deepcrawl import  save_graph_hdf5

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

import json
import os

def inspect_saved_graph(filepath: str):
    """Inspect what's actually in the saved JSON file"""
    print(f"🔍 Inspecting saved graph: {filepath}")
    
    if not os.path.exists(filepath):
        print("❌ File doesn't exist")
        return
    
    file_size = os.path.getsize(filepath)
    print(f"📏 File size: {file_size} bytes")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print("📊 JSON structure analysis:")
        print(f"  🗂️  Top-level keys: {list(data.keys())}")
        
        if 'metadata' in data:
            print(f"  📈 Metadata: {data['metadata']}")
        
        if 'nodes' in data:
            node_count = len(data['nodes'])
            print(f"  🌐 Nodes count: {node_count}")
            
            if node_count > 0:
                # Show first few node keys
                node_keys = list(data['nodes'].keys())[:3]
                print(f"  🔑 Sample node keys: {node_keys}")
                
                # Show structure of first node
                if node_keys:
                    first_node = data['nodes'][node_keys[0]]
                    print(f"  📝 First node structure: {list(first_node.keys())}")
                    print(f"  📄 First node content length: {len(first_node.get('content', ''))}")
                    print(f"  🏷️  First node keywords count: {len(first_node.get('keywords', []))}")
            else:
                print("  ⚠️  No nodes found!")
        
        if 'edges' in data:
            edge_count = len(data['edges'])
            print(f"  🔗 Edges count: {edge_count}")
            
            if edge_count > 0:
                print(f"  🔗 First edge: {data['edges'][0]}")
            else:
                print("  ⚠️  No edges found!")
        
        return data
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error: {e}")
    except Exception as e:
        print(f"❌ Error reading file: {e}")

def debug_graph_before_save(graph):
    """Debug the graph object before saving"""
    print("🔍 Debugging graph object before save:")
    print(f"  🌐 Root URL: {graph.url}")
    print(f"  📊 Root depth: {graph.depth}")
    print(f"  📄 Root content length: {len(graph.content) if graph.content else 0}")
    print(f"  🔗 Root children count: {len(graph.children)}")
    
    # Traverse and count all nodes
    all_nodes = []
    stack = [graph]
    while stack:
        node = stack.pop()
        all_nodes.append(node)
        stack.extend(node.children)
    
    print(f"  🌳 Total nodes in tree: {len(all_nodes)}")
    
    # Show depth distribution
    depth_counts = {}
    for node in all_nodes:
        depth_counts[node.depth] = depth_counts.get(node.depth, 0) + 1
    
    print(f"  📊 Depth distribution: {depth_counts}")
    
    # Show some sample URLs
    sample_urls = [node.url for node in all_nodes[:5]]
    print(f"  🔗 Sample URLs: {sample_urls}")
    
    # Check for empty content
    empty_content_count = sum(1 for node in all_nodes if not node.content or len(node.content.strip()) == 0)
    print(f"  ⚠️  Nodes with empty content: {empty_content_count}/{len(all_nodes)}")
    
    return all_nodes

def debug_save_process(graph, filepath: str):
    """Debug the entire save process step by step"""
    print("🚀 Starting comprehensive save debug...")
    
    # 1. Debug input graph
    all_nodes = debug_graph_before_save(graph)
    
    if len(all_nodes) == 0:
        print("❌ PROBLEM: Graph has no nodes!")
        return
    
    if len(all_nodes) == 1:
        print("⚠️  WARNING: Graph has only root node (no children crawled)")
    
    # 2. Test keyword extraction on a sample
    print("\n🔍 Testing keyword extraction...")
    try:
        sample_node = all_nodes[0]
        if hasattr(sample_node, 'content') and sample_node.content:
            print(f"  📝 Sample content length: {len(sample_node.content)}")
            # Test if extract_keywords_textrank function exists and works
            try:
                keywords = extract_keywords_textrank(sample_node.content, 5)  # Assuming top_k=5
                print(f"  ✅ Keywords extracted: {keywords}")
            except NameError:
                print("  ❌ extract_keywords_textrank function not defined!")
            except Exception as e:
                print(f"  ❌ Keyword extraction failed: {e}")
        else:
            print("  ⚠️  Sample node has no content")
    except Exception as e:
        print(f"  ❌ Error testing keywords: {e}")
    
    # 3. Test common keywords function
    print("\n🔍 Testing common keywords function...")
    try:
        test_result = get_common_keywords(['test', 'word'], ['test', 'another'])
        print(f"  ✅ get_common_keywords works: {test_result}")
    except NameError:
        print("  ❌ get_common_keywords function not defined!")
    except Exception as e:
        print(f"  ❌ get_common_keywords failed: {e}")
    
    # 4. Now try the actual save
    print(f"\n💾 Attempting save to: {filepath}")
    try:
        save_graph(graph, filepath)
        
        # 5. Inspect what was actually saved
        print("\n🔍 Inspecting saved result...")
        inspect_saved_graph(filepath)
        
    except Exception as e:
        print(f"❌ Save failed: {e}")
        import traceback
        traceback.print_exc()

import h5py
import numpy as np


def load_graph_hdf5(filepath: str) -> Graph:
    """Load the knowledge graph from HDF5 and reconstruct the GraphNode tree."""
    
    with h5py.File(filepath, "r") as f:
        # Load metadata
        metadata = {}
        if "metadata" in f:
            meta_grp = f["metadata"]
            for k in meta_grp.attrs:
                metadata[k] = meta_grp.attrs[k]
        root_url = metadata.get("root_url")
        if not root_url:
            raise ValueError("No root_url found in metadata")

        # Load nodes into a dict (url -> GraphNode)
        node_map = {}
        if "nodes" in f:
            nodes_grp = f["nodes"]
            for url in nodes_grp:
                node_grp = nodes_grp[url]
                
                # Reconstruct GraphNode (adjust init params to match your class)
                node = GraphNode(
                    url=url,
                    content=node_grp.attrs.get("content", ""),
                    embedding=None,  # Set below
                    depth=node_grp.attrs.get("depth", 0),
                    keywords=node_grp.attrs.get("keywords" , [])
                )
                
                # Embedding
                # if "embedding" in node_grp:
                #     node.embedding = node_grp["embedding"][:].tolist()
                
                # # Keywords (add as attribute)
                # if "keywords" in node_grp:
                #     keywords_array = node_grp["keywords"][:]
                #     node.keywords = [kw.decode("utf-8") for kw in keywords_array]  # Decode to list[str]
                
                node_map[url] = node
        else:
            raise ValueError("No nodes found in HDF5 file.")

        # Load and apply edges to link children
        graph = Graph(nodes=node_map, edges=[], metadata=metadata)
        if "edges" in f:
            edges_dataset = f["edges"][:]
            for edge in edges_dataset:
                source = edge["source"].decode("utf-8")
                target = edge["target"].decode("utf-8")
                rel_type = edge["type"].decode("utf-8")
                sim = edge["sim"]
                common_kw_str = edge["common_keywords"].decode("utf-8")
                common_kw = common_kw_str.split(',') if common_kw_str else []

                # Link children (as before)
                if source in node_map and target in node_map:
                    node_map[source].children.append(node_map[target])

                # Add full Edge to graph.edges
                graph.edges.append({
                    'source': source,
                    'target': target,
                    # 'relation_type': rel_type,
                    'common_keywords': common_kw,
                    'semantic_similarity': sim
                })
        return graph
            
    #     # Return the root node
    # root = node_map.get(root_url)
    # if not root:
    #     raise ValueError(f"Root node {root_url} not found in loaded nodes")
    
    # print(
    #     f"📂 Loaded graph from {filepath} with {len(node_map)} nodes (root: {root_url})"
    # )
    # return root

# Quick function to check if your graph is actually populated
def quick_graph_check(graph):
    """Quick check of graph content"""
    stack = [graph]
    nodes = []
    while stack:
        node = stack.pop()
        nodes.append(node)
        stack.extend(node.children)
    
    print(f"Quick check: {len(nodes)} nodes, depths: {[n.depth for n in nodes[:10]]}")
    return len(nodes) > 1  # More than just root
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
    
    kg_path = os.path.join(args.output_dir, f"{args.name}_kg.h5")

    if os.path.exists(kg_path):
        print(f"Found existing knowledge graph at {kg_path}")
        graph = load_graph_hdf5(kg_path)
    else:
        print(f"No existing graph found, running deepcrawl...")
        graph = await run_deepcrawl(args.url, args.max_depth, args.max_pages)
        # root = graph.nodes[args.url]
        save_graph_hdf5(graph, kg_path)
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
