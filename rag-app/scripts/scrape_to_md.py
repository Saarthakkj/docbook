import asyncio
import os
import json
import sys
import re
import base64
from pathlib import Path
from typing import List
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, CrawlResult
from crawl4ai import RoundRobinProxyStrategy
from crawl4ai import JsonCssExtractionStrategy, LLMExtractionStrategy
from crawl4ai import LLMConfig
from crawl4ai import PruningContentFilter, BM25ContentFilter
from crawl4ai import DefaultMarkdownGenerator
from crawl4ai import BFSDeepCrawlStrategy, DomainFilter, FilterChain
from crawl4ai import BrowserConfig


async def deep_crawl(url, final_md):
    """deep crawl with bfs"""

    print(f"\n ===== deep crawling {url} == ")
    
    # Extract domain from the URL
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    filter_chain = FilterChain([DomainFilter(allowed_domains=[domain])])
    deep_crawl_strategy = BFSDeepCrawlStrategy(
        max_depth=100, max_pages=1000, filter_chain=filter_chain
    )

    async with AsyncWebCrawler() as crawler:
        try :
            print(f"url : {url}")
            results: List[CrawlResult] = await crawler.arun(
                url=url, 
                config=CrawlerRunConfig(deep_crawl_strategy=deep_crawl_strategy),
            )
        except Exception as e:  
            print(f"Error during crawling: {e}")
            return
        print(f"crawled {len(results)} pages")

        print(f"deep crawl returned: {len(results)} pages")
        for i, result in enumerate(results):
            depth = result.metadata.get("depth", "unknown")
            
            # Skipping None or 404
            if result.markdown is None:
                continue
                
            condition = result.markdown.find('404') != -1
            if condition:
                continue

            final_md.append(result.markdown)
            print(f"\nSAVING MARKDOWN FOR THIS URL: {i+1}.{result.url} (depth: {depth})")


async def main():
    # Check for command line arguments
    if len(sys.argv) < 2:
        print("Usage: python scrape_to_md.py <url> [output_file]")
        sys.exit(1)
    
    # Get URL from command line argument
    url = sys.argv[1]
    
    # Get output file path (optional second argument)
    output_file = sys.argv[2] if len(sys.argv) > 2 else "context.md"
    
    print(f"======= running deep crawl for {url} ===============")
    print(f"Output will be saved to: {output_file}")

    final_md = []

    await deep_crawl(url, final_md)
    final_str = "\n".join(final_md)
    print(f"Generated content with {len(final_str)} characters")

    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(final_str)
        print(f"Content saved to {output_file}")
    except Exception as e:
        print(f"Error writing file: {e}")

    print("done")


if __name__ == "__main__":
    asyncio.run(main())


