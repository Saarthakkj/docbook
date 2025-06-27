[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/)


×
  * Home
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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
  * [Video Tutorial](https://docs.crawl4ai.com/#video-tutorial)
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
Copy
```

## Video Tutorial
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
#### On this page
  * [Quick Start](https://docs.crawl4ai.com/#quick-start)
  * [Video Tutorial](https://docs.crawl4ai.com/#video-tutorial)
  * [What Does Crawl4AI Do?](https://docs.crawl4ai.com/#what-does-crawl4ai-do)
  * [Documentation Structure](https://docs.crawl4ai.com/#documentation-structure)
  * [How You Can Support](https://docs.crawl4ai.com/#how-you-can-support)
  * [Quick Links](https://docs.crawl4ai.com/#quick-links)


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * Home
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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
  * [Video Tutorial](https://docs.crawl4ai.com/#video-tutorial)
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
Copy
```

## Video Tutorial
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
#### On this page
  * [Quick Start](https://docs.crawl4ai.com/#quick-start)
  * [Video Tutorial](https://docs.crawl4ai.com/#video-tutorial)
  * [What Does Crawl4AI Do?](https://docs.crawl4ai.com/#what-does-crawl4ai-do)
  * [Documentation Structure](https://docs.crawl4ai.com/#documentation-structure)
  * [How You Can Support](https://docs.crawl4ai.com/#how-you-can-support)
  * [Quick Links](https://docs.crawl4ai.com/#quick-links)


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/blog/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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


  * [Crawl4AI Blog](https://docs.crawl4ai.com/blog/#crawl4ai-blog)
  * [Latest Release](https://docs.crawl4ai.com/blog/#latest-release)
  * [License Change](https://docs.crawl4ai.com/blog/#license-change)
  * [Project History](https://docs.crawl4ai.com/blog/#project-history)
  * [Stay Updated](https://docs.crawl4ai.com/blog/#stay-updated)


# Crawl4AI Blog
Welcome to the Crawl4AI blog! Here you'll find detailed release notes, technical insights, and updates about the project. Whether you're looking for the latest improvements or want to dive deep into web crawling techniques, this is the place.
## Latest Release
Here’s the blog index entry for **v0.6.0** , written to match the exact tone and structure of your previous entries:
### [Crawl4AI v0.6.0 – World-Aware Crawling, Pre-Warmed Browsers, and the MCP API](https://docs.crawl4ai.com/blog/releases/0.6.0/)
_April 23, 2025_
Crawl4AI v0.6.0 is our most powerful release yet. This update brings major architectural upgrades including world-aware crawling (set geolocation, locale, and timezone), real-time traffic capture, and a memory-efficient crawler pool with pre-warmed pages. 
The Docker server now exposes a full-featured MCP socket + SSE interface, supports streaming, and comes with a new Playground UI. Plus, table extraction is now native, and the new stress-test framework supports crawling 1,000+ URLs. 
Other key changes: 
  * Native support for `result.media["tables"]` to export DataFrames 
  * Full network + console logs and MHTML snapshot per crawl 
  * Browser pooling and pre-warming for faster cold starts 
  * New streaming endpoints via MCP API and Playground 
  * Robots.txt support, proxy rotation, and improved session handling 
  * Deprecated old markdown names, legacy modules cleaned up 
  * Massive repo cleanup: ~36K insertions, ~5K deletions across 121 files


[Read full release notes →](https://docs.crawl4ai.com/blog/releases/0.6.0/)
Let me know if you want me to auto-update the actual file or just paste this into the markdown.
### [Crawl4AI v0.5.0: Deep Crawling, Scalability, and a New CLI!](https://docs.crawl4ai.com/blog/releases/0.5.0/)
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
### [0.4.2 - Configurable Crawlers, Session Management, and Smarter Screenshots](https://docs.crawl4ai.com/blog/releases/0.4.2/)
_December 12, 2024_
The 0.4.2 update brings massive improvements to configuration, making crawlers and browsers easier to manage with dedicated objects. You can now import/export local storage for seamless session management. Plus, long-page screenshots are faster and cleaner, and full-page PDF exports are now possible. Check out all the new features to make your crawling experience even smoother.
[Read full release notes →](https://docs.crawl4ai.com/blog/releases/0.4.2/)
### [0.4.1 - Smarter Crawling with Lazy-Load Handling, Text-Only Mode, and More](https://docs.crawl4ai.com/blog/releases/0.4.1/)
_December 8, 2024_
This release brings major improvements to handling lazy-loaded images, a blazing-fast Text-Only Mode, full-page scanning for infinite scrolls, dynamic viewport adjustments, and session reuse for efficient crawling. If you're looking to improve speed, reliability, or handle dynamic content with ease, this update has you covered.
[Read full release notes →](https://docs.crawl4ai.com/blog/releases/0.4.1/)
### [0.4.0 - Major Content Filtering Update](https://docs.crawl4ai.com/blog/releases/0.4.0/)
_December 1, 2024_
Introduced significant improvements to content filtering, multi-threaded environment handling, and user-agent generation. This release features the new PruningContentFilter, enhanced thread safety, and improved test coverage.
[Read full release notes →](https://docs.crawl4ai.com/blog/releases/0.4.0/)
## Project History
Curious about how Crawl4AI has evolved? Check out our [complete changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md) for a detailed history of all versions and updates.
## Stay Updated
  * Star us on [GitHub](https://github.com/unclecode/crawl4ai)
  * Follow [@unclecode](https://twitter.com/unclecode) on Twitter
  * Join our community discussions on GitHub


#### On this page
  * [Latest Release](https://docs.crawl4ai.com/blog/#latest-release)
  * [Crawl4AI v0.6.0 – World-Aware Crawling, Pre-Warmed Browsers, and the MCP API](https://docs.crawl4ai.com/blog/#crawl4ai-v060-world-aware-crawling-pre-warmed-browsers-and-the-mcp-api)
  * [Crawl4AI v0.5.0: Deep Crawling, Scalability, and a New CLI!](https://docs.crawl4ai.com/blog/#crawl4ai-v050-deep-crawling-scalability-and-a-new-cli)
  * [License Change](https://docs.crawl4ai.com/blog/#license-change)
  * [0.4.2 - Configurable Crawlers, Session Management, and Smarter Screenshots](https://docs.crawl4ai.com/blog/#042-configurable-crawlers-session-management-and-smarter-screenshots)
  * [0.4.1 - Smarter Crawling with Lazy-Load Handling, Text-Only Mode, and More](https://docs.crawl4ai.com/blog/#041-smarter-crawling-with-lazy-load-handling-text-only-mode-and-more)
  * [0.4.0 - Major Content Filtering Update](https://docs.crawl4ai.com/blog/#040-major-content-filtering-update)
  * [Project History](https://docs.crawl4ai.com/blog/#project-history)
  * [Stay Updated](https://docs.crawl4ai.com/blog/#stay-updated)


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/core/browser-crawler-config/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * Browser, Crawler & LLM Config
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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


  * [Browser, Crawler & LLM Configuration (Quick Overview)](https://docs.crawl4ai.com/core/browser-crawler-config/#browser-crawler-llm-configuration-quick-overview)
  * [1. BrowserConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config/#1-browserconfig-essentials)
  * [2. CrawlerRunConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config/#2-crawlerrunconfig-essentials)
  * [3. LLMConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config/#3-llmconfig-essentials)
  * [4. Putting It All Together](https://docs.crawl4ai.com/core/browser-crawler-config/#4-putting-it-all-together)
  * [5. Next Steps](https://docs.crawl4ai.com/core/browser-crawler-config/#5-next-steps)
  * [6. Conclusion](https://docs.crawl4ai.com/core/browser-crawler-config/#6-conclusion)


# Browser, Crawler & LLM Configuration (Quick Overview)
Crawl4AI's flexibility stems from two key classes:
  1. **`BrowserConfig`**– Dictates**how** the browser is launched and behaves (e.g., headless or visible, proxy, user agent). 
  2. **`CrawlerRunConfig`**– Dictates**how** each **crawl** operates (e.g., caching, extraction, timeouts, JavaScript code to run, etc.). 
  3. **`LLMConfig`**- Dictates**how** LLM providers are configured. (model, api token, base url, temperature etc.)


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
Copy
```

### Key Fields to Note
  1. **`browser_type`**
  2. Options: `"chromium"`, `"firefox"`, or `"webkit"`. 
  3. Defaults to `"chromium"`. 
  4. If you need a different engine, specify it here.
  5. **`headless`**
  6. `True`: Runs the browser in headless mode (invisible browser). 
  7. `False`: Runs the browser in visible mode, which helps with debugging.
  8. **`proxy_config`**
  9. A dictionary with fields like: 
```
{
  "server": "http://proxy.example.com:8080", 
  "username": "...", 
  "password": "..."
}
Copy
```

  10. Leave as `None` if a proxy is not required.
  11. **`viewport_width` & `viewport_height`**: 
  12. The initial window size. 
  13. Some sites behave differently with smaller or bigger viewports.
  14. **`verbose`**:
  15. If `True`, prints extra logs. 
  16. Handy for debugging.
  17. **`use_persistent_context`**:
  18. If `True`, uses a **persistent** browser profile, storing cookies/local storage across runs. 
  19. Typically also set `user_data_dir` to point to a folder.
  20. **`cookies`** & **`headers`**:
  21. If you want to start with specific cookies or add universal HTTP headers, set them here. 
  22. E.g. `cookies=[{"name": "session", "value": "abc123", "domain": "example.com"}]`.
  23. **`user_agent`**:
  24. Custom User-Agent string. If `None`, a default is used. 
  25. You can also set `user_agent_mode="random"` for randomization (if you want to fight bot detection).
  26. **`text_mode`** & **`light_mode`**:
  27. `text_mode=True` disables images, possibly speeding up text-only crawls. 
  28. `light_mode=True` turns off certain background features for performance. 
  29. **`extra_args`**:
     * Additional flags for the underlying browser. 
     * E.g. `["--disable-extensions"]`.


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
Copy
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
Copy
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
    capture_mhtml=False,
    # Location and Identity Parameters
    locale=None,      # e.g. "en-US", "fr-FR"
    timezone_id=None,    # e.g. "America/New_York"
    geolocation=None,    # GeolocationConfig object
    # Resource Management
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
Copy
```

### Key Fields to Note
  1. **`word_count_threshold`**:
  2. The minimum word count before a block is considered. 
  3. If your site has lots of short paragraphs or items, you can lower it.
  4. **`extraction_strategy`**:
  5. Where you plug in JSON-based extraction (CSS, LLM, etc.). 
  6. If `None`, no structured extraction is done (only raw/cleaned HTML + markdown).
  7. **`markdown_generator`**:
  8. E.g., `DefaultMarkdownGenerator(...)`, controlling how HTML→Markdown conversion is done. 
  9. If `None`, a default approach is used.
  10. **`cache_mode`**:
  11. Controls caching behavior (`ENABLED`, `BYPASS`, `DISABLED`, etc.). 
  12. If `None`, defaults to some level of caching or you can specify `CacheMode.ENABLED`.
  13. **`js_code`**:
  14. A string or list of JS strings to execute. 
  15. Great for "Load More" buttons or user interactions. 
  16. **`wait_for`**:
  17. A CSS or JS expression to wait for before extracting content. 
  18. Common usage: `wait_for="css:.main-loaded"` or `wait_for="js:() => window.loaded === true"`.
  19. **`screenshot`**,**`pdf`**, & **`capture_mhtml`**:
  20. If `True`, captures a screenshot, PDF, or MHTML snapshot after the page is fully loaded. 
  21. The results go to `result.screenshot` (base64), `result.pdf` (bytes), or `result.mhtml` (string).
  22. **Location Parameters** : 
  23. **`locale`**: Browser's locale (e.g.,`"en-US"` , `"fr-FR"`) for language preferences
  24. **`timezone_id`**: Browser's timezone (e.g.,`"America/New_York"` , `"Europe/Paris"`)
  25. **`geolocation`**: GPS coordinates via`GeolocationConfig(latitude=48.8566, longitude=2.3522)`
  26. See [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/#7-locale-timezone-and-geolocation-control)
  27. **`verbose`**:
  28. Logs additional runtime details. 
  29. Overlaps with the browser's verbosity if also set to `True` in `BrowserConfig`.
  30. **`enable_rate_limiting`**:
  31. If `True`, enables rate limiting for batch processing. 
  32. Requires `rate_limit_config` to be set.
  33. **`memory_threshold_percent`**:
     * The memory threshold (as a percentage) to monitor. 
     * If exceeded, the crawler will pause or slow down.
  34. **`check_interval`**:
     * The interval (in seconds) to check system resources. 
     * Affects how often memory and CPU usage are monitored.
  35. **`max_session_permit`**:
     * The maximum number of concurrent crawl sessions. 
     * Helps prevent overwhelming the system.
  36. **`display_mode`**:
     * The display mode for progress information (`DETAILED`, `BRIEF`, etc.). 
     * Affects how much information is printed during the crawl.


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
Copy
```

The `clone()` method: - Creates a new instance with all the same settings - Updates only the specified parameters - Leaves the original configuration unchanged - Perfect for creating variations without repeating all parameters
## 3. LLMConfig Essentials
### Key fields to note
  1. **`provider`**:
  2. Which LLM provoder to use. 
  3. Possible values are `"ollama/llama3","groq/llama3-70b-8192","groq/llama3-8b-8192", "openai/gpt-4o-mini" ,"openai/gpt-4o","openai/o1-mini","openai/o1-preview","openai/o3-mini","openai/o3-mini-high","anthropic/claude-3-haiku-20240307","anthropic/claude-3-opus-20240229","anthropic/claude-3-sonnet-20240229","anthropic/claude-3-5-sonnet-20240620","gemini/gemini-pro","gemini/gemini-1.5-pro","gemini/gemini-2.0-flash","gemini/gemini-2.0-flash-exp","gemini/gemini-2.0-flash-lite-preview-02-05","deepseek/deepseek-chat"`_(default:`"openai/gpt-4o-mini"`)_
  4. **`api_token`**:
     * Optional. When not provided explicitly, api_token will be read from environment variables based on provider. For example: If a gemini model is passed as provider then,`"GEMINI_API_KEY"` will be read from environment variables 
     * API token of LLM provider eg: `api_token = "gsk_1ClHGGJ7Lpn4WGybR7vNWGdyb3FY7zXEw3SCiy0BAVM9lL8CQv"`
     * Environment variable - use with prefix "env:" eg:`api_token = "env: GROQ_API_KEY"`
  5. **`base_url`**:
  6. If your provider has a custom endpoint


```
llm_config = LLMConfig(provider="openai/gpt-4o-mini", api_token=os.getenv("OPENAI_API_KEY"))
Copy
```

## 4. Putting It All Together
In a typical scenario, you define **one** `BrowserConfig` for your crawler session, then create **one or more** `CrawlerRunConfig` & `LLMConfig` depending on each call's needs:
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
Copy
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
#### On this page
  * [1. BrowserConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config/#1-browserconfig-essentials)
  * [Key Fields to Note](https://docs.crawl4ai.com/core/browser-crawler-config/#key-fields-to-note)
  * [Helper Methods](https://docs.crawl4ai.com/core/browser-crawler-config/#helper-methods)
  * [2. CrawlerRunConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config/#2-crawlerrunconfig-essentials)
  * [Key Fields to Note](https://docs.crawl4ai.com/core/browser-crawler-config/#key-fields-to-note_1)
  * [Helper Methods](https://docs.crawl4ai.com/core/browser-crawler-config/#helper-methods_1)
  * [3. LLMConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config/#3-llmconfig-essentials)
  * [Key fields to note](https://docs.crawl4ai.com/core/browser-crawler-config/#key-fields-to-note_2)
  * [4. Putting It All Together](https://docs.crawl4ai.com/core/browser-crawler-config/#4-putting-it-all-together)
  * [5. Next Steps](https://docs.crawl4ai.com/core/browser-crawler-config/#5-next-steps)
  * [6. Conclusion](https://docs.crawl4ai.com/core/browser-crawler-config/#6-conclusion)


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/core/ask-ai/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * Ask AI
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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


> Feedback 
##### Search
xClose
Type to start searching

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/core/cli/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * Command Line Interface
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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


  * [Crawl4AI CLI Guide](https://docs.crawl4ai.com/core/cli/#crawl4ai-cli-guide)
  * [Table of Contents](https://docs.crawl4ai.com/core/cli/#table-of-contents)
  * [Basic Usage](https://docs.crawl4ai.com/core/cli/#basic-usage)
  * [Quick Example of Advanced Usage](https://docs.crawl4ai.com/core/cli/#quick-example-of-advanced-usage)
  * [Configuration](https://docs.crawl4ai.com/core/cli/#configuration)
  * [Advanced Features](https://docs.crawl4ai.com/core/cli/#advanced-features)
  * [Output Formats](https://docs.crawl4ai.com/core/cli/#output-formats)
  * [Complete Examples](https://docs.crawl4ai.com/core/cli/#complete-examples)
  * [Best Practices & Tips](https://docs.crawl4ai.com/core/cli/#best-practices-tips)
  * [Recap](https://docs.crawl4ai.com/core/cli/#recap)


# Crawl4AI CLI Guide
## Table of Contents
  * [Installation](https://docs.crawl4ai.com/core/cli/#installation)
  * [Basic Usage](https://docs.crawl4ai.com/core/cli/#basic-usage)
  * [Configuration](https://docs.crawl4ai.com/core/cli/#configuration)
  * [Browser Configuration](https://docs.crawl4ai.com/core/cli/#browser-configuration)
  * [Crawler Configuration](https://docs.crawl4ai.com/core/cli/#crawler-configuration)
  * [Extraction Configuration](https://docs.crawl4ai.com/core/cli/#extraction-configuration)
  * [Content Filtering](https://docs.crawl4ai.com/core/cli/#content-filtering)
  * [Advanced Features](https://docs.crawl4ai.com/core/cli/#advanced-features)
  * [LLM Q&A](https://docs.crawl4ai.com/core/cli/#llm-qa)
  * [Structured Data Extraction](https://docs.crawl4ai.com/core/cli/#structured-data-extraction)
  * [Content Filtering](https://docs.crawl4ai.com/core/cli/#content-filtering-1)
  * [Output Formats](https://docs.crawl4ai.com/core/cli/#output-formats)
  * [Examples](https://docs.crawl4ai.com/core/cli/#examples)
  * [Configuration Reference](https://docs.crawl4ai.com/core/cli/#configuration-reference)
  * [Best Practices & Tips](https://docs.crawl4ai.com/core/cli/#best-practices--tips)


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
Copy
```

## Quick Example of Advanced Usage
If you clone the repository and run the following command, you will receive the content of the page in JSON format according to a JSON-CSS schema:
```
crwl "https://www.infoq.com/ai-ml-data-eng/" -e docs/examples/cli/extract_css.yml -s docs/examples/cli/css_schema.json -o json;
Copy
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
Copy
```

```
# Using config file
crwl https://example.com -B browser.yml
# Using direct parameters
crwl https://example.com -b "headless=true,viewport_width=1280,user_agent_mode=random"
Copy
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
Copy
```

```
# Using config file
crwl https://example.com -C crawler.yml
# Using direct parameters
crwl https://example.com -c "css_selector=#main,delay_before_return_html=2,scan_full_page=true"
Copy
```

### Extraction Configuration
Two types of extraction are supported:
  1. CSS/XPath-based extraction: 
```
# extract_css.yml
type: "json-css"
params:
 verbose: true
Copy
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
Copy
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
Copy
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
Copy
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
Copy
```

First-time setup: - Prompts for LLM provider and API token - Saves configuration in `~/.crawl4ai/global.yml` - Supports various providers (openai/gpt-4, anthropic/claude-3-sonnet, etc.) - For case of `ollama` you do not need to provide API token. - See [LiteLLM Providers](https://docs.litellm.ai/docs/providers) for full list
### Structured Data Extraction
Extract structured data using CSS selectors:
```
crwl https://example.com \
  -e extract_css.yml \
  -s css_schema.json \
  -o json
Copy
```

Or using LLM-based extraction:
```
crwl https://example.com \
  -e extract_llm.yml \
  -s llm_schema.json \
  -o json
Copy
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
Copy
```

```
crwl https://example.com -f filter_bm25.yml -o markdown-fit
Copy
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
Copy
```

  2. Structured Data Extraction: 
```
crwl https://example.com \
  -e extract_css.yml \
  -s css_schema.json \
  -o json \
  -v
Copy
```

  3. LLM Extraction with Filtering: 
```
crwl https://example.com \
  -B browser.yml \
  -e extract_llm.yml \
  -s llm_schema.json \
  -f filter_bm25.yml \
  -o json
Copy
```

  4. Interactive Q&A: 
```
# First crawl and view
crwl https://example.com -o markdown
# Then ask questions
crwl https://example.com -q "What are the main points?"
crwl https://example.com -q "Summarize the conclusions"
Copy
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
#### On this page
  * [Table of Contents](https://docs.crawl4ai.com/core/cli/#table-of-contents)
  * [Basic Usage](https://docs.crawl4ai.com/core/cli/#basic-usage)
  * [Quick Example of Advanced Usage](https://docs.crawl4ai.com/core/cli/#quick-example-of-advanced-usage)
  * [Configuration](https://docs.crawl4ai.com/core/cli/#configuration)
  * [Browser Configuration](https://docs.crawl4ai.com/core/cli/#browser-configuration)
  * [Crawler Configuration](https://docs.crawl4ai.com/core/cli/#crawler-configuration)
  * [Extraction Configuration](https://docs.crawl4ai.com/core/cli/#extraction-configuration)
  * [Advanced Features](https://docs.crawl4ai.com/core/cli/#advanced-features)
  * [LLM Q&A](https://docs.crawl4ai.com/core/cli/#llm-qa)
  * [Structured Data Extraction](https://docs.crawl4ai.com/core/cli/#structured-data-extraction)
  * [Content Filtering](https://docs.crawl4ai.com/core/cli/#content-filtering)
  * [Output Formats](https://docs.crawl4ai.com/core/cli/#output-formats)
  * [Complete Examples](https://docs.crawl4ai.com/core/cli/#complete-examples)
  * [Best Practices & Tips](https://docs.crawl4ai.com/core/cli/#best-practices-tips)
  * [Recap](https://docs.crawl4ai.com/core/cli/#recap)


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/core/examples/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Code Examples
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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


  * [Code Examples](https://docs.crawl4ai.com/core/examples/#code-examples)
  * [Getting Started Examples](https://docs.crawl4ai.com/core/examples/#getting-started-examples)
  * [Browser & Crawling Features](https://docs.crawl4ai.com/core/examples/#browser-crawling-features)
  * [Advanced Crawling & Deep Crawling](https://docs.crawl4ai.com/core/examples/#advanced-crawling-deep-crawling)
  * [Extraction Strategies](https://docs.crawl4ai.com/core/examples/#extraction-strategies)
  * [E-commerce & Specialized Crawling](https://docs.crawl4ai.com/core/examples/#e-commerce-specialized-crawling)
  * [Customization & Security](https://docs.crawl4ai.com/core/examples/#customization-security)
  * [Docker & Deployment](https://docs.crawl4ai.com/core/examples/#docker-deployment)
  * [Application Examples](https://docs.crawl4ai.com/core/examples/#application-examples)
  * [Content Generation & Markdown](https://docs.crawl4ai.com/core/examples/#content-generation-markdown)
  * [Running the Examples](https://docs.crawl4ai.com/core/examples/#running-the-examples)
  * [Contributing New Examples](https://docs.crawl4ai.com/core/examples/#contributing-new-examples)


# Code Examples
This page provides a comprehensive list of example scripts that demonstrate various features and capabilities of Crawl4AI. Each example is designed to showcase specific functionality, making it easier for you to understand how to implement these features in your own projects.
## Getting Started Examples
Example | Description | Link  
---|---|---  
Hello World | A simple introductory example demonstrating basic usage of AsyncWebCrawler with JavaScript execution and content filtering. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/hello_world.py)  
Quickstart | A comprehensive collection of examples showcasing various features including basic crawling, content cleaning, link analysis, JavaScript execution, CSS selectors, media handling, custom hooks, proxy configuration, screenshots, and multiple extraction strategies. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/quickstart.py)  
Quickstart Set 1 | Basic examples for getting started with Crawl4AI. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/quickstart_examples_set_1.py)  
Quickstart Set 2 | More advanced examples for working with Crawl4AI. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/quickstart_examples_set_2.py)  
## Browser & Crawling Features
Example | Description | Link  
---|---|---  
Built-in Browser | Demonstrates how to use the built-in browser capabilities. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/builtin_browser_example.py)  
Browser Optimization | Focuses on browser performance optimization techniques. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/browser_optimization_example.py)  
arun vs arun_many | Compares the `arun` and `arun_many` methods for single vs. multiple URL crawling. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/arun_vs_arun_many.py)  
Multiple URLs | Shows how to crawl multiple URLs asynchronously. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/async_webcrawler_multiple_urls_example.py)  
Page Interaction | Guide on interacting with dynamic elements through clicks. | [View Guide](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/tutorial_dynamic_clicks.md)  
Crawler Monitor | Shows how to monitor the crawler's activities and status. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/crawler_monitor_example.py)  
Full Page Screenshot & PDF | Guide on capturing full-page screenshots and PDFs from massive webpages. | [View Guide](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/full_page_screenshot_and_pdf_export.md)  
## Advanced Crawling & Deep Crawling
Example | Description | Link  
---|---|---  
Deep Crawling | An extensive tutorial on deep crawling capabilities, demonstrating BFS and BestFirst strategies, stream vs. non-stream execution, filters, scorers, and advanced configurations. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/deepcrawl_example.py)  
Dispatcher | Shows how to use the crawl dispatcher for advanced workload management. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/dispatcher_example.py)  
Storage State | Tutorial on managing browser storage state for persistence. | [View Guide](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/storage_state_tutorial.md)  
Network Console Capture | Demonstrates how to capture and analyze network requests and console logs. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/network_console_capture_example.py)  
## Extraction Strategies
Example | Description | Link  
---|---|---  
Extraction Strategies | Demonstrates different extraction strategies with various input formats (markdown, HTML, fit_markdown) and JSON-based extractors (CSS and XPath). | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/extraction_strategies_examples.py)  
Scraping Strategies | Compares the performance of different scraping strategies. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/scraping_strategies_performance.py)  
LLM Extraction | Demonstrates LLM-based extraction specifically for OpenAI pricing data. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/llm_extraction_openai_pricing.py)  
LLM Markdown | Shows how to use LLMs to generate markdown from crawled content. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/llm_markdown_generator.py)  
Summarize Page | Shows how to summarize web page content. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/summarize_page.py)  
## E-commerce & Specialized Crawling
Example | Description | Link  
---|---|---  
Amazon Product Extraction | Demonstrates how to extract structured product data from Amazon search results using CSS selectors. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/amazon_product_extraction_direct_url.py)  
Amazon with Hooks | Shows how to use hooks with Amazon product extraction. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/amazon_product_extraction_using_hooks.py)  
Amazon with JavaScript | Demonstrates using custom JavaScript for Amazon product extraction. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/amazon_product_extraction_using_use_javascript.py)  
Crypto Analysis | Demonstrates how to crawl and analyze cryptocurrency data. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/crypto_analysis_example.py)  
SERP API | Demonstrates using Crawl4AI with search engine result pages. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/serp_api_project_11_feb.py)  
## Customization & Security
Example | Description | Link  
---|---|---  
Hooks | Illustrates how to use hooks at different stages of the crawling process for advanced customization. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/hooks_example.py)  
Identity-Based Browsing | Illustrates identity-based browsing configurations for authentic browsing experiences. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/identity_based_browsing.py)  
Proxy Rotation | Shows how to use proxy rotation for web scraping and avoiding IP blocks. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/proxy_rotation_demo.py)  
SSL Certificate | Illustrates SSL certificate handling and verification. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/ssl_example.py)  
Language Support | Shows how to handle different languages during crawling. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/language_support_example.py)  
Geolocation | Demonstrates how to use geolocation features. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/use_geo_location.py)  
## Docker & Deployment
Example | Description | Link  
---|---|---  
Docker Config | Demonstrates how to create and use Docker configuration objects. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/docker_config_obj.py)  
Docker Basic | A test suite for Docker deployment, showcasing various functionalities through the Docker API. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/docker_example.py)  
Docker REST API | Shows how to interact with Crawl4AI Docker using REST API calls. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/docker_python_rest_api.py)  
Docker SDK | Demonstrates using the Python SDK for Crawl4AI Docker. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/docker_python_sdk.py)  
## Application Examples
Example | Description | Link  
---|---|---  
Research Assistant | Demonstrates how to build a research assistant using Crawl4AI. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/research_assistant.py)  
REST Call | Shows how to make REST API calls with Crawl4AI. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/rest_call.py)  
Chainlit Integration | Shows how to integrate Crawl4AI with Chainlit. | [View Guide](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/chainlit.md)  
Crawl4AI vs FireCrawl | Compares Crawl4AI with the FireCrawl library. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/crawlai_vs_firecrawl.py)  
## Content Generation & Markdown
Example | Description | Link  
---|---|---  
Content Source | Demonstrates how to work with different content sources in markdown generation. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/markdown/content_source_example.py)  
Content Source (Short) | A simplified version of content source usage. | [View Code](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/markdown/content_source_short_example.py)  
Built-in Browser Guide | Guide for using the built-in browser capabilities. | [View Guide](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/README_BUILTIN_BROWSER.md)  
## Running the Examples
To run any of these examples, you'll need to have Crawl4AI installed:
```
pip install crawl4ai
Copy
```

Then, you can run an example script like this:
```
python -m docs.examples.hello_world
Copy
```

For examples that require additional dependencies or environment variables, refer to the comments at the top of each file.
Some examples may require: - API keys (for LLM-based examples) - Docker setup (for Docker-related examples) - Additional dependencies (specified in the example files)
## Contributing New Examples
If you've created an interesting example that demonstrates a unique use case or feature of Crawl4AI, we encourage you to contribute it to our examples collection. Please see our [contribution guidelines](https://github.com/unclecode/crawl4ai/blob/main/CONTRIBUTORS.md) for more information.
#### On this page
  * [Getting Started Examples](https://docs.crawl4ai.com/core/examples/#getting-started-examples)
  * [Browser & Crawling Features](https://docs.crawl4ai.com/core/examples/#browser-crawling-features)
  * [Advanced Crawling & Deep Crawling](https://docs.crawl4ai.com/core/examples/#advanced-crawling-deep-crawling)
  * [Extraction Strategies](https://docs.crawl4ai.com/core/examples/#extraction-strategies)
  * [E-commerce & Specialized Crawling](https://docs.crawl4ai.com/core/examples/#e-commerce-specialized-crawling)
  * [Customization & Security](https://docs.crawl4ai.com/core/examples/#customization-security)
  * [Docker & Deployment](https://docs.crawl4ai.com/core/examples/#docker-deployment)
  * [Application Examples](https://docs.crawl4ai.com/core/examples/#application-examples)
  * [Content Generation & Markdown](https://docs.crawl4ai.com/core/examples/#content-generation-markdown)
  * [Running the Examples](https://docs.crawl4ai.com/core/examples/#running-the-examples)
  * [Contributing New Examples](https://docs.crawl4ai.com/core/examples/#contributing-new-examples)


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/core/installation/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * Installation
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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


  * [Installation & Setup (2023 Edition)](https://docs.crawl4ai.com/core/installation/#installation-setup-2023-edition)
  * [1. Basic Installation](https://docs.crawl4ai.com/core/installation/#1-basic-installation)
  * [2. Initial Setup & Diagnostics](https://docs.crawl4ai.com/core/installation/#2-initial-setup-diagnostics)
  * [3. Verifying Installation: A Simple Crawl (Skip this step if you already run crawl4ai-doctor)](https://docs.crawl4ai.com/core/installation/#3-verifying-installation-a-simple-crawl-skip-this-step-if-you-already-run-crawl4ai-doctor)
  * [4. Advanced Installation (Optional)](https://docs.crawl4ai.com/core/installation/#4-advanced-installation-optional)
  * [5. Docker (Experimental)](https://docs.crawl4ai.com/core/installation/#5-docker-experimental)
  * [6. Local Server Mode (Legacy)](https://docs.crawl4ai.com/core/installation/#6-local-server-mode-legacy)
  * [Summary](https://docs.crawl4ai.com/core/installation/#summary)


# Installation & Setup (2023 Edition)
## 1. Basic Installation
```
pip install crawl4ai
Copy
```

This installs the **core** Crawl4AI library along with essential dependencies. **No** advanced features (like transformers or PyTorch) are included yet.
## 2. Initial Setup & Diagnostics
### 2.1 Run the Setup Command
After installing, call:
```
crawl4ai-setup
Copy
```

**What does it do?** - Installs or updates required Playwright browsers (Chromium, Firefox, etc.) - Performs OS-level checks (e.g., missing libs on Linux) - Confirms your environment is ready to crawl
### 2.2 Diagnostics
Optionally, you can run **diagnostics** to confirm everything is functioning:
```
crawl4ai-doctor
Copy
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
Copy
```

**Expected** outcome: - A headless browser session loads `example.com` - Crawl4AI returns ~300 characters of markdown. If errors occur, rerun `crawl4ai-doctor` or manually ensure Playwright is installed correctly.
## 4. Advanced Installation (Optional)
**Warning** : Only install these **if you truly need them**. They bring in larger dependencies, including big models, which can increase disk usage and memory load significantly.
### 4.1 Torch, Transformers, or All
  * **Text Clustering (Torch)**
```
pip install crawl4ai[torch]
crawl4ai-setup
Copy
```

Installs PyTorch-based features (e.g., cosine similarity or advanced semantic chunking). 
  * **Transformers**
```
pip install crawl4ai[transformer]
crawl4ai-setup
Copy
```

Adds Hugging Face-based summarization or generation strategies. 
  * **All Features**
```
pip install crawl4ai[all]
crawl4ai-setup
Copy
```



#### (Optional) Pre-Fetching Models
```
crawl4ai-download-models
Copy
```

This step caches large models locally (if needed). **Only do this** if your workflow requires them. 
## 5. Docker (Experimental)
We provide a **temporary** Docker approach for testing. **It’s not stable and may break** with future releases. We plan a major Docker revamp in a future stable version, 2025 Q1. If you still want to try:
```
docker pull unclecode/crawl4ai:basic
docker run -p 11235:11235 unclecode/crawl4ai:basic
Copy
```

You can then make POST requests to `http://localhost:11235/crawl` to perform crawls. **Production usage** is discouraged until our new Docker approach is ready (planned in Jan or Feb 2025).
## 6. Local Server Mode (Legacy)
Some older docs mention running Crawl4AI as a local server. This approach has been **partially replaced** by the new Docker-based prototype and upcoming stable server release. You can experiment, but expect major changes. Official local server instructions will arrive once the new Docker architecture is finalized.
## Summary
1. **Install** with `pip install crawl4ai` and run `crawl4ai-setup`. 2. **Diagnose** with `crawl4ai-doctor` if you see errors. 3. **Verify** by crawling `example.com` with minimal `BrowserConfig` + `CrawlerRunConfig`. 4. **Advanced** features (Torch, Transformers) are **optional** —avoid them if you don’t need them (they significantly increase resource usage). 5. **Docker** is **experimental** —use at your own risk until the stable version is released. 6. **Local server** references in older docs are largely deprecated; a new solution is in progress.
**Got questions?** Check [GitHub issues](https://github.com/unclecode/crawl4ai/issues) for updates or ask the community!
#### On this page
  * [1. Basic Installation](https://docs.crawl4ai.com/core/installation/#1-basic-installation)
  * [2. Initial Setup & Diagnostics](https://docs.crawl4ai.com/core/installation/#2-initial-setup-diagnostics)
  * [2.1 Run the Setup Command](https://docs.crawl4ai.com/core/installation/#21-run-the-setup-command)
  * [2.2 Diagnostics](https://docs.crawl4ai.com/core/installation/#22-diagnostics)
  * [3. Verifying Installation: A Simple Crawl (Skip this step if you already run crawl4ai-doctor)](https://docs.crawl4ai.com/core/installation/#3-verifying-installation-a-simple-crawl-skip-this-step-if-you-already-run-crawl4ai-doctor)
  * [4. Advanced Installation (Optional)](https://docs.crawl4ai.com/core/installation/#4-advanced-installation-optional)
  * [4.1 Torch, Transformers, or All](https://docs.crawl4ai.com/core/installation/#41-torch-transformers-or-all)
  * [(Optional) Pre-Fetching Models](https://docs.crawl4ai.com/core/installation/#optional-pre-fetching-models)
  * [5. Docker (Experimental)](https://docs.crawl4ai.com/core/installation/#5-docker-experimental)
  * [6. Local Server Mode (Legacy)](https://docs.crawl4ai.com/core/installation/#6-local-server-mode-legacy)
  * [Summary](https://docs.crawl4ai.com/core/installation/#summary)


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/core/crawler-result/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * Crawler Result
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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


  * [Crawl Result and Output](https://docs.crawl4ai.com/core/crawler-result/#crawl-result-and-output)
  * [1. The CrawlResult Model](https://docs.crawl4ai.com/core/crawler-result/#1-the-crawlresult-model)
  * [2. HTML Variants](https://docs.crawl4ai.com/core/crawler-result/#2-html-variants)
  * [3. Markdown Generation](https://docs.crawl4ai.com/core/crawler-result/#3-markdown-generation)
  * [4. Structured Extraction: extracted_content](https://docs.crawl4ai.com/core/crawler-result/#4-structured-extraction-extracted_content)
  * [5. More Fields: Links, Media, and More](https://docs.crawl4ai.com/core/crawler-result/#5-more-fields-links-media-and-more)
  * [6. Accessing These Fields](https://docs.crawl4ai.com/core/crawler-result/#6-accessing-these-fields)
  * [7. Next Steps](https://docs.crawl4ai.com/core/crawler-result/#7-next-steps)


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
  mhtml: Optional[str] = None
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
Copy
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
**mhtml (`Optional[str]`)** | MHTML snapshot of the page if `capture_mhtml=True`. Contains the full page with all resources.  
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
Copy
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
Copy
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
Copy
```

Here: - `url="raw://..."` passes the HTML content directly, no network requests. - The **CSS** extraction strategy populates `result.extracted_content` with the JSON array `[{"title": "...", "link": "..."}]`.
## 5. More Fields: Links, Media, and More
### 5.1 `links`
A dictionary, typically with `"internal"` and `"external"` lists. Each entry might have `href`, `text`, `title`, etc. This is automatically captured if you haven’t disabled link extraction.
```
print(result.links["internal"][:3]) # Show first 3 internal links
Copy
```

### 5.2 `media`
Similarly, a dictionary with `"images"`, `"audio"`, `"video"`, etc. Each item could include `src`, `alt`, `score`, and more, if your crawler is set to gather them.
```
images = result.media.get("images", [])
for img in images:
  print("Image URL:", img["src"], "Alt:", img.get("alt"))
Copy
```

### 5.3 `screenshot`, `pdf`, and `mhtml`
If you set `screenshot=True`, `pdf=True`, or `capture_mhtml=True` in **`CrawlerRunConfig`**, then:
  * `result.screenshot` contains a base64-encoded PNG string.
  * `result.pdf` contains raw PDF bytes (you can write them to a file).
  * `result.mhtml` contains the MHTML snapshot of the page as a string (you can write it to a .mhtml file).


```
# Save the PDF
with open("page.pdf", "wb") as f:
  f.write(result.pdf)
# Save the MHTML
if result.mhtml:
  with open("page.mhtml", "w", encoding="utf-8") as f:
    f.write(result.mhtml)
Copy
```

The MHTML (MIME HTML) format is particularly useful as it captures the entire web page including all of its resources (CSS, images, scripts, etc.) in a single file, making it perfect for archiving or offline viewing.
### 5.4 `ssl_certificate`
If `fetch_ssl_certificate=True`, `result.ssl_certificate` holds details about the site’s SSL cert, such as issuer, validity dates, etc.
## 6. Accessing These Fields
After you run:
```
result = await crawler.arun(url="https://example.com", config=some_config)
Copy
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
Copy
```

**Deprecation** : Since v0.5 `result.markdown_v2`, `result.fit_html`,`result.fit_markdown` are deprecated. Use `result.markdown` instead! It holds `MarkdownGenerationResult`, which includes `fit_html` and `fit_markdown` as it's properties.
## 7. Next Steps
  * **Markdown Generation** : Dive deeper into how to configure `DefaultMarkdownGenerator` and various filters. 
  * **Content Filtering** : Learn how to use `BM25ContentFilter` and `PruningContentFilter`.
  * **Session & Hooks**: If you want to manipulate the page or preserve state across multiple `arun()` calls, see the hooking or session docs. 
  * **LLM Extraction** : For complex or unstructured content requiring AI-driven parsing, check the LLM-based strategies doc.


**Enjoy** exploring all that `CrawlResult` offers—whether you need raw HTML, sanitized output, markdown, or fully structured data, Crawl4AI has you covered!
#### On this page
  * [1. The CrawlResult Model](https://docs.crawl4ai.com/core/crawler-result/#1-the-crawlresult-model)
  * [Table: Key Fields in CrawlResult](https://docs.crawl4ai.com/core/crawler-result/#table-key-fields-in-crawlresult)
  * [2. HTML Variants](https://docs.crawl4ai.com/core/crawler-result/#2-html-variants)
  * [html: Raw HTML](https://docs.crawl4ai.com/core/crawler-result/#html-raw-html)
  * [cleaned_html: Sanitized](https://docs.crawl4ai.com/core/crawler-result/#cleaned_html-sanitized)
  * [3. Markdown Generation](https://docs.crawl4ai.com/core/crawler-result/#3-markdown-generation)
  * [3.1 markdown](https://docs.crawl4ai.com/core/crawler-result/#31-markdown)
  * [3.2 Basic Example with a Markdown Generator](https://docs.crawl4ai.com/core/crawler-result/#32-basic-example-with-a-markdown-generator)
  * [4. Structured Extraction: extracted_content](https://docs.crawl4ai.com/core/crawler-result/#4-structured-extraction-extracted_content)
  * [Example: CSS Extraction with raw:// HTML](https://docs.crawl4ai.com/core/crawler-result/#example-css-extraction-with-raw-html)
  * [5. More Fields: Links, Media, and More](https://docs.crawl4ai.com/core/crawler-result/#5-more-fields-links-media-and-more)
  * [5.1 links](https://docs.crawl4ai.com/core/crawler-result/#51-links)
  * [5.2 media](https://docs.crawl4ai.com/core/crawler-result/#52-media)
  * [5.3 screenshot, pdf, and mhtml](https://docs.crawl4ai.com/core/crawler-result/#53-screenshot-pdf-and-mhtml)
  * [5.4 ssl_certificate](https://docs.crawl4ai.com/core/crawler-result/#54-ssl_certificate)
  * [6. Accessing These Fields](https://docs.crawl4ai.com/core/crawler-result/#6-accessing-these-fields)
  * [7. Next Steps](https://docs.crawl4ai.com/core/crawler-result/#7-next-steps)


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/core/llmtxt/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * LLM Context
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/core/deep-crawling/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * Deep Crawling
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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


  * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/#deep-crawling)
  * [1. Quick Example](https://docs.crawl4ai.com/core/deep-crawling/#1-quick-example)
  * [2. Understanding Deep Crawling Strategy Options](https://docs.crawl4ai.com/core/deep-crawling/#2-understanding-deep-crawling-strategy-options)
  * [3. Streaming vs. Non-Streaming Results](https://docs.crawl4ai.com/core/deep-crawling/#3-streaming-vs-non-streaming-results)
  * [4. Filtering Content with Filter Chains](https://docs.crawl4ai.com/core/deep-crawling/#4-filtering-content-with-filter-chains)
  * [5. Using Scorers for Prioritized Crawling](https://docs.crawl4ai.com/core/deep-crawling/#5-using-scorers-for-prioritized-crawling)
  * [6. Advanced Filtering Techniques](https://docs.crawl4ai.com/core/deep-crawling/#6-advanced-filtering-techniques)
  * [7. Building a Complete Advanced Crawler](https://docs.crawl4ai.com/core/deep-crawling/#7-building-a-complete-advanced-crawler)
  * [8. Limiting and Controlling Crawl Size](https://docs.crawl4ai.com/core/deep-crawling/#8-limiting-and-controlling-crawl-size)
  * [9. Common Pitfalls & Tips](https://docs.crawl4ai.com/core/deep-crawling/#9-common-pitfalls-tips)
  * [10. Summary & Next Steps](https://docs.crawl4ai.com/core/deep-crawling/#10-summary-next-steps)


# Deep Crawling
One of Crawl4AI's most powerful features is its ability to perform **configurable deep crawling** that can explore websites beyond a single page. With fine-tuned control over crawl depth, domain boundaries, and content filtering, Crawl4AI gives you the tools to extract precisely the content you need.
In this tutorial, you'll learn:
  1. How to set up a **Basic Deep Crawler** with BFS strategy 
  2. Understanding the difference between **streamed and non-streamed** output 
  3. Implementing **filters and scorers** to target specific content 
  4. Creating **advanced filtering chains** for sophisticated crawls 
  5. Using **BestFirstCrawling** for intelligent exploration prioritization 


> **Prerequisites** - You’ve completed or read [AsyncWebCrawler Basics](https://docs.crawl4ai.com/core/simple-crawling/) to understand how to run a simple crawl. - You know how to configure `CrawlerRunConfig`.
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
#### On this page
  * [1. Quick Example](https://docs.crawl4ai.com/core/deep-crawling/#1-quick-example)
  * [2. Understanding Deep Crawling Strategy Options](https://docs.crawl4ai.com/core/deep-crawling/#2-understanding-deep-crawling-strategy-options)
  * [2.1 BFSDeepCrawlStrategy (Breadth-First Search)](https://docs.crawl4ai.com/core/deep-crawling/#21-bfsdeepcrawlstrategy-breadth-first-search)
  * [2.2 DFSDeepCrawlStrategy (Depth-First Search)](https://docs.crawl4ai.com/core/deep-crawling/#22-dfsdeepcrawlstrategy-depth-first-search)
  * [2.3 BestFirstCrawlingStrategy (⭐️ - Recommended Deep crawl strategy)](https://docs.crawl4ai.com/core/deep-crawling/#23-bestfirstcrawlingstrategy-recommended-deep-crawl-strategy)
  * [3. Streaming vs. Non-Streaming Results](https://docs.crawl4ai.com/core/deep-crawling/#3-streaming-vs-non-streaming-results)
  * [3.1 Non-Streaming Mode (Default)](https://docs.crawl4ai.com/core/deep-crawling/#31-non-streaming-mode-default)
  * [3.2 Streaming Mode](https://docs.crawl4ai.com/core/deep-crawling/#32-streaming-mode)
  * [4. Filtering Content with Filter Chains](https://docs.crawl4ai.com/core/deep-crawling/#4-filtering-content-with-filter-chains)
  * [4.1 Basic URL Pattern Filter](https://docs.crawl4ai.com/core/deep-crawling/#41-basic-url-pattern-filter)
  * [4.2 Combining Multiple Filters](https://docs.crawl4ai.com/core/deep-crawling/#42-combining-multiple-filters)
  * [4.3 Available Filter Types](https://docs.crawl4ai.com/core/deep-crawling/#43-available-filter-types)
  * [5. Using Scorers for Prioritized Crawling](https://docs.crawl4ai.com/core/deep-crawling/#5-using-scorers-for-prioritized-crawling)
  * [5.1 KeywordRelevanceScorer](https://docs.crawl4ai.com/core/deep-crawling/#51-keywordrelevancescorer)
  * [6. Advanced Filtering Techniques](https://docs.crawl4ai.com/core/deep-crawling/#6-advanced-filtering-techniques)
  * [6.1 SEO Filter for Quality Assessment](https://docs.crawl4ai.com/core/deep-crawling/#61-seo-filter-for-quality-assessment)
  * [6.2 Content Relevance Filter](https://docs.crawl4ai.com/core/deep-crawling/#62-content-relevance-filter)
  * [7. Building a Complete Advanced Crawler](https://docs.crawl4ai.com/core/deep-crawling/#7-building-a-complete-advanced-crawler)
  * [8. Limiting and Controlling Crawl Size](https://docs.crawl4ai.com/core/deep-crawling/#8-limiting-and-controlling-crawl-size)
  * [8.1 Using max_pages](https://docs.crawl4ai.com/core/deep-crawling/#81-using-max_pages)
  * [8.2 Using score_threshold](https://docs.crawl4ai.com/core/deep-crawling/#82-using-score_threshold)
  * [9. Common Pitfalls & Tips](https://docs.crawl4ai.com/core/deep-crawling/#9-common-pitfalls-tips)
  * [10. Summary & Next Steps](https://docs.crawl4ai.com/core/deep-crawling/#10-summary-next-steps)


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/core/quickstart/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * Quick Start
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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


  * [Getting Started with Crawl4AI](https://docs.crawl4ai.com/core/quickstart/#getting-started-with-crawl4ai)
  * [1. Introduction](https://docs.crawl4ai.com/core/quickstart/#1-introduction)
  * [2. Your First Crawl](https://docs.crawl4ai.com/core/quickstart/#2-your-first-crawl)
  * [3. Basic Configuration (Light Introduction)](https://docs.crawl4ai.com/core/quickstart/#3-basic-configuration-light-introduction)
  * [4. Generating Markdown Output](https://docs.crawl4ai.com/core/quickstart/#4-generating-markdown-output)
  * [5. Simple Data Extraction (CSS-based)](https://docs.crawl4ai.com/core/quickstart/#5-simple-data-extraction-css-based)
  * [6. Simple Data Extraction (LLM-based)](https://docs.crawl4ai.com/core/quickstart/#6-simple-data-extraction-llm-based)
  * [7. Multi-URL Concurrency (Preview)](https://docs.crawl4ai.com/core/quickstart/#7-multi-url-concurrency-preview)
  * [8. Dynamic Content Example](https://docs.crawl4ai.com/core/quickstart/#8-dynamic-content-example)
  * [9. Next Steps](https://docs.crawl4ai.com/core/quickstart/#9-next-steps)


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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
Copy
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
#### On this page
  * [1. Introduction](https://docs.crawl4ai.com/core/quickstart/#1-introduction)
  * [2. Your First Crawl](https://docs.crawl4ai.com/core/quickstart/#2-your-first-crawl)
  * [3. Basic Configuration (Light Introduction)](https://docs.crawl4ai.com/core/quickstart/#3-basic-configuration-light-introduction)
  * [4. Generating Markdown Output](https://docs.crawl4ai.com/core/quickstart/#4-generating-markdown-output)
  * [Example: Using a Filter with DefaultMarkdownGenerator](https://docs.crawl4ai.com/core/quickstart/#example-using-a-filter-with-defaultmarkdowngenerator)
  * [5. Simple Data Extraction (CSS-based)](https://docs.crawl4ai.com/core/quickstart/#5-simple-data-extraction-css-based)
  * [6. Simple Data Extraction (LLM-based)](https://docs.crawl4ai.com/core/quickstart/#6-simple-data-extraction-llm-based)
  * [7. Multi-URL Concurrency (Preview)](https://docs.crawl4ai.com/core/quickstart/#7-multi-url-concurrency-preview)
  * [8. Dynamic Content Example](https://docs.crawl4ai.com/core/quickstart/#8-dynamic-content-example)
  * [9. Next Steps](https://docs.crawl4ai.com/core/quickstart/#9-next-steps)


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/core/markdown-generation/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * Markdown Generation
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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


  * [Markdown Generation Basics](https://docs.crawl4ai.com/core/markdown-generation/#markdown-generation-basics)
  * [1. Quick Example](https://docs.crawl4ai.com/core/markdown-generation/#1-quick-example)
  * [2. How Markdown Generation Works](https://docs.crawl4ai.com/core/markdown-generation/#2-how-markdown-generation-works)
  * [3. Configuring the Default Markdown Generator](https://docs.crawl4ai.com/core/markdown-generation/#3-configuring-the-default-markdown-generator)
  * [4. Selecting the HTML Source for Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/#4-selecting-the-html-source-for-markdown-generation)
  * [5. Content Filters](https://docs.crawl4ai.com/core/markdown-generation/#5-content-filters)
  * [6. Using Fit Markdown](https://docs.crawl4ai.com/core/markdown-generation/#6-using-fit-markdown)
  * [7. The MarkdownGenerationResult Object](https://docs.crawl4ai.com/core/markdown-generation/#7-the-markdowngenerationresult-object)
  * [8. Combining Filters (BM25 + Pruning) in Two Passes](https://docs.crawl4ai.com/core/markdown-generation/#8-combining-filters-bm25-pruning-in-two-passes)
  * [9. Common Pitfalls & Tips](https://docs.crawl4ai.com/core/markdown-generation/#9-common-pitfalls-tips)
  * [10. Summary & Next Steps](https://docs.crawl4ai.com/core/markdown-generation/#10-summary-next-steps)


# Markdown Generation Basics
One of Crawl4AI’s core features is generating **clean, structured markdown** from web pages. Originally built to solve the problem of extracting only the “actual” content and discarding boilerplate or noise, Crawl4AI’s markdown system remains one of its biggest draws for AI workflows.
In this tutorial, you’ll learn:
  1. How to configure the **Default Markdown Generator**
  2. How **content filters** (BM25 or Pruning) help you refine markdown and discard junk 
  3. The difference between raw markdown (`result.markdown`) and filtered markdown (`fit_markdown`) 


> **Prerequisites** - You’ve completed or read [AsyncWebCrawler Basics](https://docs.crawl4ai.com/core/simple-crawling/) to understand how to run a simple crawl. - You know how to configure `CrawlerRunConfig`.
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
Copy
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
Copy
```

Some commonly used `options`:
  * **`ignore_links`**(bool): Whether to remove all hyperlinks in the final markdown.
  * **`ignore_images`**(bool): Remove all`![image]()` references. 
  * **`escape_html`**(bool): Turn HTML entities into text (default is often`True`). 
  * **`body_width`**(int): Wrap text at N characters.`0` or `None` means no wrapping. 
  * **`skip_internal_links`**(bool): If`True` , omit `#localAnchors` or internal links referencing the same page. 
  * **`include_sup_sub`**(bool): Attempt to handle`<sup>` / `<sub>` in a more readable way.


## 4. Selecting the HTML Source for Markdown Generation
The `content_source` parameter allows you to control which HTML content is used as input for markdown generation. This gives you flexibility in how the HTML is processed before conversion to markdown.
```
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  # Option 1: Use the raw HTML directly from the webpage (before any processing)
  raw_md_generator = DefaultMarkdownGenerator(
    content_source="raw_html",
    options={"ignore_links": True}
  )
  # Option 2: Use the cleaned HTML (after scraping strategy processing - default)
  cleaned_md_generator = DefaultMarkdownGenerator(
    content_source="cleaned_html", # This is the default
    options={"ignore_links": True}
  )
  # Option 3: Use preprocessed HTML optimized for schema extraction
  fit_md_generator = DefaultMarkdownGenerator(
    content_source="fit_html",
    options={"ignore_links": True}
  )
  # Use one of the generators in your crawler config
  config = CrawlerRunConfig(
    markdown_generator=raw_md_generator # Try each of the generators
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com", config=config)
    if result.success:
      print("Markdown:\n", result.markdown.raw_markdown[:500])
    else:
      print("Crawl failed:", result.error_message)
if __name__ == "__main__":
  import asyncio
  asyncio.run(main())
Copy
```

### HTML Source Options
  * **`"cleaned_html"`**(default): Uses the HTML after it has been processed by the scraping strategy. This HTML is typically cleaner and more focused on content, with some boilerplate removed.
  * **`"raw_html"`**: Uses the original HTML directly from the webpage, before any cleaning or processing. This preserves more of the original content, but may include navigation bars, ads, footers, and other elements that might not be relevant to the main content.
  * **`"fit_html"`**: Uses HTML preprocessed for schema extraction. This HTML is optimized for structured data extraction and may have certain elements simplified or removed.


### When to Use Each Option
  * Use **`"cleaned_html"`**(default) for most cases where you want a balance of content preservation and noise removal.
  * Use **`"raw_html"`**when you need to preserve all original content, or when the cleaning process is removing content you actually want to keep.
  * Use **`"fit_html"`**when working with structured data or when you need HTML that's optimized for schema extraction.


## 5. Content Filters
**Content filters** selectively remove or rank sections of text before turning them into Markdown. This is especially helpful if your page has ads, nav bars, or other clutter you don’t want.
### 5.1 BM25ContentFilter
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
Copy
```

  * **`user_query`**: The term you want to focus on. BM25 tries to keep only content blocks relevant to that query.
  * **`bm25_threshold`**: Raise it to keep fewer blocks; lower it to keep more.
  * **`use_stemming`**: If`True` , variations of words match (e.g., “learn,” “learning,” “learnt”).


**No query provided?** BM25 tries to glean a context from page metadata, or you can simply treat it as a scorched-earth approach that discards text with low generic score. Realistically, you want to supply a query for best results.
### 5.2 PruningContentFilter
If you **don’t** have a specific query, or if you just want a robust “junk remover,” use `PruningContentFilter`. It analyzes text density, link density, HTML structure, and known patterns (like “nav,” “footer”) to systematically prune extraneous or repetitive sections.
```
from crawl4ai.content_filter_strategy import PruningContentFilter
prune_filter = PruningContentFilter(
  threshold=0.5,
  threshold_type="fixed", # or "dynamic"
  min_word_threshold=50
)
Copy
```

  * **`threshold`**: Score boundary. Blocks below this score get removed.
  * **`threshold_type`**:
    * `"fixed"`: Straight comparison (`score >= threshold` keeps the block). 
    * `"dynamic"`: The filter adjusts threshold in a data-driven manner. 
  * **`min_word_threshold`**: Discard blocks under N words as likely too short or unhelpful.


**When to Use PruningContentFilter** - You want a broad cleanup without a user query. - The page has lots of repeated sidebars, footers, or disclaimers that hamper text extraction.
### 5.3 LLMContentFilter
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
Copy
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
Copy
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
Copy
```



> **Performance Tip** : Set a smaller `chunk_token_threshold` (e.g., 2048 or 4096) to enable parallel processing of content chunks. The default value is infinity, which processes the entire content as a single chunk.
## 6. Using Fit Markdown
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
Copy
```

## 7. The `MarkdownGenerationResult` Object
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
Copy
```

**Why Does This Matter?** - You can supply `raw_markdown` to an LLM if you want the entire text. - Or feed `fit_markdown` into a vector database to reduce token usage. - `references_markdown` can help you keep track of link provenance.
Below is a **revised section** under “Combining Filters (BM25 + Pruning)” that demonstrates how you can run **two** passes of content filtering without re-crawling, by taking the HTML (or text) from a first pass and feeding it into the second filter. It uses real code patterns from the snippet you provided for **BM25ContentFilter** , which directly accepts **HTML** strings (and can also handle plain text with minimal adaptation).
## 8. Combining Filters (BM25 + Pruning) in Two Passes
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
Copy
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
## 9. Common Pitfalls & Tips
1. **No Markdown Output?** - Make sure the crawler actually retrieved HTML. If the site is heavily JS-based, you may need to enable dynamic rendering or wait for elements. - Check if your content filter is too aggressive. Lower thresholds or disable the filter to see if content reappears.
2. **Performance Considerations** - Very large pages with multiple filters can be slower. Consider `cache_mode` to avoid re-downloading. - If your final use case is LLM ingestion, consider summarizing further or chunking big texts.
3. **Take Advantage of`fit_markdown`** - Great for RAG pipelines, semantic search, or any scenario where extraneous boilerplate is unwanted. - Still verify the textual quality—some sites have crucial data in footers or sidebars.
4. **Adjusting`html2text` Options** - If you see lots of raw HTML slipping into the text, turn on `escape_html`. - If code blocks look messy, experiment with `mark_code` or `handle_code_in_pre`.
## 10. Summary & Next Steps
In this **Markdown Generation Basics** tutorial, you learned to:
  * Configure the **DefaultMarkdownGenerator** with HTML-to-text options. 
  * Select different HTML sources using the `content_source` parameter. 
  * Use **BM25ContentFilter** for query-specific extraction or **PruningContentFilter** for general noise removal. 
  * Distinguish between raw and filtered markdown (`fit_markdown`). 
  * Leverage the `MarkdownGenerationResult` object to handle different forms of output (citations, references, etc.).


Now you can produce high-quality Markdown from any website, focusing on exactly the content you need—an essential step for powering AI models, summarization pipelines, or knowledge-base queries.
**Last Updated** : 2025-01-01
#### On this page
  * [1. Quick Example](https://docs.crawl4ai.com/core/markdown-generation/#1-quick-example)
  * [2. How Markdown Generation Works](https://docs.crawl4ai.com/core/markdown-generation/#2-how-markdown-generation-works)
  * [2.1 HTML-to-Text Conversion (Forked & Modified)](https://docs.crawl4ai.com/core/markdown-generation/#21-html-to-text-conversion-forked-modified)
  * [2.2 Link Citations & References](https://docs.crawl4ai.com/core/markdown-generation/#22-link-citations-references)
  * [2.3 Optional Content Filters](https://docs.crawl4ai.com/core/markdown-generation/#23-optional-content-filters)
  * [3. Configuring the Default Markdown Generator](https://docs.crawl4ai.com/core/markdown-generation/#3-configuring-the-default-markdown-generator)
  * [4. Selecting the HTML Source for Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/#4-selecting-the-html-source-for-markdown-generation)
  * [HTML Source Options](https://docs.crawl4ai.com/core/markdown-generation/#html-source-options)
  * [When to Use Each Option](https://docs.crawl4ai.com/core/markdown-generation/#when-to-use-each-option)
  * [5. Content Filters](https://docs.crawl4ai.com/core/markdown-generation/#5-content-filters)
  * [5.1 BM25ContentFilter](https://docs.crawl4ai.com/core/markdown-generation/#51-bm25contentfilter)
  * [5.2 PruningContentFilter](https://docs.crawl4ai.com/core/markdown-generation/#52-pruningcontentfilter)
  * [5.3 LLMContentFilter](https://docs.crawl4ai.com/core/markdown-generation/#53-llmcontentfilter)
  * [6. Using Fit Markdown](https://docs.crawl4ai.com/core/markdown-generation/#6-using-fit-markdown)
  * [7. The MarkdownGenerationResult Object](https://docs.crawl4ai.com/core/markdown-generation/#7-the-markdowngenerationresult-object)
  * [8. Combining Filters (BM25 + Pruning) in Two Passes](https://docs.crawl4ai.com/core/markdown-generation/#8-combining-filters-bm25-pruning-in-two-passes)
  * [Two-Pass Example](https://docs.crawl4ai.com/core/markdown-generation/#two-pass-example)
  * [What’s Happening?](https://docs.crawl4ai.com/core/markdown-generation/#whats-happening)
  * [Tips & Variations](https://docs.crawl4ai.com/core/markdown-generation/#tips-variations)
  * [One-Pass Combination?](https://docs.crawl4ai.com/core/markdown-generation/#one-pass-combination)
  * [9. Common Pitfalls & Tips](https://docs.crawl4ai.com/core/markdown-generation/#9-common-pitfalls-tips)
  * [10. Summary & Next Steps](https://docs.crawl4ai.com/core/markdown-generation/#10-summary-next-steps)


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

[Crawl4AI Documentation (v0.6.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ LLM Context ](https://docs.crawl4ai.com/core/llmtxt/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/core/docker-deployment/)


[ unclecode/crawl4ai 46.5k 4.4k ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [LLM Context](https://docs.crawl4ai.com/core/llmtxt/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * Docker Deployment
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
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
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


  * [Crawl4AI Docker Guide 🐳](https://docs.crawl4ai.com/core/docker-deployment/#crawl4ai-docker-guide)
  * [Table of Contents](https://docs.crawl4ai.com/core/docker-deployment/#table-of-contents)
  * [Prerequisites](https://docs.crawl4ai.com/core/docker-deployment/#prerequisites)
  * [Installation](https://docs.crawl4ai.com/core/docker-deployment/#installation)
  * [MCP (Model Context Protocol) Support](https://docs.crawl4ai.com/core/docker-deployment/#mcp-model-context-protocol-support)
  * [Additional API Endpoints](https://docs.crawl4ai.com/core/docker-deployment/#additional-api-endpoints)
  * [Dockerfile Parameters](https://docs.crawl4ai.com/core/docker-deployment/#dockerfile-parameters)
  * [Using the API](https://docs.crawl4ai.com/core/docker-deployment/#using-the-api)
  * [Metrics & Monitoring](https://docs.crawl4ai.com/core/docker-deployment/#metrics-monitoring)
  * [Server Configuration](https://docs.crawl4ai.com/core/docker-deployment/#server-configuration)
  * [Getting Help](https://docs.crawl4ai.com/core/docker-deployment/#getting-help)
  * [Summary](https://docs.crawl4ai.com/core/docker-deployment/#summary)


# Crawl4AI Docker Guide 🐳
## Table of Contents
  * [Prerequisites](https://docs.crawl4ai.com/core/docker-deployment/#prerequisites)
  * [Installation](https://docs.crawl4ai.com/core/docker-deployment/#installation)
  * [Option 1: Using Pre-built Docker Hub Images (Recommended)](https://docs.crawl4ai.com/core/docker-deployment/#option-1-using-pre-built-docker-hub-images-recommended)
  * [Option 2: Using Docker Compose](https://docs.crawl4ai.com/core/docker-deployment/#option-2-using-docker-compose)
  * [Option 3: Manual Local Build & Run](https://docs.crawl4ai.com/core/docker-deployment/#option-3-manual-local-build--run)
  * [Dockerfile Parameters](https://docs.crawl4ai.com/core/docker-deployment/#dockerfile-parameters)
  * [Using the API](https://docs.crawl4ai.com/core/docker-deployment/#using-the-api)
  * [Playground Interface](https://docs.crawl4ai.com/core/docker-deployment/#playground-interface)
  * [Python SDK](https://docs.crawl4ai.com/core/docker-deployment/#python-sdk)
  * [Understanding Request Schema](https://docs.crawl4ai.com/core/docker-deployment/#understanding-request-schema)
  * [REST API Examples](https://docs.crawl4ai.com/core/docker-deployment/#rest-api-examples)
  * [Additional API Endpoints](https://docs.crawl4ai.com/core/docker-deployment/#additional-api-endpoints)
  * [HTML Extraction Endpoint](https://docs.crawl4ai.com/core/docker-deployment/#html-extraction-endpoint)
  * [Screenshot Endpoint](https://docs.crawl4ai.com/core/docker-deployment/#screenshot-endpoint)
  * [PDF Export Endpoint](https://docs.crawl4ai.com/core/docker-deployment/#pdf-export-endpoint)
  * [JavaScript Execution Endpoint](https://docs.crawl4ai.com/core/docker-deployment/#javascript-execution-endpoint)
  * [Library Context Endpoint](https://docs.crawl4ai.com/core/docker-deployment/#library-context-endpoint)
  * [MCP (Model Context Protocol) Support](https://docs.crawl4ai.com/core/docker-deployment/#mcp-model-context-protocol-support)
  * [What is MCP?](https://docs.crawl4ai.com/core/docker-deployment/#what-is-mcp)
  * [Connecting via MCP](https://docs.crawl4ai.com/core/docker-deployment/#connecting-via-mcp)
  * [Using with Claude Code](https://docs.crawl4ai.com/core/docker-deployment/#using-with-claude-code)
  * [Available MCP Tools](https://docs.crawl4ai.com/core/docker-deployment/#available-mcp-tools)
  * [Testing MCP Connections](https://docs.crawl4ai.com/core/docker-deployment/#testing-mcp-connections)
  * [MCP Schemas](https://docs.crawl4ai.com/core/docker-deployment/#mcp-schemas)
  * [Metrics & Monitoring](https://docs.crawl4ai.com/core/docker-deployment/#metrics--monitoring)
  * [Deployment Scenarios](https://docs.crawl4ai.com/core/docker-deployment/#deployment-scenarios)
  * [Complete Examples](https://docs.crawl4ai.com/core/docker-deployment/#complete-examples)
  * [Server Configuration](https://docs.crawl4ai.com/core/docker-deployment/#server-configuration)
  * [Understanding config.yml](https://docs.crawl4ai.com/core/docker-deployment/#understanding-configyml)
  * [JWT Authentication](https://docs.crawl4ai.com/core/docker-deployment/#jwt-authentication)
  * [Configuration Tips and Best Practices](https://docs.crawl4ai.com/core/docker-deployment/#configuration-tips-and-best-practices)
  * [Customizing Your Configuration](https://docs.crawl4ai.com/core/docker-deployment/#customizing-your-configuration)
  * [Configuration Recommendations](https://docs.crawl4ai.com/core/docker-deployment/#configuration-recommendations)
  * [Getting Help](https://docs.crawl4ai.com/core/docker-deployment/#getting-help)
  * [Summary](https://docs.crawl4ai.com/core/docker-deployment/#summary)


## Prerequisites
Before we dive in, make sure you have: - Docker installed and running (version 20.10.0 or higher), including `docker compose` (usually bundled with Docker Desktop). - `git` for cloning the repository. - At least 4GB of RAM available for the container (more recommended for heavy use). - Python 3.10+ (if using the Python SDK). - Node.js 16+ (if using the Node.js examples).
> 💡 **Pro tip** : Run `docker info` to check your Docker installation and available resources.
## Installation
We offer several ways to get the Crawl4AI server running. The quickest way is to use our pre-built Docker Hub images.
### Option 1: Using Pre-built Docker Hub Images (Recommended)
Pull and run images directly from Docker Hub without building locally.
#### 1. Pull the Image
Our latest release candidate is `0.6.0-r2`. Images are built with multi-arch manifests, so Docker automatically pulls the correct version for your system.
```
# Pull the release candidate (recommended for latest features)
docker pull unclecode/crawl4ai:0.6.0-r1
# Or pull the latest stable version
docker pull unclecode/crawl4ai:latest
Copy
```

#### 2. Setup Environment (API Keys)
If you plan to use LLMs, create a `.llm.env` file in your working directory:
```
# Create a .llm.env file with your API keys
cat > .llm.env << EOL
# OpenAI
OPENAI_API_KEY=sk-your-key
# Anthropic
ANTHROPIC_API_KEY=your-anthropic-key
# Other providers as needed
# DEEPSEEK_API_KEY=your-deepseek-key
# GROQ_API_KEY=your-groq-key
# TOGETHER_API_KEY=your-together-key
# MISTRAL_API_KEY=your-mistral-key
# GEMINI_API_TOKEN=your-gemini-token
EOL
Copy
```

> 🔑 **Note** : Keep your API keys secure! Never commit `.llm.env` to version control.
#### 3. Run the Container
  * **Basic run:**
```
docker run -d \
 -p 11235:11235 \
 --name crawl4ai \
 --shm-size=1g \
 unclecode/crawl4ai:latest
Copy
```

  * **With LLM support:**
```
# Make sure .llm.env is in the current directory
docker run -d \
 -p 11235:11235 \
 --name crawl4ai \
 --env-file .llm.env \
 --shm-size=1g \
 unclecode/crawl4ai:latest
Copy
```



> The server will be available at `http://localhost:11235`. Visit `/playground` to access the interactive testing interface.
#### 4. Stopping the Container
```
docker stop crawl4ai && docker rm crawl4ai
Copy
```

#### Docker Hub Versioning Explained
  * **Image Name:** `unclecode/crawl4ai`
  * **Tag Format:** `LIBRARY_VERSION[-SUFFIX]` (e.g., `0.6.0-r2`)
    * `LIBRARY_VERSION`: The semantic version of the core `crawl4ai` Python library
    * `SUFFIX`: Optional tag for release candidates (``) and revisions (`r1`)
  * **`latest`Tag:** Points to the most recent stable version
  * **Multi-Architecture Support:** All images support both `linux/amd64` and `linux/arm64` architectures through a single tag


### Option 2: Using Docker Compose
Docker Compose simplifies building and running the service, especially for local development and testing.
#### 1. Clone Repository
```
git clone https://github.com/unclecode/crawl4ai.git
cd crawl4ai
Copy
```

#### 2. Environment Setup (API Keys)
If you plan to use LLMs, copy the example environment file and add your API keys. This file should be in the **project root directory**.
```
# Make sure you are in the 'crawl4ai' root directory
cp deploy/docker/.llm.env.example .llm.env
# Now edit .llm.env and add your API keys
Copy
```

#### 3. Build and Run with Compose
The `docker-compose.yml` file in the project root provides a simplified approach that automatically handles architecture detection using buildx.
  * **Run Pre-built Image from Docker Hub:**
```
# Pulls and runs the release candidate from Docker Hub
# Automatically selects the correct architecture
IMAGE=unclecode/crawl4ai:latest docker compose up -d
Copy
```

  * **Build and Run Locally:**
```
# Builds the image locally using Dockerfile and runs it
# Automatically uses the correct architecture for your machine
docker compose up --build -d
Copy
```

  * **Customize the Build:**
```
# Build with all features (includes torch and transformers)
INSTALL_TYPE=all docker compose up --build -d
# Build with GPU support (for AMD64 platforms)
ENABLE_GPU=true docker compose up --build -d
Copy
```



> The server will be available at `http://localhost:11235`.
#### 4. Stopping the Service
```
# Stop the service
docker compose down
Copy
```

### Option 3: Manual Local Build & Run
If you prefer not to use Docker Compose for direct control over the build and run process.
#### 1. Clone Repository & Setup Environment
Follow steps 1 and 2 from the Docker Compose section above (clone repo, `cd crawl4ai`, create `.llm.env` in the root).
#### 2. Build the Image (Multi-Arch)
Use `docker buildx` to build the image. Crawl4AI now uses buildx to handle multi-architecture builds automatically.
```
# Make sure you are in the 'crawl4ai' root directory
# Build for the current architecture and load it into Docker
docker buildx build -t crawl4ai-local:latest --load .
# Or build for multiple architectures (useful for publishing)
docker buildx build --platform linux/amd64,linux/arm64 -t crawl4ai-local:latest --load .
# Build with additional options
docker buildx build \
 --build-arg INSTALL_TYPE=all \
 --build-arg ENABLE_GPU=false \
 -t crawl4ai-local:latest --load .
Copy
```

#### 3. Run the Container
  * **Basic run (no LLM support):**
```
docker run -d \
 -p 11235:11235 \
 --name crawl4ai-standalone \
 --shm-size=1g \
 crawl4ai-local:latest
Copy
```

  * **With LLM support:**
```
# Make sure .llm.env is in the current directory (project root)
docker run -d \
 -p 11235:11235 \
 --name crawl4ai-standalone \
 --env-file .llm.env \
 --shm-size=1g \
 crawl4ai-local:latest
Copy
```



> The server will be available at `http://localhost:11235`.
#### 4. Stopping the Manual Container
```
docker stop crawl4ai-standalone && docker rm crawl4ai-standalone
Copy
```

## MCP (Model Context Protocol) Support
Crawl4AI server includes support for the Model Context Protocol (MCP), allowing you to connect the server's capabilities directly to MCP-compatible clients like Claude Code.
### What is MCP?
MCP is an open protocol that standardizes how applications provide context to LLMs. It allows AI models to access external tools, data sources, and services through a standardized interface.
### Connecting via MCP
The Crawl4AI server exposes two MCP endpoints:
  * **Server-Sent Events (SSE)** : `http://localhost:11235/mcp/sse`
  * **WebSocket** : `ws://localhost:11235/mcp/ws`


### Using with Claude Code
You can add Crawl4AI as an MCP tool provider in Claude Code with a simple command:
```
# Add the Crawl4AI server as an MCP provider
claude mcp add --transport sse c4ai-sse http://localhost:11235/mcp/sse
# List all MCP providers to verify it was added
claude mcp list
Copy
```

Once connected, Claude Code can directly use Crawl4AI's capabilities like screenshot capture, PDF generation, and HTML processing without having to make separate API calls.
### Available MCP Tools
When connected via MCP, the following tools are available:
  * `md` - Generate markdown from web content
  * `html` - Extract preprocessed HTML
  * `screenshot` - Capture webpage screenshots
  * `pdf` - Generate PDF documents
  * `execute_js` - Run JavaScript on web pages
  * `crawl` - Perform multi-URL crawling
  * `ask` - Query the Crawl4AI library context


### Testing MCP Connections
You can test the MCP WebSocket connection using the test file included in the repository:
```
# From the repository root
python tests/mcp/test_mcp_socket.py
Copy
```

### MCP Schemas
Access the MCP tool schemas at `http://localhost:11235/mcp/schema` for detailed information on each tool's parameters and capabilities.
## Additional API Endpoints
In addition to the core `/crawl` and `/crawl/stream` endpoints, the server provides several specialized endpoints:
### HTML Extraction Endpoint
```
POST /html
Copy
```

Crawls the URL and returns preprocessed HTML optimized for schema extraction.
```
{
 "url": "https://example.com"
}
Copy
```

### Screenshot Endpoint
```
POST /screenshot
Copy
```

Captures a full-page PNG screenshot of the specified URL.
```
{
 "url": "https://example.com",
 "screenshot_wait_for": 2,
 "output_path": "/path/to/save/screenshot.png"
}
Copy
```

  * `screenshot_wait_for`: Optional delay in seconds before capture (default: 2)
  * `output_path`: Optional path to save the screenshot (recommended)


### PDF Export Endpoint
```
POST /pdf
Copy
```

Generates a PDF document of the specified URL.
```
{
 "url": "https://example.com",
 "output_path": "/path/to/save/document.pdf"
}
Copy
```

  * `output_path`: Optional path to save the PDF (recommended)


### JavaScript Execution Endpoint
```
POST /execute_js
Copy
```

Executes JavaScript snippets on the specified URL and returns the full crawl result.
```
{
 "url": "https://example.com",
 "scripts": [
  "return document.title",
  "return Array.from(document.querySelectorAll('a')).map(a => a.href)"
 ]
}
Copy
```

  * `scripts`: List of JavaScript snippets to execute sequentially


## Dockerfile Parameters
You can customize the image build process using build arguments (`--build-arg`). These are typically used via `docker buildx build` or within the `docker-compose.yml` file.
```
# Example: Build with 'all' features using buildx
docker buildx build \
 --platform linux/amd64,linux/arm64 \
 --build-arg INSTALL_TYPE=all \
 -t yourname/crawl4ai-all:latest \
 --load \
 . # Build from root context
Copy
```

### Build Arguments Explained
Argument | Description | Default | Options  
---|---|---|---  
INSTALL_TYPE | Feature set | `default` | `default`, `all`, `torch`, `transformer`  
ENABLE_GPU | GPU support (CUDA for AMD64) | `false` | `true`, `false`  
APP_HOME | Install path inside container (advanced) | `/app` | any valid path  
USE_LOCAL | Install library from local source | `true` | `true`, `false`  
GITHUB_REPO | Git repo to clone if USE_LOCAL=false | _(see Dockerfile)_ | any git URL  
GITHUB_BRANCH | Git branch to clone if USE_LOCAL=false | `main` | any branch name  
_(Note: PYTHON_VERSION is fixed by the`FROM` instruction in the Dockerfile)_
### Build Best Practices
  1. **Choose the Right Install Type**
     * `default`: Basic installation, smallest image size. Suitable for most standard web scraping and markdown generation.
     * `all`: Full features including `torch` and `transformers` for advanced extraction strategies (e.g., CosineStrategy, certain LLM filters). Significantly larger image. Ensure you need these extras.
  2. **Platform Considerations**
     * Use `buildx` for building multi-architecture images, especially for pushing to registries.
     * Use `docker compose` profiles (`local-amd64`, `local-arm64`) for easy platform-specific local builds.
  3. **Performance Optimization**
     * The image automatically includes platform-specific optimizations (OpenMP for AMD64, OpenBLAS for ARM64).


## Using the API
Communicate with the running Docker server via its REST API (defaulting to `http://localhost:11235`). You can use the Python SDK or make direct HTTP requests.
### Playground Interface
A built-in web playground is available at `http://localhost:11235/playground` for testing and generating API requests. The playground allows you to:
  1. Configure `CrawlerRunConfig` and `BrowserConfig` using the main library's Python syntax
  2. Test crawling operations directly from the interface
  3. Generate corresponding JSON for REST API requests based on your configuration


This is the easiest way to translate Python configuration to JSON requests when building integrations.
### Python SDK
Install the SDK: `pip install crawl4ai`
```
import asyncio
from crawl4ai.docker_client import Crawl4aiDockerClient
from crawl4ai import BrowserConfig, CrawlerRunConfig, CacheMode # Assuming you have crawl4ai installed
async def main():
  # Point to the correct server port
  async with Crawl4aiDockerClient(base_url="http://localhost:11235", verbose=True) as client:
    # If JWT is enabled on the server, authenticate first:
    # await client.authenticate("user@example.com") # See Server Configuration section
    # Example Non-streaming crawl
    print("--- Running Non-Streaming Crawl ---")
    results = await client.crawl(
      ["https://httpbin.org/html"],
      browser_config=BrowserConfig(headless=True), # Use library classes for config aid
      crawler_config=CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
    )
    if results: # client.crawl returns None on failure
     print(f"Non-streaming results success: {results.success}")
     if results.success:
       for result in results: # Iterate through the CrawlResultContainer
         print(f"URL: {result.url}, Success: {result.success}")
    else:
      print("Non-streaming crawl failed.")

    # Example Streaming crawl
    print("\n--- Running Streaming Crawl ---")
    stream_config = CrawlerRunConfig(stream=True, cache_mode=CacheMode.BYPASS)
    try:
      async for result in await client.crawl( # client.crawl returns an async generator for streaming
        ["https://httpbin.org/html", "https://httpbin.org/links/5/0"],
        browser_config=BrowserConfig(headless=True),
        crawler_config=stream_config
      ):
        print(f"Streamed result: URL: {result.url}, Success: {result.success}")
    except Exception as e:
      print(f"Streaming crawl failed: {e}")

    # Example Get schema
    print("\n--- Getting Schema ---")
    schema = await client.get_schema()
    print(f"Schema received: {bool(schema)}") # Print whether schema was received
if __name__ == "__main__":
  asyncio.run(main())
Copy
```

_(SDK parameters like timeout, verify_ssl etc. remain the same)_
### Second Approach: Direct API Calls
Crucially, when sending configurations directly via JSON, they **must** follow the `{"type": "ClassName", "params": {...}}` structure for any non-primitive value (like config objects or strategies). Dictionaries must be wrapped as `{"type": "dict", "value": {...}}`.
_(Keep the detailed explanation of Configuration Structure, Basic Pattern, Simple vs Complex, Strategy Pattern, Complex Nested Example, Quick Grammar Overview, Important Rules, Pro Tip)_
#### More Examples _(Ensure Schema example uses type/value wrapper)_
**Advanced Crawler Configuration** _(Keep example, ensure cache_mode uses valid enum value like "bypass")_
**Extraction Strategy**
```
{
  "crawler_config": {
    "type": "CrawlerRunConfig",
    "params": {
      "extraction_strategy": {
        "type": "JsonCssExtractionStrategy",
        "params": {
          "schema": {
            "type": "dict",
            "value": {
              "baseSelector": "article.post",
              "fields": [
                {"name": "title", "selector": "h1", "type": "text"},
                {"name": "content", "selector": ".content", "type": "html"}
              ]
             }
          }
        }
      }
    }
  }
}
Copy
```

**LLM Extraction Strategy** _(Keep example, ensure schema uses type/value wrapper)_ _(Keep Deep Crawler Example)_
### REST API Examples
Update URLs to use port `11235`.
#### Simple Crawl
```
import requests
# Configuration objects converted to the required JSON structure
browser_config_payload = {
  "type": "BrowserConfig",
  "params": {"headless": True}
}
crawler_config_payload = {
  "type": "CrawlerRunConfig",
  "params": {"stream": False, "cache_mode": "bypass"} # Use string value of enum
}
crawl_payload = {
  "urls": ["https://httpbin.org/html"],
  "browser_config": browser_config_payload,
  "crawler_config": crawler_config_payload
}
response = requests.post(
  "http://localhost:11235/crawl", # Updated port
  # headers={"Authorization": f"Bearer {token}"}, # If JWT is enabled
  json=crawl_payload
)
print(f"Status Code: {response.status_code}")
if response.ok:
  print(response.json())
else:
  print(f"Error: {response.text}")
Copy
```

#### Streaming Results
```
import json
import httpx # Use httpx for async streaming example
async def test_stream_crawl(token: str = None): # Made token optional
  """Test the /crawl/stream endpoint with multiple URLs."""
  url = "http://localhost:11235/crawl/stream" # Updated port
  payload = {
    "urls": [
      "https://httpbin.org/html",
      "https://httpbin.org/links/5/0",
    ],
    "browser_config": {
      "type": "BrowserConfig",
      "params": {"headless": True, "viewport": {"type": "dict", "value": {"width": 1200, "height": 800}}} # Viewport needs type:dict
    },
    "crawler_config": {
      "type": "CrawlerRunConfig",
      "params": {"stream": True, "cache_mode": "bypass"}
    }
  }
  headers = {}
  # if token:
  #  headers = {"Authorization": f"Bearer {token}"} # If JWT is enabled
  try:
    async with httpx.AsyncClient() as client:
      async with client.stream("POST", url, json=payload, headers=headers, timeout=120.0) as response:
        print(f"Status: {response.status_code} (Expected: 200)")
        response.raise_for_status() # Raise exception for bad status codes
        # Read streaming response line-by-line (NDJSON)
        async for line in response.aiter_lines():
          if line:
            try:
              data = json.loads(line)
              # Check for completion marker
              if data.get("status") == "completed":
                print("Stream completed.")
                break
              print(f"Streamed Result: {json.dumps(data, indent=2)}")
            except json.JSONDecodeError:
              print(f"Warning: Could not decode JSON line: {line}")
  except httpx.HTTPStatusError as e:
     print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
  except Exception as e:
    print(f"Error in streaming crawl test: {str(e)}")
# To run this example:
# import asyncio
# asyncio.run(test_stream_crawl())
Copy
```

## Metrics & Monitoring
Keep an eye on your crawler with these endpoints:
  * `/health` - Quick health check
  * `/metrics` - Detailed Prometheus metrics
  * `/schema` - Full API schema


Example health check: 
```
curl http://localhost:11235/health
Copy
```

_(Deployment Scenarios and Complete Examples sections remain the same, maybe update links if examples moved)_
## Server Configuration
The server's behavior can be customized through the `config.yml` file.
### Understanding config.yml
The configuration file is loaded from `/app/config.yml` inside the container. By default, the file from `deploy/docker/config.yml` in the repository is copied there during the build.
Here's a detailed breakdown of the configuration options (using defaults from `deploy/docker/config.yml`):
```
# Application Configuration
app:
 title: "Crawl4AI API"
 version: "1.0.0" # Consider setting this to match library version, e.g., "0.5.1"
 host: "0.0.0.0"
 port: 8020 # NOTE: This port is used ONLY when running server.py directly. Gunicorn overrides this (see supervisord.conf).
 reload: False # Default set to False - suitable for production
 timeout_keep_alive: 300
# Default LLM Configuration
llm:
 provider: "openai/gpt-4o-mini"
 api_key_env: "OPENAI_API_KEY"
 # api_key: sk-... # If you pass the API key directly then api_key_env will be ignored
# Redis Configuration (Used by internal Redis server managed by supervisord)
redis:
 host: "localhost"
 port: 6379
 db: 0
 password: ""
 # ... other redis options ...
# Rate Limiting Configuration
rate_limiting:
 enabled: True
 default_limit: "1000/minute"
 trusted_proxies: []
 storage_uri: "memory://" # Use "redis://localhost:6379" if you need persistent/shared limits
# Security Configuration
security:
 enabled: false # Master toggle for security features
 jwt_enabled: false # Enable JWT authentication (requires security.enabled=true)
 https_redirect: false # Force HTTPS (requires security.enabled=true)
 trusted_hosts: ["*"] # Allowed hosts (use specific domains in production)
 headers: # Security headers (applied if security.enabled=true)
  x_content_type_options: "nosniff"
  x_frame_options: "DENY"
  content_security_policy: "default-src 'self'"
  strict_transport_security: "max-age=63072000; includeSubDomains"
# Crawler Configuration
crawler:
 memory_threshold_percent: 95.0
 rate_limiter:
  base_delay: [1.0, 2.0] # Min/max delay between requests in seconds for dispatcher
 timeouts:
  stream_init: 30.0 # Timeout for stream initialization
  batch_process: 300.0 # Timeout for non-streaming /crawl processing
# Logging Configuration
logging:
 level: "INFO"
 format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# Observability Configuration
observability:
 prometheus:
  enabled: True
  endpoint: "/metrics"
 health_check:
  endpoint: "/health"
Copy
```

_(JWT Authentication section remains the same, just note the default port is now 11235 for requests)_
_(Configuration Tips and Best Practices remain the same)_
### Customizing Your Configuration
You can override the default `config.yml`.
#### Method 1: Modify Before Build
  1. Edit the `deploy/docker/config.yml` file in your local repository clone.
  2. Build the image using `docker buildx` or `docker compose --profile local-... up --build`. The modified file will be copied into the image.


#### Method 2: Runtime Mount (Recommended for Custom Deploys)
  1. Create your custom configuration file, e.g., `my-custom-config.yml` locally. Ensure it contains all necessary sections.
  2. Mount it when running the container:
     * **Using`docker run` :**
```
# Assumes my-custom-config.yml is in the current directory
docker run -d -p 11235:11235 \
 --name crawl4ai-custom-config \
 --env-file .llm.env \
 --shm-size=1g \
 -v $(pwd)/my-custom-config.yml:/app/config.yml \
 unclecode/crawl4ai:latest # Or your specific tag
Copy
```

     * **Using`docker-compose.yml` :** Add a `volumes` section to the service definition: 
```
services:
 crawl4ai-hub-amd64: # Or your chosen service
  image: unclecode/crawl4ai:latest
  profiles: ["hub-amd64"]
  <<: *base-config
  volumes:
   # Mount local custom config over the default one in the container
   - ./my-custom-config.yml:/app/config.yml
   # Keep the shared memory volume from base-config
   - /dev/shm:/dev/shm
Copy
```

_(Note: Ensure`my-custom-config.yml` is in the same directory as `docker-compose.yml`)_


> 💡 When mounting, your custom file _completely replaces_ the default one. Ensure it's a valid and complete configuration.
### Configuration Recommendations
  1. **Security First** 🔒
  2. Always enable security in production
  3. Use specific trusted_hosts instead of wildcards
  4. Set up proper rate limiting to protect your server
  5. Consider your environment before enabling HTTPS redirect
  6. **Resource Management** 💻
  7. Adjust memory_threshold_percent based on available RAM
  8. Set timeouts according to your content size and network conditions
  9. Use Redis for rate limiting in multi-container setups
  10. **Monitoring** 📊
  11. Enable Prometheus if you need metrics
  12. Set DEBUG logging in development, INFO in production
  13. Regular health check monitoring is crucial
  14. **Performance Tuning** ⚡
  15. Start with conservative rate limiter delays
  16. Increase batch_process timeout for large content
  17. Adjust stream_init timeout based on initial response times


## Getting Help
We're here to help you succeed with Crawl4AI! Here's how to get support:
  * 📖 Check our [full documentation](https://docs.crawl4ai.com)
  * 🐛 Found a bug? [Open an issue](https://github.com/unclecode/crawl4ai/issues)
  * 💬 Join our [Discord community](https://discord.gg/crawl4ai)
  * ⭐ Star us on GitHub to show support!


## Summary
In this guide, we've covered everything you need to get started with Crawl4AI's Docker deployment: - Building and running the Docker container - Configuring the environment - Using the interactive playground for testing - Making API requests with proper typing - Using the Python SDK - Leveraging specialized endpoints for screenshots, PDFs, and JavaScript execution - Connecting via the Model Context Protocol (MCP) - Monitoring your deployment
The new playground interface at `http://localhost:11235/playground` makes it much easier to test configurations and generate the corresponding JSON for API requests.
For AI application developers, the MCP integration allows tools like Claude Code to directly access Crawl4AI's capabilities without complex API handling.
Remember, the examples in the `examples` folder are your friends - they show real-world usage patterns that you can adapt for your needs.
Keep exploring, and don't hesitate to reach out if you need help! We're building something amazing together. 🚀
Happy crawling! 🕷️
#### On this page
  * [Table of Contents](https://docs.crawl4ai.com/core/docker-deployment/#table-of-contents)
  * [Prerequisites](https://docs.crawl4ai.com/core/docker-deployment/#prerequisites)
  * [Installation](https://docs.crawl4ai.com/core/docker-deployment/#installation)
  * [Option 1: Using Pre-built Docker Hub Images (Recommended)](https://docs.crawl4ai.com/core/docker-deployment/#option-1-using-pre-built-docker-hub-images-recommended)
  * [1. Pull the Image](https://docs.crawl4ai.com/core/docker-deployment/#1-pull-the-image)
  * [2. Setup Environment (API Keys)](https://docs.crawl4ai.com/core/docker-deployment/#2-setup-environment-api-keys)
  * [3. Run the Container](https://docs.crawl4ai.com/core/docker-deployment/#3-run-the-container)
  * [4. Stopping the Container](https://docs.crawl4ai.com/core/docker-deployment/#4-stopping-the-container)
  * [Docker Hub Versioning Explained](https://docs.crawl4ai.com/core/docker-deployment/#docker-hub-versioning-explained)
  * [Option 2: Using Docker Compose](https://docs.crawl4ai.com/core/docker-deployment/#option-2-using-docker-compose)
  * [1. Clone Repository](https://docs.crawl4ai.com/core/docker-deployment/#1-clone-repository)
  * [2. Environment Setup (API Keys)](https://docs.crawl4ai.com/core/docker-deployment/#2-environment-setup-api-keys)
  * [3. Build and Run with Compose](https://docs.crawl4ai.com/core/docker-deployment/#3-build-and-run-with-compose)
  * [4. Stopping the Service](https://docs.crawl4ai.com/core/docker-deployment/#4-stopping-the-service)
  * [Option 3: Manual Local Build & Run](https://docs.crawl4ai.com/core/docker-deployment/#option-3-manual-local-build-run)
  * [1. Clone Repository & Setup Environment](https://docs.crawl4ai.com/core/docker-deployment/#1-clone-repository-setup-environment)
  * [2. Build the Image (Multi-Arch)](https://docs.crawl4ai.com/core/docker-deployment/#2-build-the-image-multi-arch)
  * [3. Run the Container](https://docs.crawl4ai.com/core/docker-deployment/#3-run-the-container_1)
  * [4. Stopping the Manual Container](https://docs.crawl4ai.com/core/docker-deployment/#4-stopping-the-manual-container)
  * [MCP (Model Context Protocol) Support](https://docs.crawl4ai.com/core/docker-deployment/#mcp-model-context-protocol-support)
  * [What is MCP?](https://docs.crawl4ai.com/core/docker-deployment/#what-is-mcp)
  * [Connecting via MCP](https://docs.crawl4ai.com/core/docker-deployment/#connecting-via-mcp)
  * [Using with Claude Code](https://docs.crawl4ai.com/core/docker-deployment/#using-with-claude-code)
  * [Available MCP Tools](https://docs.crawl4ai.com/core/docker-deployment/#available-mcp-tools)
  * [Testing MCP Connections](https://docs.crawl4ai.com/core/docker-deployment/#testing-mcp-connections)
  * [MCP Schemas](https://docs.crawl4ai.com/core/docker-deployment/#mcp-schemas)
  * [Additional API Endpoints](https://docs.crawl4ai.com/core/docker-deployment/#additional-api-endpoints)
  * [HTML Extraction Endpoint](https://docs.crawl4ai.com/core/docker-deployment/#html-extraction-endpoint)
  * [Screenshot Endpoint](https://docs.crawl4ai.com/core/docker-deployment/#screenshot-endpoint)
  * [PDF Export Endpoint](https://docs.crawl4ai.com/core/docker-deployment/#pdf-export-endpoint)
  * [JavaScript Execution Endpoint](https://docs.crawl4ai.com/core/docker-deployment/#javascript-execution-endpoint)
  * [Dockerfile Parameters](https://docs.crawl4ai.com/core/docker-deployment/#dockerfile-parameters)
  * [Build Arguments Explained](https://docs.crawl4ai.com/core/docker-deployment/#build-arguments-explained)
  * [Build Best Practices](https://docs.crawl4ai.com/core/docker-deployment/#build-best-practices)
  * [Using the API](https://docs.crawl4ai.com/core/docker-deployment/#using-the-api)
  * [Playground Interface](https://docs.crawl4ai.com/core/docker-deployment/#playground-interface)
  * [Python SDK](https://docs.crawl4ai.com/core/docker-deployment/#python-sdk)
  * [Second Approach: Direct API Calls](https://docs.crawl4ai.com/core/docker-deployment/#second-approach-direct-api-calls)
  * [More Examples (Ensure Schema example uses type/value wrapper)](https://docs.crawl4ai.com/core/docker-deployment/#more-examples-ensure-schema-example-uses-typevalue-wrapper)
  * [REST API Examples](https://docs.crawl4ai.com/core/docker-deployment/#rest-api-examples)
  * [Simple Crawl](https://docs.crawl4ai.com/core/docker-deployment/#simple-crawl)
  * [Streaming Results](https://docs.crawl4ai.com/core/docker-deployment/#streaming-results)
  * [Metrics & Monitoring](https://docs.crawl4ai.com/core/docker-deployment/#metrics-monitoring)
  * [Server Configuration](https://docs.crawl4ai.com/core/docker-deployment/#server-configuration)
  * [Understanding config.yml](https://docs.crawl4ai.com/core/docker-deployment/#understanding-configyml)
  * [Customizing Your Configuration](https://docs.crawl4ai.com/core/docker-deployment/#customizing-your-configuration)
  * [Method 1: Modify Before Build](https://docs.crawl4ai.com/core/docker-deployment/#method-1-modify-before-build)
  * [Method 2: Runtime Mount (Recommended for Custom Deploys)](https://docs.crawl4ai.com/core/docker-deployment/#method-2-runtime-mount-recommended-for-custom-deploys)
  * [Configuration Recommendations](https://docs.crawl4ai.com/core/docker-deployment/#configuration-recommendations)
  * [Getting Help](https://docs.crawl4ai.com/core/docker-deployment/#getting-help)
  * [Summary](https://docs.crawl4ai.com/core/docker-deployment/#summary)


> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")
