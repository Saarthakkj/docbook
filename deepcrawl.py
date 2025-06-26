https://github.com/Saarthakkj/docbook
import asyncio
import os
import json
import base64
from pathlib import Path
from typing import List
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

gemini_api_key = os.getenv("gemini_api_key")

if not gemini_api_key : 
    raise ValueError("Error : gemini api key env var not set")

try : 
    import google.generativeai as genai 

    genai.configure(api_key = gemini_api_key)

    model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")
    response

parser = argparse.ArgumentParser(description = "pass multiple varirables")
parser.add_argument("max_depth"  , type = int , help = "maximum depth of pages")
parser.add_argument ("max_pages" , type = int , help = "maximum number of pages")

parser.add_argument("--url" , type = str  , required = True, help = "doc url")


args = parser.parse_args()



doc_url = args.url 
max_depth = args.max_depth
max_pages = args.max_pages

domain_url = ""
if(doc_url.find('http') !=-1): domain_url = domain_url[7:]
else : domain_url = domain_url[8:]
if(domain_url == ""): print("error , doc url : " , doc_url )
async def deep_crawl(final_md):
    """deep crawl with bfs"""

    print("\n ===== deep crawling == ")

    filter_chain = FilterChain([DomainFilter(allowed_domains=[domain_url])])
    deep_crawl_strategy = BFSDeepCrawlStrategy(
        max_depth= max_depth,  max_pages = max_pages, filter_chain = filter_chain
    )

    async with AsyncWebCrawler() as crawler:
        results : List[CrawlResult] = await crawler.arun(
            url = doc_url, 
            config = CrawlerRunConfig(deep_crawl_strategy = deep_crawl_strategy) ,
        )

        print(f"deep crawl returned  : {len(results)} pages ")
        for i , result in enumerate(results):
            depth = result.metadata.get("depth" , "unknown")
            
            #skipping None or 404
            if(result.markdown is None ) : continue
            condition = result.markdown.find('404') != -1
            if(condition): continue

            final_md.append(result.markdown)
            #try : 
            #    print(f"\n\n -------Result markdown saved : {result.markdown[100:]}\n------markdown ended----\n")
            #except as E :
            #    print(f"no md in this {result.url}")

            #filename = "basic-deepcrawl"
#           print(f"results = {results.extracted_content[100:]} , {results.markdown}) 
            print(f" \n SAVING MARKDWON FOR THIS URL :  {i+1}.{result.url} (depth : {depth}) \n")

async def main(): 
    print("======= running deep crwal ===============" ) 


    final_md = []

    await deep_crawl(final_md)
    final_str = "\n".join(final_md)
    print(f"first 1000 chars : final_str[1000:]")
    try : 
        with open("basic-deepcrawl.md" , "w" , encoding = "utf-8") as file :
            file.write(final_str)
    except Exception as e: 
        print(f"error writing file : {e}")

    print("done")

    

if __name__ == "__main__":
    asyncio.run(main())



