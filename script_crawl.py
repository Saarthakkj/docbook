
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

strategy = BFSDeepCrawlStrategy(
    max_depth = 2,
    max_pages = 2,
    include_external = True
)

markdown_generator = DefaultMarkdownGenerator()
config = CrawlerRunConfig(
    stream = False
    ,deep_crawl_strategy = strategy,
    scraping_strategy = LXMLWebScrapingStrategy(),
    markdown_generator = markdown_generator,
    verbose = True
)

async def main(): 
    urls = [
        "https://developer.chrome.com/docs/extensions/get-started" , 
        "https://developer.chrome.com/docs/extensions/develop",
        "https://developer.chrome.com/docs/extensions/how-to" , 
        "https://developer.chrome.com/docs/extensions/reference"
    ]
    async with AsyncWebCrawler() as crawler:
        tasks = [
                asyncio.ensure_future(
                    crawler.arun_many(urls , config = config)
                ) 
        ]

        results = await asyncio.gather(*tasks)
        #try: 
            #print(f"type = {type(results)} , {type(results[0])}, {type(results[0][0])}  , ec = {results[0][0].extractedcontent}")
        #except : 
        #    print("error in extracting content)
        for res in results : 
            for _ in res : 
                filename = "docsmany"
                print(f"results = {_.extracted_content} , {_.markdown}")
                with open("docsmany", "a", encoding = "utf-8") as file:
                    try:
                        file.write(_.markdown)
                    except : 
                        print("error in ")
        print(f"Saved: {filename}")


if __name__ == "__main__":
    asyncio.run(main())
