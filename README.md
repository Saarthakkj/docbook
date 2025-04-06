# Documentation Crawler

A Python script that automatically crawls and extracts documentation from a website and saves it as a Markdown file.

## Overview

This tool uses [crawl4ai](https://docs.crawl4ai.com) to perform a deep breadth-first search crawl of a documentation website. It extracts the content, converts it to Markdown format, and saves everything to a single file for offline reference.

## Features

- Deep crawling with configurable depth and page limits
- Domain filtering to stay within specific websites
- Automatic handling of error pages and invalid content
- Markdown conversion of all crawled content

## Requirements

- Python 3.7+
- crawl4ai library

## Usage

Simply run the script:

```python
python basic-deepcrawl.py
```

The script will:
1. Start crawling from https://docs.crawl4ai.com
2. Follow links within the crawl4ai.com domain
3. Extract documentation content
4. Save all content to basic-deepcrawl.md

## Configuration

You can modify these parameters in the code:
- `max_depth`: How deep to crawl (default: 100)
- `max_pages`: Maximum number of pages to crawl (default: 1000)
- `allowed_domains`: Domains to restrict crawling to

## Credits

This tool relies on the [crawl4ai](https://docs.crawl4ai.com) library for web crawling functionality.
