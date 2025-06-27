# DocBook: GraphRAG Documentation Assistant

A Python-based GraphRAG system that crawls documentation websites and provides intelligent Q&A using Google's Gemini API. Crawls any documentation site, builds a knowledge graph, and answers questions using RAG (Retrieval-Augmented Generation).

## Features

- **Website Documentation Crawling**: Uses Crawl4AI to extract content from documentation sites
- **Knowledge Graph Generation**: Builds interconnected knowledge graphs from crawled content
- **Enhanced GraphRAG**: Combines keyword matching, semantic similarity, and graph relationships
- **Interactive Q&A**: Ask questions and get contextual answers from the documentation
- **Persistent Storage**: Saves knowledge graphs for fast subsequent runs

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements_graphrag.txt
```

### 2. Set up Environment Variables

Create a `.env` file in the project root:

```bash
# Required: Get your API key from https://makersuite.google.com/app/apikey
gemini_api_key=your_gemini_api_key_here
```

### 3. Install Spacy Language Model (if needed)

```bash
python -m spacy download en_core_web_sm
```

## Usage

### Quick Start

Crawl documentation and start interactive Q&A:

```bash
python main.py --url https://docs.crawl4ai.com/
```

### Custom Parameters

```bash
python main.py --url https://docs.example.com/ --max_depth 3 --max_pages 50
```

### Parameters

- `--url`: Documentation URL to crawl (required)
- `--max_depth`: Maximum crawl depth (optional)
- `--max_pages`: Maximum number of pages to crawl (optional)

### Example Session

```bash
$ python main.py --url https://docs.crawl4ai.com/

🚀 Starting GraphRAG Implementation
============================================================
📂 Loading knowledge graph from kg.json...
✅ Loaded knowledge graph:
   - Nodes: 45
   - Edges: 120
   - Root URL: https://docs.crawl4ai.com/

🤖 GraphRAG Query Interface Ready!
Ask questions about the Crawl4AI documentation.
Type 'quit' to exit.

🔍 Enter your question: How do I install Crawl4AI?

📝 Answer:
You can install Crawl4AI using pip:
```pip install crawl4ai```

For the latest features, install from the main branch:
```pip install git+https://github.com/unclecode/crawl4ai.git```
...
```

## How It Works

1. **Deep Crawling**: Extracts content from documentation websites using Crawl4AI
2. **Knowledge Graph**: Builds interconnected graph of pages with relationships
3. **Embeddings**: Creates vector embeddings for semantic similarity search
4. **GraphRAG Query**: Combines keyword matching, semantic search, and graph traversal
5. **Answer Generation**: Uses Google Gemini to generate contextual answers

## Files

- `main.py` - Main application entry point
- `deepcrawl.py` - Documentation crawler using Crawl4AI
- `enhanced_graphrag.py` - GraphRAG implementation with embeddings
- `requirements_graphrag.txt` - Python dependencies
- `kg.json` - Generated knowledge graph (created after first run)
- `enhanced_kg.json` - Enhanced knowledge graph with embeddings

## Requirements

- Python 3.8+
- Google Gemini API key
- Internet connection for crawling

## Dependencies

Key Python libraries (see `requirements_graphrag.txt` for full list):

```
google-generativeai>=0.7.0    # Gemini API
sentence-transformers>=2.2.0   # Embeddings
networkx>=3.0                  # Graph processing
crawl4ai[all]>=0.6.0          # Web crawling
scikit-learn>=1.3.0           # ML utilities
spacy>=3.7.0                  # NLP processing
```

## License

MIT License
