[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com)


  * Home
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [🚀🤖 Crawl4AI: Open-Source LLM-Friendly Web Crawler & Scraper](https://docs.crawl4ai.com#crawl4ai-open-source-llm-friendly-web-crawler-scraper)
  * [Quick Start](https://docs.crawl4ai.com#quick-start)
  * [What Does Crawl4AI Do?](https://docs.crawl4ai.com#what-does-crawl4ai-do)
  * [Documentation Structure](https://docs.crawl4ai.com#documentation-structure)
  * [How You Can Support](https://docs.crawl4ai.com#how-you-can-support)
  * [Quick Links](https://docs.crawl4ai.com#quick-links)


# 🚀🤖 Crawl4AI: Open-Source LLM-Friendly Web Crawler & Scraper
[ ![unclecode%2Fcrawl4ai | Trendshift](https://trendshift.io/api/badge/repositories/11716) ](https://trendshift.io/repositories/11716)
[ ![GitHub Stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social) ](https://github.com/unclecode/crawl4ai/stargazers) [ ![GitHub Forks](https://img.shields.io/github/forks/unclecode/crawl4ai?style=social) ](https://github.com/unclecode/crawl4ai/network/members) [ ![PyPI version](https://badge.fury.io/py/crawl4ai.svg) ](https://badge.fury.io/py/crawl4ai)
[ ![Python Version](https://img.shields.io/pypi/pyversions/crawl4ai) ](https://pypi.org/project/crawl4ai/) [ ![Downloads](https://static.pepy.tech/badge/crawl4ai/month) ](https://pepy.tech/project/crawl4ai) [ ![License](https://img.shields.io/github/license/unclecode/crawl4ai) ](https://github.com/unclecode/crawl4ai/blob/main/LICENSE)
Crawl4AI is the #1 trending GitHub repository, actively maintained by a vibrant community. It delivers blazing-fast, AI-ready web crawling tailored for large language models, AI agents, and data pipelines. Fully open source, flexible, and built for real-time performance, **Crawl4AI** empowers developers with unmatched speed, precision, and deployment ease.
> **Note** : If you're looking for the old documentation, you can access it [here](https://old.docs.crawl4ai.com).
## Quick Start
Here's a quick example to show you how easy it is to use Crawl4AI with its asynchronous capabilities:
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  # Create an instance of AsyncWebCrawler
  async with AsyncWebCrawler() as crawler:
    # Run the crawler on a URL
    result = await crawler.arun(url="https://crawl4ai.com")
    # Print the extracted content
    print(result.markdown)
# Run the async main function
asyncio.run(main())

```

## What Does Crawl4AI Do?
Crawl4AI is a feature-rich crawler and scraper that aims to:
1. **Generate Clean Markdown** : Perfect for RAG pipelines or direct ingestion into LLMs. 2. **Structured Extraction** : Parse repeated patterns with CSS, XPath, or LLM-based extraction. 3. **Advanced Browser Control** : Hooks, proxies, stealth modes, session re-use—fine-grained control. 4. **High Performance** : Parallel crawling, chunk-based extraction, real-time use cases. 5. **Open Source** : No forced API keys, no paywalls—everyone can access their data. 
**Core Philosophies** : - **Democratize Data** : Free to use, transparent, and highly configurable. - **LLM Friendly** : Minimally processed, well-structured text, images, and metadata, so AI models can easily consume it.
## Documentation Structure
To help you get started, we’ve organized our docs into clear sections:
  * **Setup & Installation** Basic instructions to install Crawl4AI via pip or Docker. 
  * **Quick Start** A hands-on introduction showing how to do your first crawl, generate Markdown, and do a simple extraction. 
  * **Core** Deeper guides on single-page crawling, advanced browser/crawler parameters, content filtering, and caching. 
  * **Advanced** Explore link & media handling, lazy loading, hooking & authentication, proxies, session management, and more. 
  * **Extraction** Detailed references for no-LLM (CSS, XPath) vs. LLM-based strategies, chunking, and clustering approaches. 
  * **API Reference** Find the technical specifics of each class and method, including `AsyncWebCrawler`, `arun()`, and `CrawlResult`.


Throughout these sections, you’ll find code samples you can **copy-paste** into your environment. If something is missing or unclear, raise an issue or PR.
## How You Can Support
  * **Star & Fork**: If you find Crawl4AI helpful, star the repo on GitHub or fork it to add your own features. 
  * **File Issues** : Encounter a bug or missing feature? Let us know by filing an issue, so we can improve. 
  * **Pull Requests** : Whether it’s a small fix, a big feature, or better docs—contributions are always welcome. 
  * **Join Discord** : Come chat about web scraping, crawling tips, or AI workflows with the community. 
  * **Spread the Word** : Mention Crawl4AI in your blog posts, talks, or on social media. 


**Our mission** : to empower everyone—students, researchers, entrepreneurs, data scientists—to access, parse, and shape the world’s data with speed, cost-efficiency, and creative freedom.
## Quick Links
  * **[GitHub Repo](https://github.com/unclecode/crawl4ai)**
  * **[Installation Guide](https://docs.crawl4ai.com/core/installation/)**
  * **[Quick Start](https://docs.crawl4ai.com/core/quickstart/)**
  * **[API Reference](https://docs.crawl4ai.com/api/async-webcrawler/)**
  * **[Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)**


Thank you for joining me on this journey. Let’s keep building an **open, democratic** approach to data extraction and AI together.
Happy Crawling! — _Unclecode, Founder & Maintainer of Crawl4AI_
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/)


  * Home
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [🚀🤖 Crawl4AI: Open-Source LLM-Friendly Web Crawler & Scraper](https://docs.crawl4ai.com/#crawl4ai-open-source-llm-friendly-web-crawler-scraper)
  * [Quick Start](https://docs.crawl4ai.com/#quick-start)
  * [What Does Crawl4AI Do?](https://docs.crawl4ai.com/#what-does-crawl4ai-do)
  * [Documentation Structure](https://docs.crawl4ai.com/#documentation-structure)
  * [How You Can Support](https://docs.crawl4ai.com/#how-you-can-support)
  * [Quick Links](https://docs.crawl4ai.com/#quick-links)


# 🚀🤖 Crawl4AI: Open-Source LLM-Friendly Web Crawler & Scraper
[ ![unclecode%2Fcrawl4ai | Trendshift](https://trendshift.io/api/badge/repositories/11716) ](https://trendshift.io/repositories/11716)
[ ![GitHub Stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social) ](https://github.com/unclecode/crawl4ai/stargazers) [ ![GitHub Forks](https://img.shields.io/github/forks/unclecode/crawl4ai?style=social) ](https://github.com/unclecode/crawl4ai/network/members) [ ![PyPI version](https://badge.fury.io/py/crawl4ai.svg) ](https://badge.fury.io/py/crawl4ai)
[ ![Python Version](https://img.shields.io/pypi/pyversions/crawl4ai) ](https://pypi.org/project/crawl4ai/) [ ![Downloads](https://static.pepy.tech/badge/crawl4ai/month) ](https://pepy.tech/project/crawl4ai) [ ![License](https://img.shields.io/github/license/unclecode/crawl4ai) ](https://github.com/unclecode/crawl4ai/blob/main/LICENSE)
Crawl4AI is the #1 trending GitHub repository, actively maintained by a vibrant community. It delivers blazing-fast, AI-ready web crawling tailored for large language models, AI agents, and data pipelines. Fully open source, flexible, and built for real-time performance, **Crawl4AI** empowers developers with unmatched speed, precision, and deployment ease.
> **Note** : If you're looking for the old documentation, you can access it [here](https://old.docs.crawl4ai.com).
## Quick Start
Here's a quick example to show you how easy it is to use Crawl4AI with its asynchronous capabilities:
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  # Create an instance of AsyncWebCrawler
  async with AsyncWebCrawler() as crawler:
    # Run the crawler on a URL
    result = await crawler.arun(url="https://crawl4ai.com")
    # Print the extracted content
    print(result.markdown)
# Run the async main function
asyncio.run(main())

```

## What Does Crawl4AI Do?
Crawl4AI is a feature-rich crawler and scraper that aims to:
1. **Generate Clean Markdown** : Perfect for RAG pipelines or direct ingestion into LLMs. 2. **Structured Extraction** : Parse repeated patterns with CSS, XPath, or LLM-based extraction. 3. **Advanced Browser Control** : Hooks, proxies, stealth modes, session re-use—fine-grained control. 4. **High Performance** : Parallel crawling, chunk-based extraction, real-time use cases. 5. **Open Source** : No forced API keys, no paywalls—everyone can access their data. 
**Core Philosophies** : - **Democratize Data** : Free to use, transparent, and highly configurable. - **LLM Friendly** : Minimally processed, well-structured text, images, and metadata, so AI models can easily consume it.
## Documentation Structure
To help you get started, we’ve organized our docs into clear sections:
  * **Setup & Installation** Basic instructions to install Crawl4AI via pip or Docker. 
  * **Quick Start** A hands-on introduction showing how to do your first crawl, generate Markdown, and do a simple extraction. 
  * **Core** Deeper guides on single-page crawling, advanced browser/crawler parameters, content filtering, and caching. 
  * **Advanced** Explore link & media handling, lazy loading, hooking & authentication, proxies, session management, and more. 
  * **Extraction** Detailed references for no-LLM (CSS, XPath) vs. LLM-based strategies, chunking, and clustering approaches. 
  * **API Reference** Find the technical specifics of each class and method, including `AsyncWebCrawler`, `arun()`, and `CrawlResult`.


Throughout these sections, you’ll find code samples you can **copy-paste** into your environment. If something is missing or unclear, raise an issue or PR.
## How You Can Support
  * **Star & Fork**: If you find Crawl4AI helpful, star the repo on GitHub or fork it to add your own features. 
  * **File Issues** : Encounter a bug or missing feature? Let us know by filing an issue, so we can improve. 
  * **Pull Requests** : Whether it’s a small fix, a big feature, or better docs—contributions are always welcome. 
  * **Join Discord** : Come chat about web scraping, crawling tips, or AI workflows with the community. 
  * **Spread the Word** : Mention Crawl4AI in your blog posts, talks, or on social media. 


**Our mission** : to empower everyone—students, researchers, entrepreneurs, data scientists—to access, parse, and shape the world’s data with speed, cost-efficiency, and creative freedom.
## Quick Links
  * **[GitHub Repo](https://github.com/unclecode/crawl4ai)**
  * **[Installation Guide](https://docs.crawl4ai.com/core/installation/)**
  * **[Quick Start](https://docs.crawl4ai.com/core/quickstart/)**
  * **[API Reference](https://docs.crawl4ai.com/api/async-webcrawler/)**
  * **[Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)**


Thank you for joining me on this journey. Let’s keep building an **open, democratic** approach to data extraction and AI together.
Happy Crawling! — _Unclecode, Founder & Maintainer of Crawl4AI_
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/)


  * Home
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [🚀🤖 Crawl4AI: Open-Source LLM-Friendly Web Crawler & Scraper](https://docs.crawl4ai.com/#crawl4ai-open-source-llm-friendly-web-crawler-scraper)
  * [Quick Start](https://docs.crawl4ai.com/#quick-start)
  * [What Does Crawl4AI Do?](https://docs.crawl4ai.com/#what-does-crawl4ai-do)
  * [Documentation Structure](https://docs.crawl4ai.com/#documentation-structure)
  * [How You Can Support](https://docs.crawl4ai.com/#how-you-can-support)
  * [Quick Links](https://docs.crawl4ai.com/#quick-links)


# 🚀🤖 Crawl4AI: Open-Source LLM-Friendly Web Crawler & Scraper
[ ![unclecode%2Fcrawl4ai | Trendshift](https://trendshift.io/api/badge/repositories/11716) ](https://trendshift.io/repositories/11716)
[ ![GitHub Stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social) ](https://github.com/unclecode/crawl4ai/stargazers) [ ![GitHub Forks](https://img.shields.io/github/forks/unclecode/crawl4ai?style=social) ](https://github.com/unclecode/crawl4ai/network/members) [ ![PyPI version](https://badge.fury.io/py/crawl4ai.svg) ](https://badge.fury.io/py/crawl4ai)
[ ![Python Version](https://img.shields.io/pypi/pyversions/crawl4ai) ](https://pypi.org/project/crawl4ai/) [ ![Downloads](https://static.pepy.tech/badge/crawl4ai/month) ](https://pepy.tech/project/crawl4ai) [ ![License](https://img.shields.io/github/license/unclecode/crawl4ai) ](https://github.com/unclecode/crawl4ai/blob/main/LICENSE)
Crawl4AI is the #1 trending GitHub repository, actively maintained by a vibrant community. It delivers blazing-fast, AI-ready web crawling tailored for large language models, AI agents, and data pipelines. Fully open source, flexible, and built for real-time performance, **Crawl4AI** empowers developers with unmatched speed, precision, and deployment ease.
> **Note** : If you're looking for the old documentation, you can access it [here](https://old.docs.crawl4ai.com).
## Quick Start
Here's a quick example to show you how easy it is to use Crawl4AI with its asynchronous capabilities:
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  # Create an instance of AsyncWebCrawler
  async with AsyncWebCrawler() as crawler:
    # Run the crawler on a URL
    result = await crawler.arun(url="https://crawl4ai.com")
    # Print the extracted content
    print(result.markdown)
# Run the async main function
asyncio.run(main())

```

## What Does Crawl4AI Do?
Crawl4AI is a feature-rich crawler and scraper that aims to:
1. **Generate Clean Markdown** : Perfect for RAG pipelines or direct ingestion into LLMs. 2. **Structured Extraction** : Parse repeated patterns with CSS, XPath, or LLM-based extraction. 3. **Advanced Browser Control** : Hooks, proxies, stealth modes, session re-use—fine-grained control. 4. **High Performance** : Parallel crawling, chunk-based extraction, real-time use cases. 5. **Open Source** : No forced API keys, no paywalls—everyone can access their data. 
**Core Philosophies** : - **Democratize Data** : Free to use, transparent, and highly configurable. - **LLM Friendly** : Minimally processed, well-structured text, images, and metadata, so AI models can easily consume it.
## Documentation Structure
To help you get started, we’ve organized our docs into clear sections:
  * **Setup & Installation** Basic instructions to install Crawl4AI via pip or Docker. 
  * **Quick Start** A hands-on introduction showing how to do your first crawl, generate Markdown, and do a simple extraction. 
  * **Core** Deeper guides on single-page crawling, advanced browser/crawler parameters, content filtering, and caching. 
  * **Advanced** Explore link & media handling, lazy loading, hooking & authentication, proxies, session management, and more. 
  * **Extraction** Detailed references for no-LLM (CSS, XPath) vs. LLM-based strategies, chunking, and clustering approaches. 
  * **API Reference** Find the technical specifics of each class and method, including `AsyncWebCrawler`, `arun()`, and `CrawlResult`.


Throughout these sections, you’ll find code samples you can **copy-paste** into your environment. If something is missing or unclear, raise an issue or PR.
## How You Can Support
  * **Star & Fork**: If you find Crawl4AI helpful, star the repo on GitHub or fork it to add your own features. 
  * **File Issues** : Encounter a bug or missing feature? Let us know by filing an issue, so we can improve. 
  * **Pull Requests** : Whether it’s a small fix, a big feature, or better docs—contributions are always welcome. 
  * **Join Discord** : Come chat about web scraping, crawling tips, or AI workflows with the community. 
  * **Spread the Word** : Mention Crawl4AI in your blog posts, talks, or on social media. 


**Our mission** : to empower everyone—students, researchers, entrepreneurs, data scientists—to access, parse, and shape the world’s data with speed, cost-efficiency, and creative freedom.
## Quick Links
  * **[GitHub Repo](https://github.com/unclecode/crawl4ai)**
  * **[Installation Guide](https://docs.crawl4ai.com/core/installation/)**
  * **[Quick Start](https://docs.crawl4ai.com/core/quickstart/)**
  * **[API Reference](https://docs.crawl4ai.com/api/async-webcrawler/)**
  * **[Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)**


Thank you for joining me on this journey. Let’s keep building an **open, democratic** approach to data extraction and AI together.
Happy Crawling! — _Unclecode, Founder & Maintainer of Crawl4AI_
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/advanced/hooks-auth)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/lazy-loading/)
    * Hooks & Auth
    * [Proxy & Security](https://docs.crawl4ai.com/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Hooks & Auth in AsyncWebCrawler](https://docs.crawl4ai.com/advanced/hooks-auth#hooks-auth-in-asyncwebcrawler)
  * [Example: Using Hooks in AsyncWebCrawler](https://docs.crawl4ai.com/advanced/hooks-auth#example-using-hooks-in-asyncwebcrawler)
  * [Hook Lifecycle Summary](https://docs.crawl4ai.com/advanced/hooks-auth#hook-lifecycle-summary)
  * [When to Handle Authentication](https://docs.crawl4ai.com/advanced/hooks-auth#when-to-handle-authentication)
  * [Additional Considerations](https://docs.crawl4ai.com/advanced/hooks-auth#additional-considerations)
  * [Conclusion](https://docs.crawl4ai.com/advanced/hooks-auth#conclusion)


# Hooks & Auth in AsyncWebCrawler
Crawl4AI’s **hooks** let you customize the crawler at specific points in the pipeline:
1. **`on_browser_created`**– After browser creation. 2.**`on_page_context_created`**– After a new context & page are created. 3. **`before_goto`**– Just before navigating to a page. 4.**`after_goto`**– Right after navigation completes. 5.**`on_user_agent_updated`**– Whenever the user agent changes. 6.**`on_execution_started`**– Once custom JavaScript execution begins. 7.**`before_retrieve_html`**– Just before the crawler retrieves final HTML. 8.**`before_return_html`**– Right before returning the HTML content.
**Important** : Avoid heavy tasks in `on_browser_created` since you don’t yet have a page context. If you need to _log in_ , do so in **`on_page_context_created`**.
> note "Important Hook Usage Warning" **Avoid Misusing Hooks** : Do not manipulate page objects in the wrong hook or at the wrong time, as it can crash the pipeline or produce incorrect results. A common mistake is attempting to handle authentication prematurely—such as creating or closing pages in `on_browser_created`. 
> **Use the Right Hook for Auth** : If you need to log in or set tokens, use `on_page_context_created`. This ensures you have a valid page/context to work with, without disrupting the main crawling flow.
> **Identity-Based Crawling** : For robust auth, consider identity-based crawling (or passing a session ID) to preserve state. Run your initial login steps in a separate, well-defined process, then feed that session to your main crawl—rather than shoehorning complex authentication into early hooks. Check out [Identity-Based Crawling](https://docs.crawl4ai.com/identity-based-crawling/) for more details.
> **Be Cautious** : Overwriting or removing elements in the wrong hook can compromise the final crawl. Keep hooks focused on smaller tasks (like route filters, custom headers), and let your main logic (crawling, data extraction) proceed normally.
Below is an example demonstration.
## Example: Using Hooks in AsyncWebCrawler
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from playwright.async_api import Page, BrowserContext
async def main():
  print("🔗 Hooks Example: Demonstrating recommended usage")
  # 1) Configure the browser
  browser_config = BrowserConfig(
    headless=True,
    verbose=True
  )
  # 2) Configure the crawler run
  crawler_run_config = CrawlerRunConfig(
    js_code="window.scrollTo(0, document.body.scrollHeight);",
    wait_for="body",
    cache_mode=CacheMode.BYPASS
  )
  # 3) Create the crawler instance
  crawler = AsyncWebCrawler(config=browser_config)
  #
  # Define Hook Functions
  #
  async def on_browser_created(browser, **kwargs):
    # Called once the browser instance is created (but no pages or contexts yet)
    print("[HOOK] on_browser_created - Browser created successfully!")
    # Typically, do minimal setup here if needed
    return browser
  async def on_page_context_created(page: Page, context: BrowserContext, **kwargs):
    # Called right after a new page + context are created (ideal for auth or route config).
    print("[HOOK] on_page_context_created - Setting up page & context.")
    # Example 1: Route filtering (e.g., block images)
    async def route_filter(route):
      if route.request.resource_type == "image":
        print(f"[HOOK] Blocking image request: {route.request.url}")
        await route.abort()
      else:
        await route.continue_()
    await context.route("**", route_filter)
    # Example 2: (Optional) Simulate a login scenario
    # (We do NOT create or close pages here, just do quick steps if needed)
    # e.g., await page.goto("https://example.com/login")
    # e.g., await page.fill("input[name='username']", "testuser")
    # e.g., await page.fill("input[name='password']", "password123")
    # e.g., await page.click("button[type='submit']")
    # e.g., await page.wait_for_selector("#welcome")
    # e.g., await context.add_cookies([...])
    # Then continue
    # Example 3: Adjust the viewport
    await page.set_viewport_size({"width": 1080, "height": 600})
    return page
  async def before_goto(
    page: Page, context: BrowserContext, url: str, **kwargs
  ):
    # Called before navigating to each URL.
    print(f"[HOOK] before_goto - About to navigate: {url}")
    # e.g., inject custom headers
    await page.set_extra_http_headers({
      "Custom-Header": "my-value"
    })
    return page
  async def after_goto(
    page: Page, context: BrowserContext, 
    url: str, response, **kwargs
  ):
    # Called after navigation completes.
    print(f"[HOOK] after_goto - Successfully loaded: {url}")
    # e.g., wait for a certain element if we want to verify
    try:
      await page.wait_for_selector('.content', timeout=1000)
      print("[HOOK] Found .content element!")
    except:
      print("[HOOK] .content not found, continuing anyway.")
    return page
  async def on_user_agent_updated(
    page: Page, context: BrowserContext, 
    user_agent: str, **kwargs
  ):
    # Called whenever the user agent updates.
    print(f"[HOOK] on_user_agent_updated - New user agent: {user_agent}")
    return page
  async def on_execution_started(page: Page, context: BrowserContext, **kwargs):
    # Called after custom JavaScript execution begins.
    print("[HOOK] on_execution_started - JS code is running!")
    return page
  async def before_retrieve_html(page: Page, context: BrowserContext, **kwargs):
    # Called before final HTML retrieval.
    print("[HOOK] before_retrieve_html - We can do final actions")
    # Example: Scroll again
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
    return page
  async def before_return_html(
    page: Page, context: BrowserContext, html: str, **kwargs
  ):
    # Called just before returning the HTML in the result.
    print(f"[HOOK] before_return_html - HTML length: {len(html)}")
    return page
  #
  # Attach Hooks
  #
  crawler.crawler_strategy.set_hook("on_browser_created", on_browser_created)
  crawler.crawler_strategy.set_hook(
    "on_page_context_created", on_page_context_created
  )
  crawler.crawler_strategy.set_hook("before_goto", before_goto)
  crawler.crawler_strategy.set_hook("after_goto", after_goto)
  crawler.crawler_strategy.set_hook(
    "on_user_agent_updated", on_user_agent_updated
  )
  crawler.crawler_strategy.set_hook(
    "on_execution_started", on_execution_started
  )
  crawler.crawler_strategy.set_hook(
    "before_retrieve_html", before_retrieve_html
  )
  crawler.crawler_strategy.set_hook(
    "before_return_html", before_return_html
  )
  await crawler.start()
  # 4) Run the crawler on an example page
  url = "https://example.com"
  result = await crawler.arun(url, config=crawler_run_config)
  if result.success:
    print("\nCrawled URL:", result.url)
    print("HTML length:", len(result.html))
  else:
    print("Error:", result.error_message)
  await crawler.close()
if __name__ == "__main__":
  asyncio.run(main())

```

## Hook Lifecycle Summary
1. **`on_browser_created`**: - Browser is up, but**no** pages or contexts yet. - Light setup only—don’t try to open or close pages here (that belongs in `on_page_context_created`).
2. **`on_page_context_created`**: - Perfect for advanced**auth** or route blocking. - You have a **page** + **context** ready but haven’t navigated to the target URL yet.
3. **`before_goto`**: - Right before navigation. Typically used for setting**custom headers** or logging the target URL.
4. **`after_goto`**: - After page navigation is done. Good place for verifying content or waiting on essential elements.
5. **`on_user_agent_updated`**: - Whenever the user agent changes (for stealth or different UA modes).
6. **`on_execution_started`**: - If you set`js_code` or run custom scripts, this runs once your JS is about to start.
7. **`before_retrieve_html`**: - Just before the final HTML snapshot is taken. Often you do a final scroll or lazy-load triggers here.
8. **`before_return_html`**: - The last hook before returning HTML to the`CrawlResult`. Good for logging HTML length or minor modifications.
## When to Handle Authentication
**Recommended** : Use **`on_page_context_created`**if you need to:
  * Navigate to a login page or fill forms
  * Set cookies or localStorage tokens
  * Block resource routes to avoid ads


This ensures the newly created context is under your control **before** `arun()` navigates to the main URL.
## Additional Considerations
  * **Session Management** : If you want multiple `arun()` calls to reuse a single session, pass `session_id=` in your `CrawlerRunConfig`. Hooks remain the same. 
  * **Performance** : Hooks can slow down crawling if they do heavy tasks. Keep them concise. 
  * **Error Handling** : If a hook fails, the overall crawl might fail. Catch exceptions or handle them gracefully. 
  * **Concurrency** : If you run `arun_many()`, each URL triggers these hooks in parallel. Ensure your hooks are thread/async-safe.


## Conclusion
Hooks provide **fine-grained** control over:
  * **Browser** creation (light tasks only)
  * **Page** and **context** creation (auth, route blocking)
  * **Navigation** phases
  * **Final HTML** retrieval


Follow the recommended usage: - **Login** or advanced tasks in `on_page_context_created` - **Custom headers** or logs in `before_goto` / `after_goto` - **Scrolling** or final checks in `before_retrieve_html` / `before_return_html`
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/advanced/advanced-features)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * Overview
    * [File Downloading](https://docs.crawl4ai.com/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Overview of Some Important Advanced Features](https://docs.crawl4ai.com/advanced/advanced-features#overview-of-some-important-advanced-features)
  * [1. Proxy Usage](https://docs.crawl4ai.com/advanced/advanced-features#1-proxy-usage)
  * [2. Capturing PDFs & Screenshots](https://docs.crawl4ai.com/advanced/advanced-features#2-capturing-pdfs-screenshots)
  * [3. Handling SSL Certificates](https://docs.crawl4ai.com/advanced/advanced-features#3-handling-ssl-certificates)
  * [4. Custom Headers](https://docs.crawl4ai.com/advanced/advanced-features#4-custom-headers)
  * [5. Session Persistence & Local Storage](https://docs.crawl4ai.com/advanced/advanced-features#5-session-persistence-local-storage)
  * [6. Robots.txt Compliance](https://docs.crawl4ai.com/advanced/advanced-features#6-robotstxt-compliance)
  * [Putting It All Together](https://docs.crawl4ai.com/advanced/advanced-features#putting-it-all-together)
  * [Conclusion & Next Steps](https://docs.crawl4ai.com/advanced/advanced-features#conclusion-next-steps)


# Overview of Some Important Advanced Features
(Proxy, PDF, Screenshot, SSL, Headers, & Storage State)
Crawl4AI offers multiple power-user features that go beyond simple crawling. This tutorial covers:
1. **Proxy Usage** 2. **Capturing PDFs & Screenshots** 3. **Handling SSL Certificates** 4. **Custom Headers** 5. **Session Persistence & Local Storage** 6. **Robots.txt Compliance**
> **Prerequisites** - You have a basic grasp of [AsyncWebCrawler Basics](https://docs.crawl4ai.com/core/simple-crawling/) - You know how to run or configure your Python environment with Playwright installed
## 1. Proxy Usage
If you need to route your crawl traffic through a proxy—whether for IP rotation, geo-testing, or privacy—Crawl4AI supports it via `BrowserConfig.proxy_config`.
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
async def main():
  browser_cfg = BrowserConfig(
    proxy_config={
      "server": "http://proxy.example.com:8080",
      "username": "myuser",
      "password": "mypass",
    },
    headless=True
  )
  crawler_cfg = CrawlerRunConfig(
    verbose=True
  )
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    result = await crawler.arun(
      url="https://www.whatismyip.com/",
      config=crawler_cfg
    )
    if result.success:
      print("[OK] Page fetched via proxy.")
      print("Page HTML snippet:", result.html[:200])
    else:
      print("[ERROR]", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Points** - **`proxy_config`**expects a dict with`server` and optional auth credentials. - Many commercial proxies provide an HTTP/HTTPS “gateway” server that you specify in `server`. - If your proxy doesn’t need auth, omit `username`/`password`.
## 2. Capturing PDFs & Screenshots
Sometimes you need a visual record of a page or a PDF “printout.” Crawl4AI can do both in one pass:
```
import os, asyncio
from base64 import b64decode
from crawl4ai import AsyncWebCrawler, CacheMode
async def main():
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://en.wikipedia.org/wiki/List_of_common_misconceptions",
      cache_mode=CacheMode.BYPASS,
      pdf=True,
      screenshot=True
    )
    if result.success:
      # Save screenshot
      if result.screenshot:
        with open("wikipedia_screenshot.png", "wb") as f:
          f.write(b64decode(result.screenshot))
      # Save PDF
      if result.pdf:
        with open("wikipedia_page.pdf", "wb") as f:
          f.write(result.pdf)
      print("[OK] PDF & screenshot captured.")
    else:
      print("[ERROR]", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**Why PDF + Screenshot?** - Large or complex pages can be slow or error-prone with “traditional” full-page screenshots. - Exporting a PDF is more reliable for very long pages. Crawl4AI automatically converts the first PDF page into an image if you request both. 
**Relevant Parameters** - **`pdf=True`**: Exports the current page as a PDF (base64-encoded in`result.pdf`). - **`screenshot=True`**: Creates a screenshot (base64-encoded in`result.screenshot`). - **`scan_full_page`**or advanced hooking can further refine how the crawler captures content.
## 3. Handling SSL Certificates
If you need to verify or export a site’s SSL certificate—for compliance, debugging, or data analysis—Crawl4AI can fetch it during the crawl:
```
import asyncio, os
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  tmp_dir = os.path.join(os.getcwd(), "tmp")
  os.makedirs(tmp_dir, exist_ok=True)
  config = CrawlerRunConfig(
    fetch_ssl_certificate=True,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url="https://example.com", config=config)
    if result.success and result.ssl_certificate:
      cert = result.ssl_certificate
      print("\nCertificate Information:")
      print(f"Issuer (CN): {cert.issuer.get('CN', '')}")
      print(f"Valid until: {cert.valid_until}")
      print(f"Fingerprint: {cert.fingerprint}")
      # Export in multiple formats:
      cert.to_json(os.path.join(tmp_dir, "certificate.json"))
      cert.to_pem(os.path.join(tmp_dir, "certificate.pem"))
      cert.to_der(os.path.join(tmp_dir, "certificate.der"))
      print("\nCertificate exported to JSON/PEM/DER in 'tmp' folder.")
    else:
      print("[ERROR] No certificate or crawl failed.")
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Points** - **`fetch_ssl_certificate=True`**triggers certificate retrieval. -`result.ssl_certificate` includes methods (`to_json`, `to_pem`, `to_der`) for saving in various formats (handy for server config, Java keystores, etc.).
## 4. Custom Headers
Sometimes you need to set custom headers (e.g., language preferences, authentication tokens, or specialized user-agent strings). You can do this in multiple ways:
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  # Option 1: Set headers at the crawler strategy level
  crawler1 = AsyncWebCrawler(
    # The underlying strategy can accept headers in its constructor
    crawler_strategy=None # We'll override below for clarity
  )
  crawler1.crawler_strategy.update_user_agent("MyCustomUA/1.0")
  crawler1.crawler_strategy.set_custom_headers({
    "Accept-Language": "fr-FR,fr;q=0.9"
  })
  result1 = await crawler1.arun("https://www.example.com")
  print("Example 1 result success:", result1.success)
  # Option 2: Pass headers directly to `arun()`
  crawler2 = AsyncWebCrawler()
  result2 = await crawler2.arun(
    url="https://www.example.com",
    headers={"Accept-Language": "es-ES,es;q=0.9"}
  )
  print("Example 2 result success:", result2.success)
if __name__ == "__main__":
  asyncio.run(main())

```

**Notes** - Some sites may react differently to certain headers (e.g., `Accept-Language`). - If you need advanced user-agent randomization or client hints, see [Identity-Based Crawling (Anti-Bot)](https://docs.crawl4ai.com/identity-based-crawling/) or use `UserAgentGenerator`.
## 5. Session Persistence & Local Storage
Crawl4AI can preserve cookies and localStorage so you can continue where you left off—ideal for logging into sites or skipping repeated auth flows.
### 5.1 `storage_state`
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  storage_dict = {
    "cookies": [
      {
        "name": "session",
        "value": "abcd1234",
        "domain": "example.com",
        "path": "/",
        "expires": 1699999999.0,
        "httpOnly": False,
        "secure": False,
        "sameSite": "None"
      }
    ],
    "origins": [
      {
        "origin": "https://example.com",
        "localStorage": [
          {"name": "token", "value": "my_auth_token"}
        ]
      }
    ]
  }
  # Provide the storage state as a dictionary to start "already logged in"
  async with AsyncWebCrawler(
    headless=True,
    storage_state=storage_dict
  ) as crawler:
    result = await crawler.arun("https://example.com/protected")
    if result.success:
      print("Protected page content length:", len(result.html))
    else:
      print("Failed to crawl protected page")
if __name__ == "__main__":
  asyncio.run(main())

```

### 5.2 Exporting & Reusing State
You can sign in once, export the browser context, and reuse it later—without re-entering credentials.
  * **`await context.storage_state(path="my_storage.json")`**: Exports cookies, localStorage, etc. to a file.
  * Provide `storage_state="my_storage.json"` on subsequent runs to skip the login step.


**See** : [Detailed session management tutorial](https://docs.crawl4ai.com/session-management/) or [Explanations → Browser Context & Managed Browser](https://docs.crawl4ai.com/identity-based-crawling/) for more advanced scenarios (like multi-step logins, or capturing after interactive pages).
## 6. Robots.txt Compliance
Crawl4AI supports respecting robots.txt rules with efficient caching:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  # Enable robots.txt checking in config
  config = CrawlerRunConfig(
    check_robots_txt=True # Will check and respect robots.txt rules
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      "https://example.com",
      config=config
    )
    if not result.success and result.status_code == 403:
      print("Access denied by robots.txt")
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Points** - Robots.txt files are cached locally for efficiency - Cache is stored in `~/.crawl4ai/robots/robots_cache.db` - Cache has a default TTL of 7 days - If robots.txt can't be fetched, crawling is allowed - Returns 403 status code if URL is disallowed
## Putting It All Together
Here’s a snippet that combines multiple “advanced” features (proxy, PDF, screenshot, SSL, custom headers, and session reuse) into one run. Normally, you’d tailor each setting to your project’s needs.
```
import os, asyncio
from base64 import b64decode
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
async def main():
  # 1. Browser config with proxy + headless
  browser_cfg = BrowserConfig(
    proxy_config={
      "server": "http://proxy.example.com:8080",
      "username": "myuser",
      "password": "mypass",
    },
    headless=True,
  )
  # 2. Crawler config with PDF, screenshot, SSL, custom headers, and ignoring caches
  crawler_cfg = CrawlerRunConfig(
    pdf=True,
    screenshot=True,
    fetch_ssl_certificate=True,
    cache_mode=CacheMode.BYPASS,
    headers={"Accept-Language": "en-US,en;q=0.8"},
    storage_state="my_storage.json", # Reuse session from a previous sign-in
    verbose=True,
  )
  # 3. Crawl
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    result = await crawler.arun(
      url = "https://secure.example.com/protected", 
      config=crawler_cfg
    )
    if result.success:
      print("[OK] Crawled the secure page. Links found:", len(result.links.get("internal", [])))
      # Save PDF & screenshot
      if result.pdf:
        with open("result.pdf", "wb") as f:
          f.write(b64decode(result.pdf))
      if result.screenshot:
        with open("result.png", "wb") as f:
          f.write(b64decode(result.screenshot))
      # Check SSL cert
      if result.ssl_certificate:
        print("SSL Issuer CN:", result.ssl_certificate.issuer.get("CN", ""))
    else:
      print("[ERROR]", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

## Conclusion & Next Steps
You’ve now explored several **advanced** features:
  * **Proxy Usage**
  * **PDF & Screenshot** capturing for large or critical pages 
  * **SSL Certificate** retrieval & exporting 
  * **Custom Headers** for language or specialized requests 
  * **Session Persistence** via storage state
  * **Robots.txt Compliance**


With these power tools, you can build robust scraping workflows that mimic real user behavior, handle secure sites, capture detailed snapshots, and manage sessions across multiple runs—streamlining your entire data collection pipeline.
**Last Updated** : 2025-01-01
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/advanced/crawl-dispatcher)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/multi-url-crawling/)
    * Crawl Dispatcher
    * [Identity Based Crawling](https://docs.crawl4ai.com/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher#crawl-dispatcher)


# Crawl Dispatcher
We’re excited to announce a **Crawl Dispatcher** module that can handle **thousands** of crawling tasks simultaneously. By efficiently managing system resources (memory, CPU, network), this dispatcher ensures high-performance data extraction at scale. It also provides **real-time monitoring** of each crawler’s status, memory usage, and overall progress.
Stay tuned—this feature is **coming soon** in an upcoming release of Crawl4AI! For the latest news, keep an eye on our changelogs and follow [@unclecode](https://twitter.com/unclecode) on X.
Below is a **sample** of how the dispatcher’s performance monitor might look in action:
![Crawl Dispatcher Performance Monitor](https://docs.crawl4ai.com/assets/images/dispatcher.png)
We can’t wait to bring you this streamlined, **scalable** approach to multi-URL crawling—**watch this space** for updates!
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/advanced/file-downloading)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced-features/)
    * File Downloading
    * [Lazy Loading](https://docs.crawl4ai.com/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Download Handling in Crawl4AI](https://docs.crawl4ai.com/advanced/file-downloading#download-handling-in-crawl4ai)
  * [Enabling Downloads](https://docs.crawl4ai.com/advanced/file-downloading#enabling-downloads)
  * [Specifying Download Location](https://docs.crawl4ai.com/advanced/file-downloading#specifying-download-location)
  * [Triggering Downloads](https://docs.crawl4ai.com/advanced/file-downloading#triggering-downloads)
  * [Accessing Downloaded Files](https://docs.crawl4ai.com/advanced/file-downloading#accessing-downloaded-files)
  * [Example: Downloading Multiple Files](https://docs.crawl4ai.com/advanced/file-downloading#example-downloading-multiple-files)
  * [Important Considerations](https://docs.crawl4ai.com/advanced/file-downloading#important-considerations)


# Download Handling in Crawl4AI
This guide explains how to use Crawl4AI to handle file downloads during crawling. You'll learn how to trigger downloads, specify download locations, and access downloaded files.
## Enabling Downloads
To enable downloads, set the `accept_downloads` parameter in the `BrowserConfig` object and pass it to the crawler.
```
from crawl4ai.async_configs import BrowserConfig, AsyncWebCrawler
async def main():
  config = BrowserConfig(accept_downloads=True) # Enable downloads globally
  async with AsyncWebCrawler(config=config) as crawler:
    # ... your crawling logic ...
asyncio.run(main())

```

## Specifying Download Location
Specify the download directory using the `downloads_path` attribute in the `BrowserConfig` object. If not provided, Crawl4AI defaults to creating a "downloads" directory inside the `.crawl4ai` folder in your home directory.
```
from crawl4ai.async_configs import BrowserConfig
import os
downloads_path = os.path.join(os.getcwd(), "my_downloads") # Custom download path
os.makedirs(downloads_path, exist_ok=True)
config = BrowserConfig(accept_downloads=True, downloads_path=downloads_path)
async def main():
  async with AsyncWebCrawler(config=config) as crawler:
    result = await crawler.arun(url="https://example.com")
    # ...

```

## Triggering Downloads
Downloads are typically triggered by user interactions on a web page, such as clicking a download button. Use `js_code` in `CrawlerRunConfig` to simulate these actions and `wait_for` to allow sufficient time for downloads to start.
```
from crawl4ai.async_configs import CrawlerRunConfig
config = CrawlerRunConfig(
  js_code="""
    const downloadLink = document.querySelector('a[href$=".exe"]');
    if (downloadLink) {
      downloadLink.click();
    }
  """,
  wait_for=5 # Wait 5 seconds for the download to start
)
result = await crawler.arun(url="https://www.python.org/downloads/", config=config)

```

## Accessing Downloaded Files
The `downloaded_files` attribute of the `CrawlResult` object contains paths to downloaded files.
```
if result.downloaded_files:
  print("Downloaded files:")
  for file_path in result.downloaded_files:
    print(f"- {file_path}")
    file_size = os.path.getsize(file_path)
    print(f"- File size: {file_size} bytes")
else:
  print("No files downloaded.")

```

## Example: Downloading Multiple Files
```
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
import os
from pathlib import Path
async def download_multiple_files(url: str, download_path: str):
  config = BrowserConfig(accept_downloads=True, downloads_path=download_path)
  async with AsyncWebCrawler(config=config) as crawler:
    run_config = CrawlerRunConfig(
      js_code="""
        const downloadLinks = document.querySelectorAll('a[download]');
        for (const link of downloadLinks) {
          link.click();
          // Delay between clicks
          await new Promise(r => setTimeout(r, 2000)); 
        }
      """,
      wait_for=10 # Wait for all downloads to start
    )
    result = await crawler.arun(url=url, config=run_config)
    if result.downloaded_files:
      print("Downloaded files:")
      for file in result.downloaded_files:
        print(f"- {file}")
    else:
      print("No files downloaded.")
# Usage
download_path = os.path.join(Path.home(), ".crawl4ai", "downloads")
os.makedirs(download_path, exist_ok=True)
asyncio.run(download_multiple_files("https://www.python.org/downloads/windows/", download_path))

```

## Important Considerations
  * **Browser Context:** Downloads are managed within the browser context. Ensure `js_code` correctly targets the download triggers on the webpage.
  * **Timing:** Use `wait_for` in `CrawlerRunConfig` to manage download timing.
  * **Error Handling:** Handle errors to manage failed downloads or incorrect paths gracefully.
  * **Security:** Scan downloaded files for potential security threats before use.


This revised guide ensures consistency with the `Crawl4AI` codebase by using `BrowserConfig` and `CrawlerRunConfig` for all download-related configurations. Let me know if further adjustments are needed!
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/advanced/identity-based-crawling)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/crawl-dispatcher/)
    * Identity Based Crawling
    * [SSL Certificate](https://docs.crawl4ai.com/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Preserve Your Identity with Crawl4AI](https://docs.crawl4ai.com/advanced/identity-based-crawling#preserve-your-identity-with-crawl4ai)
  * [1. Managed Browsers: Your Digital Identity Solution](https://docs.crawl4ai.com/advanced/identity-based-crawling#1-managed-browsers-your-digital-identity-solution)
  * [3. Using Managed Browsers in Crawl4AI](https://docs.crawl4ai.com/advanced/identity-based-crawling#3-using-managed-browsers-in-crawl4ai)
  * [4. Magic Mode: Simplified Automation](https://docs.crawl4ai.com/advanced/identity-based-crawling#4-magic-mode-simplified-automation)
  * [5. Comparing Managed Browsers vs. Magic Mode](https://docs.crawl4ai.com/advanced/identity-based-crawling#5-comparing-managed-browsers-vs-magic-mode)
  * [6. Using the BrowserProfiler Class](https://docs.crawl4ai.com/advanced/identity-based-crawling#6-using-the-browserprofiler-class)
  * [7. Summary](https://docs.crawl4ai.com/advanced/identity-based-crawling#7-summary)


# Preserve Your Identity with Crawl4AI
Crawl4AI empowers you to navigate and interact with the web using your **authentic digital identity** , ensuring you’re recognized as a human and not mistaken for a bot. This tutorial covers:
1. **Managed Browsers** – The recommended approach for persistent profiles and identity-based crawling. 2. **Magic Mode** – A simplified fallback solution for quick automation without persistent identity.
## 1. Managed Browsers: Your Digital Identity Solution
**Managed Browsers** let developers create and use **persistent browser profiles**. These profiles store local storage, cookies, and other session data, letting you browse as your **real self** —complete with logins, preferences, and cookies.
### Key Benefits
  * **Authentic Browsing Experience** : Retain session data and browser fingerprints as though you’re a normal user. 
  * **Effortless Configuration** : Once you log in or solve CAPTCHAs in your chosen data directory, you can re-run crawls without repeating those steps. 
  * **Empowered Data Access** : If you can see the data in your own browser, you can automate its retrieval with your genuine identity.


Below is a **partial update** to your **Managed Browsers** tutorial, specifically the section about **creating a user-data directory** using **Playwright’s Chromium** binary rather than a system-wide Chrome/Edge. We’ll show how to **locate** that binary and launch it with a `--user-data-dir` argument to set up your profile. You can then point `BrowserConfig.user_data_dir` to that folder for subsequent crawls.
### Creating a User Data Directory (Command-Line Approach via Playwright)
If you installed Crawl4AI (which installs Playwright under the hood), you already have a Playwright-managed Chromium on your system. Follow these steps to launch that **Chromium** from your command line, specifying a **custom** data directory:
1. **Find** the Playwright Chromium binary: - On most systems, installed browsers go under a `~/.cache/ms-playwright/` folder or similar path. - To see an overview of installed browsers, run: 
```
python -m playwright install --dry-run

```

or 
```
playwright install --dry-run

```

(depending on your environment). This shows where Playwright keeps Chromium. 
  * For instance, you might see a path like: 
```
~/.cache/ms-playwright/chromium-1234/chrome-linux/chrome

```

on Linux, or a corresponding folder on macOS/Windows.


2. **Launch** the Playwright Chromium binary with a **custom** user-data directory: 
```
# Linux example
~/.cache/ms-playwright/chromium-1234/chrome-linux/chrome \
  --user-data-dir=/home/<you>/my_chrome_profile

```

```
# macOS example (Playwright’s internal binary)
~/Library/Caches/ms-playwright/chromium-1234/chrome-mac/Chromium.app/Contents/MacOS/Chromium \
  --user-data-dir=/Users/<you>/my_chrome_profile

```

```
# Windows example (PowerShell/cmd)
"C:\Users\<you>\AppData\Local\ms-playwright\chromium-1234\chrome-win\chrome.exe" ^
  --user-data-dir="C:\Users\<you>\my_chrome_profile"

```

**Replace** the path with the actual subfolder indicated in your `ms-playwright` cache structure. - This **opens** a fresh Chromium with your new or existing data folder. - **Log into** any sites or configure your browser the way you want. - **Close** when done—your profile data is saved in that folder.
3. **Use** that folder in **`BrowserConfig.user_data_dir`**:
```
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
browser_config = BrowserConfig(
  headless=True,
  use_managed_browser=True,
  user_data_dir="/home/<you>/my_chrome_profile",
  browser_type="chromium"
)

```

- Next time you run your code, it reuses that folder—**preserving** your session data, cookies, local storage, etc. 
## 3. Using Managed Browsers in Crawl4AI
Once you have a data directory with your session data, pass it to **`BrowserConfig`**:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
async def main():
  # 1) Reference your persistent data directory
  browser_config = BrowserConfig(
    headless=True,       # 'True' for automated runs
    verbose=True,
    use_managed_browser=True, # Enables persistent browser strategy
    browser_type="chromium",
    user_data_dir="/path/to/my-chrome-profile"
  )
  # 2) Standard crawl config
  crawl_config = CrawlerRunConfig(
    wait_for="css:.logged-in-content"
  )
  async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(url="https://example.com/private", config=crawl_config)
    if result.success:
      print("Successfully accessed private data with your identity!")
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

### Workflow
1. **Login** externally (via CLI or your normal Chrome with `--user-data-dir=...`). 2. **Close** that browser. 3. **Use** the same folder in `user_data_dir=` in Crawl4AI. 4. **Crawl** – The site sees your identity as if you’re the same user who just logged in.
## 4. Magic Mode: Simplified Automation
If you **don’t** need a persistent profile or identity-based approach, **Magic Mode** offers a quick way to simulate human-like browsing without storing long-term data.
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async with AsyncWebCrawler() as crawler:
  result = await crawler.arun(
    url="https://example.com",
    config=CrawlerRunConfig(
      magic=True, # Simplifies a lot of interaction
      remove_overlay_elements=True,
      page_timeout=60000
    )
  )

```

**Magic Mode** :
  * Simulates a user-like experience 
  * Randomizes user agent & navigator
  * Randomizes interactions & timings 
  * Masks automation signals 
  * Attempts pop-up handling 


**But** it’s no substitute for **true** user-based sessions if you want a fully legitimate identity-based solution.
## 5. Comparing Managed Browsers vs. Magic Mode
Feature | **Managed Browsers** | **Magic Mode**  
---|---|---  
**Session Persistence** | Full localStorage/cookies retained in user_data_dir | No persistent data (fresh each run)  
**Genuine Identity** | Real user profile with full rights & preferences | Emulated user-like patterns, but no actual identity  
**Complex Sites** | Best for login-gated sites or heavy config | Simple tasks, minimal login or config needed  
**Setup** | External creation of user_data_dir, then use in Crawl4AI | Single-line approach (`magic=True`)  
**Reliability** | Extremely consistent (same data across runs) | Good for smaller tasks, can be less stable  
## 6. Using the BrowserProfiler Class
Crawl4AI provides a dedicated `BrowserProfiler` class for managing browser profiles, making it easy to create, list, and delete profiles for identity-based browsing.
### Creating and Managing Profiles with BrowserProfiler
The `BrowserProfiler` class offers a comprehensive API for browser profile management:
```
import asyncio
from crawl4ai import BrowserProfiler
async def manage_profiles():
  # Create a profiler instance
  profiler = BrowserProfiler()
  # Create a profile interactively - opens a browser window
  profile_path = await profiler.create_profile(
    profile_name="my-login-profile" # Optional: name your profile
  )
  print(f"Profile saved at: {profile_path}")
  # List all available profiles
  profiles = profiler.list_profiles()
  for profile in profiles:
    print(f"Profile: {profile['name']}")
    print(f" Path: {profile['path']}")
    print(f" Created: {profile['created']}")
    print(f" Browser type: {profile['type']}")
  # Get a specific profile path by name
  specific_profile = profiler.get_profile_path("my-login-profile")
  # Delete a profile when no longer needed
  success = profiler.delete_profile("old-profile-name")
asyncio.run(manage_profiles())

```

**How profile creation works:** 1. A browser window opens for you to interact with 2. You log in to websites, set preferences, etc. 3. When you're done, press 'q' in the terminal to close the browser 4. The profile is saved in the Crawl4AI profiles directory 5. You can use the returned path with `BrowserConfig.user_data_dir`
### Interactive Profile Management
The `BrowserProfiler` also offers an interactive management console that guides you through profile creation, listing, and deletion:
```
import asyncio
from crawl4ai import BrowserProfiler, AsyncWebCrawler, BrowserConfig
# Define a function to use a profile for crawling
async def crawl_with_profile(profile_path, url):
  browser_config = BrowserConfig(
    headless=True,
    use_managed_browser=True,
    user_data_dir=profile_path
  )
  async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(url)
    return result
async def main():
  # Create a profiler instance
  profiler = BrowserProfiler()
  # Launch the interactive profile manager
  # Passing the crawl function as a callback adds a "crawl with profile" option
  await profiler.interactive_manager(crawl_callback=crawl_with_profile)
asyncio.run(main())

```

### Legacy Methods
For backward compatibility, the previous methods on `ManagedBrowser` are still available, but they delegate to the new `BrowserProfiler` class:
```
from crawl4ai.browser_manager import ManagedBrowser
# These methods still work but use BrowserProfiler internally
profiles = ManagedBrowser.list_profiles()

```

### Complete Example
See the full example in `docs/examples/identity_based_browsing.py` for a complete demonstration of creating and using profiles for authenticated browsing using the new `BrowserProfiler` class.
## 7. Summary
  * **Create** your user-data directory either:
  * By launching Chrome/Chromium externally with `--user-data-dir=/some/path`
  * Or by using the built-in `BrowserProfiler.create_profile()` method
  * Or through the interactive interface with `profiler.interactive_manager()`
  * **Log in** or configure sites as needed, then close the browser
  * **Reference** that folder in `BrowserConfig(user_data_dir="...")` + `use_managed_browser=True`
  * **List and reuse** profiles with `BrowserProfiler.list_profiles()`
  * **Manage** your profiles with the dedicated `BrowserProfiler` class
  * Enjoy **persistent** sessions that reflect your real identity
  * If you only need quick, ephemeral automation, **Magic Mode** might suffice


**Recommended** : Always prefer a **Managed Browser** for robust, identity-based crawling and simpler interactions with complex sites. Use **Magic Mode** for quick tasks or prototypes where persistent data is unnecessary.
With these approaches, you preserve your **authentic** browsing environment, ensuring the site sees you exactly as a normal user—no repeated logins or wasted time.
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/blog)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * Blog Home
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Crawl4AI Blog](https://docs.crawl4ai.com/blog#crawl4ai-blog)
  * [Latest Release](https://docs.crawl4ai.com/blog#latest-release)
  * [License Change](https://docs.crawl4ai.com/blog#license-change)
  * [Project History](https://docs.crawl4ai.com/blog#project-history)
  * [Stay Updated](https://docs.crawl4ai.com/blog#stay-updated)


# Crawl4AI Blog
Welcome to the Crawl4AI blog! Here you'll find detailed release notes, technical insights, and updates about the project. Whether you're looking for the latest improvements or want to dive deep into web crawling techniques, this is the place.
## Latest Release
### [Crawl4AI v0.5.0: Deep Crawling, Scalability, and a New CLI!](https://docs.crawl4ai.com/releases/0.5.0/)
My dear friends and crawlers, there you go, this is the release of Crawl4AI v0.5.0! This release brings a wealth of new features, performance improvements, and a more streamlined developer experience. Here's a breakdown of what's new:
**Major New Features:**
  * **Deep Crawling:** Explore entire websites with configurable strategies (BFS, DFS, Best-First). Define custom filters and URL scoring for targeted crawls.
  * **Memory-Adaptive Dispatcher:** Handle large-scale crawls with ease! Our new dispatcher dynamically adjusts concurrency based on available memory and includes built-in rate limiting.
  * **Multiple Crawler Strategies:** Choose between the full-featured Playwright browser-based crawler or a new, _much_ faster HTTP-only crawler for simpler tasks.
  * **Docker Deployment:** Deploy Crawl4AI as a scalable, self-contained service with built-in API endpoints and optional JWT authentication.
  * **Command-Line Interface (CLI):** Interact with Crawl4AI directly from your terminal. Crawl, configure, and extract data with simple commands.
  * **LLM Configuration (`LLMConfig`):** A new, unified way to configure LLM providers (OpenAI, Anthropic, Ollama, etc.) for extraction, filtering, and schema generation. Simplifies API key management and switching between models.


**Minor Updates & Improvements:**
  * **LXML Scraping Mode:** Faster HTML parsing with `LXMLWebScrapingStrategy`.
  * **Proxy Rotation:** Added `ProxyRotationStrategy` with a `RoundRobinProxyStrategy` implementation.
  * **PDF Processing:** Extract text, images, and metadata from PDF files.
  * **URL Redirection Tracking:** Automatically follows and records redirects.
  * **Robots.txt Compliance:** Optionally respect website crawling rules.
  * **LLM-Powered Schema Generation:** Automatically create extraction schemas using an LLM.
  * **`LLMContentFilter`:** Generate high-quality, focused markdown using an LLM.
  * **Improved Error Handling & Stability:** Numerous bug fixes and performance enhancements.
  * **Enhanced Documentation:** Updated guides and examples.


**Breaking Changes & Migration:**
This release includes several breaking changes to improve the library's structure and consistency. Here's what you need to know:
  * **`arun_many()`Behavior:** Now uses the `MemoryAdaptiveDispatcher` by default. The return type depends on the `stream` parameter in `CrawlerRunConfig`. Adjust code that relied on unbounded concurrency.
  * **`max_depth`Location:** Moved to `CrawlerRunConfig` and now controls _crawl depth_.
  * **Deep Crawling Imports:** Import `DeepCrawlStrategy` and related classes from `crawl4ai.deep_crawling`.
  * **`BrowserContext`API:** Updated; the old `get_context` method is deprecated.
  * **Optional Model Fields:** Many data model fields are now optional. Handle potential `None` values.
  * **`ScrapingMode`Enum:** Replaced with strategy pattern (`WebScrapingStrategy`, `LXMLWebScrapingStrategy`).
  * **`content_filter`Parameter:** Removed from `CrawlerRunConfig`. Use extraction strategies or markdown generators with filters.
  * **Removed Functionality:** The synchronous `WebCrawler`, the old CLI, and docs management tools have been removed.
  * **Docker:** Significant changes to deployment. See the [Docker documentation](https://docs.crawl4ai.com/deploy/docker/README.md).
  * **`ssl_certificate.json`:** This file has been removed.
  * **Config** : FastFilterChain has been replaced with FilterChain
  * **Deep-Crawl** : DeepCrawlStrategy.arun now returns Union[CrawlResultT, List[CrawlResultT], AsyncGenerator[CrawlResultT, None]]
  * **Proxy** : Removed synchronous WebCrawler support and related rate limiting configurations
  * **LLM Parameters:** Use the new `LLMConfig` object instead of passing `provider`, `api_token`, `base_url`, and `api_base` directly to `LLMExtractionStrategy` and `LLMContentFilter`.


**In short:** Update imports, adjust `arun_many()` usage, check for optional fields, and review the Docker deployment guide.
## License Change
Crawl4AI v0.5.0 updates the license to Apache 2.0 _with a required attribution clause_. This means you are free to use, modify, and distribute Crawl4AI (even commercially), but you _must_ clearly attribute the project in any public use or distribution. See the updated `LICENSE` file for the full legal text and specific requirements.
**Get Started:**
  * **Installation:** `pip install "crawl4ai[all]"` (or use the Docker image)
  * **Documentation:** <https://docs.crawl4ai.com>
  * **GitHub:** <https://github.com/unclecode/crawl4ai>


I'm very excited to see what you build with Crawl4AI v0.5.0!
### [0.4.2 - Configurable Crawlers, Session Management, and Smarter Screenshots](https://docs.crawl4ai.com/releases/0.4.2/)
_December 12, 2024_
The 0.4.2 update brings massive improvements to configuration, making crawlers and browsers easier to manage with dedicated objects. You can now import/export local storage for seamless session management. Plus, long-page screenshots are faster and cleaner, and full-page PDF exports are now possible. Check out all the new features to make your crawling experience even smoother.
[Read full release notes →](https://docs.crawl4ai.com/releases/0.4.2/)
### [0.4.1 - Smarter Crawling with Lazy-Load Handling, Text-Only Mode, and More](https://docs.crawl4ai.com/releases/0.4.1/)
_December 8, 2024_
This release brings major improvements to handling lazy-loaded images, a blazing-fast Text-Only Mode, full-page scanning for infinite scrolls, dynamic viewport adjustments, and session reuse for efficient crawling. If you're looking to improve speed, reliability, or handle dynamic content with ease, this update has you covered.
[Read full release notes →](https://docs.crawl4ai.com/releases/0.4.1/)
### [0.4.0 - Major Content Filtering Update](https://docs.crawl4ai.com/releases/0.4.0/)
_December 1, 2024_
Introduced significant improvements to content filtering, multi-threaded environment handling, and user-agent generation. This release features the new PruningContentFilter, enhanced thread safety, and improved test coverage.
[Read full release notes →](https://docs.crawl4ai.com/releases/0.4.0/)
## Project History
Curious about how Crawl4AI has evolved? Check out our [complete changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md) for a detailed history of all versions and updates.
## Stay Updated
  * Star us on [GitHub](https://github.com/unclecode/crawl4ai)
  * Follow [@unclecode](https://twitter.com/unclecode) on Twitter
  * Join our community discussions on GitHub


Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/api/arun_many)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/arun/)
    * arun_many()
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/strategies/)


  * [arun_many(...) Reference](https://docs.crawl4ai.com/api/arun_many#arun_many-reference)
  * [Function Signature](https://docs.crawl4ai.com/api/arun_many#function-signature)
  * [Differences from arun()](https://docs.crawl4ai.com/api/arun_many#differences-from-arun)
  * [Dispatcher Reference](https://docs.crawl4ai.com/api/arun_many#dispatcher-reference)
  * [Common Pitfalls](https://docs.crawl4ai.com/api/arun_many#common-pitfalls)
  * [Conclusion](https://docs.crawl4ai.com/api/arun_many#conclusion)


# `arun_many(...)` Reference
> **Note** : This function is very similar to [`arun()`](https://docs.crawl4ai.com/arun/) but focused on **concurrent** or **batch** crawling. If you’re unfamiliar with `arun()` usage, please read that doc first, then review this for differences.
## Function Signature
```
async def arun_many(
  urls: Union[List[str], List[Any]],
  config: Optional[CrawlerRunConfig] = None,
  dispatcher: Optional[BaseDispatcher] = None,
  ...
) -> Union[List[CrawlResult], AsyncGenerator[CrawlResult, None]]:
  """
  Crawl multiple URLs concurrently or in batches.
  :param urls: A list of URLs (or tasks) to crawl.
  :param config: (Optional) A default `CrawlerRunConfig` applying to each crawl.
  :param dispatcher: (Optional) A concurrency controller (e.g. MemoryAdaptiveDispatcher).
  ...
  :return: Either a list of `CrawlResult` objects, or an async generator if streaming is enabled.
  """

```

## Differences from `arun()`
1. **Multiple URLs** : 
  * Instead of crawling a single URL, you pass a list of them (strings or tasks). 
  * The function returns either a **list** of `CrawlResult` or an **async generator** if streaming is enabled.


2. **Concurrency & Dispatchers**: 
  * **`dispatcher`**param allows advanced concurrency control.
  * If omitted, a default dispatcher (like `MemoryAdaptiveDispatcher`) is used internally. 
  * Dispatchers handle concurrency, rate limiting, and memory-based adaptive throttling (see [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)).


3. **Streaming Support** : 
  * Enable streaming by setting `stream=True` in your `CrawlerRunConfig`.
  * When streaming, use `async for` to process results as they become available.
  * Ideal for processing large numbers of URLs without waiting for all to complete.


4. **Parallel** Execution**: 
  * `arun_many()` can run multiple requests concurrently under the hood. 
  * Each `CrawlResult` might also include a **`dispatch_result`**with concurrency details (like memory usage, start/end times).


### Basic Example (Batch Mode)
```
# Minimal usage: The default dispatcher will be used
results = await crawler.arun_many(
  urls=["https://site1.com", "https://site2.com"],
  config=CrawlerRunConfig(stream=False) # Default behavior
)
for res in results:
  if res.success:
    print(res.url, "crawled OK!")
  else:
    print("Failed:", res.url, "-", res.error_message)

```

### Streaming Example
```
config = CrawlerRunConfig(
  stream=True, # Enable streaming mode
  cache_mode=CacheMode.BYPASS
)
# Process results as they complete
async for result in await crawler.arun_many(
  urls=["https://site1.com", "https://site2.com", "https://site3.com"],
  config=config
):
  if result.success:
    print(f"Just completed: {result.url}")
    # Process each result immediately
    process_result(result)

```

### With a Custom Dispatcher
```
dispatcher = MemoryAdaptiveDispatcher(
  memory_threshold_percent=70.0,
  max_session_permit=10
)
results = await crawler.arun_many(
  urls=["https://site1.com", "https://site2.com", "https://site3.com"],
  config=my_run_config,
  dispatcher=dispatcher
)

```

**Key Points** : - Each URL is processed by the same or separate sessions, depending on the dispatcher’s strategy. - `dispatch_result` in each `CrawlResult` (if using concurrency) can hold memory and timing info. - If you need to handle authentication or session IDs, pass them in each individual task or within your run config.
### Return Value
Either a **list** of [`CrawlResult`](https://docs.crawl4ai.com/crawl-result/) objects, or an **async generator** if streaming is enabled. You can iterate to check `result.success` or read each item’s `extracted_content`, `markdown`, or `dispatch_result`.
## Dispatcher Reference
  * **`MemoryAdaptiveDispatcher`**: Dynamically manages concurrency based on system memory usage.
  * **`SemaphoreDispatcher`**: Fixed concurrency limit, simpler but less adaptive.


For advanced usage or custom settings, see [Multi-URL Crawling with Dispatchers](https://docs.crawl4ai.com/advanced/multi-url-crawling/).
## Common Pitfalls
1. **Large Lists** : If you pass thousands of URLs, be mindful of memory or rate-limits. A dispatcher can help. 
2. **Session Reuse** : If you need specialized logins or persistent contexts, ensure your dispatcher or tasks handle sessions accordingly. 
3. **Error Handling** : Each `CrawlResult` might fail for different reasons—always check `result.success` or the `error_message` before proceeding.
## Conclusion
Use `arun_many()` when you want to **crawl multiple URLs** simultaneously or in controlled parallel tasks. If you need advanced concurrency features (like memory-based adaptive throttling or complex rate-limiting), provide a **dispatcher**. Each result is a standard `CrawlResult`, possibly augmented with concurrency stats (`dispatch_result`) for deeper inspection. For more details on concurrency logic and dispatchers, see the [Advanced Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/) docs.
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/advanced/multi-url-crawling)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/session-management/)
    * Multi-URL Crawling
    * [Crawl Dispatcher](https://docs.crawl4ai.com/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Advanced Multi-URL Crawling with Dispatchers](https://docs.crawl4ai.com/advanced/multi-url-crawling#advanced-multi-url-crawling-with-dispatchers)
  * [1. Introduction](https://docs.crawl4ai.com/advanced/multi-url-crawling#1-introduction)
  * [2. Core Components](https://docs.crawl4ai.com/advanced/multi-url-crawling#2-core-components)
  * [3. Available Dispatchers](https://docs.crawl4ai.com/advanced/multi-url-crawling#3-available-dispatchers)
  * [4. Usage Examples](https://docs.crawl4ai.com/advanced/multi-url-crawling#4-usage-examples)
  * [5. Dispatch Results](https://docs.crawl4ai.com/advanced/multi-url-crawling#5-dispatch-results)
  * [6. Summary](https://docs.crawl4ai.com/advanced/multi-url-crawling#6-summary)


# Advanced Multi-URL Crawling with Dispatchers
> **Heads Up** : Crawl4AI supports advanced dispatchers for **parallel** or **throttled** crawling, providing dynamic rate limiting and memory usage checks. The built-in `arun_many()` function uses these dispatchers to handle concurrency efficiently.
## 1. Introduction
When crawling many URLs:
  * **Basic** : Use `arun()` in a loop (simple but less efficient)
  * **Better** : Use `arun_many()`, which efficiently handles multiple URLs with proper concurrency control
  * **Best** : Customize dispatcher behavior for your specific needs (memory management, rate limits, etc.)


**Why Dispatchers?**
  * **Adaptive** : Memory-based dispatchers can pause or slow down based on system resources
  * **Rate-limiting** : Built-in rate limiting with exponential backoff for 429/503 responses
  * **Real-time Monitoring** : Live dashboard of ongoing tasks, memory usage, and performance
  * **Flexibility** : Choose between memory-adaptive or semaphore-based concurrency


## 2. Core Components
### 2.1 Rate Limiter
```
class RateLimiter:
  def __init__(
    # Random delay range between requests
    base_delay: Tuple[float, float] = (1.0, 3.0), 
    # Maximum backoff delay
    max_delay: float = 60.0,            
    # Retries before giving up
    max_retries: int = 3,             
    # Status codes triggering backoff
    rate_limit_codes: List[int] = [429, 503]    
  )

```

Here’s the revised and simplified explanation of the **RateLimiter** , focusing on constructor parameters and adhering to your markdown style and mkDocs guidelines.
#### RateLimiter Constructor Parameters
The **RateLimiter** is a utility that helps manage the pace of requests to avoid overloading servers or getting blocked due to rate limits. It operates internally to delay requests and handle retries but can be configured using its constructor parameters.
**Parameters of the`RateLimiter` constructor:**
1. **`base_delay`**(`Tuple[float, float]` , default: `(1.0, 3.0)`) The range for a random delay (in seconds) between consecutive requests to the same domain.
  * A random delay is chosen between `base_delay[0]` and `base_delay[1]` for each request. 
  * This prevents sending requests at a predictable frequency, reducing the chances of triggering rate limits.


**Example:** If `base_delay = (2.0, 5.0)`, delays could be randomly chosen as `2.3s`, `4.1s`, etc.
2. **`max_delay`**(`float` , default: `60.0`) The maximum allowable delay when rate-limiting errors occur.
  * When servers return rate-limit responses (e.g., 429 or 503), the delay increases exponentially with jitter. 
  * The `max_delay` ensures the delay doesn’t grow unreasonably high, capping it at this value.


**Example:** For a `max_delay = 30.0`, even if backoff calculations suggest a delay of `45s`, it will cap at `30s`.
3. **`max_retries`**(`int` , default: `3`) The maximum number of retries for a request if rate-limiting errors occur.
  * After encountering a rate-limit response, the `RateLimiter` retries the request up to this number of times. 
  * If all retries fail, the request is marked as failed, and the process continues.


**Example:** If `max_retries = 3`, the system retries a failed request three times before giving up.
4. **`rate_limit_codes`**(`List[int]` , default: `[429, 503]`) A list of HTTP status codes that trigger the rate-limiting logic.
  * These status codes indicate the server is overwhelmed or actively limiting requests. 
  * You can customize this list to include other codes based on specific server behavior.


**Example:** If `rate_limit_codes = [429, 503, 504]`, the crawler will back off on these three error codes.
**How to Use the`RateLimiter` :**
Here’s an example of initializing and using a `RateLimiter` in your project:
```
from crawl4ai import RateLimiter
# Create a RateLimiter with custom settings
rate_limiter = RateLimiter(
  base_delay=(2.0, 4.0), # Random delay between 2-4 seconds
  max_delay=30.0,     # Cap delay at 30 seconds
  max_retries=5,     # Retry up to 5 times on rate-limiting errors
  rate_limit_codes=[429, 503] # Handle these HTTP status codes
)
# RateLimiter will handle delays and retries internally
# No additional setup is required for its operation

```

The `RateLimiter` integrates seamlessly with dispatchers like `MemoryAdaptiveDispatcher` and `SemaphoreDispatcher`, ensuring requests are paced correctly without user intervention. Its internal mechanisms manage delays and retries to avoid overwhelming servers while maximizing efficiency.
### 2.2 Crawler Monitor
The CrawlerMonitor provides real-time visibility into crawling operations:
```
from crawl4ai import CrawlerMonitor, DisplayMode
monitor = CrawlerMonitor(
  # Maximum rows in live display
  max_visible_rows=15,     
  # DETAILED or AGGREGATED view
  display_mode=DisplayMode.DETAILED 
)

```

**Display Modes** :
  1. **DETAILED** : Shows individual task status, memory usage, and timing
  2. **AGGREGATED** : Displays summary statistics and overall progress


## 3. Available Dispatchers
### 3.1 MemoryAdaptiveDispatcher (Default)
Automatically manages concurrency based on system memory usage:
```
from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher
dispatcher = MemoryAdaptiveDispatcher(
  memory_threshold_percent=90.0, # Pause if memory exceeds this
  check_interval=1.0,       # How often to check memory
  max_session_permit=10,     # Maximum concurrent tasks
  rate_limiter=RateLimiter(    # Optional rate limiting
    base_delay=(1.0, 2.0),
    max_delay=30.0,
    max_retries=2
  ),
  monitor=CrawlerMonitor(     # Optional monitoring
    max_visible_rows=15,
    display_mode=DisplayMode.DETAILED
  )
)

```

**Constructor Parameters:**
1. **`memory_threshold_percent`**(`float` , default: `90.0`) Specifies the memory usage threshold (as a percentage). If system memory usage exceeds this value, the dispatcher pauses crawling to prevent system overload.
2. **`check_interval`**(`float` , default: `1.0`) The interval (in seconds) at which the dispatcher checks system memory usage.
3. **`max_session_permit`**(`int` , default: `10`) The maximum number of concurrent crawling tasks allowed. This ensures resource limits are respected while maintaining concurrency.
4. **`memory_wait_timeout`**(`float` , default: `300.0`) Optional timeout (in seconds). If memory usage exceeds `memory_threshold_percent` for longer than this duration, a `MemoryError` is raised.
5. **`rate_limiter`**(`RateLimiter` , default: `None`) Optional rate-limiting logic to avoid server-side blocking (e.g., for handling 429 or 503 errors). See **RateLimiter** for details.
6. **`monitor`**(`CrawlerMonitor` , default: `None`) Optional monitoring for real-time task tracking and performance insights. See **CrawlerMonitor** for details.
### 3.2 SemaphoreDispatcher
Provides simple concurrency control with a fixed limit:
```
from crawl4ai.async_dispatcher import SemaphoreDispatcher
dispatcher = SemaphoreDispatcher(
  max_session_permit=20,     # Maximum concurrent tasks
  rate_limiter=RateLimiter(   # Optional rate limiting
    base_delay=(0.5, 1.0),
    max_delay=10.0
  ),
  monitor=CrawlerMonitor(    # Optional monitoring
    max_visible_rows=15,
    display_mode=DisplayMode.DETAILED
  )
)

```

**Constructor Parameters:**
1. **`max_session_permit`**(`int` , default: `20`) The maximum number of concurrent crawling tasks allowed, irrespective of semaphore slots.
2. **`rate_limiter`**(`RateLimiter` , default: `None`) Optional rate-limiting logic to avoid overwhelming servers. See **RateLimiter** for details.
3. **`monitor`**(`CrawlerMonitor` , default: `None`) Optional monitoring for tracking task progress and resource usage. See **CrawlerMonitor** for details.
## 4. Usage Examples
### 4.1 Batch Processing (Default)
```
async def crawl_batch():
  browser_config = BrowserConfig(headless=True, verbose=False)
  run_config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    stream=False # Default: get all results at once
  )
  dispatcher = MemoryAdaptiveDispatcher(
    memory_threshold_percent=70.0,
    check_interval=1.0,
    max_session_permit=10,
    monitor=CrawlerMonitor(
      display_mode=DisplayMode.DETAILED
    )
  )
  async with AsyncWebCrawler(config=browser_config) as crawler:
    # Get all results at once
    results = await crawler.arun_many(
      urls=urls,
      config=run_config,
      dispatcher=dispatcher
    )
    # Process all results after completion
    for result in results:
      if result.success:
        await process_result(result)
      else:
        print(f"Failed to crawl {result.url}: {result.error_message}")

```

**Review:** - **Purpose:** Executes a batch crawl with all URLs processed together after crawling is complete. - **Dispatcher:** Uses `MemoryAdaptiveDispatcher` to manage concurrency and system memory. - **Stream:** Disabled (`stream=False`), so all results are collected at once for post-processing. - **Best Use Case:** When you need to analyze results in bulk rather than individually during the crawl.
### 4.2 Streaming Mode
```
async def crawl_streaming():
  browser_config = BrowserConfig(headless=True, verbose=False)
  run_config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    stream=True # Enable streaming mode
  )
  dispatcher = MemoryAdaptiveDispatcher(
    memory_threshold_percent=70.0,
    check_interval=1.0,
    max_session_permit=10,
    monitor=CrawlerMonitor(
      display_mode=DisplayMode.DETAILED
    )
  )
  async with AsyncWebCrawler(config=browser_config) as crawler:
    # Process results as they become available
    async for result in await crawler.arun_many(
      urls=urls,
      config=run_config,
      dispatcher=dispatcher
    ):
      if result.success:
        # Process each result immediately
        await process_result(result)
      else:
        print(f"Failed to crawl {result.url}: {result.error_message}")

```

**Review:** - **Purpose:** Enables streaming to process results as soon as they’re available. - **Dispatcher:** Uses `MemoryAdaptiveDispatcher` for concurrency and memory management. - **Stream:** Enabled (`stream=True`), allowing real-time processing during crawling. - **Best Use Case:** When you need to act on results immediately, such as for real-time analytics or progressive data storage.
### 4.3 Semaphore-based Crawling
```
async def crawl_with_semaphore(urls):
  browser_config = BrowserConfig(headless=True, verbose=False)
  run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
  dispatcher = SemaphoreDispatcher(
    semaphore_count=5,
    rate_limiter=RateLimiter(
      base_delay=(0.5, 1.0),
      max_delay=10.0
    ),
    monitor=CrawlerMonitor(
      max_visible_rows=15,
      display_mode=DisplayMode.DETAILED
    )
  )
  async with AsyncWebCrawler(config=browser_config) as crawler:
    results = await crawler.arun_many(
      urls, 
      config=run_config,
      dispatcher=dispatcher
    )
    return results

```

**Review:** - **Purpose:** Uses `SemaphoreDispatcher` to limit concurrency with a fixed number of slots. - **Dispatcher:** Configured with a semaphore to control parallel crawling tasks. - **Rate Limiter:** Prevents servers from being overwhelmed by pacing requests. - **Best Use Case:** When you want precise control over the number of concurrent requests, independent of system memory.
### 4.4 Robots.txt Consideration
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  urls = [
    "https://example1.com",
    "https://example2.com",
    "https://example3.com"
  ]
  config = CrawlerRunConfig(
    cache_mode=CacheMode.ENABLED,
    check_robots_txt=True, # Will respect robots.txt for each URL
    semaphore_count=3   # Max concurrent requests
  )
  async with AsyncWebCrawler() as crawler:
    async for result in crawler.arun_many(urls, config=config):
      if result.success:
        print(f"Successfully crawled {result.url}")
      elif result.status_code == 403 and "robots.txt" in result.error_message:
        print(f"Skipped {result.url} - blocked by robots.txt")
      else:
        print(f"Failed to crawl {result.url}: {result.error_message}")
if __name__ == "__main__":
  asyncio.run(main())

```

**Review:** - **Purpose:** Ensures compliance with `robots.txt` rules for ethical and legal web crawling. - **Configuration:** Set `check_robots_txt=True` to validate each URL against `robots.txt` before crawling. - **Dispatcher:** Handles requests with concurrency limits (`semaphore_count=3`). - **Best Use Case:** When crawling websites that strictly enforce robots.txt policies or for responsible crawling practices.
## 5. Dispatch Results
Each crawl result includes dispatch information:
```
@dataclass
class DispatchResult:
  task_id: str
  memory_usage: float
  peak_memory: float
  start_time: datetime
  end_time: datetime
  error_message: str = ""

```

Access via `result.dispatch_result`:
```
for result in results:
  if result.success:
    dr = result.dispatch_result
    print(f"URL: {result.url}")
    print(f"Memory: {dr.memory_usage:.1f}MB")
    print(f"Duration: {dr.end_time - dr.start_time}")

```

## 6. Summary
1. **Two Dispatcher Types** :
  * MemoryAdaptiveDispatcher (default): Dynamic concurrency based on memory
  * SemaphoreDispatcher: Fixed concurrency limit


2. **Optional Components** :
  * RateLimiter: Smart request pacing and backoff
  * CrawlerMonitor: Real-time progress visualization


3. **Key Benefits** :
  * Automatic memory management
  * Built-in rate limiting
  * Live progress monitoring
  * Flexible concurrency control


Choose the dispatcher that best fits your needs:
  * **MemoryAdaptiveDispatcher** : For large crawls or limited resources
  * **SemaphoreDispatcher** : For simple, fixed-concurrency scenarios


Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/advanced/ssl-certificate)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/identity-based-crawling/)
    * SSL Certificate
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [SSLCertificate Reference](https://docs.crawl4ai.com/advanced/ssl-certificate#sslcertificate-reference)
  * [1. Overview](https://docs.crawl4ai.com/advanced/ssl-certificate#1-overview)
  * [2. Construction & Fetching](https://docs.crawl4ai.com/advanced/ssl-certificate#2-construction-fetching)
  * [3. Common Properties](https://docs.crawl4ai.com/advanced/ssl-certificate#3-common-properties)
  * [4. Export Methods](https://docs.crawl4ai.com/advanced/ssl-certificate#4-export-methods)
  * [5. Example Usage in Crawl4AI](https://docs.crawl4ai.com/advanced/ssl-certificate#5-example-usage-in-crawl4ai)
  * [6. Notes & Best Practices](https://docs.crawl4ai.com/advanced/ssl-certificate#6-notes-best-practices)


# `SSLCertificate` Reference
The **`SSLCertificate`**class encapsulates an SSL certificate’s data and allows exporting it in various formats (PEM, DER, JSON, or text). It’s used within**Crawl4AI** whenever you set **`fetch_ssl_certificate=True`**in your**`CrawlerRunConfig`**.
## 1. Overview
**Location** : `crawl4ai/ssl_certificate.py`
```
class SSLCertificate:
  """
  Represents an SSL certificate with methods to export in various formats.
  Main Methods:
  - from_url(url, timeout=10)
  - from_file(file_path)
  - from_binary(binary_data)
  - to_json(filepath=None)
  - to_pem(filepath=None)
  - to_der(filepath=None)
  ...
  Common Properties:
  - issuer
  - subject
  - valid_from
  - valid_until
  - fingerprint
  """

```

### Typical Use Case
  1. You **enable** certificate fetching in your crawl by: 
```
CrawlerRunConfig(fetch_ssl_certificate=True, ...)

```

  2. After `arun()`, if `result.ssl_certificate` is present, it’s an instance of **`SSLCertificate`**.
  3. You can **read** basic properties (issuer, subject, validity) or **export** them in multiple formats.


## 2. Construction & Fetching
### 2.1 **`from_url(url, timeout=10)`**
Manually load an SSL certificate from a given URL (port 443). Typically used internally, but you can call it directly if you want:
```
cert = SSLCertificate.from_url("https://example.com")
if cert:
  print("Fingerprint:", cert.fingerprint)

```

### 2.2 **`from_file(file_path)`**
Load from a file containing certificate data in ASN.1 or DER. Rarely needed unless you have local cert files:
```
cert = SSLCertificate.from_file("/path/to/cert.der")

```

### 2.3 **`from_binary(binary_data)`**
Initialize from raw binary. E.g., if you captured it from a socket or another source:
```
cert = SSLCertificate.from_binary(raw_bytes)

```

## 3. Common Properties
After obtaining a **`SSLCertificate`**instance (e.g.`result.ssl_certificate` from a crawl), you can read:
1. **`issuer`**_(dict)_ - E.g. `{"CN": "My Root CA", "O": "..."}` 2. **`subject`**_(dict)_ - E.g. `{"CN": "example.com", "O": "ExampleOrg"}` 3. **`valid_from`**_(str)_ - NotBefore date/time. Often in ASN.1/UTC format. 4. **`valid_until`**_(str)_ - NotAfter date/time. 5. **`fingerprint`**_(str)_ - The SHA-256 digest (lowercase hex). - E.g. `"d14d2e..."`
## 4. Export Methods
Once you have a **`SSLCertificate`**object, you can**export** or **inspect** it:
### 4.1 **`to_json(filepath=None)`→`Optional[str]`**
  * Returns a JSON string containing the parsed certificate fields. 
  * If `filepath` is provided, saves it to disk instead, returning `None`.


**Usage** : 
```
json_data = cert.to_json() # returns JSON string
cert.to_json("certificate.json") # writes file, returns None

```

### 4.2 **`to_pem(filepath=None)`→`Optional[str]`**
  * Returns a PEM-encoded string (common for web servers). 
  * If `filepath` is provided, saves it to disk instead.


```
pem_str = cert.to_pem()       # in-memory PEM string
cert.to_pem("/path/to/cert.pem")   # saved to file

```

### 4.3 **`to_der(filepath=None)`→`Optional[bytes]`**
  * Returns the original DER (binary ASN.1) bytes. 
  * If `filepath` is specified, writes the bytes there instead.


```
der_bytes = cert.to_der()
cert.to_der("certificate.der")

```

### 4.4 (Optional) **`export_as_text()`**
  * If you see a method like `export_as_text()`, it typically returns an OpenSSL-style textual representation. 
  * Not always needed, but can help for debugging or manual inspection.


## 5. Example Usage in Crawl4AI
Below is a minimal sample showing how the crawler obtains an SSL cert from a site, then reads or exports it. The code snippet:
```
import asyncio
import os
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  tmp_dir = "tmp"
  os.makedirs(tmp_dir, exist_ok=True)
  config = CrawlerRunConfig(
    fetch_ssl_certificate=True,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com", config=config)
    if result.success and result.ssl_certificate:
      cert = result.ssl_certificate
      # 1. Basic Info
      print("Issuer CN:", cert.issuer.get("CN", ""))
      print("Valid until:", cert.valid_until)
      print("Fingerprint:", cert.fingerprint)
      # 2. Export
      cert.to_json(os.path.join(tmp_dir, "certificate.json"))
      cert.to_pem(os.path.join(tmp_dir, "certificate.pem"))
      cert.to_der(os.path.join(tmp_dir, "certificate.der"))
if __name__ == "__main__":
  asyncio.run(main())

```

## 6. Notes & Best Practices
1. **Timeout** : `SSLCertificate.from_url` internally uses a default **10s** socket connect and wraps SSL. 2. **Binary Form** : The certificate is loaded in ASN.1 (DER) form, then re-parsed by `OpenSSL.crypto`. 3. **Validation** : This does **not** validate the certificate chain or trust store. It only fetches and parses. 4. **Integration** : Within Crawl4AI, you typically just set `fetch_ssl_certificate=True` in `CrawlerRunConfig`; the final result’s `ssl_certificate` is automatically built. 5. **Export** : If you need to store or analyze a cert, the `to_json` and `to_pem` are quite universal.
### Summary
  * **`SSLCertificate`**is a convenience class for capturing and exporting the**TLS certificate** from your crawled site(s). 
  * Common usage is in the **`CrawlResult.ssl_certificate`**field, accessible after setting`fetch_ssl_certificate=True`. 
  * Offers quick access to essential certificate details (`issuer`, `subject`, `fingerprint`) and is easy to export (PEM, DER, JSON) for further analysis or server usage.


Use it whenever you need **insight** into a site’s certificate or require some form of cryptographic or compliance check.
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/advanced/lazy-loading)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/file-downloading/)
    * Lazy Loading
    * [Hooks & Auth](https://docs.crawl4ai.com/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Handling Lazy-Loaded Images](https://docs.crawl4ai.com/advanced/lazy-loading#handling-lazy-loaded-images)
  * [Example: Ensuring Lazy Images Appear](https://docs.crawl4ai.com/advanced/lazy-loading#example-ensuring-lazy-images-appear)
  * [Combining with Other Link & Media Filters](https://docs.crawl4ai.com/advanced/lazy-loading#combining-with-other-link-media-filters)
  * [Tips & Troubleshooting](https://docs.crawl4ai.com/advanced/lazy-loading#tips-troubleshooting)


## Handling Lazy-Loaded Images
Many websites now load images **lazily** as you scroll. If you need to ensure they appear in your final crawl (and in `result.media`), consider:
1. **`wait_for_images=True`**– Wait for images to fully load. 2.**`scan_full_page`**– Force the crawler to scroll the entire page, triggering lazy loads. 3.**`scroll_delay`**– Add small delays between scroll steps.
**Note** : If the site requires multiple “Load More” triggers or complex interactions, see the [Page Interaction docs](https://docs.crawl4ai.com/core/page-interaction/).
### Example: Ensuring Lazy Images Appear
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig
from crawl4ai.async_configs import CacheMode
async def main():
  config = CrawlerRunConfig(
    # Force the crawler to wait until images are fully loaded
    wait_for_images=True,
    # Option 1: If you want to automatically scroll the page to load images
    scan_full_page=True, # Tells the crawler to try scrolling the entire page
    scroll_delay=0.5,   # Delay (seconds) between scroll steps
    # Option 2: If the site uses a 'Load More' or JS triggers for images,
    # you can also specify js_code or wait_for logic here.
    cache_mode=CacheMode.BYPASS,
    verbose=True
  )
  async with AsyncWebCrawler(config=BrowserConfig(headless=True)) as crawler:
    result = await crawler.arun("https://www.example.com/gallery", config=config)
    if result.success:
      images = result.media.get("images", [])
      print("Images found:", len(images))
      for i, img in enumerate(images[:5]):
        print(f"[Image {i}] URL: {img['src']}, Score: {img.get('score','N/A')}")
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**Explanation** :
  * **`wait_for_images=True`**The crawler tries to ensure images have finished loading before finalizing the HTML.
  * **`scan_full_page=True`**Tells the crawler to attempt scrolling from top to bottom. Each scroll step helps trigger lazy loading.
  * **`scroll_delay=0.5`**Pause half a second between each scroll step. Helps the site load images before continuing.


**When to Use** :
  * **Lazy-Loading** : If images appear only when the user scrolls into view, `scan_full_page` + `scroll_delay` helps the crawler see them. 
  * **Heavier Pages** : If a page is extremely long, be mindful that scanning the entire page can be slow. Adjust `scroll_delay` or the max scroll steps as needed.


## Combining with Other Link & Media Filters
You can still combine **lazy-load** logic with the usual **exclude_external_images** , **exclude_domains** , or link filtration:
```
config = CrawlerRunConfig(
  wait_for_images=True,
  scan_full_page=True,
  scroll_delay=0.5,
  # Filter out external images if you only want local ones
  exclude_external_images=True,
  # Exclude certain domains for links
  exclude_domains=["spammycdn.com"],
)

```

This approach ensures you see **all** images from the main domain while ignoring external ones, and the crawler physically scrolls the entire page so that lazy-loading triggers.
## Tips & Troubleshooting
1. **Long Pages** - Setting `scan_full_page=True` on extremely long or infinite-scroll pages can be resource-intensive. - Consider using [hooks](https://docs.crawl4ai.com/core/page-interaction/) or specialized logic to load specific sections or “Load More” triggers repeatedly.
2. **Mixed Image Behavior** - Some sites load images in batches as you scroll. If you’re missing images, increase your `scroll_delay` or call multiple partial scrolls in a loop with JS code or hooks.
3. **Combining with Dynamic Wait** - If the site has a placeholder that only changes to a real image after a certain event, you might do `wait_for="css:img.loaded"` or a custom JS `wait_for`.
4. **Caching** - If `cache_mode` is enabled, repeated crawls might skip some network fetches. If you suspect caching is missing new images, set `cache_mode=CacheMode.BYPASS` for fresh fetches.
With **lazy-loading** support, **wait_for_images** , and **scan_full_page** settings, you can capture the entire gallery or feed of images you expect—even if the site only loads them as the user scrolls. Combine these with the standard media filtering and domain exclusion for a complete link & media handling strategy.
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/api/strategies)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/arun/)
    * [arun_many()](https://docs.crawl4ai.com/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/crawl-result/)
    * Strategies


  * [Extraction & Chunking Strategies API](https://docs.crawl4ai.com/api/strategies#extraction-chunking-strategies-api)
  * [Extraction Strategies](https://docs.crawl4ai.com/api/strategies#extraction-strategies)
  * [Chunking Strategies](https://docs.crawl4ai.com/api/strategies#chunking-strategies)
  * [Usage Examples](https://docs.crawl4ai.com/api/strategies#usage-examples)
  * [Best Practices](https://docs.crawl4ai.com/api/strategies#best-practices)


# Extraction & Chunking Strategies API
This documentation covers the API reference for extraction and chunking strategies in Crawl4AI.
## Extraction Strategies
All extraction strategies inherit from the base `ExtractionStrategy` class and implement two key methods: - `extract(url: str, html: str) -> List[Dict[str, Any]]` - `run(url: str, sections: List[str]) -> List[Dict[str, Any]]`
### LLMExtractionStrategy
Used for extracting structured data using Language Models.
```
LLMExtractionStrategy(
  # Required Parameters
  provider: str = DEFAULT_PROVIDER,   # LLM provider (e.g., "ollama/llama2")
  api_token: Optional[str] = None,   # API token
  # Extraction Configuration
  instruction: str = None,       # Custom extraction instruction
  schema: Dict = None,         # Pydantic model schema for structured data
  extraction_type: str = "block",    # "block" or "schema"
  # Chunking Parameters
  chunk_token_threshold: int = 4000,  # Maximum tokens per chunk
  overlap_rate: float = 0.1,      # Overlap between chunks
  word_token_rate: float = 0.75,    # Word to token conversion rate
  apply_chunking: bool = True,     # Enable/disable chunking
  # API Configuration
  base_url: str = None,        # Base URL for API
  extra_args: Dict = {},        # Additional provider arguments
  verbose: bool = False        # Enable verbose logging
)

```

### CosineStrategy
Used for content similarity-based extraction and clustering.
```
CosineStrategy(
  # Content Filtering
  semantic_filter: str = None,    # Topic/keyword filter
  word_count_threshold: int = 10,   # Minimum words per cluster
  sim_threshold: float = 0.3,     # Similarity threshold
  # Clustering Parameters
  max_dist: float = 0.2,       # Maximum cluster distance
  linkage_method: str = 'ward',    # Clustering method
  top_k: int = 3,          # Top clusters to return
  # Model Configuration
  model_name: str = 'sentence-transformers/all-MiniLM-L6-v2', # Embedding model
  verbose: bool = False       # Enable verbose logging
)

```

### JsonCssExtractionStrategy
Used for CSS selector-based structured data extraction.
```
JsonCssExtractionStrategy(
  schema: Dict[str, Any],  # Extraction schema
  verbose: bool = False   # Enable verbose logging
)
# Schema Structure
schema = {
  "name": str,       # Schema name
  "baseSelector": str,   # Base CSS selector
  "fields": [        # List of fields to extract
    {
      "name": str,   # Field name
      "selector": str, # CSS selector
      "type": str,   # Field type: "text", "attribute", "html", "regex"
      "attribute": str, # For type="attribute"
      "pattern": str, # For type="regex"
      "transform": str, # Optional: "lowercase", "uppercase", "strip"
      "default": Any  # Default value if extraction fails
    }
  ]
}

```

## Chunking Strategies
All chunking strategies inherit from `ChunkingStrategy` and implement the `chunk(text: str) -> list` method.
### RegexChunking
Splits text based on regex patterns.
```
RegexChunking(
  patterns: List[str] = None # Regex patterns for splitting
                # Default: [r'\n\n']
)

```

### SlidingWindowChunking
Creates overlapping chunks with a sliding window approach.
```
SlidingWindowChunking(
  window_size: int = 100,  # Window size in words
  step: int = 50       # Step size between windows
)

```

### OverlappingWindowChunking
Creates chunks with specified overlap.
```
OverlappingWindowChunking(
  window_size: int = 1000,  # Chunk size in words
  overlap: int = 100     # Overlap size in words
)

```

## Usage Examples
### LLM Extraction
```
from pydantic import BaseModel
from crawl4ai.extraction_strategy import LLMExtractionStrategy
from crawl4ai import LLMConfig
# Define schema
class Article(BaseModel):
  title: str
  content: str
  author: str
# Create strategy
strategy = LLMExtractionStrategy(
  llm_config = LLMConfig(provider="ollama/llama2"),
  schema=Article.schema(),
  instruction="Extract article details"
)
# Use with crawler
result = await crawler.arun(
  url="https://example.com/article",
  extraction_strategy=strategy
)
# Access extracted data
data = json.loads(result.extracted_content)

```

### CSS Extraction
```
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
# Define schema
schema = {
  "name": "Product List",
  "baseSelector": ".product-card",
  "fields": [
    {
      "name": "title",
      "selector": "h2.title",
      "type": "text"
    },
    {
      "name": "price",
      "selector": ".price",
      "type": "text",
      "transform": "strip"
    },
    {
      "name": "image",
      "selector": "img",
      "type": "attribute",
      "attribute": "src"
    }
  ]
}
# Create and use strategy
strategy = JsonCssExtractionStrategy(schema)
result = await crawler.arun(
  url="https://example.com/products",
  extraction_strategy=strategy
)

```

### Content Chunking
```
from crawl4ai.chunking_strategy import OverlappingWindowChunking
from crawl4ai import LLMConfig
# Create chunking strategy
chunker = OverlappingWindowChunking(
  window_size=500, # 500 words per chunk
  overlap=50    # 50 words overlap
)
# Use with extraction strategy
strategy = LLMExtractionStrategy(
  llm_config = LLMConfig(provider="ollama/llama2"),
  chunking_strategy=chunker
)
result = await crawler.arun(
  url="https://example.com/long-article",
  extraction_strategy=strategy
)

```

## Best Practices
1. **Choose the Right Strategy** - Use `LLMExtractionStrategy` for complex, unstructured content - Use `JsonCssExtractionStrategy` for well-structured HTML - Use `CosineStrategy` for content similarity and clustering
2. **Optimize Chunking**
```
# For long documents
strategy = LLMExtractionStrategy(
  chunk_token_threshold=2000, # Smaller chunks
  overlap_rate=0.1      # 10% overlap
)

```

3. **Handle Errors**
```
try:
  result = await crawler.arun(
    url="https://example.com",
    extraction_strategy=strategy
  )
  if result.success:
    content = json.loads(result.extracted_content)
except Exception as e:
  print(f"Extraction failed: {e}")

```

4. **Monitor Performance**
```
strategy = CosineStrategy(
  verbose=True, # Enable logging
  word_count_threshold=20, # Filter short content
  top_k=5 # Limit results
)

```

Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/api/async-webcrawler)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * AsyncWebCrawler
    * [arun()](https://docs.crawl4ai.com/arun/)
    * [arun_many()](https://docs.crawl4ai.com/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/strategies/)


  * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler#asyncwebcrawler)
  * [1. Constructor Overview](https://docs.crawl4ai.com/api/async-webcrawler#1-constructor-overview)
  * [2. Lifecycle: Start/Close or Context Manager](https://docs.crawl4ai.com/api/async-webcrawler#2-lifecycle-startclose-or-context-manager)
  * [3. Primary Method: arun()](https://docs.crawl4ai.com/api/async-webcrawler#3-primary-method-arun)
  * [4. Batch Processing: arun_many()](https://docs.crawl4ai.com/api/async-webcrawler#4-batch-processing-arun_many)
  * [7. Best Practices & Migration Notes](https://docs.crawl4ai.com/api/async-webcrawler#7-best-practices-migration-notes)
  * [8. Summary](https://docs.crawl4ai.com/api/async-webcrawler#8-summary)


# AsyncWebCrawler
The **`AsyncWebCrawler`**is the core class for asynchronous web crawling in Crawl4AI. You typically create it**once** , optionally customize it with a **`BrowserConfig`**(e.g., headless, user agent), then**run** multiple **`arun()`**calls with different**`CrawlerRunConfig`**objects.
**Recommended usage** :
1. **Create** a `BrowserConfig` for global browser settings. 
2. **Instantiate** `AsyncWebCrawler(config=browser_config)`. 
3. **Use** the crawler in an async context manager (`async with`) or manage start/close manually. 
4. **Call** `arun(url, config=crawler_run_config)` for each page you want.
## 1. Constructor Overview
```
class AsyncWebCrawler:
  def __init__(
    self,
    crawler_strategy: Optional[AsyncCrawlerStrategy] = None,
    config: Optional[BrowserConfig] = None,
    always_bypass_cache: bool = False,      # deprecated
    always_by_pass_cache: Optional[bool] = None, # also deprecated
    base_directory: str = ...,
    thread_safe: bool = False,
    **kwargs,
  ):
    """
    Create an AsyncWebCrawler instance.
    Args:
      crawler_strategy: 
        (Advanced) Provide a custom crawler strategy if needed.
      config: 
        A BrowserConfig object specifying how the browser is set up.
      always_bypass_cache: 
        (Deprecated) Use CrawlerRunConfig.cache_mode instead.
      base_directory:   
        Folder for storing caches/logs (if relevant).
      thread_safe: 
        If True, attempts some concurrency safeguards. Usually False.
      **kwargs: 
        Additional legacy or debugging parameters.
    """
  )
### Typical Initialization
```python
from crawl4ai import AsyncWebCrawler, BrowserConfig
browser_cfg = BrowserConfig(
  browser_type="chromium",
  headless=True,
  verbose=True
)
crawler = AsyncWebCrawler(config=browser_cfg)

```

**Notes** :
  * **Legacy** parameters like `always_bypass_cache` remain for backward compatibility, but prefer to set **caching** in `CrawlerRunConfig`.


## 2. Lifecycle: Start/Close or Context Manager
### 2.1 Context Manager (Recommended)
```
async with AsyncWebCrawler(config=browser_cfg) as crawler:
  result = await crawler.arun("https://example.com")
  # The crawler automatically starts/closes resources

```

When the `async with` block ends, the crawler cleans up (closes the browser, etc.).
### 2.2 Manual Start & Close
```
crawler = AsyncWebCrawler(config=browser_cfg)
await crawler.start()
result1 = await crawler.arun("https://example.com")
result2 = await crawler.arun("https://another.com")
await crawler.close()

```

Use this style if you have a **long-running** application or need full control of the crawler’s lifecycle.
## 3. Primary Method: `arun()`
```
async def arun(
  self,
  url: str,
  config: Optional[CrawlerRunConfig] = None,
  # Legacy parameters for backward compatibility...
) -> CrawlResult:
  ...

```

### 3.1 New Approach
You pass a `CrawlerRunConfig` object that sets up everything about a crawl—content filtering, caching, session reuse, JS code, screenshots, etc.
```
import asyncio
from crawl4ai import CrawlerRunConfig, CacheMode
run_cfg = CrawlerRunConfig(
  cache_mode=CacheMode.BYPASS,
  css_selector="main.article",
  word_count_threshold=10,
  screenshot=True
)
async with AsyncWebCrawler(config=browser_cfg) as crawler:
  result = await crawler.arun("https://example.com/news", config=run_cfg)
  print("Crawled HTML length:", len(result.cleaned_html))
  if result.screenshot:
    print("Screenshot base64 length:", len(result.screenshot))

```

### 3.2 Legacy Parameters Still Accepted
For **backward** compatibility, `arun()` can still accept direct arguments like `css_selector=...`, `word_count_threshold=...`, etc., but we strongly advise migrating them into a **`CrawlerRunConfig`**.
## 4. Batch Processing: `arun_many()`
```
async def arun_many(
  self,
  urls: List[str],
  config: Optional[CrawlerRunConfig] = None,
  # Legacy parameters maintained for backwards compatibility...
) -> List[CrawlResult]:
  """
  Process multiple URLs with intelligent rate limiting and resource monitoring.
  """

```

### 4.1 Resource-Aware Crawling
The `arun_many()` method now uses an intelligent dispatcher that:
  * Monitors system memory usage
  * Implements adaptive rate limiting
  * Provides detailed progress monitoring
  * Manages concurrent crawls efficiently


### 4.2 Example Usage
Check page [Multi-url Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/) for a detailed example of how to use `arun_many()`.
```
### 4.3 Key Features
1. **Rate Limiting**
  - Automatic delay between requests
  - Exponential backoff on rate limit detection
  - Domain-specific rate limiting
  - Configurable retry strategy
2. **Resource Monitoring**
  - Memory usage tracking
  - Adaptive concurrency based on system load
  - Automatic pausing when resources are constrained
3. **Progress Monitoring**
  - Detailed or aggregated progress display
  - Real-time status updates
  - Memory usage statistics
4. **Error Handling**
  - Graceful handling of rate limits
  - Automatic retries with backoff
  - Detailed error reporting
---
## 5. `CrawlResult` Output
Each `arun()` returns a **`CrawlResult`** containing:
- `url`: Final URL (if redirected).
- `html`: Original HTML.
- `cleaned_html`: Sanitized HTML.
- `markdown_v2`: Deprecated. Instead just use regular `markdown`
- `extracted_content`: If an extraction strategy was used (JSON for CSS/LLM strategies).
- `screenshot`, `pdf`: If screenshots/PDF requested.
- `media`, `links`: Information about discovered images/links.
- `success`, `error_message`: Status info.
For details, see [CrawlResult doc](./crawl-result.md).
---
## 6. Quick Example
Below is an example hooking it all together:
```python
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
import json
async def main():
  # 1. Browser config
  browser_cfg = BrowserConfig(
    browser_type="firefox",
    headless=False,
    verbose=True
  )
  # 2. Run config
  schema = {
    "name": "Articles",
    "baseSelector": "article.post",
    "fields": [
      {
        "name": "title", 
        "selector": "h2", 
        "type": "text"
      },
      {
        "name": "url", 
        "selector": "a", 
        "type": "attribute", 
        "attribute": "href"
      }
    ]
  }
  run_cfg = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    extraction_strategy=JsonCssExtractionStrategy(schema),
    word_count_threshold=15,
    remove_overlay_elements=True,
    wait_for="css:.post" # Wait for posts to appear
  )
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    result = await crawler.arun(
      url="https://example.com/blog",
      config=run_cfg
    )
    if result.success:
      print("Cleaned HTML length:", len(result.cleaned_html))
      if result.extracted_content:
        articles = json.loads(result.extracted_content)
        print("Extracted articles:", articles[:2])
    else:
      print("Error:", result.error_message)
asyncio.run(main())

```

**Explanation** :
  * We define a **`BrowserConfig`**with Firefox, no headless, and`verbose=True`. 
  * We define a **`CrawlerRunConfig`**that**bypasses cache** , uses a **CSS** extraction schema, has a `word_count_threshold=15`, etc. 
  * We pass them to `AsyncWebCrawler(config=...)` and `arun(url=..., config=...)`.


## 7. Best Practices & Migration Notes
1. **Use** `BrowserConfig` for **global** settings about the browser’s environment. 2. **Use** `CrawlerRunConfig` for **per-crawl** logic (caching, content filtering, extraction strategies, wait conditions). 3. **Avoid** legacy parameters like `css_selector` or `word_count_threshold` directly in `arun()`. Instead:
```
run_cfg = CrawlerRunConfig(css_selector=".main-content", word_count_threshold=20)
result = await crawler.arun(url="...", config=run_cfg)

```

4. **Context Manager** usage is simplest unless you want a persistent crawler across many calls.
## 8. Summary
**AsyncWebCrawler** is your entry point to asynchronous crawling:
  * **Constructor** accepts **`BrowserConfig`**(or defaults).
  * **`arun(url, config=CrawlerRunConfig)`**is the main method for single-page crawls.
  * **`arun_many(urls, config=CrawlerRunConfig)`**handles concurrency across multiple URLs.
  * For advanced lifecycle control, use `start()` and `close()` explicitly. 


**Migration** : 
  * If you used `AsyncWebCrawler(browser_type="chromium", css_selector="...")`, move browser settings to `BrowserConfig(...)` and content/crawl logic to `CrawlerRunConfig(...)`.


This modular approach ensures your code is **clean** , **scalable** , and **easy to maintain**. For any advanced or rarely used parameters, see the [BrowserConfig docs](https://docs.crawl4ai.com/parameters/).
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/api/arun)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/async-webcrawler/)
    * arun()
    * [arun_many()](https://docs.crawl4ai.com/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/strategies/)


  * [arun() Parameter Guide (New Approach)](https://docs.crawl4ai.com/api/arun#arun-parameter-guide-new-approach)
  * [1. Core Usage](https://docs.crawl4ai.com/api/arun#1-core-usage)
  * [2. Cache Control](https://docs.crawl4ai.com/api/arun#2-cache-control)
  * [3. Content Processing & Selection](https://docs.crawl4ai.com/api/arun#3-content-processing-selection)
  * [4. Page Navigation & Timing](https://docs.crawl4ai.com/api/arun#4-page-navigation-timing)
  * [5. Session Management](https://docs.crawl4ai.com/api/arun#5-session-management)
  * [6. Screenshot, PDF & Media Options](https://docs.crawl4ai.com/api/arun#6-screenshot-pdf-media-options)
  * [7. Extraction Strategy](https://docs.crawl4ai.com/api/arun#7-extraction-strategy)
  * [8. Comprehensive Example](https://docs.crawl4ai.com/api/arun#8-comprehensive-example)
  * [9. Best Practices](https://docs.crawl4ai.com/api/arun#9-best-practices)
  * [10. Conclusion](https://docs.crawl4ai.com/api/arun#10-conclusion)


# `arun()` Parameter Guide (New Approach)
In Crawl4AI’s **latest** configuration model, nearly all parameters that once went directly to `arun()` are now part of **`CrawlerRunConfig`**. When calling`arun()` , you provide:
```
await crawler.arun(
  url="https://example.com", 
  config=my_run_config
)

```

Below is an organized look at the parameters that can go inside `CrawlerRunConfig`, divided by their functional areas. For **Browser** settings (e.g., `headless`, `browser_type`), see [BrowserConfig](https://docs.crawl4ai.com/parameters/).
## 1. Core Usage
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  run_config = CrawlerRunConfig(
    verbose=True,      # Detailed logging
    cache_mode=CacheMode.ENABLED, # Use normal read/write cache
    check_robots_txt=True,  # Respect robots.txt rules
    # ... other parameters
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://example.com",
      config=run_config
    )
    # Check if blocked by robots.txt
    if not result.success and result.status_code == 403:
      print(f"Error: {result.error_message}")

```

**Key Fields** : - `verbose=True` logs each crawl step. - `cache_mode` decides how to read/write the local crawl cache.
## 2. Cache Control
**`cache_mode`**(default:`CacheMode.ENABLED`) Use a built-in enum from `CacheMode`:
  * `ENABLED`: Normal caching—reads if available, writes if missing.
  * `DISABLED`: No caching—always refetch pages.
  * `READ_ONLY`: Reads from cache only; no new writes.
  * `WRITE_ONLY`: Writes to cache but doesn’t read existing data.
  * `BYPASS`: Skips reading cache for this crawl (though it might still write if set up that way).


```
run_config = CrawlerRunConfig(
  cache_mode=CacheMode.BYPASS
)

```

**Additional flags** :
  * `bypass_cache=True` acts like `CacheMode.BYPASS`.
  * `disable_cache=True` acts like `CacheMode.DISABLED`.
  * `no_cache_read=True` acts like `CacheMode.WRITE_ONLY`.
  * `no_cache_write=True` acts like `CacheMode.READ_ONLY`.


## 3. Content Processing & Selection
### 3.1 Text Processing
```
run_config = CrawlerRunConfig(
  word_count_threshold=10,  # Ignore text blocks <10 words
  only_text=False,      # If True, tries to remove non-text elements
  keep_data_attributes=False # Keep or discard data-* attributes
)

```

### 3.2 Content Selection
```
run_config = CrawlerRunConfig(
  css_selector=".main-content", # Focus on .main-content region only
  excluded_tags=["form", "nav"], # Remove entire tag blocks
  remove_forms=True,       # Specifically strip <form> elements
  remove_overlay_elements=True, # Attempt to remove modals/popups
)

```

### 3.3 Link Handling
```
run_config = CrawlerRunConfig(
  exclude_external_links=True,     # Remove external links from final content
  exclude_social_media_links=True,   # Remove links to known social sites
  exclude_domains=["ads.example.com"], # Exclude links to these domains
  exclude_social_media_domains=["facebook.com","twitter.com"], # Extend the default list
)

```

### 3.4 Media Filtering
```
run_config = CrawlerRunConfig(
  exclude_external_images=True # Strip images from other domains
)

```

## 4. Page Navigation & Timing
### 4.1 Basic Browser Flow
```
run_config = CrawlerRunConfig(
  wait_for="css:.dynamic-content", # Wait for .dynamic-content
  delay_before_return_html=2.0,  # Wait 2s before capturing final HTML
  page_timeout=60000,       # Navigation & script timeout (ms)
)

```

**Key Fields** :
  * `wait_for`: 
  * `"css:selector"` or 
  * `"js:() => boolean"` e.g. `js:() => document.querySelectorAll('.item').length > 10`.
  * `mean_delay` & `max_range`: define random delays for `arun_many()` calls. 
  * `semaphore_count`: concurrency limit when crawling multiple URLs.


### 4.2 JavaScript Execution
```
run_config = CrawlerRunConfig(
  js_code=[
    "window.scrollTo(0, document.body.scrollHeight);",
    "document.querySelector('.load-more')?.click();"
  ],
  js_only=False
)

```

  * `js_code` can be a single string or a list of strings. 
  * `js_only=True` means “I’m continuing in the same session with new JS steps, no new full navigation.”


### 4.3 Anti-Bot
```
run_config = CrawlerRunConfig(
  magic=True,
  simulate_user=True,
  override_navigator=True
)

```

- `magic=True` tries multiple stealth features. - `simulate_user=True` mimics mouse movements or random delays. - `override_navigator=True` fakes some navigator properties (like user agent checks). 
## 5. Session Management
**`session_id`**:
```
run_config = CrawlerRunConfig(
  session_id="my_session123"
)

```

If re-used in subsequent `arun()` calls, the same tab/page context is continued (helpful for multi-step tasks or stateful browsing). 
## 6. Screenshot, PDF & Media Options
```
run_config = CrawlerRunConfig(
  screenshot=True,       # Grab a screenshot as base64
  screenshot_wait_for=1.0,   # Wait 1s before capturing
  pdf=True,          # Also produce a PDF
  image_description_min_word_threshold=5, # If analyzing alt text
  image_score_threshold=3,        # Filter out low-score images
)

```

**Where they appear** : - `result.screenshot` → Base64 screenshot string. - `result.pdf` → Byte array with PDF data. 
## 7. Extraction Strategy
**For advanced data extraction** (CSS/LLM-based), set `extraction_strategy`:
```
run_config = CrawlerRunConfig(
  extraction_strategy=my_css_or_llm_strategy
)

```

The extracted data will appear in `result.extracted_content`.
## 8. Comprehensive Example
Below is a snippet combining many parameters:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  # Example schema
  schema = {
    "name": "Articles",
    "baseSelector": "article.post",
    "fields": [
      {"name": "title", "selector": "h2", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
  run_config = CrawlerRunConfig(
    # Core
    verbose=True,
    cache_mode=CacheMode.ENABLED,
    check_robots_txt=True,  # Respect robots.txt rules
    # Content
    word_count_threshold=10,
    css_selector="main.content",
    excluded_tags=["nav", "footer"],
    exclude_external_links=True,
    # Page & JS
    js_code="document.querySelector('.show-more')?.click();",
    wait_for="css:.loaded-block",
    page_timeout=30000,
    # Extraction
    extraction_strategy=JsonCssExtractionStrategy(schema),
    # Session
    session_id="persistent_session",
    # Media
    screenshot=True,
    pdf=True,
    # Anti-bot
    simulate_user=True,
    magic=True,
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com/posts", config=run_config)
    if result.success:
      print("HTML length:", len(result.cleaned_html))
      print("Extraction JSON:", result.extracted_content)
      if result.screenshot:
        print("Screenshot length:", len(result.screenshot))
      if result.pdf:
        print("PDF bytes length:", len(result.pdf))
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**What we covered** :
1. **Crawling** the main content region, ignoring external links. 2. Running **JavaScript** to click “.show-more”. 3. **Waiting** for “.loaded-block” to appear. 4. Generating a **screenshot** & **PDF** of the final page. 5. Extracting repeated “article.post” elements with a **CSS-based** extraction strategy.
## 9. Best Practices
1. **Use`BrowserConfig` for global browser** settings (headless, user agent). 2. **Use`CrawlerRunConfig`** to handle the **specific** crawl needs: content filtering, caching, JS, screenshot, extraction, etc. 3. Keep your **parameters consistent** in run configs—especially if you’re part of a large codebase with multiple crawls. 4. **Limit** large concurrency (`semaphore_count`) if the site or your system can’t handle it. 5. For dynamic pages, set `js_code` or `scan_full_page` so you load all content.
## 10. Conclusion
All parameters that used to be direct arguments to `arun()` now belong in **`CrawlerRunConfig`**. This approach:
  * Makes code **clearer** and **more maintainable**. 
  * Minimizes confusion about which arguments affect global vs. per-crawl behavior. 
  * Allows you to create **reusable** config objects for different pages or tasks.


For a **full** reference, check out the [CrawlerRunConfig Docs](https://docs.crawl4ai.com/parameters/). 
Happy crawling with your **structured, flexible** config approach!
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/advanced/proxy-security)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/hooks-auth/)
    * Proxy & Security
    * [Session Management](https://docs.crawl4ai.com/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Proxy](https://docs.crawl4ai.com/advanced/proxy-security#proxy)
  * [Basic Proxy Setup](https://docs.crawl4ai.com/advanced/proxy-security#basic-proxy-setup)
  * [Authenticated Proxy](https://docs.crawl4ai.com/advanced/proxy-security#authenticated-proxy)
  * [Rotating Proxies](https://docs.crawl4ai.com/advanced/proxy-security#rotating-proxies)


# Proxy
## Basic Proxy Setup
Simple proxy configuration with `BrowserConfig`:
```
from crawl4ai.async_configs import BrowserConfig
# Using proxy URL
browser_config = BrowserConfig(proxy="http://proxy.example.com:8080")
async with AsyncWebCrawler(config=browser_config) as crawler:
  result = await crawler.arun(url="https://example.com")
# Using SOCKS proxy
browser_config = BrowserConfig(proxy="socks5://proxy.example.com:1080")
async with AsyncWebCrawler(config=browser_config) as crawler:
  result = await crawler.arun(url="https://example.com")

```

## Authenticated Proxy
Use an authenticated proxy with `BrowserConfig`:
```
from crawl4ai.async_configs import BrowserConfig
proxy_config = {
  "server": "http://proxy.example.com:8080",
  "username": "user",
  "password": "pass"
}
browser_config = BrowserConfig(proxy_config=proxy_config)
async with AsyncWebCrawler(config=browser_config) as crawler:
  result = await crawler.arun(url="https://example.com")

```

Here's the corrected documentation:
## Rotating Proxies
Example using a proxy rotation service dynamically:
```
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
async def get_next_proxy():
  # Your proxy rotation logic here
  return {"server": "http://next.proxy.com:8080"}
async def main():
  browser_config = BrowserConfig()
  run_config = CrawlerRunConfig()
  async with AsyncWebCrawler(config=browser_config) as crawler:
    # For each URL, create a new run config with different proxy
    for url in urls:
      proxy = await get_next_proxy()
      # Clone the config and update proxy - this creates a new browser context
      current_config = run_config.clone(proxy_config=proxy)
      result = await crawler.arun(url=url, config=current_config)
if __name__ == "__main__":
  import asyncio
  asyncio.run(main())

```

Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/cache-modes)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * Cache Modes
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Crawl4AI Cache System and Migration Guide](https://docs.crawl4ai.com/core/cache-modes#crawl4ai-cache-system-and-migration-guide)
  * [Overview](https://docs.crawl4ai.com/core/cache-modes#overview)
  * [Old vs New Approach](https://docs.crawl4ai.com/core/cache-modes#old-vs-new-approach)
  * [Migration Example](https://docs.crawl4ai.com/core/cache-modes#migration-example)
  * [Common Migration Patterns](https://docs.crawl4ai.com/core/cache-modes#common-migration-patterns)


# Crawl4AI Cache System and Migration Guide
## Overview
Starting from version 0.5.0, Crawl4AI introduces a new caching system that replaces the old boolean flags with a more intuitive `CacheMode` enum. This change simplifies cache control and makes the behavior more predictable.
## Old vs New Approach
### Old Way (Deprecated)
The old system used multiple boolean flags: - `bypass_cache`: Skip cache entirely - `disable_cache`: Disable all caching - `no_cache_read`: Don't read from cache - `no_cache_write`: Don't write to cache
### New Way (Recommended)
The new system uses a single `CacheMode` enum: - `CacheMode.ENABLED`: Normal caching (read/write) - `CacheMode.DISABLED`: No caching at all - `CacheMode.READ_ONLY`: Only read from cache - `CacheMode.WRITE_ONLY`: Only write to cache - `CacheMode.BYPASS`: Skip cache for this operation
## Migration Example
### Old Code (Deprecated)
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def use_proxy():
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
      url="https://www.nbcnews.com/business",
      bypass_cache=True # Old way
    )
    print(len(result.markdown))
async def main():
  await use_proxy()
if __name__ == "__main__":
  asyncio.run(main())

```

### New Code (Recommended)
```
import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode
from crawl4ai.async_configs import CrawlerRunConfig
async def use_proxy():
  # Use CacheMode in CrawlerRunConfig
  config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS) 
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
      url="https://www.nbcnews.com/business",
      config=config # Pass the configuration object
    )
    print(len(result.markdown))
async def main():
  await use_proxy()
if __name__ == "__main__":
  asyncio.run(main())

```

## Common Migration Patterns
Old Flag | New Mode  
---|---  
`bypass_cache=True` | `cache_mode=CacheMode.BYPASS`  
`disable_cache=True` | `cache_mode=CacheMode.DISABLED`  
`no_cache_read=True` | `cache_mode=CacheMode.WRITE_ONLY`  
`no_cache_write=True` | `cache_mode=CacheMode.READ_ONLY`  
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/browser-crawler-config)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * Browser, Crawler & LLM Config
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Browser, Crawler & LLM Configuration (Quick Overview)](https://docs.crawl4ai.com/core/browser-crawler-config#browser-crawler-llm-configuration-quick-overview)
  * [1. BrowserConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config#1-browserconfig-essentials)
  * [2. CrawlerRunConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config#2-crawlerrunconfig-essentials)
  * [3. LLMConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config#3-llmconfig-essentials)
  * [4. Putting It All Together](https://docs.crawl4ai.com/core/browser-crawler-config#4-putting-it-all-together)
  * [5. Next Steps](https://docs.crawl4ai.com/core/browser-crawler-config#5-next-steps)
  * [6. Conclusion](https://docs.crawl4ai.com/core/browser-crawler-config#6-conclusion)


# Browser, Crawler & LLM Configuration (Quick Overview)
Crawl4AI’s flexibility stems from two key classes:
1. **`BrowserConfig`**– Dictates**how** the browser is launched and behaves (e.g., headless or visible, proxy, user agent). 2. **`CrawlerRunConfig`**– Dictates**how** each **crawl** operates (e.g., caching, extraction, timeouts, JavaScript code to run, etc.). 3. **`LLMConfig`**- Dictates**how** LLM providers are configured. (model, api token, base url, temperature etc.)
In most examples, you create **one** `BrowserConfig` for the entire crawler session, then pass a **fresh** or re-used `CrawlerRunConfig` whenever you call `arun()`. This tutorial shows the most commonly used parameters. If you need advanced or rarely used fields, see the [Configuration Parameters](https://docs.crawl4ai.com/api/parameters/).
## 1. BrowserConfig Essentials
```
class BrowserConfig:
  def __init__(
    browser_type="chromium",
    headless=True,
    proxy_config=None,
    viewport_width=1080,
    viewport_height=600,
    verbose=True,
    use_persistent_context=False,
    user_data_dir=None,
    cookies=None,
    headers=None,
    user_agent=None,
    text_mode=False,
    light_mode=False,
    extra_args=None,
    # ... other advanced parameters omitted here
  ):
    ...

```

### Key Fields to Note
1. **`browser_type`**- Options:`"chromium"` , `"firefox"`, or `"webkit"`. - Defaults to `"chromium"`. - If you need a different engine, specify it here.
2. **`headless`**-`True` : Runs the browser in headless mode (invisible browser). - `False`: Runs the browser in visible mode, which helps with debugging.
3. **`proxy_config`**- A dictionary with fields like:
```
{
  "server": "http://proxy.example.com:8080", 
  "username": "...", 
  "password": "..."
}

```

- Leave as `None` if a proxy is not required. 
4. **`viewport_width` & `viewport_height`**: - The initial window size. - Some sites behave differently with smaller or bigger viewports.
5. **`verbose`**: - If`True` , prints extra logs. - Handy for debugging.
6. **`use_persistent_context`**: - If`True` , uses a **persistent** browser profile, storing cookies/local storage across runs. - Typically also set `user_data_dir` to point to a folder.
7. **`cookies`** & **`headers`**: - If you want to start with specific cookies or add universal HTTP headers, set them here. - E.g.`cookies=[{"name": "session", "value": "abc123", "domain": "example.com"}]`.
8. **`user_agent`**: - Custom User-Agent string. If`None` , a default is used. - You can also set `user_agent_mode="random"` for randomization (if you want to fight bot detection).
9. **`text_mode`** & **`light_mode`**: -`text_mode=True` disables images, possibly speeding up text-only crawls. - `light_mode=True` turns off certain background features for performance. 
10. **`extra_args`**: - Additional flags for the underlying browser. - E.g.`["--disable-extensions"]`.
### Helper Methods
Both configuration classes provide a `clone()` method to create modified copies:
```
# Create a base browser config
base_browser = BrowserConfig(
  browser_type="chromium",
  headless=True,
  text_mode=True
)
# Create a visible browser config for debugging
debug_browser = base_browser.clone(
  headless=False,
  verbose=True
)

```

**Minimal Example** :
```
from crawl4ai import AsyncWebCrawler, BrowserConfig
browser_conf = BrowserConfig(
  browser_type="firefox",
  headless=False,
  text_mode=True
)
async with AsyncWebCrawler(config=browser_conf) as crawler:
  result = await crawler.arun("https://example.com")
  print(result.markdown[:300])

```

## 2. CrawlerRunConfig Essentials
```
class CrawlerRunConfig:
  def __init__(
    word_count_threshold=200,
    extraction_strategy=None,
    markdown_generator=None,
    cache_mode=None,
    js_code=None,
    wait_for=None,
    screenshot=False,
    pdf=False,
    enable_rate_limiting=False,
    rate_limit_config=None,
    memory_threshold_percent=70.0,
    check_interval=1.0,
    max_session_permit=20,
    display_mode=None,
    verbose=True,
    stream=False, # Enable streaming for arun_many()
    # ... other advanced parameters omitted
  ):
    ...

```

### Key Fields to Note
1. **`word_count_threshold`**: - The minimum word count before a block is considered. - If your site has lots of short paragraphs or items, you can lower it.
2. **`extraction_strategy`**: - Where you plug in JSON-based extraction (CSS, LLM, etc.). - If`None` , no structured extraction is done (only raw/cleaned HTML + markdown).
3. **`markdown_generator`**: - E.g.,`DefaultMarkdownGenerator(...)` , controlling how HTML→Markdown conversion is done. - If `None`, a default approach is used.
4. **`cache_mode`**: - Controls caching behavior (`ENABLED` , `BYPASS`, `DISABLED`, etc.). - If `None`, defaults to some level of caching or you can specify `CacheMode.ENABLED`.
5. **`js_code`**: - A string or list of JS strings to execute. - Great for “Load More” buttons or user interactions.
6. **`wait_for`**: - A CSS or JS expression to wait for before extracting content. - Common usage:`wait_for="css:.main-loaded"` or `wait_for="js:() => window.loaded === true"`.
7. **`screenshot`** & **`pdf`**: - If`True` , captures a screenshot or PDF after the page is fully loaded. - The results go to `result.screenshot` (base64) or `result.pdf` (bytes).
8. **`verbose`**: - Logs additional runtime details. - Overlaps with the browser’s verbosity if also set to`True` in `BrowserConfig`.
9. **`enable_rate_limiting`**: - If`True` , enables rate limiting for batch processing. - Requires `rate_limit_config` to be set.
10. **`memory_threshold_percent`**: - The memory threshold (as a percentage) to monitor. - If exceeded, the crawler will pause or slow down.
11. **`check_interval`**: - The interval (in seconds) to check system resources. - Affects how often memory and CPU usage are monitored.
12. **`max_session_permit`**: - The maximum number of concurrent crawl sessions. - Helps prevent overwhelming the system.
13. **`display_mode`**: - The display mode for progress information (`DETAILED` , `BRIEF`, etc.). - Affects how much information is printed during the crawl.
### Helper Methods
The `clone()` method is particularly useful for creating variations of your crawler configuration:
```
# Create a base configuration
base_config = CrawlerRunConfig(
  cache_mode=CacheMode.ENABLED,
  word_count_threshold=200,
  wait_until="networkidle"
)
# Create variations for different use cases
stream_config = base_config.clone(
  stream=True, # Enable streaming mode
  cache_mode=CacheMode.BYPASS
)
debug_config = base_config.clone(
  page_timeout=120000, # Longer timeout for debugging
  verbose=True
)

```

The `clone()` method: - Creates a new instance with all the same settings - Updates only the specified parameters - Leaves the original configuration unchanged - Perfect for creating variations without repeating all parameters
## 3. LLMConfig Essentials
### Key fields to note
1. **`provider`**: - Which LLM provoder to use. - Possible values are`"ollama/llama3","groq/llama3-70b-8192","groq/llama3-8b-8192", "openai/gpt-4o-mini" ,"openai/gpt-4o","openai/o1-mini","openai/o1-preview","openai/o3-mini","openai/o3-mini-high","anthropic/claude-3-haiku-20240307","anthropic/claude-3-opus-20240229","anthropic/claude-3-sonnet-20240229","anthropic/claude-3-5-sonnet-20240620","gemini/gemini-pro","gemini/gemini-1.5-pro","gemini/gemini-2.0-flash","gemini/gemini-2.0-flash-exp","gemini/gemini-2.0-flash-lite-preview-02-05","deepseek/deepseek-chat"` _(default:`"openai/gpt-4o-mini"`)_
2. **`api_token`**: - Optional. When not provided explicitly, api_token will be read from environment variables based on provider. For example: If a gemini model is passed as provider then,`"GEMINI_API_KEY"` will be read from environment variables - API token of LLM provider eg: `api_token = "gsk_1ClHGGJ7Lpn4WGybR7vNWGdyb3FY7zXEw3SCiy0BAVM9lL8CQv"` - Environment variable - use with prefix "env:" eg:`api_token = "env: GROQ_API_KEY"`
3. **`base_url`**: - If your provider has a custom endpoint
```
llm_config = LLMConfig(provider="openai/gpt-4o-mini", api_token=os.getenv("OPENAI_API_KEY"))

```

## 4. Putting It All Together
In a typical scenario, you define **one** `BrowserConfig` for your crawler session, then create **one or more** `CrawlerRunConfig` & `LLMConfig` depending on each call’s needs:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  # 1) Browser config: headless, bigger viewport, no proxy
  browser_conf = BrowserConfig(
    headless=True,
    viewport_width=1280,
    viewport_height=720
  )
  # 2) Example extraction strategy
  schema = {
    "name": "Articles",
    "baseSelector": "div.article",
    "fields": [
      {"name": "title", "selector": "h2", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
  extraction = JsonCssExtractionStrategy(schema)
  # 3) Example LLM content filtering
  gemini_config = LLMConfig(
    provider="gemini/gemini-1.5-pro" 
    api_token = "env:GEMINI_API_TOKEN"
  )
  # Initialize LLM filter with specific instruction
  filter = LLMContentFilter(
    llm_config=gemini_config, # or your preferred provider
    instruction="""
    Focus on extracting the core educational content.
    Include:
    - Key concepts and explanations
    - Important code examples
    - Essential technical details
    Exclude:
    - Navigation elements
    - Sidebars
    - Footer content
    Format the output as clean markdown with proper code blocks and headers.
    """,
    chunk_token_threshold=500, # Adjust based on your needs
    verbose=True
  )
  md_generator = DefaultMarkdownGenerator(
  content_filter=filter,
  options={"ignore_links": True}
  # 4) Crawler run config: skip cache, use extraction
  run_conf = CrawlerRunConfig(
    markdown_generator=md_generator,
    extraction_strategy=extraction,
    cache_mode=CacheMode.BYPASS,
  )
  async with AsyncWebCrawler(config=browser_conf) as crawler:
    # 4) Execute the crawl
    result = await crawler.arun(url="https://example.com/news", config=run_conf)
    if result.success:
      print("Extracted content:", result.extracted_content)
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

## 5. Next Steps
For a **detailed list** of available parameters (including advanced ones), see:
  * [BrowserConfig, CrawlerRunConfig & LLMConfig Reference](https://docs.crawl4ai.com/api/parameters/)


You can explore topics like:
  * **Custom Hooks & Auth** (Inject JavaScript or handle login forms). 
  * **Session Management** (Re-use pages, preserve state across multiple calls). 
  * **Magic Mode** or **Identity-based Crawling** (Fight bot detection by simulating user behavior). 
  * **Advanced Caching** (Fine-tune read/write cache modes). 


## 6. Conclusion
**BrowserConfig** , **CrawlerRunConfig** and **LLMConfig** give you straightforward ways to define:
  * **Which** browser to launch, how it should run, and any proxy or user agent needs. 
  * **How** each crawl should behave—caching, timeouts, JavaScript code, extraction strategies, etc.
  * **Which** LLM provider to use, api token, temperature and base url for custom endpoints


Use them together for **clear, maintainable** code, and when you need more specialized behavior, check out the advanced parameters in the [reference docs](https://docs.crawl4ai.com/api/parameters/). Happy crawling!
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/api/parameters)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/arun/)
    * [arun_many()](https://docs.crawl4ai.com/arun_many/)
    * Browser, Crawler & LLM Config
    * [CrawlResult](https://docs.crawl4ai.com/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/strategies/)


  * [1. BrowserConfig – Controlling the Browser](https://docs.crawl4ai.com/api/parameters#1-browserconfig-controlling-the-browser)
  * [1.1 Parameter Highlights](https://docs.crawl4ai.com/api/parameters#11-parameter-highlights)
  * [2. CrawlerRunConfig – Controlling Each Crawl](https://docs.crawl4ai.com/api/parameters#2-crawlerrunconfig-controlling-each-crawl)
  * [2.1 Parameter Highlights](https://docs.crawl4ai.com/api/parameters#21-parameter-highlights)
  * [2.2 Helper Methods](https://docs.crawl4ai.com/api/parameters#22-helper-methods)
  * [2.3 Example Usage](https://docs.crawl4ai.com/api/parameters#23-example-usage)
  * [3. LLMConfig - Setting up LLM providers](https://docs.crawl4ai.com/api/parameters#3-llmconfig-setting-up-llm-providers)
  * [3.1 Parameters](https://docs.crawl4ai.com/api/parameters#31-parameters)
  * [3.2 Example Usage](https://docs.crawl4ai.com/api/parameters#32-example-usage)
  * [4. Putting It All Together](https://docs.crawl4ai.com/api/parameters#4-putting-it-all-together)


# 1. **BrowserConfig** – Controlling the Browser
`BrowserConfig` focuses on **how** the browser is launched and behaves. This includes headless mode, proxies, user agents, and other environment tweaks.
```
from crawl4ai import AsyncWebCrawler, BrowserConfig
browser_cfg = BrowserConfig(
  browser_type="chromium",
  headless=True,
  viewport_width=1280,
  viewport_height=720,
  proxy="http://user:pass@proxy:8080",
  user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/116.0.0.0 Safari/537.36",
)

```

## 1.1 Parameter Highlights
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`browser_type`**| `"chromium"` , `"firefox"`, `"webkit"`_(default:`"chromium"`)_ | Which browser engine to use. `"chromium"` is typical for many sites, `"firefox"` or `"webkit"` for specialized tests.  
**`headless`**| `bool` (default: `True`) | Headless means no visible UI. `False` is handy for debugging.  
**`viewport_width`**| `int` (default: `1080`) | Initial page width (in px). Useful for testing responsive layouts.  
**`viewport_height`**| `int` (default: `600`) | Initial page height (in px).  
**`proxy`**| `str` (default: `None`) | Single-proxy URL if you want all traffic to go through it, e.g. `"http://user:pass@proxy:8080"`.  
**`proxy_config`**| `dict` (default: `None`) | For advanced or multi-proxy needs, specify details like `{"server": "...", "username": "...", ...}`.  
**`use_persistent_context`**| `bool` (default: `False`) | If `True`, uses a **persistent** browser context (keep cookies, sessions across runs). Also sets `use_managed_browser=True`.  
**`user_data_dir`**| `str or None` (default: `None`) | Directory to store user data (profiles, cookies). Must be set if you want permanent sessions.  
**`ignore_https_errors`**| `bool` (default: `True`) | If `True`, continues despite invalid certificates (common in dev/staging).  
**`java_script_enabled`**| `bool` (default: `True`) | Disable if you want no JS overhead, or if only static content is needed.  
**`cookies`**| `list` (default: `[]`) | Pre-set cookies, each a dict like `{"name": "session", "value": "...", "url": "..."}`.  
**`headers`**| `dict` (default: `{}`) | Extra HTTP headers for every request, e.g. `{"Accept-Language": "en-US"}`.  
**`user_agent`**| `str` (default: Chrome-based UA) | Your custom or random user agent. `user_agent_mode="random"` can shuffle it.  
**`light_mode`**| `bool` (default: `False`) | Disables some background features for performance gains.  
**`text_mode`**| `bool` (default: `False`) | If `True`, tries to disable images/other heavy content for speed.  
**`use_managed_browser`**| `bool` (default: `False`) | For advanced “managed” interactions (debugging, CDP usage). Typically set automatically if persistent context is on.  
**`extra_args`**| `list` (default: `[]`) | Additional flags for the underlying browser process, e.g. `["--disable-extensions"]`.  
**Tips** : - Set `headless=False` to visually **debug** how pages load or how interactions proceed. - If you need **authentication** storage or repeated sessions, consider `use_persistent_context=True` and specify `user_data_dir`. - For large pages, you might need a bigger `viewport_width` and `viewport_height` to handle dynamic content.
# 2. **CrawlerRunConfig** – Controlling Each Crawl
While `BrowserConfig` sets up the **environment** , `CrawlerRunConfig` details **how** each **crawl operation** should behave: caching, content filtering, link or domain blocking, timeouts, JavaScript code, etc.
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
run_cfg = CrawlerRunConfig(
  wait_for="css:.main-content",
  word_count_threshold=15,
  excluded_tags=["nav", "footer"],
  exclude_external_links=True,
  stream=True, # Enable streaming for arun_many()
)

```

## 2.1 Parameter Highlights
We group them by category. 
### A) **Content Processing**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`word_count_threshold`**| `int` (default: ~200) | Skips text blocks below X words. Helps ignore trivial sections.  
**`extraction_strategy`**| `ExtractionStrategy` (default: None) | If set, extracts structured data (CSS-based, LLM-based, etc.).  
**`markdown_generator`**| `MarkdownGenerationStrategy` (None) | If you want specialized markdown output (citations, filtering, chunking, etc.).  
**`css_selector`**| `str` (None) | Retains only the part of the page matching this selector. Affects the entire extraction process.  
**`target_elements`**| `List[str]` (None) | List of CSS selectors for elements to focus on for markdown generation and data extraction, while still processing the entire page for links, media, etc. Provides more flexibility than `css_selector`.  
**`excluded_tags`**| `list` (None) | Removes entire tags (e.g. `["script", "style"]`).  
**`excluded_selector`**| `str` (None) | Like `css_selector` but to exclude. E.g. `"#ads, .tracker"`.  
**`only_text`**| `bool` (False) | If `True`, tries to extract text-only content.  
**`prettiify`**| `bool` (False) | If `True`, beautifies final HTML (slower, purely cosmetic).  
**`keep_data_attributes`**| `bool` (False) | If `True`, preserve `data-*` attributes in cleaned HTML.  
**`remove_forms`**| `bool` (False) | If `True`, remove all `<form>` elements.  
### B) **Caching & Session**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`cache_mode`**| `CacheMode or None` | Controls how caching is handled (`ENABLED`, `BYPASS`, `DISABLED`, etc.). If `None`, typically defaults to `ENABLED`.  
**`session_id`**| `str or None` | Assign a unique ID to reuse a single browser session across multiple `arun()` calls.  
**`bypass_cache`**| `bool` (False) | If `True`, acts like `CacheMode.BYPASS`.  
**`disable_cache`**| `bool` (False) | If `True`, acts like `CacheMode.DISABLED`.  
**`no_cache_read`**| `bool` (False) | If `True`, acts like `CacheMode.WRITE_ONLY` (writes cache but never reads).  
**`no_cache_write`**| `bool` (False) | If `True`, acts like `CacheMode.READ_ONLY` (reads cache but never writes).  
Use these for controlling whether you read or write from a local content cache. Handy for large batch crawls or repeated site visits.
### C) **Page Navigation & Timing**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`wait_until`**| `str` (domcontentloaded) | Condition for navigation to “complete”. Often `"networkidle"` or `"domcontentloaded"`.  
**`page_timeout`**| `int` (60000 ms) | Timeout for page navigation or JS steps. Increase for slow sites.  
**`wait_for`**| `str or None` | Wait for a CSS (`"css:selector"`) or JS (`"js:() => bool"`) condition before content extraction.  
**`wait_for_images`**| `bool` (False) | Wait for images to load before finishing. Slows down if you only want text.  
**`delay_before_return_html`**| `float` (0.1) | Additional pause (seconds) before final HTML is captured. Good for last-second updates.  
**`check_robots_txt`**| `bool` (False) | Whether to check and respect robots.txt rules before crawling. If True, caches robots.txt for efficiency.  
**`mean_delay`**and**`max_range`**| `float` (0.1, 0.3) | If you call `arun_many()`, these define random delay intervals between crawls, helping avoid detection or rate limits.  
**`semaphore_count`**| `int` (5) | Max concurrency for `arun_many()`. Increase if you have resources for parallel crawls.  
### D) **Page Interaction**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`js_code`**| `str or list[str]` (None) | JavaScript to run after load. E.g. `"document.querySelector('button')?.click();"`.  
**`js_only`**| `bool` (False) | If `True`, indicates we’re reusing an existing session and only applying JS. No full reload.  
**`ignore_body_visibility`**| `bool` (True) | Skip checking if `<body>` is visible. Usually best to keep `True`.  
**`scan_full_page`**| `bool` (False) | If `True`, auto-scroll the page to load dynamic content (infinite scroll).  
**`scroll_delay`**| `float` (0.2) | Delay between scroll steps if `scan_full_page=True`.  
**`process_iframes`**| `bool` (False) | Inlines iframe content for single-page extraction.  
**`remove_overlay_elements`**| `bool` (False) | Removes potential modals/popups blocking the main content.  
**`simulate_user`**| `bool` (False) | Simulate user interactions (mouse movements) to avoid bot detection.  
**`override_navigator`**| `bool` (False) | Override `navigator` properties in JS for stealth.  
**`magic`**| `bool` (False) | Automatic handling of popups/consent banners. Experimental.  
**`adjust_viewport_to_content`**| `bool` (False) | Resizes viewport to match page content height.  
If your page is a single-page app with repeated JS updates, set `js_only=True` in subsequent calls, plus a `session_id` for reusing the same tab.
### E) **Media Handling**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`screenshot`**| `bool` (False) | Capture a screenshot (base64) in `result.screenshot`.  
**`screenshot_wait_for`**| `float or None` | Extra wait time before the screenshot.  
**`screenshot_height_threshold`**| `int` (~20000) | If the page is taller than this, alternate screenshot strategies are used.  
**`pdf`**| `bool` (False) | If `True`, returns a PDF in `result.pdf`.  
**`image_description_min_word_threshold`**| `int` (~50) | Minimum words for an image’s alt text or description to be considered valid.  
**`image_score_threshold`**| `int` (~3) | Filter out low-scoring images. The crawler scores images by relevance (size, context, etc.).  
**`exclude_external_images`**| `bool` (False) | Exclude images from other domains.  
### F) **Link/Domain Handling**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`exclude_social_media_domains`**| `list` (e.g. Facebook/Twitter) | A default list can be extended. Any link to these domains is removed from final output.  
**`exclude_external_links`**| `bool` (False) | Removes all links pointing outside the current domain.  
**`exclude_social_media_links`**| `bool` (False) | Strips links specifically to social sites (like Facebook or Twitter).  
**`exclude_domains`**| `list` ([]) | Provide a custom list of domains to exclude (like `["ads.com", "trackers.io"]`).  
Use these for link-level content filtering (often to keep crawls “internal” or to remove spammy domains).
### G) **Debug & Logging**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`verbose`**| `bool` (True) | Prints logs detailing each step of crawling, interactions, or errors.  
**`log_console`**| `bool` (False) | Logs the page’s JavaScript console output if you want deeper JS debugging.  
## 2.2 Helper Methods
Both `BrowserConfig` and `CrawlerRunConfig` provide a `clone()` method to create modified copies:
```
# Create a base configuration
base_config = CrawlerRunConfig(
  cache_mode=CacheMode.ENABLED,
  word_count_threshold=200
)
# Create variations using clone()
stream_config = base_config.clone(stream=True)
no_cache_config = base_config.clone(
  cache_mode=CacheMode.BYPASS,
  stream=True
)

```

The `clone()` method is particularly useful when you need slightly different configurations for different use cases, without modifying the original config.
## 2.3 Example Usage
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
async def main():
  # Configure the browser
  browser_cfg = BrowserConfig(
    headless=False,
    viewport_width=1280,
    viewport_height=720,
    proxy="http://user:pass@myproxy:8080",
    text_mode=True
  )
  # Configure the run
  run_cfg = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    session_id="my_session",
    css_selector="main.article",
    excluded_tags=["script", "style"],
    exclude_external_links=True,
    wait_for="css:.article-loaded",
    screenshot=True,
    stream=True
  )
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    result = await crawler.arun(
      url="https://example.com/news",
      config=run_cfg
    )
    if result.success:
      print("Final cleaned_html length:", len(result.cleaned_html))
      if result.screenshot:
        print("Screenshot captured (base64, length):", len(result.screenshot))
    else:
      print("Crawl failed:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())
## 2.4 Compliance & Ethics
| **Parameter**     | **Type / Default**   | **What It Does**                                                  |
|-----------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------|
| **`check_robots_txt`**| `bool` (False)     | When True, checks and respects robots.txt rules before crawling. Uses efficient caching with SQLite backend.     |
| **`user_agent`**   | `str` (None)      | User agent string to identify your crawler. Used for robots.txt checking when enabled.                |
```python
run_config = CrawlerRunConfig(
  check_robots_txt=True, # Enable robots.txt compliance
  user_agent="MyBot/1.0" # Identify your crawler
)

```

# 3. **LLMConfig** - Setting up LLM providers
LLMConfig is useful to pass LLM provider config to strategies and functions that rely on LLMs to do extraction, filtering, schema generation etc. Currently it can be used in the following -
  1. LLMExtractionStrategy
  2. LLMContentFilter
  3. JsonCssExtractionStrategy.generate_schema
  4. JsonXPathExtractionStrategy.generate_schema


## 3.1 Parameters
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`provider`**| `"ollama/llama3","groq/llama3-70b-8192","groq/llama3-8b-8192", "openai/gpt-4o-mini" ,"openai/gpt-4o","openai/o1-mini","openai/o1-preview","openai/o3-mini","openai/o3-mini-high","anthropic/claude-3-haiku-20240307","anthropic/claude-3-opus-20240229","anthropic/claude-3-sonnet-20240229","anthropic/claude-3-5-sonnet-20240620","gemini/gemini-pro","gemini/gemini-1.5-pro","gemini/gemini-2.0-flash","gemini/gemini-2.0-flash-exp","gemini/gemini-2.0-flash-lite-preview-02-05","deepseek/deepseek-chat"`_(default:`"openai/gpt-4o-mini"`)_ | Which LLM provoder to use.  
**`api_token`**|  1.Optional. When not provided explicitly, api_token will be read from environment variables based on provider. For example: If a gemini model is passed as provider then,`"GEMINI_API_KEY"` will be read from environment variables 2. API token of LLM provider eg: `api_token = "gsk_1ClHGGJ7Lpn4WGybR7vNWGdyb3FY7zXEw3SCiy0BAVM9lL8CQv"` 3. Environment variable - use with prefix "env:" eg:`api_token = "env: GROQ_API_KEY"` | API token to use for the given provider  
**`base_url`**|  Optional. Custom API endpoint | If your provider has a custom endpoint  
## 3.2 Example Usage
```
llm_config = LLMConfig(provider="openai/gpt-4o-mini", api_token=os.getenv("OPENAI_API_KEY"))

```

## 4. Putting It All Together
  * **Use** `BrowserConfig` for **global** browser settings: engine, headless, proxy, user agent. 
  * **Use** `CrawlerRunConfig` for each crawl’s **context** : how to filter content, handle caching, wait for dynamic elements, or run JS. 
  * **Pass** both configs to `AsyncWebCrawler` (the `BrowserConfig`) and then to `arun()` (the `CrawlerRunConfig`). 
  * **Use** `LLMConfig` for LLM provider configurations that can be used across all extraction, filtering, schema generation tasks. Can be used in - `LLMExtractionStrategy`, `LLMContentFilter`, `JsonCssExtractionStrategy.generate_schema` & `JsonXPathExtractionStrategy.generate_schema`


```
# Create a modified copy with the clone() method
stream_cfg = run_cfg.clone(
  stream=True,
  cache_mode=CacheMode.BYPASS
)

```

Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/advanced/session-management)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/proxy-security/)
    * Session Management
    * [Multi-URL Crawling](https://docs.crawl4ai.com/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Session Management](https://docs.crawl4ai.com/advanced/session-management#session-management)
  * [Basic Session Usage](https://docs.crawl4ai.com/advanced/session-management#basic-session-usage)
  * [Dynamic Content with Sessions](https://docs.crawl4ai.com/advanced/session-management#dynamic-content-with-sessions)
  * [Example 1: Basic Session-Based Crawling](https://docs.crawl4ai.com/advanced/session-management#example-1-basic-session-based-crawling)
  * [Advanced Technique 1: Custom Execution Hooks](https://docs.crawl4ai.com/advanced/session-management#advanced-technique-1-custom-execution-hooks)
  * [Advanced Technique 2: Integrated JavaScript Execution and Waiting](https://docs.crawl4ai.com/advanced/session-management#advanced-technique-2-integrated-javascript-execution-and-waiting)


# Session Management
Session management in Crawl4AI is a powerful feature that allows you to maintain state across multiple requests, making it particularly suitable for handling complex multi-step crawling tasks. It enables you to reuse the same browser tab (or page object) across sequential actions and crawls, which is beneficial for:
  * **Performing JavaScript actions before and after crawling.**
  * **Executing multiple sequential crawls faster** without needing to reopen tabs or allocate memory repeatedly.


**Note:** This feature is designed for sequential workflows and is not suitable for parallel operations.
#### Basic Session Usage
Use `BrowserConfig` and `CrawlerRunConfig` to maintain state with a `session_id`:
```
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
async with AsyncWebCrawler() as crawler:
  session_id = "my_session"
  # Define configurations
  config1 = CrawlerRunConfig(
    url="https://example.com/page1", session_id=session_id
  )
  config2 = CrawlerRunConfig(
    url="https://example.com/page2", session_id=session_id
  )
  # First request
  result1 = await crawler.arun(config=config1)
  # Subsequent request using the same session
  result2 = await crawler.arun(config=config2)
  # Clean up when done
  await crawler.crawler_strategy.kill_session(session_id)

```

#### Dynamic Content with Sessions
Here's an example of crawling GitHub commits across multiple pages while preserving session state:
```
from crawl4ai.async_configs import CrawlerRunConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from crawl4ai.cache_context import CacheMode
async def crawl_dynamic_content():
  async with AsyncWebCrawler() as crawler:
    session_id = "github_commits_session"
    url = "https://github.com/microsoft/TypeScript/commits/main"
    all_commits = []
    # Define extraction schema
    schema = {
      "name": "Commit Extractor",
      "baseSelector": "li.Box-sc-g0xbh4-0",
      "fields": [{
        "name": "title", "selector": "h4.markdown-title", "type": "text"
      }],
    }
    extraction_strategy = JsonCssExtractionStrategy(schema)
    # JavaScript and wait configurations
    js_next_page = """document.querySelector('a[data-testid="pagination-next-button"]').click();"""
    wait_for = """() => document.querySelectorAll('li.Box-sc-g0xbh4-0').length > 0"""
    # Crawl multiple pages
    for page in range(3):
      config = CrawlerRunConfig(
        url=url,
        session_id=session_id,
        extraction_strategy=extraction_strategy,
        js_code=js_next_page if page > 0 else None,
        wait_for=wait_for if page > 0 else None,
        js_only=page > 0,
        cache_mode=CacheMode.BYPASS
      )
      result = await crawler.arun(config=config)
      if result.success:
        commits = json.loads(result.extracted_content)
        all_commits.extend(commits)
        print(f"Page {page + 1}: Found {len(commits)} commits")
    # Clean up session
    await crawler.crawler_strategy.kill_session(session_id)
    return all_commits

```

## Example 1: Basic Session-Based Crawling
A simple example using session-based crawling:
```
import asyncio
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from crawl4ai.cache_context import CacheMode
async def basic_session_crawl():
  async with AsyncWebCrawler() as crawler:
    session_id = "dynamic_content_session"
    url = "https://example.com/dynamic-content"
    for page in range(3):
      config = CrawlerRunConfig(
        url=url,
        session_id=session_id,
        js_code="document.querySelector('.load-more-button').click();" if page > 0 else None,
        css_selector=".content-item",
        cache_mode=CacheMode.BYPASS
      )
      result = await crawler.arun(config=config)
      print(f"Page {page + 1}: Found {result.extracted_content.count('.content-item')} items")
    await crawler.crawler_strategy.kill_session(session_id)
asyncio.run(basic_session_crawl())

```

This example shows: 1. Reusing the same `session_id` across multiple requests. 2. Executing JavaScript to load more content dynamically. 3. Properly closing the session to free resources.
## Advanced Technique 1: Custom Execution Hooks
> Warning: You might feel confused by the end of the next few examples 😅, so make sure you are comfortable with the order of the parts before you start this.
Use custom hooks to handle complex scenarios, such as waiting for content to load dynamically:
```
async def advanced_session_crawl_with_hooks():
  first_commit = ""
  async def on_execution_started(page):
    nonlocal first_commit
    try:
      while True:
        await page.wait_for_selector("li.commit-item h4")
        commit = await page.query_selector("li.commit-item h4")
        commit = await commit.evaluate("(element) => element.textContent").strip()
        if commit and commit != first_commit:
          first_commit = commit
          break
        await asyncio.sleep(0.5)
    except Exception as e:
      print(f"Warning: New content didn't appear: {e}")
  async with AsyncWebCrawler() as crawler:
    session_id = "commit_session"
    url = "https://github.com/example/repo/commits/main"
    crawler.crawler_strategy.set_hook("on_execution_started", on_execution_started)
    js_next_page = """document.querySelector('a.pagination-next').click();"""
    for page in range(3):
      config = CrawlerRunConfig(
        url=url,
        session_id=session_id,
        js_code=js_next_page if page > 0 else None,
        css_selector="li.commit-item",
        js_only=page > 0,
        cache_mode=CacheMode.BYPASS
      )
      result = await crawler.arun(config=config)
      print(f"Page {page + 1}: Found {len(result.extracted_content)} commits")
    await crawler.crawler_strategy.kill_session(session_id)
asyncio.run(advanced_session_crawl_with_hooks())

```

This technique ensures new content loads before the next action.
## Advanced Technique 2: Integrated JavaScript Execution and Waiting
Combine JavaScript execution and waiting logic for concise handling of dynamic content:
```
async def integrated_js_and_wait_crawl():
  async with AsyncWebCrawler() as crawler:
    session_id = "integrated_session"
    url = "https://github.com/example/repo/commits/main"
    js_next_page_and_wait = """
    (async () => {
      const getCurrentCommit = () => document.querySelector('li.commit-item h4').textContent.trim();
      const initialCommit = getCurrentCommit();
      document.querySelector('a.pagination-next').click();
      while (getCurrentCommit() === initialCommit) {
        await new Promise(resolve => setTimeout(resolve, 100));
      }
    })();
    """
    for page in range(3):
      config = CrawlerRunConfig(
        url=url,
        session_id=session_id,
        js_code=js_next_page_and_wait if page > 0 else None,
        css_selector="li.commit-item",
        js_only=page > 0,
        cache_mode=CacheMode.BYPASS
      )
      result = await crawler.arun(config=config)
      print(f"Page {page + 1}: Found {len(result.extracted_content)} commits")
    await crawler.crawler_strategy.kill_session(session_id)
asyncio.run(integrated_js_and_wait_crawl())

```

#### Common Use Cases for Sessions
1. **Authentication Flows** : Login and interact with secured pages.
2. **Pagination Handling** : Navigate through multiple pages.
3. **Form Submissions** : Fill forms, submit, and process results.
4. **Multi-step Processes** : Complete workflows that span multiple actions.
5. **Dynamic Content Navigation** : Handle JavaScript-rendered or event-triggered content.
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/cli)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * Command Line Interface
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Crawl4AI CLI Guide](https://docs.crawl4ai.com/core/cli#crawl4ai-cli-guide)
  * [Table of Contents](https://docs.crawl4ai.com/core/cli#table-of-contents)
  * [Basic Usage](https://docs.crawl4ai.com/core/cli#basic-usage)
  * [Quick Example of Advanced Usage](https://docs.crawl4ai.com/core/cli#quick-example-of-advanced-usage)
  * [Configuration](https://docs.crawl4ai.com/core/cli#configuration)
  * [Advanced Features](https://docs.crawl4ai.com/core/cli#advanced-features)
  * [Output Formats](https://docs.crawl4ai.com/core/cli#output-formats)
  * [Complete Examples](https://docs.crawl4ai.com/core/cli#complete-examples)
  * [Best Practices & Tips](https://docs.crawl4ai.com/core/cli#best-practices-tips)
  * [Recap](https://docs.crawl4ai.com/core/cli#recap)


# Crawl4AI CLI Guide
## Table of Contents
  * [Installation](https://docs.crawl4ai.com/core/cli#installation)
  * [Basic Usage](https://docs.crawl4ai.com/core/cli#basic-usage)
  * [Configuration](https://docs.crawl4ai.com/core/cli#configuration)
  * [Browser Configuration](https://docs.crawl4ai.com/core/cli#browser-configuration)
  * [Crawler Configuration](https://docs.crawl4ai.com/core/cli#crawler-configuration)
  * [Extraction Configuration](https://docs.crawl4ai.com/core/cli#extraction-configuration)
  * [Content Filtering](https://docs.crawl4ai.com/core/cli#content-filtering)
  * [Advanced Features](https://docs.crawl4ai.com/core/cli#advanced-features)
  * [LLM Q&A](https://docs.crawl4ai.com/core/cli#llm-qa)
  * [Structured Data Extraction](https://docs.crawl4ai.com/core/cli#structured-data-extraction)
  * [Content Filtering](https://docs.crawl4ai.com/core/cli#content-filtering-1)
  * [Output Formats](https://docs.crawl4ai.com/core/cli#output-formats)
  * [Examples](https://docs.crawl4ai.com/core/cli#examples)
  * [Configuration Reference](https://docs.crawl4ai.com/core/cli#configuration-reference)
  * [Best Practices & Tips](https://docs.crawl4ai.com/core/cli#best-practices--tips)


## Basic Usage
The Crawl4AI CLI (`crwl`) provides a simple interface to the Crawl4AI library:
```
# Basic crawling
crwl https://example.com
# Get markdown output
crwl https://example.com -o markdown
# Verbose JSON output with cache bypass
crwl https://example.com -o json -v --bypass-cache
# See usage examples
crwl --example

```

## Quick Example of Advanced Usage
If you clone the repository and run the following command, you will receive the content of the page in JSON format according to a JSON-CSS schema:
```
crwl "https://www.infoq.com/ai-ml-data-eng/" -e docs/examples/cli/extract_css.yml -s docs/examples/cli/css_schema.json -o json;

```

## Configuration
### Browser Configuration
Browser settings can be configured via YAML file or command line parameters:
```
# browser.yml
headless: true
viewport_width: 1280
user_agent_mode: "random"
verbose: true
ignore_https_errors: true

```

```
# Using config file
crwl https://example.com -B browser.yml
# Using direct parameters
crwl https://example.com -b "headless=true,viewport_width=1280,user_agent_mode=random"

```

### Crawler Configuration
Control crawling behavior:
```
# crawler.yml
cache_mode: "bypass"
wait_until: "networkidle"
page_timeout: 30000
delay_before_return_html: 0.5
word_count_threshold: 100
scan_full_page: true
scroll_delay: 0.3
process_iframes: false
remove_overlay_elements: true
magic: true
verbose: true

```

```
# Using config file
crwl https://example.com -C crawler.yml
# Using direct parameters
crwl https://example.com -c "css_selector=#main,delay_before_return_html=2,scan_full_page=true"

```

### Extraction Configuration
Two types of extraction are supported:
  1. CSS/XPath-based extraction: 
```
# extract_css.yml
type: "json-css"
params:
 verbose: true

```



```
// css_schema.json
{
 "name": "ArticleExtractor",
 "baseSelector": ".article",
 "fields": [
  {
   "name": "title",
   "selector": "h1.title",
   "type": "text"
  },
  {
   "name": "link",
   "selector": "a.read-more",
   "type": "attribute",
   "attribute": "href"
  }
 ]
}

```

  1. LLM-based extraction: 
```
# extract_llm.yml
type: "llm"
provider: "openai/gpt-4"
instruction: "Extract all articles with their titles and links"
api_token: "your-token"
params:
 temperature: 0.3
 max_tokens: 1000

```



```
// llm_schema.json
{
 "title": "Article",
 "type": "object",
 "properties": {
  "title": {
   "type": "string",
   "description": "The title of the article"
  },
  "link": {
   "type": "string",
   "description": "URL to the full article"
  }
 }
}

```

## Advanced Features
### LLM Q&A
Ask questions about crawled content:
```
# Simple question
crwl https://example.com -q "What is the main topic discussed?"
# View content then ask questions
crwl https://example.com -o markdown # See content first
crwl https://example.com -q "Summarize the key points"
crwl https://example.com -q "What are the conclusions?"
# Combined with advanced crawling
crwl https://example.com \
  -B browser.yml \
  -c "css_selector=article,scan_full_page=true" \
  -q "What are the pros and cons mentioned?"

```

First-time setup: - Prompts for LLM provider and API token - Saves configuration in `~/.crawl4ai/global.yml` - Supports various providers (openai/gpt-4, anthropic/claude-3-sonnet, etc.) - For case of `ollama` you do not need to provide API token. - See [LiteLLM Providers](https://docs.litellm.ai/docs/providers) for full list
### Structured Data Extraction
Extract structured data using CSS selectors:
```
crwl https://example.com \
  -e extract_css.yml \
  -s css_schema.json \
  -o json

```

Or using LLM-based extraction:
```
crwl https://example.com \
  -e extract_llm.yml \
  -s llm_schema.json \
  -o json

```

### Content Filtering
Filter content for relevance:
```
# filter_bm25.yml
type: "bm25"
query: "target content"
threshold: 1.0
# filter_pruning.yml
type: "pruning"
query: "focus topic"
threshold: 0.48

```

```
crwl https://example.com -f filter_bm25.yml -o markdown-fit

```

## Output Formats
  * `all` - Full crawl result including metadata
  * `json` - Extracted structured data (when using extraction)
  * `markdown` / `md` - Raw markdown output
  * `markdown-fit` / `md-fit` - Filtered markdown for better readability


## Complete Examples
  1. Basic Extraction: 
```
crwl https://example.com \
  -B browser.yml \
  -C crawler.yml \
  -o json

```

  2. Structured Data Extraction: 
```
crwl https://example.com \
  -e extract_css.yml \
  -s css_schema.json \
  -o json \
  -v

```

  3. LLM Extraction with Filtering: 
```
crwl https://example.com \
  -B browser.yml \
  -e extract_llm.yml \
  -s llm_schema.json \
  -f filter_bm25.yml \
  -o json

```

  4. Interactive Q&A: 
```
# First crawl and view
crwl https://example.com -o markdown
# Then ask questions
crwl https://example.com -q "What are the main points?"
crwl https://example.com -q "Summarize the conclusions"

```



## Best Practices & Tips
  1. **Configuration Management** :
  2. Keep common configurations in YAML files
  3. Use CLI parameters for quick overrides
  4. Store sensitive data (API tokens) in `~/.crawl4ai/global.yml`
  5. **Performance Optimization** :
  6. Use `--bypass-cache` for fresh content
  7. Enable `scan_full_page` for infinite scroll pages
  8. Adjust `delay_before_return_html` for dynamic content
  9. **Content Extraction** :
  10. Use CSS extraction for structured content
  11. Use LLM extraction for unstructured content
  12. Combine with filters for focused results
  13. **Q &A Workflow**:
  14. View content first with `-o markdown`
  15. Ask specific questions
  16. Use broader context with appropriate selectors


## Recap
The Crawl4AI CLI provides: - Flexible configuration via files and parameters - Multiple extraction strategies (CSS, XPath, LLM) - Content filtering and optimization - Interactive Q&A capabilities - Various output formats
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/content-selection)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * Content Selection
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Content Selection](https://docs.crawl4ai.com/core/content-selection#content-selection)
  * [1. CSS-Based Selection](https://docs.crawl4ai.com/core/content-selection#1-css-based-selection)
  * [2. Content Filtering & Exclusions](https://docs.crawl4ai.com/core/content-selection#2-content-filtering-exclusions)
  * [3. Handling Iframes](https://docs.crawl4ai.com/core/content-selection#3-handling-iframes)
  * [4. Structured Extraction Examples](https://docs.crawl4ai.com/core/content-selection#4-structured-extraction-examples)
  * [5. Comprehensive Example](https://docs.crawl4ai.com/core/content-selection#5-comprehensive-example)
  * [6. Scraping Modes](https://docs.crawl4ai.com/core/content-selection#6-scraping-modes)
  * [7. Combining CSS Selection Methods](https://docs.crawl4ai.com/core/content-selection#7-combining-css-selection-methods)
  * [8. Conclusion](https://docs.crawl4ai.com/core/content-selection#8-conclusion)


# Content Selection
Crawl4AI provides multiple ways to **select** , **filter** , and **refine** the content from your crawls. Whether you need to target a specific CSS region, exclude entire tags, filter out external links, or remove certain domains and images, **`CrawlerRunConfig`**offers a wide range of parameters.
Below, we show how to configure these parameters and combine them for precise control.
## 1. CSS-Based Selection
There are two ways to select content from a page: using `css_selector` or the more flexible `target_elements`.
### 1.1 Using `css_selector`
A straightforward way to **limit** your crawl results to a certain region of the page is **`css_selector`**in**`CrawlerRunConfig`**:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  config = CrawlerRunConfig(
    # e.g., first 30 items from Hacker News
    css_selector=".athing:nth-child(-n+30)" 
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com/newest", 
      config=config
    )
    print("Partial HTML length:", len(result.cleaned_html))
if __name__ == "__main__":
  asyncio.run(main())

```

**Result** : Only elements matching that selector remain in `result.cleaned_html`.
### 1.2 Using `target_elements`
The `target_elements` parameter provides more flexibility by allowing you to target **multiple elements** for content extraction while preserving the entire page context for other features:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  config = CrawlerRunConfig(
    # Target article body and sidebar, but not other content
    target_elements=["article.main-content", "aside.sidebar"]
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://example.com/blog-post", 
      config=config
    )
    print("Markdown focused on target elements")
    print("Links from entire page still available:", len(result.links.get("internal", [])))
if __name__ == "__main__":
  asyncio.run(main())

```

**Key difference** : With `target_elements`, the markdown generation and structural data extraction focus on those elements, but other page elements (like links, images, and tables) are still extracted from the entire page. This gives you fine-grained control over what appears in your markdown content while preserving full page context for link analysis and media collection.
## 2. Content Filtering & Exclusions
### 2.1 Basic Overview
```
config = CrawlerRunConfig(
  # Content thresholds
  word_count_threshold=10,    # Minimum words per block
  # Tag exclusions
  excluded_tags=['form', 'header', 'footer', 'nav'],
  # Link filtering
  exclude_external_links=True,  
  exclude_social_media_links=True,
  # Block entire domains
  exclude_domains=["adtrackers.com", "spammynews.org"],  
  exclude_social_media_domains=["facebook.com", "twitter.com"],
  # Media filtering
  exclude_external_images=True
)

```

**Explanation** :
  * **`word_count_threshold`**: Ignores text blocks under X words. Helps skip trivial blocks like short nav or disclaimers.
  * **`excluded_tags`**: Removes entire tags (`<form>` , `<header>`, `<footer>`, etc.). 
  * **Link Filtering** : 
  * `exclude_external_links`: Strips out external links and may remove them from `result.links`. 
  * `exclude_social_media_links`: Removes links pointing to known social media domains. 
  * `exclude_domains`: A custom list of domains to block if discovered in links. 
  * `exclude_social_media_domains`: A curated list (override or add to it) for social media sites. 
  * **Media Filtering** : 
  * `exclude_external_images`: Discards images not hosted on the same domain as the main page (or its subdomains).


By default in case you set `exclude_social_media_links=True`, the following social media domains are excluded: 
```
[
  'facebook.com',
  'twitter.com',
  'x.com',
  'linkedin.com',
  'instagram.com',
  'pinterest.com',
  'tiktok.com',
  'snapchat.com',
  'reddit.com',
]

```

### 2.2 Example Usage
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  config = CrawlerRunConfig(
    css_selector="main.content", 
    word_count_threshold=10,
    excluded_tags=["nav", "footer"],
    exclude_external_links=True,
    exclude_social_media_links=True,
    exclude_domains=["ads.com", "spammytrackers.net"],
    exclude_external_images=True,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url="https://news.ycombinator.com", config=config)
    print("Cleaned HTML length:", len(result.cleaned_html))
if __name__ == "__main__":
  asyncio.run(main())

```

**Note** : If these parameters remove too much, reduce or disable them accordingly.
## 3. Handling Iframes
Some sites embed content in `<iframe>` tags. If you want that inline: 
```
config = CrawlerRunConfig(
  # Merge iframe content into the final output
  process_iframes=True,  
  remove_overlay_elements=True
)

```

**Usage** : 
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  config = CrawlerRunConfig(
    process_iframes=True,
    remove_overlay_elements=True
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://example.org/iframe-demo", 
      config=config
    )
    print("Iframe-merged length:", len(result.cleaned_html))
if __name__ == "__main__":
  asyncio.run(main())

```

## 4. Structured Extraction Examples
You can combine content selection with a more advanced extraction strategy. For instance, a **CSS-based** or **LLM-based** extraction strategy can run on the filtered HTML.
### 4.1 Pattern-Based with `JsonCssExtractionStrategy`
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  # Minimal schema for repeated items
  schema = {
    "name": "News Items",
    "baseSelector": "tr.athing",
    "fields": [
      {"name": "title", "selector": "span.titleline a", "type": "text"},
      {
        "name": "link", 
        "selector": "span.titleline a", 
        "type": "attribute", 
        "attribute": "href"
      }
    ]
  }
  config = CrawlerRunConfig(
    # Content filtering
    excluded_tags=["form", "header"],
    exclude_domains=["adsite.com"],
    # CSS selection or entire page
    css_selector="table.itemlist",
    # No caching for demonstration
    cache_mode=CacheMode.BYPASS,
    # Extraction strategy
    extraction_strategy=JsonCssExtractionStrategy(schema)
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com/newest", 
      config=config
    )
    data = json.loads(result.extracted_content)
    print("Sample extracted item:", data[:1]) # Show first item
if __name__ == "__main__":
  asyncio.run(main())

```

### 4.2 LLM-Based Extraction
```
import asyncio
import json
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
class ArticleData(BaseModel):
  headline: str
  summary: str
async def main():
  llm_strategy = LLMExtractionStrategy(
    llm_config = LLMConfig(provider="openai/gpt-4",api_token="sk-YOUR_API_KEY")
    schema=ArticleData.schema(),
    extraction_type="schema",
    instruction="Extract 'headline' and a short 'summary' from the content."
  )
  config = CrawlerRunConfig(
    exclude_external_links=True,
    word_count_threshold=20,
    extraction_strategy=llm_strategy
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url="https://news.ycombinator.com", config=config)
    article = json.loads(result.extracted_content)
    print(article)
if __name__ == "__main__":
  asyncio.run(main())

```

Here, the crawler:
  * Filters out external links (`exclude_external_links=True`). 
  * Ignores very short text blocks (`word_count_threshold=20`). 
  * Passes the final HTML to your LLM strategy for an AI-driven parse.


## 5. Comprehensive Example
Below is a short function that unifies **CSS selection** , **exclusion** logic, and a pattern-based extraction, demonstrating how you can fine-tune your final data:
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def extract_main_articles(url: str):
  schema = {
    "name": "ArticleBlock",
    "baseSelector": "div.article-block",
    "fields": [
      {"name": "headline", "selector": "h2", "type": "text"},
      {"name": "summary", "selector": ".summary", "type": "text"},
      {
        "name": "metadata",
        "type": "nested",
        "fields": [
          {"name": "author", "selector": ".author", "type": "text"},
          {"name": "date", "selector": ".date", "type": "text"}
        ]
      }
    ]
  }
  config = CrawlerRunConfig(
    # Keep only #main-content
    css_selector="#main-content",
    # Filtering
    word_count_threshold=10,
    excluded_tags=["nav", "footer"], 
    exclude_external_links=True,
    exclude_domains=["somebadsite.com"],
    exclude_external_images=True,
    # Extraction
    extraction_strategy=JsonCssExtractionStrategy(schema),
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url=url, config=config)
    if not result.success:
      print(f"Error: {result.error_message}")
      return None
    return json.loads(result.extracted_content)
async def main():
  articles = await extract_main_articles("https://news.ycombinator.com/newest")
  if articles:
    print("Extracted Articles:", articles[:2]) # Show first 2
if __name__ == "__main__":
  asyncio.run(main())

```

**Why This Works** : - **CSS** scoping with `#main-content`. - Multiple **exclude_** parameters to remove domains, external images, etc. - A **JsonCssExtractionStrategy** to parse repeated article blocks.
## 6. Scraping Modes
Crawl4AI provides two different scraping strategies for HTML content processing: `WebScrapingStrategy` (BeautifulSoup-based, default) and `LXMLWebScrapingStrategy` (LXML-based). The LXML strategy offers significantly better performance, especially for large HTML documents.
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LXMLWebScrapingStrategy
async def main():
  config = CrawlerRunConfig(
    scraping_strategy=LXMLWebScrapingStrategy() # Faster alternative to default BeautifulSoup
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://example.com", 
      config=config
    )

```

You can also create your own custom scraping strategy by inheriting from `ContentScrapingStrategy`. The strategy must return a `ScrapingResult` object with the following structure:
```
from crawl4ai import ContentScrapingStrategy, ScrapingResult, MediaItem, Media, Link, Links
class CustomScrapingStrategy(ContentScrapingStrategy):
  def scrap(self, url: str, html: str, **kwargs) -> ScrapingResult:
    # Implement your custom scraping logic here
    return ScrapingResult(
      cleaned_html="<html>...</html>", # Cleaned HTML content
      success=True,           # Whether scraping was successful
      media=Media(
        images=[           # List of images found
          MediaItem(
            src="https://example.com/image.jpg",
            alt="Image description",
            desc="Surrounding text",
            score=1,
            type="image",
            group_id=1,
            format="jpg",
            width=800
          )
        ],
        videos=[],          # List of videos (same structure as images)
        audios=[]           # List of audio files (same structure as images)
      ),
      links=Links(
        internal=[          # List of internal links
          Link(
            href="https://example.com/page",
            text="Link text",
            title="Link title",
            base_domain="example.com"
          )
        ],
        external=[]          # List of external links (same structure)
      ),
      metadata={            # Additional metadata
        "title": "Page Title",
        "description": "Page description"
      }
    )
  async def ascrap(self, url: str, html: str, **kwargs) -> ScrapingResult:
    # For simple cases, you can use the sync version
    return await asyncio.to_thread(self.scrap, url, html, **kwargs)

```

### Performance Considerations
The LXML strategy can be up to 10-20x faster than BeautifulSoup strategy, particularly when processing large HTML documents. However, please note:
  1. LXML strategy is currently experimental
  2. In some edge cases, the parsing results might differ slightly from BeautifulSoup
  3. If you encounter any inconsistencies between LXML and BeautifulSoup results, please [raise an issue](https://github.com/codeium/crawl4ai/issues) with a reproducible example


Choose LXML strategy when: - Processing large HTML documents (recommended for >100KB) - Performance is critical - Working with well-formed HTML
Stick to BeautifulSoup strategy (default) when: - Maximum compatibility is needed - Working with malformed HTML - Exact parsing behavior is critical
## 7. Combining CSS Selection Methods
You can combine `css_selector` and `target_elements` in powerful ways to achieve fine-grained control over your output:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  # Target specific content but preserve page context
  config = CrawlerRunConfig(
    # Focus markdown on main content and sidebar
    target_elements=["#main-content", ".sidebar"],
    # Global filters applied to entire page
    excluded_tags=["nav", "footer", "header"],
    exclude_external_links=True,
    # Use basic content thresholds
    word_count_threshold=15,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://example.com/article",
      config=config
    )
    print(f"Content focuses on specific elements, but all links still analyzed")
    print(f"Internal links: {len(result.links.get('internal', []))}")
    print(f"External links: {len(result.links.get('external', []))}")
if __name__ == "__main__":
  asyncio.run(main())

```

This approach gives you the best of both worlds: - Markdown generation and content extraction focus on the elements you care about - Links, images and other page data still give you the full context of the page - Content filtering still applies globally
## 8. Conclusion
By mixing **target_elements** or **css_selector** scoping, **content filtering** parameters, and advanced **extraction strategies** , you can precisely **choose** which data to keep. Key parameters in **`CrawlerRunConfig`**for content selection include:
  1. **`target_elements`**– Array of CSS selectors to focus markdown generation and data extraction, while preserving full page context for links and media.
  2. **`css_selector`**– Basic scoping to an element or region for all extraction processes.
  3. **`word_count_threshold`**– Skip short blocks.
  4. **`excluded_tags`**– Remove entire HTML tags.
  5. **`exclude_external_links`**,**`exclude_social_media_links`**,**`exclude_domains`**– Filter out unwanted links or domains.
  6. **`exclude_external_images`**– Remove images from external sources.
  7. **`process_iframes`**– Merge iframe content if needed.


Combine these with structured extraction (CSS, LLM-based, or others) to build powerful crawls that yield exactly the content you want, from raw or cleaned HTML up to sophisticated JSON structures. For more detail, see [Configuration Reference](https://docs.crawl4ai.com/api/parameters/). Enjoy curating your data to the max!
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/deep-crawling)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * Deep Crawling
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling#deep-crawling)
  * [1. Quick Example](https://docs.crawl4ai.com/core/deep-crawling#1-quick-example)
  * [2. Understanding Deep Crawling Strategy Options](https://docs.crawl4ai.com/core/deep-crawling#2-understanding-deep-crawling-strategy-options)
  * [3. Streaming vs. Non-Streaming Results](https://docs.crawl4ai.com/core/deep-crawling#3-streaming-vs-non-streaming-results)
  * [4. Filtering Content with Filter Chains](https://docs.crawl4ai.com/core/deep-crawling#4-filtering-content-with-filter-chains)
  * [5. Using Scorers for Prioritized Crawling](https://docs.crawl4ai.com/core/deep-crawling#5-using-scorers-for-prioritized-crawling)
  * [6. Advanced Filtering Techniques](https://docs.crawl4ai.com/core/deep-crawling#6-advanced-filtering-techniques)
  * [7. Building a Complete Advanced Crawler](https://docs.crawl4ai.com/core/deep-crawling#7-building-a-complete-advanced-crawler)
  * [8. Limiting and Controlling Crawl Size](https://docs.crawl4ai.com/core/deep-crawling#8-limiting-and-controlling-crawl-size)
  * [9. Common Pitfalls & Tips](https://docs.crawl4ai.com/core/deep-crawling#9-common-pitfalls-tips)
  * [10. Summary & Next Steps](https://docs.crawl4ai.com/core/deep-crawling#10-summary-next-steps)


# Deep Crawling
One of Crawl4AI's most powerful features is its ability to perform **configurable deep crawling** that can explore websites beyond a single page. With fine-tuned control over crawl depth, domain boundaries, and content filtering, Crawl4AI gives you the tools to extract precisely the content you need.
In this tutorial, you'll learn:
  1. How to set up a **Basic Deep Crawler** with BFS strategy 
  2. Understanding the difference between **streamed and non-streamed** output 
  3. Implementing **filters and scorers** to target specific content 
  4. Creating **advanced filtering chains** for sophisticated crawls 
  5. Using **BestFirstCrawling** for intelligent exploration prioritization 


> **Prerequisites** - You’ve completed or read [AsyncWebCrawler Basics](https://docs.crawl4ai.com/simple-crawling/) to understand how to run a simple crawl. - You know how to configure `CrawlerRunConfig`.
## 1. Quick Example
Here's a minimal code snippet that implements a basic deep crawl using the **BFSDeepCrawlStrategy** :
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
async def main():
  # Configure a 2-level deep crawl
  config = CrawlerRunConfig(
    deep_crawl_strategy=BFSDeepCrawlStrategy(
      max_depth=2, 
      include_external=False
    ),
    scraping_strategy=LXMLWebScrapingStrategy(),
    verbose=True
  )
  async with AsyncWebCrawler() as crawler:
    results = await crawler.arun("https://example.com", config=config)
    print(f"Crawled {len(results)} pages in total")
    # Access individual results
    for result in results[:3]: # Show first 3 results
      print(f"URL: {result.url}")
      print(f"Depth: {result.metadata.get('depth', 0)}")
if __name__ == "__main__":
  asyncio.run(main())

```

**What's happening?** - `BFSDeepCrawlStrategy(max_depth=2, include_external=False)` instructs Crawl4AI to: - Crawl the starting page (depth 0) plus 2 more levels - Stay within the same domain (don't follow external links) - Each result contains metadata like the crawl depth - Results are returned as a list after all crawling is complete
## 2. Understanding Deep Crawling Strategy Options
### 2.1 BFSDeepCrawlStrategy (Breadth-First Search)
The **BFSDeepCrawlStrategy** uses a breadth-first approach, exploring all links at one depth before moving deeper:
```
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
# Basic configuration
strategy = BFSDeepCrawlStrategy(
  max_depth=2,        # Crawl initial page + 2 levels deep
  include_external=False,  # Stay within the same domain
  max_pages=50,       # Maximum number of pages to crawl (optional)
  score_threshold=0.3,    # Minimum score for URLs to be crawled (optional)
)

```

**Key parameters:** - **`max_depth`**: Number of levels to crawl beyond the starting page -**`include_external`**: Whether to follow links to other domains -**`max_pages`**: Maximum number of pages to crawl (default: infinite) -**`score_threshold`**: Minimum score for URLs to be crawled (default: -inf) -**`filter_chain`**: FilterChain instance for URL filtering -**`url_scorer`**: Scorer instance for evaluating URLs
### 2.2 DFSDeepCrawlStrategy (Depth-First Search)
The **DFSDeepCrawlStrategy** uses a depth-first approach, explores as far down a branch as possible before backtracking.
```
from crawl4ai.deep_crawling import DFSDeepCrawlStrategy
# Basic configuration
strategy = DFSDeepCrawlStrategy(
  max_depth=2,        # Crawl initial page + 2 levels deep
  include_external=False,  # Stay within the same domain
  max_pages=30,       # Maximum number of pages to crawl (optional)
  score_threshold=0.5,    # Minimum score for URLs to be crawled (optional)
)

```

**Key parameters:** - **`max_depth`**: Number of levels to crawl beyond the starting page -**`include_external`**: Whether to follow links to other domains -**`max_pages`**: Maximum number of pages to crawl (default: infinite) -**`score_threshold`**: Minimum score for URLs to be crawled (default: -inf) -**`filter_chain`**: FilterChain instance for URL filtering -**`url_scorer`**: Scorer instance for evaluating URLs
### 2.3 BestFirstCrawlingStrategy (⭐️ - Recommended Deep crawl strategy)
For more intelligent crawling, use **BestFirstCrawlingStrategy** with scorers to prioritize the most relevant pages:
```
from crawl4ai.deep_crawling import BestFirstCrawlingStrategy
from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer
# Create a scorer
scorer = KeywordRelevanceScorer(
  keywords=["crawl", "example", "async", "configuration"],
  weight=0.7
)
# Configure the strategy
strategy = BestFirstCrawlingStrategy(
  max_depth=2,
  include_external=False,
  url_scorer=scorer,
  max_pages=25,       # Maximum number of pages to crawl (optional)
)

```

This crawling approach: - Evaluates each discovered URL based on scorer criteria - Visits higher-scoring pages first - Helps focus crawl resources on the most relevant content - Can limit total pages crawled with `max_pages` - Does not need `score_threshold` as it naturally prioritizes by score
## 3. Streaming vs. Non-Streaming Results
Crawl4AI can return results in two modes:
### 3.1 Non-Streaming Mode (Default)
```
config = CrawlerRunConfig(
  deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=1),
  stream=False # Default behavior
)
async with AsyncWebCrawler() as crawler:
  # Wait for ALL results to be collected before returning
  results = await crawler.arun("https://example.com", config=config)
  for result in results:
    process_result(result)

```

**When to use non-streaming mode:** - You need the complete dataset before processing - You're performing batch operations on all results together - Crawl time isn't a critical factor
### 3.2 Streaming Mode
```
config = CrawlerRunConfig(
  deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=1),
  stream=True # Enable streaming
)
async with AsyncWebCrawler() as crawler:
  # Returns an async iterator
  async for result in await crawler.arun("https://example.com", config=config):
    # Process each result as it becomes available
    process_result(result)

```

**Benefits of streaming mode:** - Process results immediately as they're discovered - Start working with early results while crawling continues - Better for real-time applications or progressive display - Reduces memory pressure when handling many pages
## 4. Filtering Content with Filter Chains
Filters help you narrow down which pages to crawl. Combine multiple filters using **FilterChain** for powerful targeting.
### 4.1 Basic URL Pattern Filter
```
from crawl4ai.deep_crawling.filters import FilterChain, URLPatternFilter
# Only follow URLs containing "blog" or "docs"
url_filter = URLPatternFilter(patterns=["*blog*", "*docs*"])
config = CrawlerRunConfig(
  deep_crawl_strategy=BFSDeepCrawlStrategy(
    max_depth=1,
    filter_chain=FilterChain([url_filter])
  )
)

```

### 4.2 Combining Multiple Filters
```
from crawl4ai.deep_crawling.filters import (
  FilterChain,
  URLPatternFilter,
  DomainFilter,
  ContentTypeFilter
)
# Create a chain of filters
filter_chain = FilterChain([
  # Only follow URLs with specific patterns
  URLPatternFilter(patterns=["*guide*", "*tutorial*"]),
  # Only crawl specific domains
  DomainFilter(
    allowed_domains=["docs.example.com"],
    blocked_domains=["old.docs.example.com"]
  ),
  # Only include specific content types
  ContentTypeFilter(allowed_types=["text/html"])
])
config = CrawlerRunConfig(
  deep_crawl_strategy=BFSDeepCrawlStrategy(
    max_depth=2,
    filter_chain=filter_chain
  )
)

```

### 4.3 Available Filter Types
Crawl4AI includes several specialized filters:
  * **`URLPatternFilter`**: Matches URL patterns using wildcard syntax
  * **`DomainFilter`**: Controls which domains to include or exclude
  * **`ContentTypeFilter`**: Filters based on HTTP Content-Type
  * **`ContentRelevanceFilter`**: Uses similarity to a text query
  * **`SEOFilter`**: Evaluates SEO elements (meta tags, headers, etc.)


## 5. Using Scorers for Prioritized Crawling
Scorers assign priority values to discovered URLs, helping the crawler focus on the most relevant content first.
### 5.1 KeywordRelevanceScorer
```
from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer
from crawl4ai.deep_crawling import BestFirstCrawlingStrategy
# Create a keyword relevance scorer
keyword_scorer = KeywordRelevanceScorer(
  keywords=["crawl", "example", "async", "configuration"],
  weight=0.7 # Importance of this scorer (0.0 to 1.0)
)
config = CrawlerRunConfig(
  deep_crawl_strategy=BestFirstCrawlingStrategy(
    max_depth=2,
    url_scorer=keyword_scorer
  ),
  stream=True # Recommended with BestFirstCrawling
)
# Results will come in order of relevance score
async with AsyncWebCrawler() as crawler:
  async for result in await crawler.arun("https://example.com", config=config):
    score = result.metadata.get("score", 0)
    print(f"Score: {score:.2f} | {result.url}")

```

**How scorers work:** - Evaluate each discovered URL before crawling - Calculate relevance based on various signals - Help the crawler make intelligent choices about traversal order
## 6. Advanced Filtering Techniques
### 6.1 SEO Filter for Quality Assessment
The **SEOFilter** helps you identify pages with strong SEO characteristics:
```
from crawl4ai.deep_crawling.filters import FilterChain, SEOFilter
# Create an SEO filter that looks for specific keywords in page metadata
seo_filter = SEOFilter(
  threshold=0.5, # Minimum score (0.0 to 1.0)
  keywords=["tutorial", "guide", "documentation"]
)
config = CrawlerRunConfig(
  deep_crawl_strategy=BFSDeepCrawlStrategy(
    max_depth=1,
    filter_chain=FilterChain([seo_filter])
  )
)

```

### 6.2 Content Relevance Filter
The **ContentRelevanceFilter** analyzes the actual content of pages:
```
from crawl4ai.deep_crawling.filters import FilterChain, ContentRelevanceFilter
# Create a content relevance filter
relevance_filter = ContentRelevanceFilter(
  query="Web crawling and data extraction with Python",
  threshold=0.7 # Minimum similarity score (0.0 to 1.0)
)
config = CrawlerRunConfig(
  deep_crawl_strategy=BFSDeepCrawlStrategy(
    max_depth=1,
    filter_chain=FilterChain([relevance_filter])
  )
)

```

This filter: - Measures semantic similarity between query and page content - It's a BM25-based relevance filter using head section content
## 7. Building a Complete Advanced Crawler
This example combines multiple techniques for a sophisticated crawl:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.deep_crawling import BestFirstCrawlingStrategy
from crawl4ai.deep_crawling.filters import (
  FilterChain,
  DomainFilter,
  URLPatternFilter,
  ContentTypeFilter
)
from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer
async def run_advanced_crawler():
  # Create a sophisticated filter chain
  filter_chain = FilterChain([
    # Domain boundaries
    DomainFilter(
      allowed_domains=["docs.example.com"],
      blocked_domains=["old.docs.example.com"]
    ),
    # URL patterns to include
    URLPatternFilter(patterns=["*guide*", "*tutorial*", "*blog*"]),
    # Content type filtering
    ContentTypeFilter(allowed_types=["text/html"])
  ])
  # Create a relevance scorer
  keyword_scorer = KeywordRelevanceScorer(
    keywords=["crawl", "example", "async", "configuration"],
    weight=0.7
  )
  # Set up the configuration
  config = CrawlerRunConfig(
    deep_crawl_strategy=BestFirstCrawlingStrategy(
      max_depth=2,
      include_external=False,
      filter_chain=filter_chain,
      url_scorer=keyword_scorer
    ),
    scraping_strategy=LXMLWebScrapingStrategy(),
    stream=True,
    verbose=True
  )
  # Execute the crawl
  results = []
  async with AsyncWebCrawler() as crawler:
    async for result in await crawler.arun("https://docs.example.com", config=config):
      results.append(result)
      score = result.metadata.get("score", 0)
      depth = result.metadata.get("depth", 0)
      print(f"Depth: {depth} | Score: {score:.2f} | {result.url}")
  # Analyze the results
  print(f"Crawled {len(results)} high-value pages")
  print(f"Average score: {sum(r.metadata.get('score', 0) for r in results) / len(results):.2f}")
  # Group by depth
  depth_counts = {}
  for result in results:
    depth = result.metadata.get("depth", 0)
    depth_counts[depth] = depth_counts.get(depth, 0) + 1
  print("Pages crawled by depth:")
  for depth, count in sorted(depth_counts.items()):
    print(f" Depth {depth}: {count} pages")
if __name__ == "__main__":
  asyncio.run(run_advanced_crawler())

```

## 8. Limiting and Controlling Crawl Size
### 8.1 Using max_pages
You can limit the total number of pages crawled with the `max_pages` parameter:
```
# Limit to exactly 20 pages regardless of depth
strategy = BFSDeepCrawlStrategy(
  max_depth=3,
  max_pages=20
)

```

This feature is useful for: - Controlling API costs - Setting predictable execution times - Focusing on the most important content - Testing crawl configurations before full execution
### 8.2 Using score_threshold
For BFS and DFS strategies, you can set a minimum score threshold to only crawl high-quality pages:
```
# Only follow links with scores above 0.4
strategy = DFSDeepCrawlStrategy(
  max_depth=2,
  url_scorer=KeywordRelevanceScorer(keywords=["api", "guide", "reference"]),
  score_threshold=0.4 # Skip URLs with scores below this value
)

```

Note that for BestFirstCrawlingStrategy, score_threshold is not needed since pages are already processed in order of highest score first.
## 9. Common Pitfalls & Tips
1.**Set realistic limits.** Be cautious with `max_depth` values > 3, which can exponentially increase crawl size. Use `max_pages` to set hard limits.
2.**Don't neglect the scoring component.** BestFirstCrawling works best with well-tuned scorers. Experiment with keyword weights for optimal prioritization.
3.**Be a good web citizen.** Respect robots.txt. (disabled by default)
4.**Handle page errors gracefully.** Not all pages will be accessible. Check `result.status` when processing results.
5.**Balance breadth vs. depth.** Choose your strategy wisely - BFS for comprehensive coverage, DFS for deep exploration, BestFirst for focused relevance-based crawling.
## 10. Summary & Next Steps
In this **Deep Crawling with Crawl4AI** tutorial, you learned to:
  * Configure **BFSDeepCrawlStrategy** , **DFSDeepCrawlStrategy** , and **BestFirstCrawlingStrategy**
  * Process results in streaming or non-streaming mode
  * Apply filters to target specific content
  * Use scorers to prioritize the most relevant pages
  * Limit crawls with `max_pages` and `score_threshold` parameters
  * Build a complete advanced crawler with combined techniques


With these tools, you can efficiently extract structured data from websites at scale, focusing precisely on the content you need for your specific use case.
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/fit-markdown)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * Fit Markdown
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Fit Markdown with Pruning & BM25](https://docs.crawl4ai.com/core/fit-markdown#fit-markdown-with-pruning-bm25)
  * [1. How “Fit Markdown” Works](https://docs.crawl4ai.com/core/fit-markdown#1-how-fit-markdown-works)
  * [2. PruningContentFilter](https://docs.crawl4ai.com/core/fit-markdown#2-pruningcontentfilter)
  * [3. BM25ContentFilter](https://docs.crawl4ai.com/core/fit-markdown#3-bm25contentfilter)
  * [4. Accessing the “Fit” Output](https://docs.crawl4ai.com/core/fit-markdown#4-accessing-the-fit-output)
  * [5. Code Patterns Recap](https://docs.crawl4ai.com/core/fit-markdown#5-code-patterns-recap)
  * [6. Combining with “word_count_threshold” & Exclusions](https://docs.crawl4ai.com/core/fit-markdown#6-combining-with-word_count_threshold-exclusions)
  * [7. Custom Filters](https://docs.crawl4ai.com/core/fit-markdown#7-custom-filters)
  * [8. Final Thoughts](https://docs.crawl4ai.com/core/fit-markdown#8-final-thoughts)


# Fit Markdown with Pruning & BM25
**Fit Markdown** is a specialized **filtered** version of your page’s markdown, focusing on the most relevant content. By default, Crawl4AI converts the entire HTML into a broad **raw_markdown**. With fit markdown, we apply a **content filter** algorithm (e.g., **Pruning** or **BM25**) to remove or rank low-value sections—such as repetitive sidebars, shallow text blocks, or irrelevancies—leaving a concise textual “core.”
## 1. How “Fit Markdown” Works
### 1.1 The `content_filter`
In **`CrawlerRunConfig`**, you can specify a**`content_filter`**to shape how content is pruned or ranked before final markdown generation. A filter’s logic is applied**before** or **during** the HTML→Markdown process, producing:
  * **`result.markdown.raw_markdown`**(unfiltered)
  * **`result.markdown.fit_markdown`**(filtered or “fit” version)
  * **`result.markdown.fit_html`**(the corresponding HTML snippet that produced`fit_markdown`)


### 1.2 Common Filters
1. **PruningContentFilter** – Scores each node by text density, link density, and tag importance, discarding those below a threshold. 2. **BM25ContentFilter** – Focuses on textual relevance using BM25 ranking, especially useful if you have a specific user query (e.g., “machine learning” or “food nutrition”).
## 2. PruningContentFilter
**Pruning** discards less relevant nodes based on **text density, link density, and tag importance**. It’s a heuristic-based approach—if certain sections appear too “thin” or too “spammy,” they’re pruned.
### 2.1 Usage Example
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
async def main():
  # Step 1: Create a pruning filter
  prune_filter = PruningContentFilter(
    # Lower → more content retained, higher → more content pruned
    threshold=0.45,      
    # "fixed" or "dynamic"
    threshold_type="dynamic", 
    # Ignore nodes with <5 words
    min_word_threshold=5   
  )
  # Step 2: Insert it into a Markdown Generator
  md_generator = DefaultMarkdownGenerator(content_filter=prune_filter)
  # Step 3: Pass it to CrawlerRunConfig
  config = CrawlerRunConfig(
    markdown_generator=md_generator
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com", 
      config=config
    )
    if result.success:
      # 'fit_markdown' is your pruned content, focusing on "denser" text
      print("Raw Markdown length:", len(result.markdown.raw_markdown))
      print("Fit Markdown length:", len(result.markdown.fit_markdown))
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

### 2.2 Key Parameters
  * **`min_word_threshold`**(int): If a block has fewer words than this, it’s pruned.
  * **`threshold_type`**(str):
  * `"fixed"` → each node must exceed `threshold` (0–1). 
  * `"dynamic"` → node scoring adjusts according to tag type, text/link density, etc. 
  * **`threshold`**(float, default ~0.48): The base or “anchor” cutoff.


**Algorithmic Factors** :
  * **Text density** – Encourages blocks that have a higher ratio of text to overall content. 
  * **Link density** – Penalizes sections that are mostly links. 
  * **Tag importance** – e.g., an `<article>` or `<p>` might be more important than a `<div>`. 
  * **Structural context** – If a node is deeply nested or in a suspected sidebar, it might be deprioritized.


## 3. BM25ContentFilter
**BM25** is a classical text ranking algorithm often used in search engines. If you have a **user query** or rely on page metadata to derive a query, BM25 can identify which text chunks best match that query.
### 3.1 Usage Example
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import BM25ContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
async def main():
  # 1) A BM25 filter with a user query
  bm25_filter = BM25ContentFilter(
    user_query="startup fundraising tips",
    # Adjust for stricter or looser results
    bm25_threshold=1.2 
  )
  # 2) Insert into a Markdown Generator
  md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter)
  # 3) Pass to crawler config
  config = CrawlerRunConfig(
    markdown_generator=md_generator
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com", 
      config=config
    )
    if result.success:
      print("Fit Markdown (BM25 query-based):")
      print(result.markdown.fit_markdown)
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

### 3.2 Parameters
  * **`user_query`**(str, optional): E.g.`"machine learning"`. If blank, the filter tries to glean a query from page metadata. 
  * **`bm25_threshold`**(float, default 1.0):
  * Higher → fewer chunks but more relevant. 
  * Lower → more inclusive. 


> In more advanced scenarios, you might see parameters like `use_stemming`, `case_sensitive`, or `priority_tags` to refine how text is tokenized or weighted.
## 4. Accessing the “Fit” Output
After the crawl, your “fit” content is found in **`result.markdown.fit_markdown`**.
```
fit_md = result.markdown.fit_markdown
fit_html = result.markdown.fit_html

```

If the content filter is **BM25** , you might see additional logic or references in `fit_markdown` that highlight relevant segments. If it’s **Pruning** , the text is typically well-cleaned but not necessarily matched to a query.
## 5. Code Patterns Recap
### 5.1 Pruning
```
prune_filter = PruningContentFilter(
  threshold=0.5,
  threshold_type="fixed",
  min_word_threshold=10
)
md_generator = DefaultMarkdownGenerator(content_filter=prune_filter)
config = CrawlerRunConfig(markdown_generator=md_generator)

```

### 5.2 BM25
```
bm25_filter = BM25ContentFilter(
  user_query="health benefits fruit",
  bm25_threshold=1.2
)
md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter)
config = CrawlerRunConfig(markdown_generator=md_generator)

```

## 6. Combining with “word_count_threshold” & Exclusions
Remember you can also specify:
```
config = CrawlerRunConfig(
  word_count_threshold=10,
  excluded_tags=["nav", "footer", "header"],
  exclude_external_links=True,
  markdown_generator=DefaultMarkdownGenerator(
    content_filter=PruningContentFilter(threshold=0.5)
  )
)

```

Thus, **multi-level** filtering occurs:
  1. The crawler’s `excluded_tags` are removed from the HTML first. 
  2. The content filter (Pruning, BM25, or custom) prunes or ranks the remaining text blocks. 
  3. The final “fit” content is generated in `result.markdown.fit_markdown`.


## 7. Custom Filters
If you need a different approach (like a specialized ML model or site-specific heuristics), you can create a new class inheriting from `RelevantContentFilter` and implement `filter_content(html)`. Then inject it into your **markdown generator** :
```
from crawl4ai.content_filter_strategy import RelevantContentFilter
class MyCustomFilter(RelevantContentFilter):
  def filter_content(self, html, min_word_threshold=None):
    # parse HTML, implement custom logic
    return [block for block in ... if ... some condition...]

```

**Steps** :
  1. Subclass `RelevantContentFilter`. 
  2. Implement `filter_content(...)`. 
  3. Use it in your `DefaultMarkdownGenerator(content_filter=MyCustomFilter(...))`.


## 8. Final Thoughts
**Fit Markdown** is a crucial feature for:
  * **Summaries** : Quickly get the important text from a cluttered page. 
  * **Search** : Combine with **BM25** to produce content relevant to a query. 
  * **AI Pipelines** : Filter out boilerplate so LLM-based extraction or summarization runs on denser text.


**Key Points** : - **PruningContentFilter** : Great if you just want the “meatiest” text without a user query. - **BM25ContentFilter** : Perfect for query-based extraction or searching. - Combine with **`excluded_tags`,`exclude_external_links` , `word_count_threshold`** to refine your final “fit” text. - Fit markdown ends up in **`result.markdown.fit_markdown`**; eventually**`result.markdown.fit_markdown`**in future versions.
With these tools, you can **zero in** on the text that truly matters, ignoring spammy or boilerplate content, and produce a concise, relevant “fit markdown” for your AI or data pipelines. Happy pruning and searching!
  * Last Updated: 2025-01-01


Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/installation)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * Installation
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Installation & Setup (2023 Edition)](https://docs.crawl4ai.com/core/installation#installation-setup-2023-edition)
  * [1. Basic Installation](https://docs.crawl4ai.com/core/installation#1-basic-installation)
  * [2. Initial Setup & Diagnostics](https://docs.crawl4ai.com/core/installation#2-initial-setup-diagnostics)
  * [3. Verifying Installation: A Simple Crawl (Skip this step if you already run crawl4ai-doctor)](https://docs.crawl4ai.com/core/installation#3-verifying-installation-a-simple-crawl-skip-this-step-if-you-already-run-crawl4ai-doctor)
  * [4. Advanced Installation (Optional)](https://docs.crawl4ai.com/core/installation#4-advanced-installation-optional)
  * [5. Docker (Experimental)](https://docs.crawl4ai.com/core/installation#5-docker-experimental)
  * [6. Local Server Mode (Legacy)](https://docs.crawl4ai.com/core/installation#6-local-server-mode-legacy)
  * [Summary](https://docs.crawl4ai.com/core/installation#summary)


# Installation & Setup (2023 Edition)
## 1. Basic Installation
```
pip install crawl4ai

```

This installs the **core** Crawl4AI library along with essential dependencies. **No** advanced features (like transformers or PyTorch) are included yet.
## 2. Initial Setup & Diagnostics
### 2.1 Run the Setup Command
After installing, call:
```
crawl4ai-setup

```

**What does it do?** - Installs or updates required Playwright browsers (Chromium, Firefox, etc.) - Performs OS-level checks (e.g., missing libs on Linux) - Confirms your environment is ready to crawl
### 2.2 Diagnostics
Optionally, you can run **diagnostics** to confirm everything is functioning:
```
crawl4ai-doctor

```

This command attempts to: - Check Python version compatibility - Verify Playwright installation - Inspect environment variables or library conflicts
If any issues arise, follow its suggestions (e.g., installing additional system packages) and re-run `crawl4ai-setup`.
## 3. Verifying Installation: A Simple Crawl (Skip this step if you already run `crawl4ai-doctor`)
Below is a minimal Python script demonstrating a **basic** crawl. It uses our new **`BrowserConfig`**and**`CrawlerRunConfig`**for clarity, though no custom settings are passed in this example:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
async def main():
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://www.example.com",
    )
    print(result.markdown[:300]) # Show the first 300 characters of extracted text
if __name__ == "__main__":
  asyncio.run(main())

```

**Expected** outcome: - A headless browser session loads `example.com` - Crawl4AI returns ~300 characters of markdown. If errors occur, rerun `crawl4ai-doctor` or manually ensure Playwright is installed correctly.
## 4. Advanced Installation (Optional)
**Warning** : Only install these **if you truly need them**. They bring in larger dependencies, including big models, which can increase disk usage and memory load significantly.
### 4.1 Torch, Transformers, or All
  * **Text Clustering (Torch)**
```
pip install crawl4ai[torch]
crawl4ai-setup

```

Installs PyTorch-based features (e.g., cosine similarity or advanced semantic chunking). 
  * **Transformers**
```
pip install crawl4ai[transformer]
crawl4ai-setup

```

Adds Hugging Face-based summarization or generation strategies. 
  * **All Features**
```
pip install crawl4ai[all]
crawl4ai-setup

```



#### (Optional) Pre-Fetching Models
```
crawl4ai-download-models

```

This step caches large models locally (if needed). **Only do this** if your workflow requires them. 
## 5. Docker (Experimental)
We provide a **temporary** Docker approach for testing. **It’s not stable and may break** with future releases. We plan a major Docker revamp in a future stable version, 2025 Q1. If you still want to try:
```
docker pull unclecode/crawl4ai:basic
docker run -p 11235:11235 unclecode/crawl4ai:basic

```

You can then make POST requests to `http://localhost:11235/crawl` to perform crawls. **Production usage** is discouraged until our new Docker approach is ready (planned in Jan or Feb 2025).
## 6. Local Server Mode (Legacy)
Some older docs mention running Crawl4AI as a local server. This approach has been **partially replaced** by the new Docker-based prototype and upcoming stable server release. You can experiment, but expect major changes. Official local server instructions will arrive once the new Docker architecture is finalized.
## Summary
1. **Install** with `pip install crawl4ai` and run `crawl4ai-setup`. 2. **Diagnose** with `crawl4ai-doctor` if you see errors. 3. **Verify** by crawling `example.com` with minimal `BrowserConfig` + `CrawlerRunConfig`. 4. **Advanced** features (Torch, Transformers) are **optional** —avoid them if you don’t need them (they significantly increase resource usage). 5. **Docker** is **experimental** —use at your own risk until the stable version is released. 6. **Local server** references in older docs are largely deprecated; a new solution is in progress.
**Got questions?** Check [GitHub issues](https://github.com/unclecode/crawl4ai/issues) for updates or ask the community!
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/crawler-result)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * Crawler Result
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Crawl Result and Output](https://docs.crawl4ai.com/core/crawler-result#crawl-result-and-output)
  * [1. The CrawlResult Model](https://docs.crawl4ai.com/core/crawler-result#1-the-crawlresult-model)
  * [2. HTML Variants](https://docs.crawl4ai.com/core/crawler-result#2-html-variants)
  * [3. Markdown Generation](https://docs.crawl4ai.com/core/crawler-result#3-markdown-generation)
  * [4. Structured Extraction: extracted_content](https://docs.crawl4ai.com/core/crawler-result#4-structured-extraction-extracted_content)
  * [5. More Fields: Links, Media, and More](https://docs.crawl4ai.com/core/crawler-result#5-more-fields-links-media-and-more)
  * [6. Accessing These Fields](https://docs.crawl4ai.com/core/crawler-result#6-accessing-these-fields)
  * [7. Next Steps](https://docs.crawl4ai.com/core/crawler-result#7-next-steps)


# Crawl Result and Output
When you call `arun()` on a page, Crawl4AI returns a **`CrawlResult`**object containing everything you might need—raw HTML, a cleaned version, optional screenshots or PDFs, structured extraction results, and more. This document explains those fields and how they map to different output types.
## 1. The `CrawlResult` Model
Below is the core schema. Each field captures a different aspect of the crawl’s result:
```
class MarkdownGenerationResult(BaseModel):
  raw_markdown: str
  markdown_with_citations: str
  references_markdown: str
  fit_markdown: Optional[str] = None
  fit_html: Optional[str] = None
class CrawlResult(BaseModel):
  url: str
  html: str
  success: bool
  cleaned_html: Optional[str] = None
  media: Dict[str, List[Dict]] = {}
  links: Dict[str, List[Dict]] = {}
  downloaded_files: Optional[List[str]] = None
  screenshot: Optional[str] = None
  pdf : Optional[bytes] = None
  markdown: Optional[Union[str, MarkdownGenerationResult]] = None
  extracted_content: Optional[str] = None
  metadata: Optional[dict] = None
  error_message: Optional[str] = None
  session_id: Optional[str] = None
  response_headers: Optional[dict] = None
  status_code: Optional[int] = None
  ssl_certificate: Optional[SSLCertificate] = None
  class Config:
    arbitrary_types_allowed = True

```

### Table: Key Fields in `CrawlResult`
Field (Name & Type) | Description  
---|---  
**url (`str`)** | The final or actual URL crawled (in case of redirects).  
**html (`str`)** | Original, unmodified page HTML. Good for debugging or custom processing.  
**success (`bool`)** | `True` if the crawl completed without major errors, else `False`.  
**cleaned_html (`Optional[str]`)** | Sanitized HTML with scripts/styles removed; can exclude tags if configured via `excluded_tags` etc.  
**media (`Dict[str, List[Dict]]`)** | Extracted media info (images, audio, etc.), each with attributes like `src`, `alt`, `score`, etc.  
**links (`Dict[str, List[Dict]]`)** | Extracted link data, split by `internal` and `external`. Each link usually has `href`, `text`, etc.  
**downloaded_files (`Optional[List[str]]`)** | If `accept_downloads=True` in `BrowserConfig`, this lists the filepaths of saved downloads.  
**screenshot (`Optional[str]`)** | Screenshot of the page (base64-encoded) if `screenshot=True`.  
**pdf (`Optional[bytes]`)** | PDF of the page if `pdf=True`.  
**markdown (`Optional[str or MarkdownGenerationResult]`)** | It holds a `MarkdownGenerationResult`. Over time, this will be consolidated into `markdown`. The generator can provide raw markdown, citations, references, and optionally `fit_markdown`.  
**extracted_content (`Optional[str]`)** | The output of a structured extraction (CSS/LLM-based) stored as JSON string or other text.  
**metadata (`Optional[dict]`)** | Additional info about the crawl or extracted data.  
**error_message (`Optional[str]`)** | If `success=False`, contains a short description of what went wrong.  
**session_id (`Optional[str]`)** | The ID of the session used for multi-page or persistent crawling.  
**response_headers (`Optional[dict]`)** | HTTP response headers, if captured.  
**status_code (`Optional[int]`)** | HTTP status code (e.g., 200 for OK).  
**ssl_certificate (`Optional[SSLCertificate]`)** | SSL certificate info if `fetch_ssl_certificate=True`.  
## 2. HTML Variants
### `html`: Raw HTML
Crawl4AI preserves the exact HTML as `result.html`. Useful for:
  * Debugging page issues or checking the original content.
  * Performing your own specialized parse if needed.


### `cleaned_html`: Sanitized
If you specify any cleanup or exclusion parameters in `CrawlerRunConfig` (like `excluded_tags`, `remove_forms`, etc.), you’ll see the result here:
```
config = CrawlerRunConfig(
  excluded_tags=["form", "header", "footer"],
  keep_data_attributes=False
)
result = await crawler.arun("https://example.com", config=config)
print(result.cleaned_html) # Freed of forms, header, footer, data-* attributes

```

## 3. Markdown Generation
### 3.1 `markdown`
  * **`markdown`**: The current location for detailed markdown output, returning a**`MarkdownGenerationResult`**object.
  * **`markdown_v2`**: Deprecated since v0.5.


**`MarkdownGenerationResult`**Fields:
Field | Description  
---|---  
**raw_markdown** | The basic HTML→Markdown conversion.  
**markdown_with_citations** | Markdown including inline citations that reference links at the end.  
**references_markdown** | The references/citations themselves (if `citations=True`).  
**fit_markdown** | The filtered/“fit” markdown if a content filter was used.  
**fit_html** | The filtered HTML that generated `fit_markdown`.  
### 3.2 Basic Example with a Markdown Generator
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
config = CrawlerRunConfig(
  markdown_generator=DefaultMarkdownGenerator(
    options={"citations": True, "body_width": 80} # e.g. pass html2text style options
  )
)
result = await crawler.arun(url="https://example.com", config=config)
md_res = result.markdown # or eventually 'result.markdown'
print(md_res.raw_markdown[:500])
print(md_res.markdown_with_citations)
print(md_res.references_markdown)

```

**Note** : If you use a filter like `PruningContentFilter`, you’ll get `fit_markdown` and `fit_html` as well.
## 4. Structured Extraction: `extracted_content`
If you run a JSON-based extraction strategy (CSS, XPath, LLM, etc.), the structured data is **not** stored in `markdown`—it’s placed in **`result.extracted_content`**as a JSON string (or sometimes plain text).
### Example: CSS Extraction with `raw://` HTML
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  schema = {
    "name": "Example Items",
    "baseSelector": "div.item",
    "fields": [
      {"name": "title", "selector": "h2", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
  raw_html = "<div class='item'><h2>Item 1</h2><a href='https://example.com/item1'>Link 1</a></div>"
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="raw://" + raw_html,
      config=CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=JsonCssExtractionStrategy(schema)
      )
    )
    data = json.loads(result.extracted_content)
    print(data)
if __name__ == "__main__":
  asyncio.run(main())

```

Here: - `url="raw://..."` passes the HTML content directly, no network requests. - The **CSS** extraction strategy populates `result.extracted_content` with the JSON array `[{"title": "...", "link": "..."}]`.
## 5. More Fields: Links, Media, and More
### 5.1 `links`
A dictionary, typically with `"internal"` and `"external"` lists. Each entry might have `href`, `text`, `title`, etc. This is automatically captured if you haven’t disabled link extraction.
```
print(result.links["internal"][:3]) # Show first 3 internal links

```

### 5.2 `media`
Similarly, a dictionary with `"images"`, `"audio"`, `"video"`, etc. Each item could include `src`, `alt`, `score`, and more, if your crawler is set to gather them.
```
images = result.media.get("images", [])
for img in images:
  print("Image URL:", img["src"], "Alt:", img.get("alt"))

```

### 5.3 `screenshot` and `pdf`
If you set `screenshot=True` or `pdf=True` in **`CrawlerRunConfig`**, then:
  * `result.screenshot` contains a base64-encoded PNG string. 
  * `result.pdf` contains raw PDF bytes (you can write them to a file).


```
with open("page.pdf", "wb") as f:
  f.write(result.pdf)

```

### 5.4 `ssl_certificate`
If `fetch_ssl_certificate=True`, `result.ssl_certificate` holds details about the site’s SSL cert, such as issuer, validity dates, etc.
## 6. Accessing These Fields
After you run:
```
result = await crawler.arun(url="https://example.com", config=some_config)

```

Check any field:
```
if result.success:
  print(result.status_code, result.response_headers)
  print("Links found:", len(result.links.get("internal", [])))
  if result.markdown:
    print("Markdown snippet:", result.markdown.raw_markdown[:200])
  if result.extracted_content:
    print("Structured JSON:", result.extracted_content)
else:
  print("Error:", result.error_message)

```

**Deprecation** : Since v0.5 `result.markdown_v2`, `result.fit_html`,`result.fit_markdown` are deprecated. Use `result.markdown` instead! It holds `MarkdownGenerationResult`, which includes `fit_html` and `fit_markdown` as it's properties.
## 7. Next Steps
  * **Markdown Generation** : Dive deeper into how to configure `DefaultMarkdownGenerator` and various filters. 
  * **Content Filtering** : Learn how to use `BM25ContentFilter` and `PruningContentFilter`.
  * **Session & Hooks**: If you want to manipulate the page or preserve state across multiple `arun()` calls, see the hooking or session docs. 
  * **LLM Extraction** : For complex or unstructured content requiring AI-driven parsing, check the LLM-based strategies doc.


**Enjoy** exploring all that `CrawlResult` offers—whether you need raw HTML, sanitized output, markdown, or fully structured data, Crawl4AI has you covered!
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/link-media)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * Link & Media
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Link & Media](https://docs.crawl4ai.com/core/link-media#link-media)
  * [1. Link Extraction](https://docs.crawl4ai.com/core/link-media#1-link-extraction)
  * [2. Domain Filtering](https://docs.crawl4ai.com/core/link-media#2-domain-filtering)
  * [3. Media Extraction](https://docs.crawl4ai.com/core/link-media#3-media-extraction)
  * [4. Putting It All Together: Link & Media Filtering](https://docs.crawl4ai.com/core/link-media#4-putting-it-all-together-link-media-filtering)
  * [5. Common Pitfalls & Tips](https://docs.crawl4ai.com/core/link-media#5-common-pitfalls-tips)


# Link & Media
In this tutorial, you’ll learn how to:
  1. Extract links (internal, external) from crawled pages 
  2. Filter or exclude specific domains (e.g., social media or custom domains) 
  3. Access and manage media data (especially images) in the crawl result 
  4. Configure your crawler to exclude or prioritize certain images


> **Prerequisites** - You have completed or are familiar with the [AsyncWebCrawler Basics](https://docs.crawl4ai.com/simple-crawling/) tutorial. - You can run Crawl4AI in your environment (Playwright, Python, etc.).
Below is a revised version of the **Link Extraction** and **Media Extraction** sections that includes example data structures showing how links and media items are stored in `CrawlResult`. Feel free to adjust any field names or descriptions to match your actual output.
## 1. Link Extraction
### 1.1 `result.links`
When you call `arun()` or `arun_many()` on a URL, Crawl4AI automatically extracts links and stores them in the `links` field of `CrawlResult`. By default, the crawler tries to distinguish **internal** links (same domain) from **external** links (different domains).
**Basic Example** :
```
from crawl4ai import AsyncWebCrawler
async with AsyncWebCrawler() as crawler:
  result = await crawler.arun("https://www.example.com")
  if result.success:
    internal_links = result.links.get("internal", [])
    external_links = result.links.get("external", [])
    print(f"Found {len(internal_links)} internal links.")
    print(f"Found {len(internal_links)} external links.")
    print(f"Found {len(result.media)} media items.")
    # Each link is typically a dictionary with fields like:
    # { "href": "...", "text": "...", "title": "...", "base_domain": "..." }
    if internal_links:
      print("Sample Internal Link:", internal_links[0])
  else:
    print("Crawl failed:", result.error_message)

```

**Structure Example** :
```
result.links = {
 "internal": [
  {
   "href": "https://kidocode.com/",
   "text": "",
   "title": "",
   "base_domain": "kidocode.com"
  },
  {
   "href": "https://kidocode.com/degrees/technology",
   "text": "Technology Degree",
   "title": "KidoCode Tech Program",
   "base_domain": "kidocode.com"
  },
  # ...
 ],
 "external": [
  # possibly other links leading to third-party sites
 ]
}

```

  * **`href`**: The raw hyperlink URL.
  * **`text`**: The link text (if any) within the`<a>` tag. 
  * **`title`**: The`title` attribute of the link (if present). 
  * **`base_domain`**: The domain extracted from`href`. Helpful for filtering or grouping by domain.


## 2. Domain Filtering
Some websites contain hundreds of third-party or affiliate links. You can filter out certain domains at **crawl time** by configuring the crawler. The most relevant parameters in `CrawlerRunConfig` are:
  * **`exclude_external_links`**: If`True` , discard any link pointing outside the root domain. 
  * **`exclude_social_media_domains`**: Provide a list of social media platforms (e.g.,`["facebook.com", "twitter.com"]`) to exclude from your crawl. 
  * **`exclude_social_media_links`**: If`True` , automatically skip known social platforms. 
  * **`exclude_domains`**: Provide a list of custom domains you want to exclude (e.g.,`["spammyads.com", "tracker.net"]`).


### 2.1 Example: Excluding External & Social Media Links
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
async def main():
  crawler_cfg = CrawlerRunConfig(
    exclude_external_links=True,     # No links outside primary domain
    exclude_social_media_links=True    # Skip recognized social media domains
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      "https://www.example.com",
      config=crawler_cfg
    )
    if result.success:
      print("[OK] Crawled:", result.url)
      print("Internal links count:", len(result.links.get("internal", [])))
      print("External links count:", len(result.links.get("external", []))) 
      # Likely zero external links in this scenario
    else:
      print("[ERROR]", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

### 2.2 Example: Excluding Specific Domains
If you want to let external links in, but specifically exclude a domain (e.g., `suspiciousads.com`), do this:
```
crawler_cfg = CrawlerRunConfig(
  exclude_domains=["suspiciousads.com"]
)

```

This approach is handy when you still want external links but need to block certain sites you consider spammy.
## 3. Media Extraction
### 3.1 Accessing `result.media`
By default, Crawl4AI collects images, audio, video URLs, and data tables it finds on the page. These are stored in `result.media`, a dictionary keyed by media type (e.g., `images`, `videos`, `audio`, `tables`).
**Basic Example** :
```
if result.success:
  # Get images
  images_info = result.media.get("images", [])
  print(f"Found {len(images_info)} images in total.")
  for i, img in enumerate(images_info[:3]): # Inspect just the first 3
    print(f"[Image {i}] URL: {img['src']}")
    print(f"      Alt text: {img.get('alt', '')}")
    print(f"      Score: {img.get('score')}")
    print(f"      Description: {img.get('desc', '')}\n")
  # Get tables
  tables = result.media.get("tables", [])
  print(f"Found {len(tables)} data tables in total.")
  for i, table in enumerate(tables):
    print(f"[Table {i}] Caption: {table.get('caption', 'No caption')}")
    print(f"      Columns: {len(table.get('headers', []))}")
    print(f"      Rows: {len(table.get('rows', []))}")

```

**Structure Example** :
```
result.media = {
 "images": [
  {
   "src": "https://cdn.prod.website-files.com/.../Group%2089.svg",
   "alt": "coding school for kids",
   "desc": "Trial Class Degrees degrees All Degrees AI Degree Technology ...",
   "score": 3,
   "type": "image",
   "group_id": 0,
   "format": None,
   "width": None,
   "height": None
  },
  # ...
 ],
 "videos": [
  # Similar structure but with video-specific fields
 ],
 "audio": [
  # Similar structure but with audio-specific fields
 ],
 "tables": [
  {
   "headers": ["Name", "Age", "Location"],
   "rows": [
    ["John Doe", "34", "New York"],
    ["Jane Smith", "28", "San Francisco"],
    ["Alex Johnson", "42", "Chicago"]
   ],
   "caption": "Employee Directory",
   "summary": "Directory of company employees"
  },
  # More tables if present
 ]
}

```

Depending on your Crawl4AI version or scraping strategy, these dictionaries can include fields like:
  * **`src`**: The media URL (e.g., image source)
  * **`alt`**: The alt text for images (if present)
  * **`desc`**: A snippet of nearby text or a short description (optional)
  * **`score`**: A heuristic relevance score if you’re using content-scoring features
  * **`width`**,**`height`**: If the crawler detects dimensions for the image/video
  * **`type`**: Usually`"image"` , `"video"`, or `"audio"`
  * **`group_id`**: If you’re grouping related media items, the crawler might assign an ID


With these details, you can easily filter out or focus on certain images (for instance, ignoring images with very low scores or a different domain), or gather metadata for analytics.
### 3.2 Excluding External Images
If you’re dealing with heavy pages or want to skip third-party images (advertisements, for example), you can turn on:
```
crawler_cfg = CrawlerRunConfig(
  exclude_external_images=True
)

```

This setting attempts to discard images from outside the primary domain, keeping only those from the site you’re crawling.
### 3.3 Working with Tables
Crawl4AI can detect and extract structured data from HTML tables. Tables are analyzed based on various criteria to determine if they are actual data tables (as opposed to layout tables), including:
  * Presence of thead and tbody sections
  * Use of th elements for headers
  * Column consistency
  * Text density
  * And other factors


Tables that score above the threshold (default: 7) are extracted and stored in `result.media.tables`.
**Accessing Table Data** :
```
if result.success:
  tables = result.media.get("tables", [])
  print(f"Found {len(tables)} data tables on the page")
  if tables:
    # Access the first table
    first_table = tables[0]
    print(f"Table caption: {first_table.get('caption', 'No caption')}")
    print(f"Headers: {first_table.get('headers', [])}")
    # Print the first 3 rows
    for i, row in enumerate(first_table.get('rows', [])[:3]):
      print(f"Row {i+1}: {row}")

```

**Configuring Table Extraction** :
You can adjust the sensitivity of the table detection algorithm with:
```
crawler_cfg = CrawlerRunConfig(
  table_score_threshold=5 # Lower value = more tables detected (default: 7)
)

```

Each extracted table contains: - `headers`: Column header names - `rows`: List of rows, each containing cell values - `caption`: Table caption text (if available) - `summary`: Table summary attribute (if specified)
### 3.4 Additional Media Config
  * **`screenshot`**: Set to`True` if you want a full-page screenshot stored as `base64` in `result.screenshot`. 
  * **`pdf`**: Set to`True` if you want a PDF version of the page in `result.pdf`. 
  * **`wait_for_images`**: If`True` , attempts to wait until images are fully loaded before final extraction.


## 4. Putting It All Together: Link & Media Filtering
Here’s a combined example demonstrating how to filter out external links, skip certain domains, and exclude external images:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
async def main():
  # Suppose we want to keep only internal links, remove certain domains, 
  # and discard external images from the final crawl data.
  crawler_cfg = CrawlerRunConfig(
    exclude_external_links=True,
    exclude_domains=["spammyads.com"],
    exclude_social_media_links=True,  # skip Twitter, Facebook, etc.
    exclude_external_images=True,   # keep only images from main domain
    wait_for_images=True,       # ensure images are loaded
    verbose=True
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://www.example.com", config=crawler_cfg)
    if result.success:
      print("[OK] Crawled:", result.url)
      # 1. Links
      in_links = result.links.get("internal", [])
      ext_links = result.links.get("external", [])
      print("Internal link count:", len(in_links))
      print("External link count:", len(ext_links)) # should be zero with exclude_external_links=True
      # 2. Images
      images = result.media.get("images", [])
      print("Images found:", len(images))
      # Let's see a snippet of these images
      for i, img in enumerate(images[:3]):
        print(f" - {img['src']} (alt={img.get('alt','')}, score={img.get('score','N/A')})")
    else:
      print("[ERROR] Failed to crawl. Reason:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

## 5. Common Pitfalls & Tips
1. **Conflicting Flags** : - `exclude_external_links=True` but then also specifying `exclude_social_media_links=True` is typically fine, but understand that the first setting already discards _all_ external links. The second becomes somewhat redundant. - `exclude_external_images=True` but want to keep some external images? Currently no partial domain-based setting for images, so you might need a custom approach or hook logic.
2. **Relevancy Scores** : - If your version of Crawl4AI or your scraping strategy includes an `img["score"]`, it’s typically a heuristic based on size, position, or content analysis. Evaluate carefully if you rely on it.
3. **Performance** : - Excluding certain domains or external images can speed up your crawl, especially for large, media-heavy pages. - If you want a “full” link map, do _not_ exclude them. Instead, you can post-filter in your own code.
4. **Social Media Lists** : - `exclude_social_media_links=True` typically references an internal list of known social domains like Facebook, Twitter, LinkedIn, etc. If you need to add or remove from that list, look for library settings or a local config file (depending on your version).
**That’s it for Link & Media Analysis!** You’re now equipped to filter out unwanted sites and zero in on the images and videos that matter for your project.
### Table Extraction Tips
  * Not all HTML tables are extracted - only those detected as "data tables" vs. layout tables.
  * Tables with inconsistent cell counts, nested tables, or those used purely for layout may be skipped.
  * If you're missing tables, try adjusting the `table_score_threshold` to a lower value (default is 7).


The table detection algorithm scores tables based on features like consistent columns, presence of headers, text density, and more. Tables scoring above the threshold are considered data tables worth extracting.
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/docker-deployment)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * Docker Deployment
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment#docker-deployment)
  * [Quick Start 🚀](https://docs.crawl4ai.com/core/docker-deployment#quick-start)
  * [Running with Docker Compose 🐳](https://docs.crawl4ai.com/core/docker-deployment#running-with-docker-compose)
  * [API Security 🔒](https://docs.crawl4ai.com/core/docker-deployment#api-security)
  * [Configuration Options 🔧](https://docs.crawl4ai.com/core/docker-deployment#configuration-options)
  * [Usage Examples 📝](https://docs.crawl4ai.com/core/docker-deployment#usage-examples)
  * [Platform-Specific Instructions 💻](https://docs.crawl4ai.com/core/docker-deployment#platform-specific-instructions)
  * [Testing 🧪](https://docs.crawl4ai.com/core/docker-deployment#testing)
  * [Advanced Configuration ⚙️](https://docs.crawl4ai.com/core/docker-deployment#advanced-configuration)
  * [Troubleshooting 🔍](https://docs.crawl4ai.com/core/docker-deployment#troubleshooting)
  * [Best Practices 🌟](https://docs.crawl4ai.com/core/docker-deployment#best-practices)
  * [API Reference 📚](https://docs.crawl4ai.com/core/docker-deployment#api-reference)


# Docker Deployment
Crawl4AI provides official Docker images for easy deployment and scalability. This guide covers installation, configuration, and usage of Crawl4AI in Docker environments.
## Quick Start 🚀
Pull and run the basic version:
```
# Basic run without security
docker pull unclecode/crawl4ai:basic
docker run -p 11235:11235 unclecode/crawl4ai:basic
# Run with API security enabled
docker run -p 11235:11235 -e CRAWL4AI_API_TOKEN=your_secret_token unclecode/crawl4ai:basic

```

## Running with Docker Compose 🐳
### Use Docker Compose (From Local Dockerfile or Docker Hub)
Crawl4AI provides flexibility to use Docker Compose for managing your containerized services. You can either build the image locally from the provided `Dockerfile` or use the pre-built image from Docker Hub.
### **Option 1: Using Docker Compose to Build Locally**
If you want to build the image locally, use the provided `docker-compose.local.yml` file.
```
docker-compose -f docker-compose.local.yml up -d

```

This will: 1. Build the Docker image from the provided `Dockerfile`. 2. Start the container and expose it on `http://localhost:11235`.
### **Option 2: Using Docker Compose with Pre-Built Image from Hub**
If you prefer using the pre-built image on Docker Hub, use the `docker-compose.hub.yml` file.
```
docker-compose -f docker-compose.hub.yml up -d

```

This will: 1. Pull the pre-built image `unclecode/crawl4ai:basic` (or `all`, depending on your configuration). 2. Start the container and expose it on `http://localhost:11235`.
### **Stopping the Running Services**
To stop the services started via Docker Compose, you can use:
```
docker-compose -f docker-compose.local.yml down
# OR
docker-compose -f docker-compose.hub.yml down

```

If the containers don’t stop and the application is still running, check the running containers:
```
docker ps

```

Find the `CONTAINER ID` of the running service and stop it forcefully:
```
docker stop <CONTAINER_ID>

```

### **Debugging with Docker Compose**
  * **Check Logs** : To view the container logs: 
```
docker-compose -f docker-compose.local.yml logs -f

```

  * **Remove Orphaned Containers** : If the service is still running unexpectedly: 
```
docker-compose -f docker-compose.local.yml down --remove-orphans

```

  * **Manually Remove Network** : If the network is still in use: 
```
docker network ls
docker network rm crawl4ai_default

```



### Why Use Docker Compose?
Docker Compose is the recommended way to deploy Crawl4AI because: 1. It simplifies multi-container setups. 2. Allows you to define environment variables, resources, and ports in a single file. 3. Makes it easier to switch between local development and production-ready images.
For example, your `docker-compose.yml` could include API keys, token settings, and memory limits, making deployment quick and consistent.
## API Security 🔒
### Understanding CRAWL4AI_API_TOKEN
The `CRAWL4AI_API_TOKEN` provides optional security for your Crawl4AI instance:
  * If `CRAWL4AI_API_TOKEN` is set: All API endpoints (except `/health`) require authentication
  * If `CRAWL4AI_API_TOKEN` is not set: The API is publicly accessible


```
# Secured Instance
docker run -p 11235:11235 -e CRAWL4AI_API_TOKEN=your_secret_token unclecode/crawl4ai:all
# Unsecured Instance
docker run -p 11235:11235 unclecode/crawl4ai:all

```

### Making API Calls
For secured instances, include the token in all requests:
```
import requests
# Setup headers if token is being used
api_token = "your_secret_token" # Same token set in CRAWL4AI_API_TOKEN
headers = {"Authorization": f"Bearer {api_token}"} if api_token else {}
# Making authenticated requests
response = requests.post(
  "http://localhost:11235/crawl",
  headers=headers,
  json={
    "urls": "https://example.com",
    "priority": 10
  }
)
# Checking task status
task_id = response.json()["task_id"]
status = requests.get(
  f"http://localhost:11235/task/{task_id}",
  headers=headers
)

```

### Using with Docker Compose
In your `docker-compose.yml`: 
```
services:
 crawl4ai:
  image: unclecode/crawl4ai:all
  environment:
   - CRAWL4AI_API_TOKEN=${CRAWL4AI_API_TOKEN:-} # Optional
  # ... other configuration

```

Then either: 1. Set in `.env` file: 
```
CRAWL4AI_API_TOKEN=your_secret_token

```

  1. Or set via command line: 
```
CRAWL4AI_API_TOKEN=your_secret_token docker-compose up

```



> **Security Note** : If you enable the API token, make sure to keep it secure and never commit it to version control. The token will be required for all API endpoints except the health check endpoint (`/health`).
## Configuration Options 🔧
### Environment Variables
You can configure the service using environment variables:
```
# Basic configuration
docker run -p 11235:11235 \
  -e MAX_CONCURRENT_TASKS=5 \
  unclecode/crawl4ai:all
# With security and LLM support
docker run -p 11235:11235 \
  -e CRAWL4AI_API_TOKEN=your_secret_token \
  -e OPENAI_API_KEY=sk-... \
  -e ANTHROPIC_API_KEY=sk-ant-... \
  unclecode/crawl4ai:all

```

### Using Docker Compose (Recommended) 🐳
Create a `docker-compose.yml`:
```
version: '3.8'
services:
 crawl4ai:
  image: unclecode/crawl4ai:all
  ports:
   - "11235:11235"
  environment:
   - CRAWL4AI_API_TOKEN=${CRAWL4AI_API_TOKEN:-} # Optional API security
   - MAX_CONCURRENT_TASKS=5
   # LLM Provider Keys
   - OPENAI_API_KEY=${OPENAI_API_KEY:-}
   - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY:-}
  volumes:
   - /dev/shm:/dev/shm
  deploy:
   resources:
    limits:
     memory: 4G
    reservations:
     memory: 1G

```

You can run it in two ways:
  1. Using environment variables directly: 
```
CRAWL4AI_API_TOKEN=secret123 OPENAI_API_KEY=sk-... docker-compose up

```

  2. Using a `.env` file (recommended): Create a `.env` file in the same directory: 
```
# API Security (optional)
CRAWL4AI_API_TOKEN=your_secret_token
# LLM Provider Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
# Other Configuration
MAX_CONCURRENT_TASKS=5

```



Then simply run: 
```
docker-compose up

```

### Testing the Deployment 🧪
```
import requests
# For unsecured instances
def test_unsecured():
  # Health check
  health = requests.get("http://localhost:11235/health")
  print("Health check:", health.json())
  # Basic crawl
  response = requests.post(
    "http://localhost:11235/crawl",
    json={
      "urls": "https://www.nbcnews.com/business",
      "priority": 10
    }
  )
  task_id = response.json()["task_id"]
  print("Task ID:", task_id)
# For secured instances
def test_secured(api_token):
  headers = {"Authorization": f"Bearer {api_token}"}
  # Basic crawl with authentication
  response = requests.post(
    "http://localhost:11235/crawl",
    headers=headers,
    json={
      "urls": "https://www.nbcnews.com/business",
      "priority": 10
    }
  )
  task_id = response.json()["task_id"]
  print("Task ID:", task_id)

```

### LLM Extraction Example 🤖
When you've configured your LLM provider keys (via environment variables or `.env`), you can use LLM extraction:
```
request = {
  "urls": "https://example.com",
  "extraction_config": {
    "type": "llm",
    "params": {
      "provider": "openai/gpt-4",
      "instruction": "Extract main topics from the page"
    }
  }
}
# Make the request (add headers if using API security)
response = requests.post("http://localhost:11235/crawl", json=request)

```

> **Note** : Remember to add `.env` to your `.gitignore` to keep your API keys secure!
## Usage Examples 📝
### Basic Crawling
```
request = {
  "urls": "https://www.nbcnews.com/business",
  "priority": 10
}
response = requests.post("http://localhost:11235/crawl", json=request)
task_id = response.json()["task_id"]
# Get results
result = requests.get(f"http://localhost:11235/task/{task_id}")

```

### Structured Data Extraction
```
schema = {
  "name": "Crypto Prices",
  "baseSelector": ".cds-tableRow-t45thuk",
  "fields": [
    {
      "name": "crypto",
      "selector": "td:nth-child(1) h2",
      "type": "text",
    },
    {
      "name": "price",
      "selector": "td:nth-child(2)",
      "type": "text",
    }
  ],
}
request = {
  "urls": "https://www.coinbase.com/explore",
  "extraction_config": {
    "type": "json_css",
    "params": {"schema": schema}
  }
}

```

### Dynamic Content Handling
```
request = {
  "urls": "https://www.nbcnews.com/business",
  "js_code": [
    "const loadMoreButton = Array.from(document.querySelectorAll('button')).find(button => button.textContent.includes('Load More')); loadMoreButton && loadMoreButton.click();"
  ],
  "wait_for": "article.tease-card:nth-child(10)"
}

```

### AI-Powered Extraction (Full Version)
```
request = {
  "urls": "https://www.nbcnews.com/business",
  "extraction_config": {
    "type": "cosine",
    "params": {
      "semantic_filter": "business finance economy",
      "word_count_threshold": 10,
      "max_dist": 0.2,
      "top_k": 3
    }
  }
}

```

## Platform-Specific Instructions 💻
### macOS
```
docker pull unclecode/crawl4ai:basic
docker run -p 11235:11235 unclecode/crawl4ai:basic

```

### Ubuntu
```
# Basic version
docker pull unclecode/crawl4ai:basic
docker run -p 11235:11235 unclecode/crawl4ai:basic
# With GPU support
docker pull unclecode/crawl4ai:gpu
docker run --gpus all -p 11235:11235 unclecode/crawl4ai:gpu

```

### Windows (PowerShell)
```
docker pull unclecode/crawl4ai:basic
docker run -p 11235:11235 unclecode/crawl4ai:basic

```

## Testing 🧪
Save this as `test_docker.py`:
```
import requests
import json
import time
import sys
class Crawl4AiTester:
  def __init__(self, base_url: str = "http://localhost:11235"):
    self.base_url = base_url
  def submit_and_wait(self, request_data: dict, timeout: int = 300) -> dict:
    # Submit crawl job
    response = requests.post(f"{self.base_url}/crawl", json=request_data)
    task_id = response.json()["task_id"]
    print(f"Task ID: {task_id}")
    # Poll for result
    start_time = time.time()
    while True:
      if time.time() - start_time > timeout:
        raise TimeoutError(f"Task {task_id} timeout")
      result = requests.get(f"{self.base_url}/task/{task_id}")
      status = result.json()
      if status["status"] == "completed":
        return status
      time.sleep(2)
def test_deployment():
  tester = Crawl4AiTester()
  # Test basic crawl
  request = {
    "urls": "https://www.nbcnews.com/business",
    "priority": 10
  }
  result = tester.submit_and_wait(request)
  print("Basic crawl successful!")
  print(f"Content length: {len(result['result']['markdown'])}")
if __name__ == "__main__":
  test_deployment()

```

## Advanced Configuration ⚙️
### Crawler Parameters
The `crawler_params` field allows you to configure the browser instance and crawling behavior. Here are key parameters you can use:
```
request = {
  "urls": "https://example.com",
  "crawler_params": {
    # Browser Configuration
    "headless": True,          # Run in headless mode
    "browser_type": "chromium",     # chromium/firefox/webkit
    "user_agent": "custom-agent",    # Custom user agent
    "proxy": "http://proxy:8080",    # Proxy configuration
    # Performance & Behavior
    "page_timeout": 30000,        # Page load timeout (ms)
    "verbose": True,           # Enable detailed logging
    "semaphore_count": 5,        # Concurrent request limit
    # Anti-Detection Features
    "simulate_user": True,        # Simulate human behavior
    "magic": True,            # Advanced anti-detection
    "override_navigator": True,     # Override navigator properties
    # Session Management
    "user_data_dir": "./browser-data",  # Browser profile location
    "use_managed_browser": True,     # Use persistent browser
  }
}

```

### Extra Parameters
The `extra` field allows passing additional parameters directly to the crawler's `arun` function:
```
request = {
  "urls": "https://example.com",
  "extra": {
    "word_count_threshold": 10,     # Min words per block
    "only_text": True,          # Extract only text
    "bypass_cache": True,        # Force fresh crawl
    "process_iframes": True,       # Include iframe content
  }
}

```

### Complete Examples
1. **Advanced News Crawling**
```
request = {
  "urls": "https://www.nbcnews.com/business",
  "crawler_params": {
    "headless": True,
    "page_timeout": 30000,
    "remove_overlay_elements": True   # Remove popups
  },
  "extra": {
    "word_count_threshold": 50,     # Longer content blocks
    "bypass_cache": True         # Fresh content
  },
  "css_selector": ".article-body"
}

```

2. **Anti-Detection Configuration**
```
request = {
  "urls": "https://example.com",
  "crawler_params": {
    "simulate_user": True,
    "magic": True,
    "override_navigator": True,
    "user_agent": "Mozilla/5.0 ...",
    "headers": {
      "Accept-Language": "en-US,en;q=0.9"
    }
  }
}

```

3. **LLM Extraction with Custom Parameters**
```
request = {
  "urls": "https://openai.com/pricing",
  "extraction_config": {
    "type": "llm",
    "params": {
      "provider": "openai/gpt-4",
      "schema": pricing_schema
    }
  },
  "crawler_params": {
    "verbose": True,
    "page_timeout": 60000
  },
  "extra": {
    "word_count_threshold": 1,
    "only_text": True
  }
}

```

4. **Session-Based Dynamic Content**
```
request = {
  "urls": "https://example.com",
  "crawler_params": {
    "session_id": "dynamic_session",
    "headless": False,
    "page_timeout": 60000
  },
  "js_code": ["window.scrollTo(0, document.body.scrollHeight);"],
  "wait_for": "js:() => document.querySelectorAll('.item').length > 10",
  "extra": {
    "delay_before_return_html": 2.0
  }
}

```

5. **Screenshot with Custom Timing**
```
request = {
  "urls": "https://example.com",
  "screenshot": True,
  "crawler_params": {
    "headless": True,
    "screenshot_wait_for": ".main-content"
  },
  "extra": {
    "delay_before_return_html": 3.0
  }
}

```

### Parameter Reference Table
Category | Parameter | Type | Description  
---|---|---|---  
Browser | headless | bool | Run browser in headless mode  
Browser | browser_type | str | Browser engine selection  
Browser | user_agent | str | Custom user agent string  
Network | proxy | str | Proxy server URL  
Network | headers | dict | Custom HTTP headers  
Timing | page_timeout | int | Page load timeout (ms)  
Timing | delay_before_return_html | float | Wait before capture  
Anti-Detection | simulate_user | bool | Human behavior simulation  
Anti-Detection | magic | bool | Advanced protection  
Session | session_id | str | Browser session ID  
Session | user_data_dir | str | Profile directory  
Content | word_count_threshold | int | Minimum words per block  
Content | only_text | bool | Text-only extraction  
Content | process_iframes | bool | Include iframe content  
Debug | verbose | bool | Detailed logging  
Debug | log_console | bool | Browser console logs  
## Troubleshooting 🔍
### Common Issues
1. **Connection Refused**
```
Error: Connection refused at localhost:11235

```

Solution: Ensure the container is running and ports are properly mapped. 
2. **Resource Limits**
```
Error: No available slots

```

Solution: Increase MAX_CONCURRENT_TASKS or container resources. 
3. **GPU Access**
```
Error: GPU not found

```

Solution: Ensure proper NVIDIA drivers and use `--gpus all` flag. 
### Debug Mode
Access container for debugging: 
```
docker run -it --entrypoint /bin/bash unclecode/crawl4ai:all

```

View container logs: 
```
docker logs [container_id]

```

## Best Practices 🌟
1. **Resource Management** - Set appropriate memory and CPU limits - Monitor resource usage via health endpoint - Use basic version for simple crawling tasks
2. **Scaling** - Use multiple containers for high load - Implement proper load balancing - Monitor performance metrics
3. **Security** - Use environment variables for sensitive data - Implement proper network isolation - Regular security updates
## API Reference 📚
### Health Check
```
GET /health

```

### Submit Crawl Task
```
POST /crawl
Content-Type: application/json
{
  "urls": "string or array",
  "extraction_config": {
    "type": "basic|llm|cosine|json_css",
    "params": {}
  },
  "priority": 1-10,
  "ttl": 3600
}

```

### Get Task Status
```
GET /task/{task_id}

```

For more details, visit the [official documentation](https://docs.crawl4ai.com/).
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/extraction/llm-strategies)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/no-llm-strategies/)
    * LLM Strategies
    * [Clustering Strategies](https://docs.crawl4ai.com/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Extracting JSON (LLM)](https://docs.crawl4ai.com/extraction/llm-strategies#extracting-json-llm)
  * [1. Why Use an LLM?](https://docs.crawl4ai.com/extraction/llm-strategies#1-why-use-an-llm)
  * [2. Provider-Agnostic via LightLLM](https://docs.crawl4ai.com/extraction/llm-strategies#2-provider-agnostic-via-lightllm)
  * [3. How LLM Extraction Works](https://docs.crawl4ai.com/extraction/llm-strategies#3-how-llm-extraction-works)
  * [4. Key Parameters](https://docs.crawl4ai.com/extraction/llm-strategies#4-key-parameters)
  * [5. Putting It in CrawlerRunConfig](https://docs.crawl4ai.com/extraction/llm-strategies#5-putting-it-in-crawlerrunconfig)
  * [6. Chunking Details](https://docs.crawl4ai.com/extraction/llm-strategies#6-chunking-details)
  * [7. Input Format](https://docs.crawl4ai.com/extraction/llm-strategies#7-input-format)
  * [8. Token Usage & Show Usage](https://docs.crawl4ai.com/extraction/llm-strategies#8-token-usage-show-usage)
  * [9. Example: Building a Knowledge Graph](https://docs.crawl4ai.com/extraction/llm-strategies#9-example-building-a-knowledge-graph)
  * [10. Best Practices & Caveats](https://docs.crawl4ai.com/extraction/llm-strategies#10-best-practices-caveats)
  * [11. Conclusion](https://docs.crawl4ai.com/extraction/llm-strategies#11-conclusion)


# Extracting JSON (LLM)
In some cases, you need to extract **complex or unstructured** information from a webpage that a simple CSS/XPath schema cannot easily parse. Or you want **AI** -driven insights, classification, or summarization. For these scenarios, Crawl4AI provides an **LLM-based extraction strategy** that:
  1. Works with **any** large language model supported by [LightLLM](https://github.com/LightLLM) (Ollama, OpenAI, Claude, and more). 
  2. Automatically splits content into chunks (if desired) to handle token limits, then combines results. 
  3. Lets you define a **schema** (like a Pydantic model) or a simpler “block” extraction approach.


**Important** : LLM-based extraction can be slower and costlier than schema-based approaches. If your page data is highly structured, consider using [`JsonCssExtractionStrategy`](https://docs.crawl4ai.com/no-llm-strategies/) or [`JsonXPathExtractionStrategy`](https://docs.crawl4ai.com/no-llm-strategies/) first. But if you need AI to interpret or reorganize content, read on!
## 1. Why Use an LLM?
  * **Complex Reasoning** : If the site’s data is unstructured, scattered, or full of natural language context. 
  * **Semantic Extraction** : Summaries, knowledge graphs, or relational data that require comprehension. 
  * **Flexible** : You can pass instructions to the model to do more advanced transformations or classification.


## 2. Provider-Agnostic via LightLLM
Crawl4AI uses a “provider string” (e.g., `"openai/gpt-4o"`, `"ollama/llama2.0"`, `"aws/titan"`) to identify your LLM. **Any** model that LightLLM supports is fair game. You just provide:
  * **`provider`**: The`<provider>/<model_name>` identifier (e.g., `"openai/gpt-4"`, `"ollama/llama2"`, `"huggingface/google-flan"`, etc.). 
  * **`api_token`**: If needed (for OpenAI, HuggingFace, etc.); local models or Ollama might not require it.
  * **`api_base`**(optional): If your provider has a custom endpoint.


This means you **aren’t locked** into a single LLM vendor. Switch or experiment easily.
## 3. How LLM Extraction Works
### 3.1 Flow
1. **Chunking** (optional): The HTML or markdown is split into smaller segments if it’s very long (based on `chunk_token_threshold`, overlap, etc.). 2. **Prompt Construction** : For each chunk, the library forms a prompt that includes your **`instruction`**(and possibly schema or examples). 3.**LLM Inference** : Each chunk is sent to the model in parallel or sequentially (depending on your concurrency). 4. **Combining** : The results from each chunk are merged and parsed into JSON.
### 3.2 `extraction_type`
  * **`"schema"`**: The model tries to return JSON conforming to your Pydantic-based schema.
  * **`"block"`**: The model returns freeform text, or smaller JSON structures, which the library collects.


For structured data, `"schema"` is recommended. You provide `schema=YourPydanticModel.model_json_schema()`.
## 4. Key Parameters
Below is an overview of important LLM extraction parameters. All are typically set inside `LLMExtractionStrategy(...)`. You then put that strategy in your `CrawlerRunConfig(..., extraction_strategy=...)`.
1. **`provider`**(str): e.g.,`"openai/gpt-4"` , `"ollama/llama2"`. 2. **`api_token`**(str): The API key or token for that model. May not be needed for local models. 3.**`schema`**(dict): A JSON schema describing the fields you want. Usually generated by`YourModel.model_json_schema()`. 4. **`extraction_type`**(str):`"schema"` or `"block"`. 5. **`instruction`**(str): Prompt text telling the LLM what you want extracted. E.g., “Extract these fields as a JSON array.” 6.**`chunk_token_threshold`**(int): Maximum tokens per chunk. If your content is huge, you can break it up for the LLM. 7.**`overlap_rate`**(float): Overlap ratio between adjacent chunks. E.g.,`0.1` means 10% of each chunk is repeated to preserve context continuity. 8. **`apply_chunking`**(bool): Set`True` to chunk automatically. If you want a single pass, set `False`. 9. **`input_format`**(str): Determines**which** crawler result is passed to the LLM. Options include: - `"markdown"`: The raw markdown (default). - `"fit_markdown"`: The filtered “fit” markdown if you used a content filter. - `"html"`: The cleaned or raw HTML. 10. **`extra_args`**(dict): Additional LLM parameters like`temperature` , `max_tokens`, `top_p`, etc. 11. **`show_usage()`**: A method you can call to print out usage info (token usage per chunk, total cost if known).
**Example** :
```
extraction_strategy = LLMExtractionStrategy(
  llm_config = LLMConfig(provider="openai/gpt-4", api_token="YOUR_OPENAI_KEY"),
  schema=MyModel.model_json_schema(),
  extraction_type="schema",
  instruction="Extract a list of items from the text with 'name' and 'price' fields.",
  chunk_token_threshold=1200,
  overlap_rate=0.1,
  apply_chunking=True,
  input_format="html",
  extra_args={"temperature": 0.1, "max_tokens": 1000},
  verbose=True
)

```

## 5. Putting It in `CrawlerRunConfig`
**Important** : In Crawl4AI, all strategy definitions should go inside the `CrawlerRunConfig`, not directly as a param in `arun()`. Here’s a full example:
```
import os
import asyncio
import json
from pydantic import BaseModel, Field
from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
class Product(BaseModel):
  name: str
  price: str
async def main():
  # 1. Define the LLM extraction strategy
  llm_strategy = LLMExtractionStrategy(
    llm_config = LLMConfig(provider="openai/gpt-4o-mini", api_token=os.getenv('OPENAI_API_KEY')),
    schema=Product.schema_json(), # Or use model_json_schema()
    extraction_type="schema",
    instruction="Extract all product objects with 'name' and 'price' from the content.",
    chunk_token_threshold=1000,
    overlap_rate=0.0,
    apply_chunking=True,
    input_format="markdown",  # or "html", "fit_markdown"
    extra_args={"temperature": 0.0, "max_tokens": 800}
  )
  # 2. Build the crawler config
  crawl_config = CrawlerRunConfig(
    extraction_strategy=llm_strategy,
    cache_mode=CacheMode.BYPASS
  )
  # 3. Create a browser config if needed
  browser_cfg = BrowserConfig(headless=True)
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    # 4. Let's say we want to crawl a single page
    result = await crawler.arun(
      url="https://example.com/products",
      config=crawl_config
    )
    if result.success:
      # 5. The extracted content is presumably JSON
      data = json.loads(result.extracted_content)
      print("Extracted items:", data)
      # 6. Show usage stats
      llm_strategy.show_usage() # prints token usage
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

## 6. Chunking Details
### 6.1 `chunk_token_threshold`
If your page is large, you might exceed your LLM’s context window. **`chunk_token_threshold`**sets the approximate max tokens per chunk. The library calculates word→token ratio using`word_token_rate` (often ~0.75 by default). If chunking is enabled (`apply_chunking=True`), the text is split into segments.
### 6.2 `overlap_rate`
To keep context continuous across chunks, we can overlap them. E.g., `overlap_rate=0.1` means each subsequent chunk includes 10% of the previous chunk’s text. This is helpful if your needed info might straddle chunk boundaries.
### 6.3 Performance & Parallelism
By chunking, you can potentially process multiple chunks in parallel (depending on your concurrency settings and the LLM provider). This reduces total time if the site is huge or has many sections.
## 7. Input Format
By default, **LLMExtractionStrategy** uses `input_format="markdown"`, meaning the **crawler’s final markdown** is fed to the LLM. You can change to:
  * **`html`**: The cleaned HTML or raw HTML (depending on your crawler config) goes into the LLM.
  * **`fit_markdown`**: If you used, for instance,`PruningContentFilter` , the “fit” version of the markdown is used. This can drastically reduce tokens if you trust the filter. 
  * **`markdown`**: Standard markdown output from the crawler’s`markdown_generator`.


This setting is crucial: if the LLM instructions rely on HTML tags, pick `"html"`. If you prefer a text-based approach, pick `"markdown"`.
```
LLMExtractionStrategy(
  # ...
  input_format="html", # Instead of "markdown" or "fit_markdown"
)

```

## 8. Token Usage & Show Usage
To keep track of tokens and cost, each chunk is processed with an LLM call. We record usage in:
  * **`usages`**(list): token usage per chunk or call.
  * **`total_usage`**: sum of all chunk calls.
  * **`show_usage()`**: prints a usage report (if the provider returns usage data).


```
llm_strategy = LLMExtractionStrategy(...)
# ...
llm_strategy.show_usage()
# e.g. “Total usage: 1241 tokens across 2 chunk calls”

```

If your model provider doesn’t return usage info, these fields might be partial or empty.
## 9. Example: Building a Knowledge Graph
Below is a snippet combining **`LLMExtractionStrategy`**with a Pydantic schema for a knowledge graph. Notice how we pass an**`instruction`**telling the model what to parse.
```
import os
import json
import asyncio
from typing import List
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import LLMExtractionStrategy
class Entity(BaseModel):
  name: str
  description: str
class Relationship(BaseModel):
  entity1: Entity
  entity2: Entity
  description: str
  relation_type: str
class KnowledgeGraph(BaseModel):
  entities: List[Entity]
  relationships: List[Relationship]
async def main():
  # LLM extraction strategy
  llm_strat = LLMExtractionStrategy(
    provider="openai/gpt-4",
    api_token=os.getenv('OPENAI_API_KEY'),
    schema=KnowledgeGraph.schema_json(),
    extraction_type="schema",
    instruction="Extract entities and relationships from the content. Return valid JSON.",
    chunk_token_threshold=1400,
    apply_chunking=True,
    input_format="html",
    extra_args={"temperature": 0.1, "max_tokens": 1500}
  )
  crawl_config = CrawlerRunConfig(
    extraction_strategy=llm_strat,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler(config=BrowserConfig(headless=True)) as crawler:
    # Example page
    url = "https://www.nbcnews.com/business"
    result = await crawler.arun(url=url, config=crawl_config)
    if result.success:
      with open("kb_result.json", "w", encoding="utf-8") as f:
        f.write(result.extracted_content)
      llm_strat.show_usage()
    else:
      print("Crawl failed:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Observations** :
  * **`extraction_type="schema"`**ensures we get JSON fitting our`KnowledgeGraph`. 
  * **`input_format="html"`**means we feed HTML to the model.
  * **`instruction`**guides the model to output a structured knowledge graph.


## 10. Best Practices & Caveats
1. **Cost & Latency**: LLM calls can be slow or expensive. Consider chunking or smaller coverage if you only need partial data. 2. **Model Token Limits** : If your page + instruction exceed the context window, chunking is essential. 3. **Instruction Engineering** : Well-crafted instructions can drastically improve output reliability. 4. **Schema Strictness** : `"schema"` extraction tries to parse the model output as JSON. If the model returns invalid JSON, partial extraction might happen, or you might get an error. 5. **Parallel vs. Serial** : The library can process multiple chunks in parallel, but you must watch out for rate limits on certain providers. 6. **Check Output** : Sometimes, an LLM might omit fields or produce extraneous text. You may want to post-validate with Pydantic or do additional cleanup.
## 11. Conclusion
**LLM-based extraction** in Crawl4AI is **provider-agnostic** , letting you choose from hundreds of models via LightLLM. It’s perfect for **semantically complex** tasks or generating advanced structures like knowledge graphs. However, it’s **slower** and potentially costlier than schema-based approaches. Keep these tips in mind:
  * Put your LLM strategy **in`CrawlerRunConfig`**. 
  * Use **`input_format`**to pick which form (markdown, HTML, fit_markdown) the LLM sees.
  * Tweak **`chunk_token_threshold`**,**`overlap_rate`**, and**`apply_chunking`**to handle large content efficiently.
  * Monitor token usage with `show_usage()`.


If your site’s data is consistent or repetitive, consider [`JsonCssExtractionStrategy`](https://docs.crawl4ai.com/no-llm-strategies/) first for speed and simplicity. But if you need an **AI-driven** approach, `LLMExtractionStrategy` offers a flexible, multi-provider solution for extracting structured JSON from any website.
**Next Steps** :
1. **Experiment with Different Providers** - Try switching the `provider` (e.g., `"ollama/llama2"`, `"openai/gpt-4o"`, etc.) to see differences in speed, accuracy, or cost. - Pass different `extra_args` like `temperature`, `top_p`, and `max_tokens` to fine-tune your results.
2. **Performance Tuning** - If pages are large, tweak `chunk_token_threshold`, `overlap_rate`, or `apply_chunking` to optimize throughput. - Check the usage logs with `show_usage()` to keep an eye on token consumption and identify potential bottlenecks.
3. **Validate Outputs** - If using `extraction_type="schema"`, parse the LLM’s JSON with a Pydantic model for a final validation step. - Log or handle any parse errors gracefully, especially if the model occasionally returns malformed JSON.
4. **Explore Hooks & Automation** - Integrate LLM extraction with [hooks](https://docs.crawl4ai.com/advanced/hooks-auth/) for complex pre/post-processing. - Use a multi-step pipeline: crawl, filter, LLM-extract, then store or index results for further analysis.
**Last Updated** : 2025-01-01
That’s it for **Extracting JSON (LLM)** —now you can harness AI to parse, classify, or reorganize data on the web. Happy crawling!
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/extraction/no-llm-strategies)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * LLM-Free Strategies
    * [LLM Strategies](https://docs.crawl4ai.com/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Extracting JSON (No LLM)](https://docs.crawl4ai.com/extraction/no-llm-strategies#extracting-json-no-llm)
  * [1. Intro to Schema-Based Extraction](https://docs.crawl4ai.com/extraction/no-llm-strategies#1-intro-to-schema-based-extraction)
  * [2. Simple Example: Crypto Prices](https://docs.crawl4ai.com/extraction/no-llm-strategies#2-simple-example-crypto-prices)
  * [3. Advanced Schema & Nested Structures](https://docs.crawl4ai.com/extraction/no-llm-strategies#3-advanced-schema-nested-structures)
  * [4. Why “No LLM” Is Often Better](https://docs.crawl4ai.com/extraction/no-llm-strategies#4-why-no-llm-is-often-better)
  * [5. Base Element Attributes & Additional Fields](https://docs.crawl4ai.com/extraction/no-llm-strategies#5-base-element-attributes-additional-fields)
  * [6. Putting It All Together: Larger Example](https://docs.crawl4ai.com/extraction/no-llm-strategies#6-putting-it-all-together-larger-example)
  * [7. Tips & Best Practices](https://docs.crawl4ai.com/extraction/no-llm-strategies#7-tips-best-practices)
  * [8. Schema Generation Utility](https://docs.crawl4ai.com/extraction/no-llm-strategies#8-schema-generation-utility)
  * [9. Conclusion](https://docs.crawl4ai.com/extraction/no-llm-strategies#9-conclusion)


# Extracting JSON (No LLM)
One of Crawl4AI’s **most powerful** features is extracting **structured JSON** from websites **without** relying on large language models. By defining a **schema** with CSS or XPath selectors, you can extract data instantly—even from complex or nested HTML structures—without the cost, latency, or environmental impact of an LLM.
**Why avoid LLM for basic extractions?**
1. **Faster & Cheaper**: No API calls or GPU overhead. 2. **Lower Carbon Footprint** : LLM inference can be energy-intensive. A well-defined schema is practically carbon-free. 3. **Precise & Repeatable**: CSS/XPath selectors do exactly what you specify. LLM outputs can vary or hallucinate. 4. **Scales Readily** : For thousands of pages, schema-based extraction runs quickly and in parallel.
Below, we’ll explore how to craft these schemas and use them with **JsonCssExtractionStrategy** (or **JsonXPathExtractionStrategy** if you prefer XPath). We’ll also highlight advanced features like **nested fields** and **base element attributes**.
## 1. Intro to Schema-Based Extraction
A schema defines:
  1. A **base selector** that identifies each “container” element on the page (e.g., a product row, a blog post card). 2. **Fields** describing which CSS/XPath selectors to use for each piece of data you want to capture (text, attribute, HTML block, etc.). 3. **Nested** or **list** types for repeated or hierarchical structures. 


For example, if you have a list of products, each one might have a name, price, reviews, and “related products.” This approach is faster and more reliable than an LLM for consistent, structured pages.
## 2. Simple Example: Crypto Prices
Let’s begin with a **simple** schema-based extraction using the `JsonCssExtractionStrategy`. Below is a snippet that extracts cryptocurrency prices from a site (similar to the legacy Coinbase example). Notice we **don’t** call any LLM:
```
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def extract_crypto_prices():
  # 1. Define a simple extraction schema
  schema = {
    "name": "Crypto Prices",
    "baseSelector": "div.crypto-row",  # Repeated elements
    "fields": [
      {
        "name": "coin_name",
        "selector": "h2.coin-name",
        "type": "text"
      },
      {
        "name": "price",
        "selector": "span.coin-price",
        "type": "text"
      }
    ]
  }
  # 2. Create the extraction strategy
  extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
  # 3. Set up your crawler config (if needed)
  config = CrawlerRunConfig(
    # e.g., pass js_code or wait_for if the page is dynamic
    # wait_for="css:.crypto-row:nth-child(20)"
    cache_mode = CacheMode.BYPASS,
    extraction_strategy=extraction_strategy,
  )
  async with AsyncWebCrawler(verbose=True) as crawler:
    # 4. Run the crawl and extraction
    result = await crawler.arun(
      url="https://example.com/crypto-prices",
      config=config
    )
    if not result.success:
      print("Crawl failed:", result.error_message)
      return
    # 5. Parse the extracted JSON
    data = json.loads(result.extracted_content)
    print(f"Extracted {len(data)} coin entries")
    print(json.dumps(data[0], indent=2) if data else "No data found")
asyncio.run(extract_crypto_prices())

```

**Highlights** :
  * **`baseSelector`**: Tells us where each “item” (crypto row) is.
  * **`fields`**: Two fields (`coin_name` , `price`) using simple CSS selectors. 
  * Each field defines a **`type`**(e.g.,`text` , `attribute`, `html`, `regex`, etc.).


No LLM is needed, and the performance is **near-instant** for hundreds or thousands of items.
### **XPath Example with`raw://` HTML**
Below is a short example demonstrating **XPath** extraction plus the **`raw://`**scheme. We’ll pass a**dummy HTML** directly (no network request) and define the extraction strategy in `CrawlerRunConfig`.
```
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.extraction_strategy import JsonXPathExtractionStrategy
async def extract_crypto_prices_xpath():
  # 1. Minimal dummy HTML with some repeating rows
  dummy_html = """
  <html>
   <body>
    <div class='crypto-row'>
     <h2 class='coin-name'>Bitcoin</h2>
     <span class='coin-price'>$28,000</span>
    </div>
    <div class='crypto-row'>
     <h2 class='coin-name'>Ethereum</h2>
     <span class='coin-price'>$1,800</span>
    </div>
   </body>
  </html>
  """
  # 2. Define the JSON schema (XPath version)
  schema = {
    "name": "Crypto Prices via XPath",
    "baseSelector": "//div[@class='crypto-row']",
    "fields": [
      {
        "name": "coin_name",
        "selector": ".//h2[@class='coin-name']",
        "type": "text"
      },
      {
        "name": "price",
        "selector": ".//span[@class='coin-price']",
        "type": "text"
      }
    ]
  }
  # 3. Place the strategy in the CrawlerRunConfig
  config = CrawlerRunConfig(
    extraction_strategy=JsonXPathExtractionStrategy(schema, verbose=True)
  )
  # 4. Use raw:// scheme to pass dummy_html directly
  raw_url = f"raw://{dummy_html}"
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
      url=raw_url,
      config=config
    )
    if not result.success:
      print("Crawl failed:", result.error_message)
      return
    data = json.loads(result.extracted_content)
    print(f"Extracted {len(data)} coin rows")
    if data:
      print("First item:", data[0])
asyncio.run(extract_crypto_prices_xpath())

```

**Key Points** :
1. **`JsonXPathExtractionStrategy`**is used instead of`JsonCssExtractionStrategy`. 2. **`baseSelector`**and each field’s`"selector"` use **XPath** instead of CSS. 3. **`raw://`**lets us pass`dummy_html` with no real network request—handy for local testing. 4. Everything (including the extraction strategy) is in **`CrawlerRunConfig`**.
That’s how you keep the config self-contained, illustrate **XPath** usage, and demonstrate the **raw** scheme for direct HTML input—all while avoiding the old approach of passing `extraction_strategy` directly to `arun()`.
## 3. Advanced Schema & Nested Structures
Real sites often have **nested** or repeated data—like categories containing products, which themselves have a list of reviews or features. For that, we can define **nested** or **list** (and even **nested_list**) fields.
### Sample E-Commerce HTML
We have a **sample e-commerce** HTML file on GitHub (example): 
```
https://gist.githubusercontent.com/githubusercontent/2d7b8ba3cd8ab6cf3c8da771ddb36878/raw/1ae2f90c6861ce7dd84cc50d3df9920dee5e1fd2/sample_ecommerce.html

```

This snippet includes categories, products, features, reviews, and related items. Let’s see how to define a schema that fully captures that structure **without LLM**. 
```
schema = {
  "name": "E-commerce Product Catalog",
  "baseSelector": "div.category",
  # (1) We can define optional baseFields if we want to extract attributes 
  # from the category container
  "baseFields": [
    {"name": "data_cat_id", "type": "attribute", "attribute": "data-cat-id"}, 
  ],
  "fields": [
    {
      "name": "category_name",
      "selector": "h2.category-name",
      "type": "text"
    },
    {
      "name": "products",
      "selector": "div.product",
      "type": "nested_list",  # repeated sub-objects
      "fields": [
        {
          "name": "name",
          "selector": "h3.product-name",
          "type": "text"
        },
        {
          "name": "price",
          "selector": "p.product-price",
          "type": "text"
        },
        {
          "name": "details",
          "selector": "div.product-details",
          "type": "nested", # single sub-object
          "fields": [
            {
              "name": "brand",
              "selector": "span.brand",
              "type": "text"
            },
            {
              "name": "model",
              "selector": "span.model",
              "type": "text"
            }
          ]
        },
        {
          "name": "features",
          "selector": "ul.product-features li",
          "type": "list",
          "fields": [
            {"name": "feature", "type": "text"} 
          ]
        },
        {
          "name": "reviews",
          "selector": "div.review",
          "type": "nested_list",
          "fields": [
            {
              "name": "reviewer", 
              "selector": "span.reviewer", 
              "type": "text"
            },
            {
              "name": "rating", 
              "selector": "span.rating", 
              "type": "text"
            },
            {
              "name": "comment", 
              "selector": "p.review-text", 
              "type": "text"
            }
          ]
        },
        {
          "name": "related_products",
          "selector": "ul.related-products li",
          "type": "list",
          "fields": [
            {
              "name": "name", 
              "selector": "span.related-name", 
              "type": "text"
            },
            {
              "name": "price", 
              "selector": "span.related-price", 
              "type": "text"
            }
          ]
        }
      ]
    }
  ]
}

```

Key Takeaways:
  * **Nested vs. List** : 
  * **`type: "nested"`**means a**single** sub-object (like `details`). 
  * **`type: "list"`**means multiple items that are**simple** dictionaries or single text fields. 
  * **`type: "nested_list"`**means repeated**complex** objects (like `products` or `reviews`).
  * **Base Fields** : We can extract **attributes** from the container element via `"baseFields"`. For instance, `"data_cat_id"` might be `data-cat-id="elect123"`. 
  * **Transforms** : We can also define a `transform` if we want to lower/upper case, strip whitespace, or even run a custom function.


### Running the Extraction
```
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
ecommerce_schema = {
  # ... the advanced schema from above ...
}
async def extract_ecommerce_data():
  strategy = JsonCssExtractionStrategy(ecommerce_schema, verbose=True)
  config = CrawlerRunConfig()
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
      url="https://gist.githubusercontent.com/githubusercontent/2d7b8ba3cd8ab6cf3c8da771ddb36878/raw/1ae2f90c6861ce7dd84cc50d3df9920dee5e1fd2/sample_ecommerce.html",
      extraction_strategy=strategy,
      config=config
    )
    if not result.success:
      print("Crawl failed:", result.error_message)
      return
    # Parse the JSON output
    data = json.loads(result.extracted_content)
    print(json.dumps(data, indent=2) if data else "No data found.")
asyncio.run(extract_ecommerce_data())

```

If all goes well, you get a **structured** JSON array with each “category,” containing an array of `products`. Each product includes `details`, `features`, `reviews`, etc. All of that **without** an LLM.
## 4. Why “No LLM” Is Often Better
1. **Zero Hallucination** : Schema-based extraction doesn’t guess text. It either finds it or not. 2. **Guaranteed Structure** : The same schema yields consistent JSON across many pages, so your downstream pipeline can rely on stable keys. 3. **Speed** : LLM-based extraction can be 10–1000x slower for large-scale crawling. 4. **Scalable** : Adding or updating a field is a matter of adjusting the schema, not re-tuning a model.
**When might you consider an LLM?** Possibly if the site is extremely unstructured or you want AI summarization. But always try a schema approach first for repeated or consistent data patterns.
## 5. Base Element Attributes & Additional Fields
It’s easy to **extract attributes** (like `href`, `src`, or `data-xxx`) from your base or nested elements using:
```
{
 "name": "href",
 "type": "attribute",
 "attribute": "href",
 "default": null
}

```

You can define them in **`baseFields`**(extracted from the main container element) or in each field’s sub-lists. This is especially helpful if you need an item’s link or ID stored in the parent`<div>`.
## 6. Putting It All Together: Larger Example
Consider a blog site. We have a schema that extracts the **URL** from each post card (via `baseFields` with an `"attribute": "href"`), plus the title, date, summary, and author:
```
schema = {
 "name": "Blog Posts",
 "baseSelector": "a.blog-post-card",
 "baseFields": [
  {"name": "post_url", "type": "attribute", "attribute": "href"}
 ],
 "fields": [
  {"name": "title", "selector": "h2.post-title", "type": "text", "default": "No Title"},
  {"name": "date", "selector": "time.post-date", "type": "text", "default": ""},
  {"name": "summary", "selector": "p.post-summary", "type": "text", "default": ""},
  {"name": "author", "selector": "span.post-author", "type": "text", "default": ""}
 ]
}

```

Then run with `JsonCssExtractionStrategy(schema)` to get an array of blog post objects, each with `"post_url"`, `"title"`, `"date"`, `"summary"`, `"author"`.
## 7. Tips & Best Practices
1. **Inspect the DOM** in Chrome DevTools or Firefox’s Inspector to find stable selectors. 2. **Start Simple** : Verify you can extract a single field. Then add complexity like nested objects or lists. 3. **Test** your schema on partial HTML or a test page before a big crawl. 4. **Combine with JS Execution** if the site loads content dynamically. You can pass `js_code` or `wait_for` in `CrawlerRunConfig`. 5. **Look at Logs** when `verbose=True`: if your selectors are off or your schema is malformed, it’ll often show warnings. 6. **Use baseFields** if you need attributes from the container element (e.g., `href`, `data-id`), especially for the “parent” item. 7. **Performance** : For large pages, make sure your selectors are as narrow as possible.
## 8. Schema Generation Utility
While manually crafting schemas is powerful and precise, Crawl4AI now offers a convenient utility to **automatically generate** extraction schemas using LLM. This is particularly useful when:
  1. You're dealing with a new website structure and want a quick starting point
  2. You need to extract complex nested data structures
  3. You want to avoid the learning curve of CSS/XPath selector syntax


### Using the Schema Generator
The schema generator is available as a static method on both `JsonCssExtractionStrategy` and `JsonXPathExtractionStrategy`. You can choose between OpenAI's GPT-4 or the open-source Ollama for schema generation:
```
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy, JsonXPathExtractionStrategy
from crawl4ai import LLMConfig
# Sample HTML with product information
html = """
<div class="product-card">
  <h2 class="title">Gaming Laptop</h2>
  <div class="price">$999.99</div>
  <div class="specs">
    <ul>
      <li>16GB RAM</li>
      <li>1TB SSD</li>
    </ul>
  </div>
</div>
"""
# Option 1: Using OpenAI (requires API token)
css_schema = JsonCssExtractionStrategy.generate_schema(
  html,
  schema_type="css", 
  llm_config = LLMConfig(provider="openai/gpt-4o",api_token="your-openai-token")
)
# Option 2: Using Ollama (open source, no token needed)
xpath_schema = JsonXPathExtractionStrategy.generate_schema(
  html,
  schema_type="xpath",
  llm_config = LLMConfig(provider="ollama/llama3.3", api_token=None) # Not needed for Ollama
)
# Use the generated schema for fast, repeated extractions
strategy = JsonCssExtractionStrategy(css_schema)

```

### LLM Provider Options
  1. **OpenAI GPT-4 (`openai/gpt4o`)**
  2. Default provider
  3. Requires an API token
  4. Generally provides more accurate schemas
  5. Set via environment variable: `OPENAI_API_KEY`
  6. **Ollama (`ollama/llama3.3`)**
  7. Open source alternative
  8. No API token required
  9. Self-hosted option
  10. Good for development and testing


### Benefits of Schema Generation
  1. **One-Time Cost** : While schema generation uses LLM, it's a one-time cost. The generated schema can be reused for unlimited extractions without further LLM calls.
  2. **Smart Pattern Recognition** : The LLM analyzes the HTML structure and identifies common patterns, often producing more robust selectors than manual attempts.
  3. **Automatic Nesting** : Complex nested structures are automatically detected and properly represented in the schema.
  4. **Learning Tool** : The generated schemas serve as excellent examples for learning how to write your own schemas.


### Best Practices
  1. **Review Generated Schemas** : While the generator is smart, always review and test the generated schema before using it in production.
  2. **Provide Representative HTML** : The better your sample HTML represents the overall structure, the more accurate the generated schema will be.
  3. **Consider Both CSS and XPath** : Try both schema types and choose the one that works best for your specific case.
  4. **Cache Generated Schemas** : Since generation uses LLM, save successful schemas for reuse.
  5. **API Token Security** : Never hardcode API tokens. Use environment variables or secure configuration management.
  6. **Choose Provider Wisely** : 
  7. Use OpenAI for production-quality schemas
  8. Use Ollama for development, testing, or when you need a self-hosted solution


That's it for **Extracting JSON (No LLM)**! You've seen how schema-based approaches (either CSS or XPath) can handle everything from simple lists to deeply nested product catalogs—instantly, with minimal overhead. Enjoy building robust scrapers that produce consistent, structured JSON for your data pipelines!
## 9. Conclusion
With **JsonCssExtractionStrategy** (or **JsonXPathExtractionStrategy**), you can build powerful, **LLM-free** pipelines that:
  * Scrape any consistent site for structured data. 
  * Support nested objects, repeating lists, or advanced transformations. 
  * Scale to thousands of pages quickly and reliably.


**Next Steps** :
  * Combine your extracted JSON with advanced filtering or summarization in a second pass if needed. 
  * For dynamic pages, combine strategies with `js_code` or infinite scroll hooking to ensure all content is loaded.


**Remember** : For repeated, structured data, you don’t need to pay for or wait on an LLM. A well-crafted schema plus CSS or XPath gets you the data faster, cleaner, and cheaper—**the real power** of Crawl4AI.
**Last Updated** : 2025-01-01
That’s it for **Extracting JSON (No LLM)**! You’ve seen how schema-based approaches (either CSS or XPath) can handle everything from simple lists to deeply nested product catalogs—instantly, with minimal overhead. Enjoy building robust scrapers that produce consistent, structured JSON for your data pipelines!
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/markdown-generation)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * Markdown Generation
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Markdown Generation Basics](https://docs.crawl4ai.com/core/markdown-generation#markdown-generation-basics)
  * [1. Quick Example](https://docs.crawl4ai.com/core/markdown-generation#1-quick-example)
  * [2. How Markdown Generation Works](https://docs.crawl4ai.com/core/markdown-generation#2-how-markdown-generation-works)
  * [3. Configuring the Default Markdown Generator](https://docs.crawl4ai.com/core/markdown-generation#3-configuring-the-default-markdown-generator)
  * [4. Content Filters](https://docs.crawl4ai.com/core/markdown-generation#4-content-filters)
  * [5. Using Fit Markdown](https://docs.crawl4ai.com/core/markdown-generation#5-using-fit-markdown)
  * [6. The MarkdownGenerationResult Object](https://docs.crawl4ai.com/core/markdown-generation#6-the-markdowngenerationresult-object)
  * [7. Combining Filters (BM25 + Pruning) in Two Passes](https://docs.crawl4ai.com/core/markdown-generation#7-combining-filters-bm25-pruning-in-two-passes)
  * [8. Common Pitfalls & Tips](https://docs.crawl4ai.com/core/markdown-generation#8-common-pitfalls-tips)
  * [9. Summary & Next Steps](https://docs.crawl4ai.com/core/markdown-generation#9-summary-next-steps)


# Markdown Generation Basics
One of Crawl4AI’s core features is generating **clean, structured markdown** from web pages. Originally built to solve the problem of extracting only the “actual” content and discarding boilerplate or noise, Crawl4AI’s markdown system remains one of its biggest draws for AI workflows.
In this tutorial, you’ll learn:
  1. How to configure the **Default Markdown Generator**
  2. How **content filters** (BM25 or Pruning) help you refine markdown and discard junk 
  3. The difference between raw markdown (`result.markdown`) and filtered markdown (`fit_markdown`) 


> **Prerequisites** - You’ve completed or read [AsyncWebCrawler Basics](https://docs.crawl4ai.com/simple-crawling/) to understand how to run a simple crawl. - You know how to configure `CrawlerRunConfig`.
## 1. Quick Example
Here’s a minimal code snippet that uses the **DefaultMarkdownGenerator** with no additional filtering:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
async def main():
  config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator()
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com", config=config)
    if result.success:
      print("Raw Markdown Output:\n")
      print(result.markdown) # The unfiltered markdown from the page
    else:
      print("Crawl failed:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**What’s happening?** - `CrawlerRunConfig( markdown_generator = DefaultMarkdownGenerator() )` instructs Crawl4AI to convert the final HTML into markdown at the end of each crawl. - The resulting markdown is accessible via `result.markdown`.
## 2. How Markdown Generation Works
### 2.1 HTML-to-Text Conversion (Forked & Modified)
Under the hood, **DefaultMarkdownGenerator** uses a specialized HTML-to-text approach that:
  * Preserves headings, code blocks, bullet points, etc. 
  * Removes extraneous tags (scripts, styles) that don’t add meaningful content. 
  * Can optionally generate references for links or skip them altogether.


A set of **options** (passed as a dict) allows you to customize precisely how HTML converts to markdown. These map to standard html2text-like configuration plus your own enhancements (e.g., ignoring internal links, preserving certain tags verbatim, or adjusting line widths).
### 2.2 Link Citations & References
By default, the generator can convert `<a href="...">` elements into `[text][1]` citations, then place the actual links at the bottom of the document. This is handy for research workflows that demand references in a structured manner.
### 2.3 Optional Content Filters
Before or after the HTML-to-Markdown step, you can apply a **content filter** (like BM25 or Pruning) to reduce noise and produce a “fit_markdown”—a heavily pruned version focusing on the page’s main text. We’ll cover these filters shortly.
## 3. Configuring the Default Markdown Generator
You can tweak the output by passing an `options` dict to `DefaultMarkdownGenerator`. For example:
```
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  # Example: ignore all links, don't escape HTML, and wrap text at 80 characters
  md_generator = DefaultMarkdownGenerator(
    options={
      "ignore_links": True,
      "escape_html": False,
      "body_width": 80
    }
  )
  config = CrawlerRunConfig(
    markdown_generator=md_generator
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com/docs", config=config)
    if result.success:
      print("Markdown:\n", result.markdown[:500]) # Just a snippet
    else:
      print("Crawl failed:", result.error_message)
if __name__ == "__main__":
  import asyncio
  asyncio.run(main())

```

Some commonly used `options`:
  * **`ignore_links`**(bool): Whether to remove all hyperlinks in the final markdown.
  * **`ignore_images`**(bool): Remove all`![image]()` references. 
  * **`escape_html`**(bool): Turn HTML entities into text (default is often`True`). 
  * **`body_width`**(int): Wrap text at N characters.`0` or `None` means no wrapping. 
  * **`skip_internal_links`**(bool): If`True` , omit `#localAnchors` or internal links referencing the same page. 
  * **`include_sup_sub`**(bool): Attempt to handle`<sup>` / `<sub>` in a more readable way.


## 4. Content Filters
**Content filters** selectively remove or rank sections of text before turning them into Markdown. This is especially helpful if your page has ads, nav bars, or other clutter you don’t want.
### 4.1 BM25ContentFilter
If you have a **search query** , BM25 is a good choice:
```
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import BM25ContentFilter
from crawl4ai import CrawlerRunConfig
bm25_filter = BM25ContentFilter(
  user_query="machine learning",
  bm25_threshold=1.2,
  use_stemming=True
)
md_generator = DefaultMarkdownGenerator(
  content_filter=bm25_filter,
  options={"ignore_links": True}
)
config = CrawlerRunConfig(markdown_generator=md_generator)

```

  * **`user_query`**: The term you want to focus on. BM25 tries to keep only content blocks relevant to that query.
  * **`bm25_threshold`**: Raise it to keep fewer blocks; lower it to keep more.
  * **`use_stemming`**: If`True` , variations of words match (e.g., “learn,” “learning,” “learnt”).


**No query provided?** BM25 tries to glean a context from page metadata, or you can simply treat it as a scorched-earth approach that discards text with low generic score. Realistically, you want to supply a query for best results.
### 4.2 PruningContentFilter
If you **don’t** have a specific query, or if you just want a robust “junk remover,” use `PruningContentFilter`. It analyzes text density, link density, HTML structure, and known patterns (like “nav,” “footer”) to systematically prune extraneous or repetitive sections.
```
from crawl4ai.content_filter_strategy import PruningContentFilter
prune_filter = PruningContentFilter(
  threshold=0.5,
  threshold_type="fixed", # or "dynamic"
  min_word_threshold=50
)

```

  * **`threshold`**: Score boundary. Blocks below this score get removed.
  * **`threshold_type`**:
    * `"fixed"`: Straight comparison (`score >= threshold` keeps the block). 
    * `"dynamic"`: The filter adjusts threshold in a data-driven manner. 
  * **`min_word_threshold`**: Discard blocks under N words as likely too short or unhelpful.


**When to Use PruningContentFilter** - You want a broad cleanup without a user query. - The page has lots of repeated sidebars, footers, or disclaimers that hamper text extraction.
### 4.3 LLMContentFilter
For intelligent content filtering and high-quality markdown generation, you can use the **LLMContentFilter**. This filter leverages LLMs to generate relevant markdown while preserving the original content's meaning and structure:
```
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, LLMConfig
from crawl4ai.content_filter_strategy import LLMContentFilter
async def main():
  # Initialize LLM filter with specific instruction
  filter = LLMContentFilter(
    llm_config = LLMConfig(provider="openai/gpt-4o",api_token="your-api-token"), #or use environment variable
    instruction="""
    Focus on extracting the core educational content.
    Include:
    - Key concepts and explanations
    - Important code examples
    - Essential technical details
    Exclude:
    - Navigation elements
    - Sidebars
    - Footer content
    Format the output as clean markdown with proper code blocks and headers.
    """,
    chunk_token_threshold=4096, # Adjust based on your needs
    verbose=True
  )
  config = CrawlerRunConfig(
    content_filter=filter
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com", config=config)
    print(result.markdown.fit_markdown) # Filtered markdown content

```

**Key Features:** - **Intelligent Filtering** : Uses LLMs to understand and extract relevant content while maintaining context - **Customizable Instructions** : Tailor the filtering process with specific instructions - **Chunk Processing** : Handles large documents by processing them in chunks (controlled by `chunk_token_threshold`) - **Parallel Processing** : For better performance, use smaller `chunk_token_threshold` (e.g., 2048 or 4096) to enable parallel processing of content chunks
**Two Common Use Cases:**
  1. **Exact Content Preservation** : 
```
filter = LLMContentFilter(
  instruction="""
  Extract the main educational content while preserving its original wording and substance completely.
  1. Maintain the exact language and terminology
  2. Keep all technical explanations and examples intact
  3. Preserve the original flow and structure
  4. Remove only clearly irrelevant elements like navigation menus and ads
  """,
  chunk_token_threshold=4096
)

```

  2. **Focused Content Extraction** : 
```
filter = LLMContentFilter(
  instruction="""
  Focus on extracting specific types of content:
  - Technical documentation
  - Code examples
  - API references
  Reformat the content into clear, well-structured markdown
  """,
  chunk_token_threshold=4096
)

```



> **Performance Tip** : Set a smaller `chunk_token_threshold` (e.g., 2048 or 4096) to enable parallel processing of content chunks. The default value is infinity, which processes the entire content as a single chunk.
## 5. Using Fit Markdown
When a content filter is active, the library produces two forms of markdown inside `result.markdown`:
1. **`raw_markdown`**: The full unfiltered markdown. 2.**`fit_markdown`**: A “fit” version where the filter has removed or trimmed noisy segments.
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter
async def main():
  config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator(
      content_filter=PruningContentFilter(threshold=0.6),
      options={"ignore_links": True}
    )
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://news.example.com/tech", config=config)
    if result.success:
      print("Raw markdown:\n", result.markdown)
      # If a filter is used, we also have .fit_markdown:
      md_object = result.markdown # or your equivalent
      print("Filtered markdown:\n", md_object.fit_markdown)
    else:
      print("Crawl failed:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

## 6. The `MarkdownGenerationResult` Object
If your library stores detailed markdown output in an object like `MarkdownGenerationResult`, you’ll see fields such as:
  * **`raw_markdown`**: The direct HTML-to-markdown transformation (no filtering).
  * **`markdown_with_citations`**: A version that moves links to reference-style footnotes.
  * **`references_markdown`**: A separate string or section containing the gathered references.
  * **`fit_markdown`**: The filtered markdown if you used a content filter.
  * **`fit_html`**: The corresponding HTML snippet used to generate`fit_markdown` (helpful for debugging or advanced usage).


**Example** :
```
md_obj = result.markdown # your library’s naming may vary
print("RAW:\n", md_obj.raw_markdown)
print("CITED:\n", md_obj.markdown_with_citations)
print("REFERENCES:\n", md_obj.references_markdown)
print("FIT:\n", md_obj.fit_markdown)

```

**Why Does This Matter?** - You can supply `raw_markdown` to an LLM if you want the entire text. - Or feed `fit_markdown` into a vector database to reduce token usage. - `references_markdown` can help you keep track of link provenance.
Below is a **revised section** under “Combining Filters (BM25 + Pruning)” that demonstrates how you can run **two** passes of content filtering without re-crawling, by taking the HTML (or text) from a first pass and feeding it into the second filter. It uses real code patterns from the snippet you provided for **BM25ContentFilter** , which directly accepts **HTML** strings (and can also handle plain text with minimal adaptation).
## 7. Combining Filters (BM25 + Pruning) in Two Passes
You might want to **prune out** noisy boilerplate first (with `PruningContentFilter`), and then **rank what’s left** against a user query (with `BM25ContentFilter`). You don’t have to crawl the page twice. Instead:
1. **First pass** : Apply `PruningContentFilter` directly to the raw HTML from `result.html` (the crawler’s downloaded HTML). 2. **Second pass** : Take the pruned HTML (or text) from step 1, and feed it into `BM25ContentFilter`, focusing on a user query.
### Two-Pass Example
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter, BM25ContentFilter
from bs4 import BeautifulSoup
async def main():
  # 1. Crawl with minimal or no markdown generator, just get raw HTML
  config = CrawlerRunConfig(
    # If you only want raw HTML, you can skip passing a markdown_generator
    # or provide one but focus on .html in this example
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com/tech-article", config=config)
    if not result.success or not result.html:
      print("Crawl failed or no HTML content.")
      return
    raw_html = result.html
    # 2. First pass: PruningContentFilter on raw HTML
    pruning_filter = PruningContentFilter(threshold=0.5, min_word_threshold=50)
    # filter_content returns a list of "text chunks" or cleaned HTML sections
    pruned_chunks = pruning_filter.filter_content(raw_html)
    # This list is basically pruned content blocks, presumably in HTML or text form
    # For demonstration, let's combine these chunks back into a single HTML-like string
    # or you could do further processing. It's up to your pipeline design.
    pruned_html = "\n".join(pruned_chunks)
    # 3. Second pass: BM25ContentFilter with a user query
    bm25_filter = BM25ContentFilter(
      user_query="machine learning",
      bm25_threshold=1.2,
      language="english"
    )
    # returns a list of text chunks
    bm25_chunks = bm25_filter.filter_content(pruned_html) 
    if not bm25_chunks:
      print("Nothing matched the BM25 query after pruning.")
      return
    # 4. Combine or display final results
    final_text = "\n---\n".join(bm25_chunks)
    print("==== PRUNED OUTPUT (first pass) ====")
    print(pruned_html[:500], "... (truncated)") # preview
    print("\n==== BM25 OUTPUT (second pass) ====")
    print(final_text[:500], "... (truncated)")
if __name__ == "__main__":
  asyncio.run(main())

```

### What’s Happening?
1. **Raw HTML** : We crawl once and store the raw HTML in `result.html`. 2. **PruningContentFilter** : Takes HTML + optional parameters. It extracts blocks of text or partial HTML, removing headings/sections deemed “noise.” It returns a **list of text chunks**. 3. **Combine or Transform** : We join these pruned chunks back into a single HTML-like string. (Alternatively, you could store them in a list for further logic—whatever suits your pipeline.) 4. **BM25ContentFilter** : We feed the pruned string into `BM25ContentFilter` with a user query. This second pass further narrows the content to chunks relevant to “machine learning.”
**No Re-Crawling** : We used `raw_html` from the first pass, so there’s no need to run `arun()` again—**no second network request**.
### Tips & Variations
  * **Plain Text vs. HTML** : If your pruned output is mostly text, BM25 can still handle it; just keep in mind it expects a valid string input. If you supply partial HTML (like `"<p>some text</p>"`), it will parse it as HTML. 
  * **Chaining in a Single Pipeline** : If your code supports it, you can chain multiple filters automatically. Otherwise, manual two-pass filtering (as shown) is straightforward. 
  * **Adjust Thresholds** : If you see too much or too little text in step one, tweak `threshold=0.5` or `min_word_threshold=50`. Similarly, `bm25_threshold=1.2` can be raised/lowered for more or fewer chunks in step two.


### One-Pass Combination?
If your codebase or pipeline design allows applying multiple filters in one pass, you could do so. But often it’s simpler—and more transparent—to run them sequentially, analyzing each step’s result.
**Bottom Line** : By **manually chaining** your filtering logic in two passes, you get powerful incremental control over the final content. First, remove “global” clutter with Pruning, then refine further with BM25-based query relevance—without incurring a second network crawl.
## 8. Common Pitfalls & Tips
1. **No Markdown Output?** - Make sure the crawler actually retrieved HTML. If the site is heavily JS-based, you may need to enable dynamic rendering or wait for elements. - Check if your content filter is too aggressive. Lower thresholds or disable the filter to see if content reappears.
2. **Performance Considerations** - Very large pages with multiple filters can be slower. Consider `cache_mode` to avoid re-downloading. - If your final use case is LLM ingestion, consider summarizing further or chunking big texts.
3. **Take Advantage of`fit_markdown`** - Great for RAG pipelines, semantic search, or any scenario where extraneous boilerplate is unwanted. - Still verify the textual quality—some sites have crucial data in footers or sidebars.
4. **Adjusting`html2text` Options** - If you see lots of raw HTML slipping into the text, turn on `escape_html`. - If code blocks look messy, experiment with `mark_code` or `handle_code_in_pre`.
## 9. Summary & Next Steps
In this **Markdown Generation Basics** tutorial, you learned to:
  * Configure the **DefaultMarkdownGenerator** with HTML-to-text options. 
  * Use **BM25ContentFilter** for query-specific extraction or **PruningContentFilter** for general noise removal. 
  * Distinguish between raw and filtered markdown (`fit_markdown`). 
  * Leverage the `MarkdownGenerationResult` object to handle different forms of output (citations, references, etc.).


Now you can produce high-quality Markdown from any website, focusing on exactly the content you need—an essential step for powering AI models, summarization pipelines, or knowledge-base queries.
**Last Updated** : 2025-01-01
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/)
  * [ Search ](https://docs.crawl4ai.com/core/quickstart)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * Quick Start
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Getting Started with Crawl4AI](https://docs.crawl4ai.com/core/quickstart#getting-started-with-crawl4ai)
  * [1. Introduction](https://docs.crawl4ai.com/core/quickstart#1-introduction)
  * [2. Your First Crawl](https://docs.crawl4ai.com/core/quickstart#2-your-first-crawl)
  * [3. Basic Configuration (Light Introduction)](https://docs.crawl4ai.com/core/quickstart#3-basic-configuration-light-introduction)
  * [4. Generating Markdown Output](https://docs.crawl4ai.com/core/quickstart#4-generating-markdown-output)
  * [5. Simple Data Extraction (CSS-based)](https://docs.crawl4ai.com/core/quickstart#5-simple-data-extraction-css-based)
  * [6. Simple Data Extraction (LLM-based)](https://docs.crawl4ai.com/core/quickstart#6-simple-data-extraction-llm-based)
  * [7. Multi-URL Concurrency (Preview)](https://docs.crawl4ai.com/core/quickstart#7-multi-url-concurrency-preview)
  * [8. Dynamic Content Example](https://docs.crawl4ai.com/core/quickstart#8-dynamic-content-example)
  * [9. Next Steps](https://docs.crawl4ai.com/core/quickstart#9-next-steps)


# Getting Started with Crawl4AI
Welcome to **Crawl4AI** , an open-source LLM-friendly Web Crawler & Scraper. In this tutorial, you’ll:
  1. Run your **first crawl** using minimal configuration. 
  2. Generate **Markdown** output (and learn how it’s influenced by content filters). 
  3. Experiment with a simple **CSS-based extraction** strategy. 
  4. See a glimpse of **LLM-based extraction** (including open-source and closed-source model options). 
  5. Crawl a **dynamic** page that loads content via JavaScript.


## 1. Introduction
Crawl4AI provides:
  * An asynchronous crawler, **`AsyncWebCrawler`**.
  * Configurable browser and run settings via **`BrowserConfig`**and**`CrawlerRunConfig`**.
  * Automatic HTML-to-Markdown conversion via **`DefaultMarkdownGenerator`**(supports optional filters).
  * Multiple extraction strategies (LLM-based or “traditional” CSS/XPath-based).


By the end of this guide, you’ll have performed a basic crawl, generated Markdown, tried out two extraction strategies, and crawled a dynamic page that uses “Load More” buttons or JavaScript updates.
## 2. Your First Crawl
Here’s a minimal Python script that creates an **`AsyncWebCrawler`**, fetches a webpage, and prints the first 300 characters of its Markdown output:
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com")
    print(result.markdown[:300]) # Print first 300 chars
if __name__ == "__main__":
  asyncio.run(main())

```

**What’s happening?** - **`AsyncWebCrawler`**launches a headless browser (Chromium by default). - It fetches`https://example.com`. - Crawl4AI automatically converts the HTML into Markdown.
You now have a simple, working crawl!
## 3. Basic Configuration (Light Introduction)
Crawl4AI’s crawler can be heavily customized using two main classes:
1. **`BrowserConfig`**: Controls browser behavior (headless or full UI, user agent, JavaScript toggles, etc.). 2.**`CrawlerRunConfig`**: Controls how each crawl runs (caching, extraction, timeouts, hooking, etc.).
Below is an example with minimal usage:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
async def main():
  browser_conf = BrowserConfig(headless=True) # or False to see the browser
  run_conf = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler(config=browser_conf) as crawler:
    result = await crawler.arun(
      url="https://example.com",
      config=run_conf
    )
    print(result.markdown)
if __name__ == "__main__":
  asyncio.run(main())

```

> IMPORTANT: By default cache mode is set to `CacheMode.ENABLED`. So to have fresh content, you need to set it to `CacheMode.BYPASS`
We’ll explore more advanced config in later tutorials (like enabling proxies, PDF output, multi-tab sessions, etc.). For now, just note how you pass these objects to manage crawling.
## 4. Generating Markdown Output
By default, Crawl4AI automatically generates Markdown from each crawled page. However, the exact output depends on whether you specify a **markdown generator** or **content filter**.
  * **`result.markdown`**: The direct HTML-to-Markdown conversion.
  * **`result.markdown.fit_markdown`**: The same content after applying any configured**content filter** (e.g., `PruningContentFilter`).


### Example: Using a Filter with `DefaultMarkdownGenerator`
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
md_generator = DefaultMarkdownGenerator(
  content_filter=PruningContentFilter(threshold=0.4, threshold_type="fixed")
)
config = CrawlerRunConfig(
  cache_mode=CacheMode.BYPASS,
  markdown_generator=md_generator
)
async with AsyncWebCrawler() as crawler:
  result = await crawler.arun("https://news.ycombinator.com", config=config)
  print("Raw Markdown length:", len(result.markdown.raw_markdown))
  print("Fit Markdown length:", len(result.markdown.fit_markdown))

```

**Note** : If you do **not** specify a content filter or markdown generator, you’ll typically see only the raw Markdown. `PruningContentFilter` may adds around `50ms` in processing time. We’ll dive deeper into these strategies in a dedicated **Markdown Generation** tutorial.
## 5. Simple Data Extraction (CSS-based)
Crawl4AI can also extract structured data (JSON) using CSS or XPath selectors. Below is a minimal CSS-based example:
> **New!** Crawl4AI now provides a powerful utility to automatically generate extraction schemas using LLM. This is a one-time cost that gives you a reusable schema for fast, LLM-free extractions:
```
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from crawl4ai import LLMConfig
# Generate a schema (one-time cost)
html = "<div class='product'><h2>Gaming Laptop</h2><span class='price'>$999.99</span></div>"
# Using OpenAI (requires API token)
schema = JsonCssExtractionStrategy.generate_schema(
  html,
  llm_config = LLMConfig(provider="openai/gpt-4o",api_token="your-openai-token") # Required for OpenAI
)
# Or using Ollama (open source, no token needed)
schema = JsonCssExtractionStrategy.generate_schema(
  html,
  llm_config = LLMConfig(provider="ollama/llama3.3", api_token=None) # Not needed for Ollama
)
# Use the schema for fast, repeated extractions
strategy = JsonCssExtractionStrategy(schema)

```

For a complete guide on schema generation and advanced usage, see [No-LLM Extraction Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/).
Here's a basic extraction example:
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  schema = {
    "name": "Example Items",
    "baseSelector": "div.item",
    "fields": [
      {"name": "title", "selector": "h2", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
  raw_html = "<div class='item'><h2>Item 1</h2><a href='https://example.com/item1'>Link 1</a></div>"
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="raw://" + raw_html,
      config=CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=JsonCssExtractionStrategy(schema)
      )
    )
    # The JSON output is stored in 'extracted_content'
    data = json.loads(result.extracted_content)
    print(data)
if __name__ == "__main__":
  asyncio.run(main())

```

**Why is this helpful?** - Great for repetitive page structures (e.g., item listings, articles). - No AI usage or costs. - The crawler returns a JSON string you can parse or store.
> Tips: You can pass raw HTML to the crawler instead of a URL. To do so, prefix the HTML with `raw://`.
## 6. Simple Data Extraction (LLM-based)
For more complex or irregular pages, a language model can parse text intelligently into a structure you define. Crawl4AI supports **open-source** or **closed-source** providers:
  * **Open-Source Models** (e.g., `ollama/llama3.3`, `no_token`) 
  * **OpenAI Models** (e.g., `openai/gpt-4`, requires `api_token`) 
  * Or any provider supported by the underlying library


Below is an example using **open-source** style (no token) and closed-source:
```
import os
import json
import asyncio
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
class OpenAIModelFee(BaseModel):
  model_name: str = Field(..., description="Name of the OpenAI model.")
  input_fee: str = Field(..., description="Fee for input token for the OpenAI model.")
  output_fee: str = Field(
    ..., description="Fee for output token for the OpenAI model."
  )
async def extract_structured_data_using_llm(
  provider: str, api_token: str = None, extra_headers: Dict[str, str] = None
):
  print(f"\n--- Extracting Structured Data with {provider} ---")
  if api_token is None and provider != "ollama":
    print(f"API token is required for {provider}. Skipping this example.")
    return
  browser_config = BrowserConfig(headless=True)
  extra_args = {"temperature": 0, "top_p": 0.9, "max_tokens": 2000}
  if extra_headers:
    extra_args["extra_headers"] = extra_headers
  crawler_config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    word_count_threshold=1,
    page_timeout=80000,
    extraction_strategy=LLMExtractionStrategy(
      llm_config = LLMConfig(provider=provider,api_token=api_token),
      schema=OpenAIModelFee.model_json_schema(),
      extraction_type="schema",
      instruction="""From the crawled content, extract all mentioned model names along with their fees for input and output tokens. 
      Do not miss any models in the entire content.""",
      extra_args=extra_args,
    ),
  )
  async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(
      url="https://openai.com/api/pricing/", config=crawler_config
    )
    print(result.extracted_content)
if __name__ == "__main__":
  asyncio.run(
    extract_structured_data_using_llm(
      provider="openai/gpt-4o", api_token=os.getenv("OPENAI_API_KEY")
    )
  )

```

**What’s happening?** - We define a Pydantic schema (`PricingInfo`) describing the fields we want. - The LLM extraction strategy uses that schema and your instructions to transform raw text into structured JSON. - Depending on the **provider** and **api_token** , you can use local models or a remote API.
## 7. Multi-URL Concurrency (Preview)
If you need to crawl multiple URLs in **parallel** , you can use `arun_many()`. By default, Crawl4AI employs a **MemoryAdaptiveDispatcher** , automatically adjusting concurrency based on system resources. Here’s a quick glimpse:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def quick_parallel_example():
  urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
  ]
  run_conf = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    stream=True # Enable streaming mode
  )
  async with AsyncWebCrawler() as crawler:
    # Stream results as they complete
    async for result in await crawler.arun_many(urls, config=run_conf):
      if result.success:
        print(f"[OK] {result.url}, length: {len(result.markdown.raw_markdown)}")
      else:
        print(f"[ERROR] {result.url} => {result.error_message}")
    # Or get all results at once (default behavior)
    run_conf = run_conf.clone(stream=False)
    results = await crawler.arun_many(urls, config=run_conf)
    for res in results:
      if res.success:
        print(f"[OK] {res.url}, length: {len(res.markdown.raw_markdown)}")
      else:
        print(f"[ERROR] {res.url} => {res.error_message}")
if __name__ == "__main__":
  asyncio.run(quick_parallel_example())

```

The example above shows two ways to handle multiple URLs: 1. **Streaming mode** (`stream=True`): Process results as they become available using `async for` 2. **Batch mode** (`stream=False`): Wait for all results to complete
For more advanced concurrency (e.g., a **semaphore-based** approach, **adaptive memory usage throttling** , or customized rate limiting), see [Advanced Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/).
## 8. Dynamic Content Example
Some sites require multiple “page clicks” or dynamic JavaScript updates. Below is an example showing how to **click** a “Next Page” button and wait for new commits to load on GitHub, using **`BrowserConfig`**and**`CrawlerRunConfig`**:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def extract_structured_data_using_css_extractor():
  print("\n--- Using JsonCssExtractionStrategy for Fast Structured Output ---")
  schema = {
    "name": "KidoCode Courses",
    "baseSelector": "section.charge-methodology .w-tab-content > div",
    "fields": [
      {
        "name": "section_title",
        "selector": "h3.heading-50",
        "type": "text",
      },
      {
        "name": "section_description",
        "selector": ".charge-content",
        "type": "text",
      },
      {
        "name": "course_name",
        "selector": ".text-block-93",
        "type": "text",
      },
      {
        "name": "course_description",
        "selector": ".course-content-text",
        "type": "text",
      },
      {
        "name": "course_icon",
        "selector": ".image-92",
        "type": "attribute",
        "attribute": "src",
      },
    ],
  }
  browser_config = BrowserConfig(headless=True, java_script_enabled=True)
  js_click_tabs = """
  (async () => {
    const tabs = document.querySelectorAll("section.charge-methodology .tabs-menu-3 > div");
    for(let tab of tabs) {
      tab.scrollIntoView();
      tab.click();
      await new Promise(r => setTimeout(r, 500));
    }
  })();
  """
  crawler_config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    extraction_strategy=JsonCssExtractionStrategy(schema),
    js_code=[js_click_tabs],
  )
  async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(
      url="https://www.kidocode.com/degrees/technology", config=crawler_config
    )
    companies = json.loads(result.extracted_content)
    print(f"Successfully extracted {len(companies)} companies")
    print(json.dumps(companies[0], indent=2))
async def main():
  await extract_structured_data_using_css_extractor()
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Points** :
  * **`BrowserConfig(headless=False)`**: We want to watch it click “Next Page.”
  * **`CrawlerRunConfig(...)`**: We specify the extraction strategy, pass`session_id` to reuse the same page. 
  * **`js_code`**and**`wait_for`**are used for subsequent pages (`page > 0`) to click the “Next” button and wait for new commits to load. 
  * **`js_only=True`**indicates we’re not re-navigating but continuing the existing session.
  * Finally, we call `kill_session()` to clean up the page and browser session.


## 9. Next Steps
Congratulations! You have:
  1. Performed a basic crawl and printed Markdown. 
  2. Used **content filters** with a markdown generator. 
  3. Extracted JSON via **CSS** or **LLM** strategies. 
  4. Handled **dynamic** pages with JavaScript triggers.


If you’re ready for more, check out:
  * **Installation** : A deeper dive into advanced installs, Docker usage (experimental), or optional dependencies. 
  * **Hooks & Auth**: Learn how to run custom JavaScript or handle logins with cookies, local storage, etc. 
  * **Deployment** : Explore ephemeral testing in Docker or plan for the upcoming stable Docker release. 
  * **Browser Management** : Delve into user simulation, stealth modes, and concurrency best practices. 


Crawl4AI is a powerful, flexible tool. Enjoy building out your scrapers, data pipelines, or AI-driven extraction flows. Happy crawling!
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/page-interaction)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * Page Interaction
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction#page-interaction)
  * [1. JavaScript Execution](https://docs.crawl4ai.com/core/page-interaction#1-javascript-execution)
  * [2. Wait Conditions](https://docs.crawl4ai.com/core/page-interaction#2-wait-conditions)
  * [3. Handling Dynamic Content](https://docs.crawl4ai.com/core/page-interaction#3-handling-dynamic-content)
  * [4. Timing Control](https://docs.crawl4ai.com/core/page-interaction#4-timing-control)
  * [5. Multi-Step Interaction Example](https://docs.crawl4ai.com/core/page-interaction#5-multi-step-interaction-example)
  * [6. Combine Interaction with Extraction](https://docs.crawl4ai.com/core/page-interaction#6-combine-interaction-with-extraction)
  * [7. Relevant CrawlerRunConfig Parameters](https://docs.crawl4ai.com/core/page-interaction#7-relevant-crawlerrunconfig-parameters)
  * [8. Conclusion](https://docs.crawl4ai.com/core/page-interaction#8-conclusion)


# Page Interaction
Crawl4AI provides powerful features for interacting with **dynamic** webpages, handling JavaScript execution, waiting for conditions, and managing multi-step flows. By combining **js_code** , **wait_for** , and certain **CrawlerRunConfig** parameters, you can:
  1. Click “Load More” buttons 
  2. Fill forms and submit them 
  3. Wait for elements or data to appear 
  4. Reuse sessions across multiple steps 


Below is a quick overview of how to do it.
## 1. JavaScript Execution
### Basic Execution
**`js_code`**in**`CrawlerRunConfig`**accepts either a single JS string or a list of JS snippets.**Example** : We’ll scroll to the bottom of the page, then optionally click a “Load More” button.
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  # Single JS command
  config = CrawlerRunConfig(
    js_code="window.scrollTo(0, document.body.scrollHeight);"
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com", # Example site
      config=config
    )
    print("Crawled length:", len(result.cleaned_html))
  # Multiple commands
  js_commands = [
    "window.scrollTo(0, document.body.scrollHeight);",
    # 'More' link on Hacker News
    "document.querySelector('a.morelink')?.click();", 
  ]
  config = CrawlerRunConfig(js_code=js_commands)
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com", # Another pass
      config=config
    )
    print("After scroll+click, length:", len(result.cleaned_html))
if __name__ == "__main__":
  asyncio.run(main())

```

**Relevant`CrawlerRunConfig` params**: - **`js_code`**: A string or list of strings with JavaScript to run after the page loads. -**`js_only`**: If set to`True` on subsequent calls, indicates we’re continuing an existing session without a new full navigation. - **`session_id`**: If you want to keep the same page across multiple calls, specify an ID.
## 2. Wait Conditions
### 2.1 CSS-Based Waiting
Sometimes, you just want to wait for a specific element to appear. For example:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  config = CrawlerRunConfig(
    # Wait for at least 30 items on Hacker News
    wait_for="css:.athing:nth-child(30)" 
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com",
      config=config
    )
    print("We have at least 30 items loaded!")
    # Rough check
    print("Total items in HTML:", result.cleaned_html.count("athing")) 
if __name__ == "__main__":
  asyncio.run(main())

```

**Key param** : - **`wait_for="css:..."`**: Tells the crawler to wait until that CSS selector is present.
### 2.2 JavaScript-Based Waiting
For more complex conditions (e.g., waiting for content length to exceed a threshold), prefix `js:`:
```
wait_condition = """() => {
  const items = document.querySelectorAll('.athing');
  return items.length > 50; // Wait for at least 51 items
}"""
config = CrawlerRunConfig(wait_for=f"js:{wait_condition}")

```

**Behind the Scenes** : Crawl4AI keeps polling the JS function until it returns `true` or a timeout occurs.
## 3. Handling Dynamic Content
Many modern sites require **multiple steps** : scrolling, clicking “Load More,” or updating via JavaScript. Below are typical patterns.
### 3.1 Load More Example (Hacker News “More” Link)
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  # Step 1: Load initial Hacker News page
  config = CrawlerRunConfig(
    wait_for="css:.athing:nth-child(30)" # Wait for 30 items
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com",
      config=config
    )
    print("Initial items loaded.")
    # Step 2: Let's scroll and click the "More" link
    load_more_js = [
      "window.scrollTo(0, document.body.scrollHeight);",
      # The "More" link at page bottom
      "document.querySelector('a.morelink')?.click();" 
    ]
    next_page_conf = CrawlerRunConfig(
      js_code=load_more_js,
      wait_for="""js:() => {
        return document.querySelectorAll('.athing').length > 30;
      }""",
      # Mark that we do not re-navigate, but run JS in the same session:
      js_only=True,
      session_id="hn_session"
    )
    # Re-use the same crawler session
    result2 = await crawler.arun(
      url="https://news.ycombinator.com", # same URL but continuing session
      config=next_page_conf
    )
    total_items = result2.cleaned_html.count("athing")
    print("Items after load-more:", total_items)
if __name__ == "__main__":
  asyncio.run(main())

```

**Key params** : - **`session_id="hn_session"`**: Keep the same page across multiple calls to`arun()`. - **`js_only=True`**: We’re not performing a full reload, just applying JS in the existing page. -**`wait_for`**with`js:` : Wait for item count to grow beyond 30.
### 3.2 Form Interaction
If the site has a search or login form, you can fill fields and submit them with **`js_code`**. For instance, if GitHub had a local search form:
```
js_form_interaction = """
document.querySelector('#your-search').value = 'TypeScript commits';
document.querySelector('form').submit();
"""
config = CrawlerRunConfig(
  js_code=js_form_interaction,
  wait_for="css:.commit"
)
result = await crawler.arun(url="https://github.com/search", config=config)

```

**In reality** : Replace IDs or classes with the real site’s form selectors.
## 4. Timing Control
1. **`page_timeout`**(ms): Overall page load or script execution time limit. 2.**`delay_before_return_html`**(seconds): Wait an extra moment before capturing the final HTML. 3.**`mean_delay`** & **`max_range`**: If you call`arun_many()` with multiple URLs, these add a random pause between each request.
**Example** :
```
config = CrawlerRunConfig(
  page_timeout=60000, # 60s limit
  delay_before_return_html=2.5
)

```

## 5. Multi-Step Interaction Example
Below is a simplified script that does multiple “Load More” clicks on GitHub’s TypeScript commits page. It **re-uses** the same session to accumulate new commits each time. The code includes the relevant **`CrawlerRunConfig`**parameters you’d rely on.
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
async def multi_page_commits():
  browser_cfg = BrowserConfig(
    headless=False, # Visible for demonstration
    verbose=True
  )
  session_id = "github_ts_commits"
  base_wait = """js:() => {
    const commits = document.querySelectorAll('li.Box-sc-g0xbh4-0 h4');
    return commits.length > 0;
  }"""
  # Step 1: Load initial commits
  config1 = CrawlerRunConfig(
    wait_for=base_wait,
    session_id=session_id,
    cache_mode=CacheMode.BYPASS,
    # Not using js_only yet since it's our first load
  )
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    result = await crawler.arun(
      url="https://github.com/microsoft/TypeScript/commits/main",
      config=config1
    )
    print("Initial commits loaded. Count:", result.cleaned_html.count("commit"))
    # Step 2: For subsequent pages, we run JS to click 'Next Page' if it exists
    js_next_page = """
    const selector = 'a[data-testid="pagination-next-button"]';
    const button = document.querySelector(selector);
    if (button) button.click();
    """
    # Wait until new commits appear
    wait_for_more = """js:() => {
      const commits = document.querySelectorAll('li.Box-sc-g0xbh4-0 h4');
      if (!window.firstCommit && commits.length>0) {
        window.firstCommit = commits[0].textContent;
        return false;
      }
      // If top commit changes, we have new commits
      const topNow = commits[0]?.textContent.trim();
      return topNow && topNow !== window.firstCommit;
    }"""
    for page in range(2): # let's do 2 more "Next" pages
      config_next = CrawlerRunConfig(
        session_id=session_id,
        js_code=js_next_page,
        wait_for=wait_for_more,
        js_only=True,    # We're continuing from the open tab
        cache_mode=CacheMode.BYPASS
      )
      result2 = await crawler.arun(
        url="https://github.com/microsoft/TypeScript/commits/main",
        config=config_next
      )
      print(f"Page {page+2} commits count:", result2.cleaned_html.count("commit"))
    # Optionally kill session
    await crawler.crawler_strategy.kill_session(session_id)
async def main():
  await multi_page_commits()
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Points** :
  * **`session_id`**: Keep the same page open.
  * **`js_code`**+**`wait_for`**+**`js_only=True`**: We do partial refreshes, waiting for new commits to appear.
  * **`cache_mode=CacheMode.BYPASS`**ensures we always see fresh data each step.


## 6. Combine Interaction with Extraction
Once dynamic content is loaded, you can attach an **`extraction_strategy`**(like`JsonCssExtractionStrategy` or `LLMExtractionStrategy`). For example:
```
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
schema = {
  "name": "Commits",
  "baseSelector": "li.Box-sc-g0xbh4-0",
  "fields": [
    {"name": "title", "selector": "h4.markdown-title", "type": "text"}
  ]
}
config = CrawlerRunConfig(
  session_id="ts_commits_session",
  js_code=js_next_page,
  wait_for=wait_for_more,
  extraction_strategy=JsonCssExtractionStrategy(schema)
)

```

When done, check `result.extracted_content` for the JSON.
## 7. Relevant `CrawlerRunConfig` Parameters
Below are the key interaction-related parameters in `CrawlerRunConfig`. For a full list, see [Configuration Parameters](https://docs.crawl4ai.com/api/parameters/).
  * **`js_code`**: JavaScript to run after initial load.
  * **`js_only`**: If`True` , no new page navigation—only JS in the existing session. 
  * **`wait_for`**: CSS (`"css:..."`) or JS (`"js:..."`) expression to wait for. 
  * **`session_id`**: Reuse the same page across calls.
  * **`cache_mode`**: Whether to read/write from the cache or bypass.
  * **`remove_overlay_elements`**: Remove certain popups automatically.
  * **`simulate_user`,`override_navigator` , `magic`**: Anti-bot or “human-like” interactions.


## 8. Conclusion
Crawl4AI’s **page interaction** features let you:
1. **Execute JavaScript** for scrolling, clicks, or form filling. 2. **Wait** for CSS or custom JS conditions before capturing data. 3. **Handle** multi-step flows (like “Load More”) with partial reloads or persistent sessions. 4. Combine with **structured extraction** for dynamic sites.
With these tools, you can scrape modern, interactive webpages confidently. For advanced hooking, user simulation, or in-depth config, check the [API reference](https://docs.crawl4ai.com/api/parameters/) or related advanced docs. Happy scripting!
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/local-files)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/cache-modes/)
    * Local Files & Raw HTML
    * [Link & Media](https://docs.crawl4ai.com/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Prefix-Based Input Handling in Crawl4AI](https://docs.crawl4ai.com/core/local-files#prefix-based-input-handling-in-crawl4ai)
  * [Crawling a Web URL](https://docs.crawl4ai.com/core/local-files#crawling-a-web-url)
  * [Crawling a Local HTML File](https://docs.crawl4ai.com/core/local-files#crawling-a-local-html-file)
  * [Crawling Raw HTML Content](https://docs.crawl4ai.com/core/local-files#crawling-raw-html-content)
  * [Complete Example](https://docs.crawl4ai.com/core/local-files#complete-example)
  * [Conclusion](https://docs.crawl4ai.com/core/local-files#conclusion)


# Prefix-Based Input Handling in Crawl4AI
This guide will walk you through using the Crawl4AI library to crawl web pages, local HTML files, and raw HTML strings. We'll demonstrate these capabilities using a Wikipedia page as an example.
## Crawling a Web URL
To crawl a live web page, provide the URL starting with `http://` or `https://`, using a `CrawlerRunConfig` object:
```
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig
async def crawl_web():
  config = CrawlerRunConfig(bypass_cache=True)
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://en.wikipedia.org/wiki/apple", 
      config=config
    )
    if result.success:
      print("Markdown Content:")
      print(result.markdown)
    else:
      print(f"Failed to crawl: {result.error_message}")
asyncio.run(crawl_web())

```

## Crawling a Local HTML File
To crawl a local HTML file, prefix the file path with `file://`.
```
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig
async def crawl_local_file():
  local_file_path = "/path/to/apple.html" # Replace with your file path
  file_url = f"file://{local_file_path}"
  config = CrawlerRunConfig(bypass_cache=True)
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url=file_url, config=config)
    if result.success:
      print("Markdown Content from Local File:")
      print(result.markdown)
    else:
      print(f"Failed to crawl local file: {result.error_message}")
asyncio.run(crawl_local_file())

```

## Crawling Raw HTML Content
To crawl raw HTML content, prefix the HTML string with `raw:`.
```
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig
async def crawl_raw_html():
  raw_html = "<html><body><h1>Hello, World!</h1></body></html>"
  raw_html_url = f"raw:{raw_html}"
  config = CrawlerRunConfig(bypass_cache=True)
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url=raw_html_url, config=config)
    if result.success:
      print("Markdown Content from Raw HTML:")
      print(result.markdown)
    else:
      print(f"Failed to crawl raw HTML: {result.error_message}")
asyncio.run(crawl_raw_html())

```

# Complete Example
Below is a comprehensive script that:
  1. Crawls the Wikipedia page for "Apple."
  2. Saves the HTML content to a local file (`apple.html`).
  3. Crawls the local HTML file and verifies the markdown length matches the original crawl.
  4. Crawls the raw HTML content from the saved file and verifies consistency.


```
import os
import sys
import asyncio
from pathlib import Path
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig
async def main():
  wikipedia_url = "https://en.wikipedia.org/wiki/apple"
  script_dir = Path(__file__).parent
  html_file_path = script_dir / "apple.html"
  async with AsyncWebCrawler() as crawler:
    # Step 1: Crawl the Web URL
    print("\n=== Step 1: Crawling the Wikipedia URL ===")
    web_config = CrawlerRunConfig(bypass_cache=True)
    result = await crawler.arun(url=wikipedia_url, config=web_config)
    if not result.success:
      print(f"Failed to crawl {wikipedia_url}: {result.error_message}")
      return
    with open(html_file_path, 'w', encoding='utf-8') as f:
      f.write(result.html)
    web_crawl_length = len(result.markdown)
    print(f"Length of markdown from web crawl: {web_crawl_length}\n")
    # Step 2: Crawl from the Local HTML File
    print("=== Step 2: Crawling from the Local HTML File ===")
    file_url = f"file://{html_file_path.resolve()}"
    file_config = CrawlerRunConfig(bypass_cache=True)
    local_result = await crawler.arun(url=file_url, config=file_config)
    if not local_result.success:
      print(f"Failed to crawl local file {file_url}: {local_result.error_message}")
      return
    local_crawl_length = len(local_result.markdown)
    assert web_crawl_length == local_crawl_length, "Markdown length mismatch"
    print("✅ Markdown length matches between web and local file crawl.\n")
    # Step 3: Crawl Using Raw HTML Content
    print("=== Step 3: Crawling Using Raw HTML Content ===")
    with open(html_file_path, 'r', encoding='utf-8') as f:
      raw_html_content = f.read()
    raw_html_url = f"raw:{raw_html_content}"
    raw_config = CrawlerRunConfig(bypass_cache=True)
    raw_result = await crawler.arun(url=raw_html_url, config=raw_config)
    if not raw_result.success:
      print(f"Failed to crawl raw HTML content: {raw_result.error_message}")
      return
    raw_crawl_length = len(raw_result.markdown)
    assert web_crawl_length == raw_crawl_length, "Markdown length mismatch"
    print("✅ Markdown length matches between web and raw HTML crawl.\n")
    print("All tests passed successfully!")
  if html_file_path.exists():
    os.remove(html_file_path)
if __name__ == "__main__":
  asyncio.run(main())

```

# Conclusion
With the unified `url` parameter and prefix-based handling in **Crawl4AI** , you can seamlessly handle web URLs, local HTML files, and raw HTML content. Use `CrawlerRunConfig` for flexible and consistent configuration in all scenarios.
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/extraction/chunking)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/clustring-strategies/)
    * Chunking
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Chunking Strategies](https://docs.crawl4ai.com/extraction/chunking#chunking-strategies)
  * [Why Use Chunking?](https://docs.crawl4ai.com/extraction/chunking#why-use-chunking)
  * [Methods of Chunking](https://docs.crawl4ai.com/extraction/chunking#methods-of-chunking)
  * [Combining Chunking with Cosine Similarity](https://docs.crawl4ai.com/extraction/chunking#combining-chunking-with-cosine-similarity)


# Chunking Strategies
Chunking strategies are critical for dividing large texts into manageable parts, enabling effective content processing and extraction. These strategies are foundational in cosine similarity-based extraction techniques, which allow users to retrieve only the most relevant chunks of content for a given query. Additionally, they facilitate direct integration into RAG (Retrieval-Augmented Generation) systems for structured and scalable workflows.
### Why Use Chunking?
1. **Cosine Similarity and Query Relevance** : Prepares chunks for semantic similarity analysis. 2. **RAG System Integration** : Seamlessly processes and stores chunks for retrieval. 3. **Structured Processing** : Allows for diverse segmentation methods, such as sentence-based, topic-based, or windowed approaches.
### Methods of Chunking
#### 1. Regex-Based Chunking
Splits text based on regular expression patterns, useful for coarse segmentation.
**Code Example** : 
```
class RegexChunking:
  def __init__(self, patterns=None):
    self.patterns = patterns or [r'\n\n'] # Default pattern for paragraphs
  def chunk(self, text):
    paragraphs = [text]
    for pattern in self.patterns:
      paragraphs = [seg for p in paragraphs for seg in re.split(pattern, p)]
    return paragraphs
# Example Usage
text = """This is the first paragraph.
This is the second paragraph."""
chunker = RegexChunking()
print(chunker.chunk(text))

```

#### 2. Sentence-Based Chunking
Divides text into sentences using NLP tools, ideal for extracting meaningful statements.
**Code Example** : 
```
from nltk.tokenize import sent_tokenize
class NlpSentenceChunking:
  def chunk(self, text):
    sentences = sent_tokenize(text)
    return [sentence.strip() for sentence in sentences]
# Example Usage
text = "This is sentence one. This is sentence two."
chunker = NlpSentenceChunking()
print(chunker.chunk(text))

```

#### 3. Topic-Based Segmentation
Uses algorithms like TextTiling to create topic-coherent chunks.
**Code Example** : 
```
from nltk.tokenize import TextTilingTokenizer
class TopicSegmentationChunking:
  def __init__(self):
    self.tokenizer = TextTilingTokenizer()
  def chunk(self, text):
    return self.tokenizer.tokenize(text)
# Example Usage
text = """This is an introduction.
This is a detailed discussion on the topic."""
chunker = TopicSegmentationChunking()
print(chunker.chunk(text))

```

#### 4. Fixed-Length Word Chunking
Segments text into chunks of a fixed word count.
**Code Example** : 
```
class FixedLengthWordChunking:
  def __init__(self, chunk_size=100):
    self.chunk_size = chunk_size
  def chunk(self, text):
    words = text.split()
    return [' '.join(words[i:i + self.chunk_size]) for i in range(0, len(words), self.chunk_size)]
# Example Usage
text = "This is a long text with many words to be chunked into fixed sizes."
chunker = FixedLengthWordChunking(chunk_size=5)
print(chunker.chunk(text))

```

#### 5. Sliding Window Chunking
Generates overlapping chunks for better contextual coherence.
**Code Example** : 
```
class SlidingWindowChunking:
  def __init__(self, window_size=100, step=50):
    self.window_size = window_size
    self.step = step
  def chunk(self, text):
    words = text.split()
    chunks = []
    for i in range(0, len(words) - self.window_size + 1, self.step):
      chunks.append(' '.join(words[i:i + self.window_size]))
    return chunks
# Example Usage
text = "This is a long text to demonstrate sliding window chunking."
chunker = SlidingWindowChunking(window_size=5, step=2)
print(chunker.chunk(text))

```

### Combining Chunking with Cosine Similarity
To enhance the relevance of extracted content, chunking strategies can be paired with cosine similarity techniques. Here’s an example workflow:
**Code Example** : 
```
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
class CosineSimilarityExtractor:
  def __init__(self, query):
    self.query = query
    self.vectorizer = TfidfVectorizer()
  def find_relevant_chunks(self, chunks):
    vectors = self.vectorizer.fit_transform([self.query] + chunks)
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    return [(chunks[i], similarities[i]) for i in range(len(chunks))]
# Example Workflow
text = """This is a sample document. It has multiple sentences. 
We are testing chunking and similarity."""
chunker = SlidingWindowChunking(window_size=5, step=3)
chunks = chunker.chunk(text)
query = "testing chunking"
extractor = CosineSimilarityExtractor(query)
relevant_chunks = extractor.find_relevant_chunks(chunks)
print(relevant_chunks)

```

Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/extraction/clustring-strategies)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/llm-strategies/)
    * Clustering Strategies
    * [Chunking](https://docs.crawl4ai.com/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Cosine Strategy](https://docs.crawl4ai.com/extraction/clustring-strategies#cosine-strategy)
  * [How It Works](https://docs.crawl4ai.com/extraction/clustring-strategies#how-it-works)
  * [Basic Usage](https://docs.crawl4ai.com/extraction/clustring-strategies#basic-usage)
  * [Configuration Options](https://docs.crawl4ai.com/extraction/clustring-strategies#configuration-options)
  * [Use Cases](https://docs.crawl4ai.com/extraction/clustring-strategies#use-cases)
  * [Advanced Features](https://docs.crawl4ai.com/extraction/clustring-strategies#advanced-features)
  * [Best Practices](https://docs.crawl4ai.com/extraction/clustring-strategies#best-practices)
  * [Error Handling](https://docs.crawl4ai.com/extraction/clustring-strategies#error-handling)


# Cosine Strategy
The Cosine Strategy in Crawl4AI uses similarity-based clustering to identify and extract relevant content sections from web pages. This strategy is particularly useful when you need to find and extract content based on semantic similarity rather than structural patterns.
## How It Works
The Cosine Strategy: 1. Breaks down page content into meaningful chunks 2. Converts text into vector representations 3. Calculates similarity between chunks 4. Clusters similar content together 5. Ranks and filters content based on relevance
## Basic Usage
```
from crawl4ai.extraction_strategy import CosineStrategy
strategy = CosineStrategy(
  semantic_filter="product reviews",  # Target content type
  word_count_threshold=10,       # Minimum words per cluster
  sim_threshold=0.3          # Similarity threshold
)
async with AsyncWebCrawler() as crawler:
  result = await crawler.arun(
    url="https://example.com/reviews",
    extraction_strategy=strategy
  )
  content = result.extracted_content

```

## Configuration Options
### Core Parameters
```
CosineStrategy(
  # Content Filtering
  semantic_filter: str = None,    # Keywords/topic for content filtering
  word_count_threshold: int = 10,  # Minimum words per cluster
  sim_threshold: float = 0.3,    # Similarity threshold (0.0 to 1.0)
  # Clustering Parameters
  max_dist: float = 0.2,      # Maximum distance for clustering
  linkage_method: str = 'ward',   # Clustering linkage method
  top_k: int = 3,          # Number of top categories to extract
  # Model Configuration
  model_name: str = 'sentence-transformers/all-MiniLM-L6-v2', # Embedding model
  verbose: bool = False       # Enable logging
)

```

### Parameter Details
1. **semantic_filter** - Sets the target topic or content type - Use keywords relevant to your desired content - Example: "technical specifications", "user reviews", "pricing information"
2. **sim_threshold** - Controls how similar content must be to be grouped together - Higher values (e.g., 0.8) mean stricter matching - Lower values (e.g., 0.3) allow more variation 
```
# Strict matching
strategy = CosineStrategy(sim_threshold=0.8)
# Loose matching
strategy = CosineStrategy(sim_threshold=0.3)

```

3. **word_count_threshold** - Filters out short content blocks - Helps eliminate noise and irrelevant content 
```
# Only consider substantial paragraphs
strategy = CosineStrategy(word_count_threshold=50)

```

4. **top_k** - Number of top content clusters to return - Higher values return more diverse content 
```
# Get top 5 most relevant content clusters
strategy = CosineStrategy(top_k=5)

```

## Use Cases
### 1. Article Content Extraction
```
strategy = CosineStrategy(
  semantic_filter="main article content",
  word_count_threshold=100, # Longer blocks for articles
  top_k=1          # Usually want single main content
)
result = await crawler.arun(
  url="https://example.com/blog/post",
  extraction_strategy=strategy
)

```

### 2. Product Review Analysis
```
strategy = CosineStrategy(
  semantic_filter="customer reviews and ratings",
  word_count_threshold=20,  # Reviews can be shorter
  top_k=10,         # Get multiple reviews
  sim_threshold=0.4     # Allow variety in review content
)

```

### 3. Technical Documentation
```
strategy = CosineStrategy(
  semantic_filter="technical specifications documentation",
  word_count_threshold=30,
  sim_threshold=0.6,    # Stricter matching for technical content
  max_dist=0.3       # Allow related technical sections
)

```

## Advanced Features
### Custom Clustering
```
strategy = CosineStrategy(
  linkage_method='complete', # Alternative clustering method
  max_dist=0.4,       # Larger clusters
  model_name='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2' # Multilingual support
)

```

### Content Filtering Pipeline
```
strategy = CosineStrategy(
  semantic_filter="pricing plans features",
  word_count_threshold=15,
  sim_threshold=0.5,
  top_k=3
)
async def extract_pricing_features(url: str):
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url=url,
      extraction_strategy=strategy
    )
    if result.success:
      content = json.loads(result.extracted_content)
      return {
        'pricing_features': content,
        'clusters': len(content),
        'similarity_scores': [item['score'] for item in content]
      }

```

## Best Practices
1. **Adjust Thresholds Iteratively** - Start with default values - Adjust based on results - Monitor clustering quality
2. **Choose Appropriate Word Count Thresholds** - Higher for articles (100+) - Lower for reviews/comments (20+) - Medium for product descriptions (50+)
3. **Optimize Performance**
```
strategy = CosineStrategy(
  word_count_threshold=10, # Filter early
  top_k=5,         # Limit results
  verbose=True       # Monitor performance
)

```

4. **Handle Different Content Types**
```
# For mixed content pages
strategy = CosineStrategy(
  semantic_filter="product features",
  sim_threshold=0.4,   # More flexible matching
  max_dist=0.3,     # Larger clusters
  top_k=3        # Multiple relevant sections
)

```

## Error Handling
```
try:
  result = await crawler.arun(
    url="https://example.com",
    extraction_strategy=strategy
  )
  if result.success:
    content = json.loads(result.extracted_content)
    if not content:
      print("No relevant content found")
  else:
    print(f"Extraction failed: {result.error_message}")
except Exception as e:
  print(f"Error during extraction: {str(e)}")

```

The Cosine Strategy is particularly effective when: - Content structure is inconsistent - You need semantic understanding - You want to find similar content blocks - Structure-based extraction (CSS/XPath) isn't reliable
It works well with other strategies and can be used as a pre-processing step for LLM-based extraction.
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching

# 403 Forbidden
nginx/1.24.0 (Ubuntu)
