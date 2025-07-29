# DocBook: GraphRAG Documentation Assistant
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Saarthakkj/docbook)


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

## gRPC Server Usage

The project includes a gRPC server in the `grpc/` directory that allows remote execution of `main.py` and `deepcrawl.py` scripts.

### Starting the gRPC Server

1. Navigate to the `grpc/` directory:
   ```bash
   cd grpc
   ```

2. Run the server:
   ```bash
   python server.py
   ```
   This starts the gRPC server on `localhost:50051`.

### Using the TypeScript Client

The `grpc/` directory contains a TypeScript client for interacting with the server.

1. Install dependencies (if not already done):
   ```bash
   npm install
   ```

2. To run a script, use or modify `example.ts`. For example, to run `main.py`:

   ```typescript
   import PythonScriptRunner from './client';

   async function runMain() {
     const runner = new PythonScriptRunner();
     const result = await runner.executeScript('main', [
       '--url', 'https://docs.example.com/',
       '--name', 'example'
     ]);
     console.log('Exit code:', result.exitCode);
     console.log('Stdout:', result.stdout);
     console.log('Stderr:', result.stderr);
   }

   runMain();
   ```

3. Run the TypeScript file:
   ```bash
   ts-node example.ts
   ```

   For streaming output (real-time stdout/stderr), use `executeScriptStream` as shown in `example.ts`.

### Running deepcrawl.py via gRPC

Similarly, use script_name 'deepcrawl' with appropriate arguments.

For more details, see `grpc/client.ts` and `grpc/example.ts`.

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
