import asyncio
import os
import json
import base64
from pathlib import Path
from typing import List, Optional, Dict
from crawl4ai.proxy_strategy import ProxyConfig
import sys
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, CrawlResult
from crawl4ai import RoundRobinProxyStrategy
from crawl4ai import JsonCssExtractionStrategy, LLMExtractionStrategy
from crawl4ai import LLMConfig
from crawl4ai import PruningContentFilter, BM25ContentFilter
from crawl4ai import DefaultMarkdownGenerator
from crawl4ai import BFSDeepCrawlStrategy, DomainFilter, FilterChain
from crawl4ai import BrowserConfig
import argparse
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from summa import keywords as textrank_keywords
import re
from collections import Counter
from pathlib import Path
from typing import Set, Optional, List, Dict, Any , TypedDict

from dataclasses import dataclass, field


@dataclass
class GraphNode:
    """Simple graph node representation for the crawler"""
    url: str
    content: str
    depth: int
    score: float
    keywords : List[str]
    embedding : List[float]
    children: List['GraphNode'] = field(default_factory=list)
    
    def add_child(self, child_node: 'GraphNode') -> None:
        """Add a child GraphNode to this node"""
        self.children.append(child_node)
    
@dataclass        
class Graph : 
    nodes: Dict[str, GraphNode] = field(default_factory=dict)
    edges: List['Edge'] = field(default_factory=list)
    metadata : metadata = field(default_factory=dict)

        
        
class Edge(TypedDict) : 
    source : str 
    target : str 
    relation_type : str
    common_keywords : List[str]
    semantic_similarity : float
    
class metadata(TypedDict):
    total_nodes: int
    max_depth: int
    root_url: str


top_k = 25


parser = argparse.ArgumentParser(description = "pass multiple varirables")
parser.add_argument("--max_depth"  , type = int  , help = "maximum depth of pages")
parser.add_argument ("--max_pages" , type = int ,  help = "maximum number of pages")

parser.add_argument("--url" , type = str  , required = True, help = "doc url")
parser.add_argument("--output_dir" , type = str  , required = True, help = "output dir")
parser.add_argument("--name" , type = str  , required = True, help = "name")

args = parser.parse_args()



doc_url = args.url 
max_depth = args.max_depth
max_pages = args.max_pages
OUTPUT_DIR = args.output_dir
name = args.name

uris = [[]]


def extract_keywords_textrank(content: str, top_k: int ) -> List[str]:
    """Extract keywords using TextRank algorithm from summa library"""
    # if not TEXTRANK_AVAILABLE or not content.strip():
    #     return extract_keywords_fallback(content, top_k)
    
    try:
        # Clean content and extract keywords
        cleaned_content = re.sub(r'[^\w\s]', ' ', content)
        cleaned_content = re.sub(r'\s+', ' ', cleaned_content).strip()
        
        if len(cleaned_content) < 50:  # Too short for TextRank
            return extract_keywords_fallback(content, top_k)
            
        keywords_text = textrank_keywords.keywords(cleaned_content, words=top_k, split=True)
        return [kw.strip() for kw in keywords_text if kw.strip()]
        
    except Exception as e:
        print(f"⚠️  TextRank failed: {e}. Using fallback method.")
        return extract_keywords_fallback(content, top_k)

def extract_keywords_fallback(content: str, top_k: int = 10) -> List[str]:
    """Fallback keyword extraction using simple frequency analysis"""
    if not content.strip():
        return []
    
    # Remove common stop words
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 
        'by', 'from', 'up', 'about', 'into', 'through', 'during', 'before', 'after', 
        'above', 'below', 'between', 'among', 'is', 'are', 'was', 'were', 'be', 'been', 
        'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 
        'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'i', 
        'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 
        'your', 'his', 'its', 'our', 'their', 'mine', 'yours', 'ours', 'theirs'
    }
    
    # Extract words (alphabetic, length >= 3)
    words = re.findall(r'\b[a-zA-Z]{3,}\b', content.lower())
    
    # Filter out stop words and get frequency
    filtered_words = [word for word in words if word not in stop_words]
    word_freq = Counter(filtered_words)
    
    # Return top k most frequent words
    return [word for word, _ in word_freq.most_common(top_k)]

def get_common_keywords(keywords1: List[str], keywords2: List[str]) -> List[str]:
    """Find common keywords between two lists"""
    set1 = set(keyword.lower() for keyword in keywords1)
    set2 = set(keyword.lower() for keyword in keywords2)
    common = set1.intersection(set2)
    return list(common)


def create_embeddings(content: str) -> List[float]:
    """Create embeddings for a given content"""
    return SentenceTransformer('all-MiniLM-L6-v2').encode(content)
    
def find_parent_node(graph: GraphNode, target_url: str) -> Optional[GraphNode]:
    """
    Search for a parent node that contains the target URL as a child.
    Uses depth-first search to traverse the graph.
    
    Args:
        graph: The root GraphNode of the graph
        target_url: The URL to search for among children
        
    Returns:
        GraphNode if found, None otherwise
    """
    def dfs_search(node: GraphNode) -> Optional[GraphNode]:
        # Check if current node has the target URL as a child
        for child in node.children:
            if child.url == target_url:
                return node
        
        # Recursively search in children
        for child in node.children:
            result = dfs_search(child)
            if result:
                return result
        
        return None
    
    return dfs_search(graph)

def find_node_by_url(graph: GraphNode, target_url: str) -> Optional[GraphNode]:
    """
    Find a specific node by its URL in the graph.
    Uses depth-first search to traverse the graph.
    
    Args:
        graph: The root GraphNode of the graph
        target_url: The URL to search for
        
    Returns:
        GraphNode if found, None otherwise
    """
    def dfs_search(node: GraphNode) -> Optional[GraphNode]:
        if node.url == target_url:
            return node
        
        for child in node.children:
            result = dfs_search(child)
            if result:
                return result
        
        return None
    
    return dfs_search(graph)
    


async def deep_crawl():
    """deep crawl with bfs"""

    print("\n ===== deep crawling == ")
    
    deep_crawl_strategy = BFSDeepCrawlStrategy(    max_depth = float('inf') if max_depth is None else max_depth , include_external = False)
    
    if max_pages is not None : 
        deep_crawl_strategy.max_pages = max_pages
    
    


    async with AsyncWebCrawler() as crawler:
        results : List[CrawlResult] = await crawler.arun(
            url = doc_url, 
            config = CrawlerRunConfig(deep_crawl_strategy = deep_crawl_strategy) ,
        )
        
        root : GraphNode
        graph : Graph = Graph()
        
        # graph.metadata = {'root_url' : doc_url }


        print(f"deep crawl returned  : {len(results)} pages ")
        for i , result in enumerate(results):
            depth = result.metadata.get("depth")
            parent_url = result.metadata.get("parent_url")
            score = result.metadata.get("score", 0.0)  # Get URL relevance score, default to 0.0
            
            #skipping for 404 : 
            if(result.markdown is None ) : continue
            condition = result.markdown.find('404') != -1
            if(condition): continue

            # Debug: Print score information
            # print(f"URL: {result.url[:50]}... | Depth: {depth} | Score: {score:.3f}")
            keywords = extract_keywords_textrank(result.markdown, top_k)
            embedding = create_embeddings(result.markdown)

            if result.url == doc_url : 
                # keywords = extract_keywords_textrank(result.markdown, top_k)
                root = GraphNode(url=doc_url, content=result.markdown, depth=0, score=score, keywords = keywords , embedding = embedding , children = [] )
                graph.nodes[doc_url] = root
                continue
            
            try : 
                
                parent_node = graph.nodes[parent_url]
                child_node = GraphNode(url=result.url, content=result.markdown, depth=depth, score=score , keywords = keywords , embedding = embedding , children = [] )
                parent_node.add_child(child_node)
                graph.nodes[result.url] = child_node
                
                common_keywords = get_common_keywords(parent_node.keywords , keywords)
                semantic_similarity = len(common_keywords) / max(len(parent_node.keywords), len(keywords), 1)
                
                
                graph.edges.append({
                    'source' : parent_node.url , 
                    'target' : result.url , 
                    'relation_type' : 'NAVIGATES_TO' , 
                    'common_keywords' : common_keywords , 
                    'semantic_similarity' : semantic_similarity
                })
            except Exception as e:
                print(f"Error adding child: {e}")
                continue
        
        graph.metadata = {
            'total_nodes' : len(graph.nodes),  
            'max_depth' : max(node.depth for node in graph.nodes.values()) , 
            'root_url' : doc_url
        }
        
    return graph 

def print_graph_structure(root: GraphNode):
    """Pretty-print the graph rooted at ``root`` now that we use ``GraphNode`` objects.

    The routine traverses the graph (DFS), shows each node with its depth, score,
    content length, and the number of children, then outputs summary statistics.
    """

    if root is None:
        print("❌ Graph is empty!")
        return

    # ── Collect all nodes ──────────────────────────────────────────────────────
    all_nodes: List[GraphNode] = []
    stack: List[GraphNode] = [root]
    while stack:
        node = stack.pop()
        all_nodes.append(node)
        stack.extend(node.children)

    # Sort by depth for nicer visual ordering
    all_nodes.sort(key=lambda n: n.depth)

    print("\n" + "=" * 80)
    print("📊 KNOWLEDGE GRAPH STRUCTURE")
    print("=" * 80)

    print(f"📈 Total Nodes: {len(all_nodes)}")
    max_depth_val = max(n.depth for n in all_nodes)
    print(f"🌳 Max Depth: {max_depth_val}")
    print(f"🎯 Root URL: {root.url}")
    print("\n" + "-" * 80)

    # ── Per-node details ─────────────────────────────────────────────────────
    for node in all_nodes:
        indent = "  " * node.depth
        children_count = len(node.children)
        content_length = len(node.content or "")

        print(f"{indent}📍 Node: {node.url[:60]}{'...' if len(node.url) > 60 else ''}")
        print(f"{indent}   ├─ Depth: {node.depth}")
        print(f"{indent}   ├─ Score: {node.score:.3f}")
        print(f"{indent}   ├─ Content Length: {content_length:,} chars")
        print(f"{indent}   └─ Children: {children_count}")

        # Display children URLs
        for idx, child in enumerate(node.children):
            child_prefix = "   └─" if idx == children_count - 1 else "   ├─"
            print(f"{indent}{child_prefix} ➤ {child.url[:50]}{'...' if len(child.url) > 50 else ''}")
        if children_count:
            print()

    # ── Summary statistics ────────────────────────────────────────────────────
    depths = [n.depth for n in all_nodes]
    scores = [n.score for n in all_nodes]
    children_counts = [len(n.children) for n in all_nodes]

    print("=" * 80)
    print("📊 GRAPH SUMMARY")
    print("=" * 80)

    # Depth distribution
    print("📊 Depth Distribution:")
    depth_counts: Dict[int, int] = {}
    for d in depths:
        depth_counts[d] = depth_counts.get(d, 0) + 1
    for d in sorted(depth_counts):
        print(f"   Depth {d}: {depth_counts[d]} nodes")

    # Score statistics
    if scores:
        avg_score = sum(scores) / len(scores)
        print(f"\n📊 Score Statistics:")
        print(f"   Average Score: {avg_score:.3f}")
        print(f"   Max Score: {max(scores):.3f}")
        print(f"   Min Score: {min(scores):.3f}")

    # Connectivity stats
    print(f"\n📊 Connectivity:")
    if children_counts:
        avg_children = sum(children_counts) / len(children_counts)
        print(f"   Average Children per Node: {avg_children:.1f}")
        print(f"   Nodes with Children: {sum(1 for c in children_counts if c > 0)}")
        print(f"   Leaf Nodes: {sum(1 for c in children_counts if c == 0)}")

    print("=" * 80)
                    


def save_graph(graph: GraphNode, filepath: str):
    """Save the knowledge graph to disk with streamlined structure"""
    
    # Collect all nodes from the graph tree
    all_nodes: List[GraphNode] = []
    stack: List[GraphNode] = [graph]
    while stack:
        node = stack.pop()
        all_nodes.append(node)
        stack.extend(node.children)

    # Sort by depth for nicer visual ordering
    all_nodes.sort(key=lambda n: n.depth)
    
    print(f"🔍 Extracting keywords for {len(all_nodes)} nodes...")
    
    # Extract keywords for all nodes
    node_keywords = {}
    for node in all_nodes:
        print(f"  📝 Processing keywords for: {node.url[:50]}...")
        keywords = extract_keywords_textrank(node.content, top_k)
        node_keywords[node.url] = keywords
    
    # Convert GraphNode objects to serializable format
    serializable_graph = {
        "nodes": {},
        "edges": [],
        "metadata": {
            "total_nodes": len(all_nodes),
            "max_depth": max(node.depth for node in all_nodes) if all_nodes else 0,
            "root_url": graph.url,
            
        }
    }
    
    # Create a mapping of URL to GraphNode for easier access
    node_map = {node.url: node for node in all_nodes}
    
    # Process nodes
    for node in all_nodes:
        serializable_graph["nodes"][node.url] = {
            "source_url": node.url,
            "content": node.content,
            # "embedding": getattr(node, 'embedding', None),  # Will be None initially
            "depth": node.depth,
            "score": node.score,
            "keywords": node_keywords.get(node.url, [])
        }
        
        # Process edges (relationships)
        for child in node.children:
            # weight = calculate_link_weight(node.url, child.url, node_map, max_depth)
            
            # Calculate common keywords between parent and child
            parent_keywords = node_keywords.get(node.url, [])
            child_keywords = node_keywords.get(child.url, [])
            common_keywords = get_common_keywords(parent_keywords, child_keywords)
            
            # if weight is not None:  # Only add edges with valid weights
            serializable_graph["edges"].append({
                "source": node.url,
                "target": child.url,
                "relation_type": "NAVIGATES_TO",
                "common_keywords": common_keywords,
                "semantic_similarity": len(common_keywords) / max(len(parent_keywords), len(child_keywords), 1)
            })

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(serializable_graph, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Knowledge graph saved to {filepath}")
    print(f"📊 Added keywords to {len(all_nodes)} nodes and {len(serializable_graph['edges'])} edges")

async def main(url : str , max_depth : int , max_pages : int ) -> GraphNode: 
    print("======= running deep crwal ===============" ) 

    # final_md = []
    
    # print(f"output path : {OUTPUT_DIR}")

    graph  = await deep_crawl()
    
    return graph
    
    # save_graph(graph , "kg.json")
    
    # OUTPUT_PATH = os.path.join(OUTPUT_DIR , "kg.json")
    # save_graph(graph, OUTPUT_PATH)

    # print("done")

    

if __name__ == "__main__":
    asyncio.run(main())




