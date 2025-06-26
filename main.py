import asyncio
import os
import argparse
import logging
from pathlib import Path
import yaml
from deepcrawl import deep_crawl
from embed import generate_embeddings



async def run_workflow(args , config : dict ) -> bool : 
    '''run the full workflow : crawl -> embed'''

    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key : 
        logger.error("Gemini api key env var not set")
        return False


    if args.step in ["all" , "crawl"]:
        logger.info("\n Starting deep crawling.. ")

        crawl_success = await deep_crawl(
                url = args.url  ,
                max_depth = args.max_depth or config.get("max_depth" , 3) , 
                max_pages = args.max_pages
or config.get("max_pages" , 50) , 
                output_file = args.crawl_output or config.get("crawl_output" , "output/crawl_output.md")
                )


        if not crawl_success:
            logger.error("deep crawl failed")
            return False

        logger.info("deep crawl completed....")
