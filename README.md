
# DocBook: GraphRAG Documentation Assistant
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Saarthakkj/docbook)


A Python-based system that crawls documentation websites using Crawl4AI, builds a knowledge graph with embeddings and relationships, and provides intelligent question-answering capabilities using Retrieval-Augmented Generation (RAG) powered by Google's Gemini API.

## Project Overview

DocBook is designed to create an intelligent assistant for any documentation website. It performs a deep crawl of the target site, extracts content, builds a structured knowledge graph with semantic embeddings, and enables natural language querying of the documentation using an enhanced GraphRAG implementation.

Key technical aspects:
- **Crawling**: Uses Crawl4AI for asynchronous, depth-limited crawling with content extraction.
- **Graph Construction**: Builds a hierarchical graph with nodes representing pages, including metadata like depth, score, keywords (extracted via TextRank), and embeddings (using Sentence Transformers).
- **RAG System**: Combines keyword matching, semantic similarity (cosine similarity on embeddings), and graph traversal for context retrieval, followed by generation using Gemini API.
- **Persistence**: Saves knowledge graphs as HDF5 for reuse, avoiding repeated crawls.

## Features

- **Asynchronous Deep Crawling**: BFS-based crawling with configurable max depth and pages, skipping 404 errors.
- **Keyword Extraction**: Uses TextRank (from summa library) with fallback to frequency-based method for robustness.
- **Embeddings**: Generates vector embeddings using 'all-MiniLM-L6-v2' model from Sentence Transformers.
- **Knowledge Graph**: Directed graph with NAVIGATES_TO relationships, including common keywords and semantic similarity scores.
- **Multi-Method Retrieval**: Combines keyword indexing, semantic similarity, and graph expansion for relevant context.
- **Interactive Q&A**: Command-line interface for querying with 'quit' to exit.
- **Testing**: Dedicated test script with sample queries.
- **Logging**: Timestamped logging utility.

## Architecture and Technical Details

### Core Components

1. **deepcrawl.py** (457 lines):
   - Implements BFS deep crawling using Crawl4AI's AsyncWebCrawler.
   - Configurable via CLI args: --url, --max_depth, --max_pages, --output_dir, --name.
   - Builds a Graph dataclass with GraphNode objects (url, content, depth, keywords, embedding, children).
   - Extracts keywords using TextRank or fallback frequency analysis (ignores stop words, min word length 3).
   - Creates embeddings with SentenceTransformer.
   - Constructs edges with common keywords and semantic similarity (ratio of common keywords).
   - Saves graph to HDF5 format in output_dir with metadata (total_nodes, max_depth, root_url).
   - Includes print_graph_structure for visualizing the graph with stats (depth distribution, connectivity).

2. **enhanced_graphrag.py** (631 lines):
   - Defines EnhancedEntity and EnhancedRelationship dataclasses.
   - EnhancedGraphRAGSystem class:
     - Initializes with graph, Gemini API key; loads SentenceTransformer and Gemini model.
     - Builds NetworkX DiGraph from entities/relationships.
     - Keyword index: defaultdict of keyword to list of URLs.
     - load_from_kg_json: Creates entities from nodes, relationships from edges, builds graph.
     - retrieve_and_generate: Finds relevant URLs (keyword + semantic scores), expands with graph neighbors, generates answer via LLM.
     - _find_relevant_urls: Combines keyword scores (overlap count), cosine similarity on embeddings.
     - _expand_context_with_graph: Adds top 2 neighbors per seed URL, collects important relationships.
     - _generate_enhanced_answer: Constructs detailed prompt with context sections, relationships, and instructions for LLM.

3. **main.py** (256 lines):
   - Parses CLI args: --url (required), --max_depth, --max_pages, --output_dir (required), --name (required).
   - Checks for existing {name}_kg.h5; if not, runs deepcrawl and saves.
   - Initializes EnhancedGraphRAGSystem from graph.
   - Enters interactive loop: Prompts for questions, uses retrieve_and_generate, exits on 'quit'.

4. **time_logger.py** (28 lines):
   - Sets up logging with ISO-8601 timestamps, INFO level, stdout handler.
   - Reuses logger instance to avoid multiple handlers.

5. **test_graphrag.py** (65 lines):
   - Tests GraphRAG with sample queries (e.g., "How do I install Crawl4AI?").
   - Initializes from kg.h5, runs queries asynchronously with 1s delay.

### How It Works (Step-by-Step)

1. **Crawling (deepcrawl.py)**:
   - Starts BFS from root URL, limits by depth/pages.
   - Extracts markdown content, skips invalid pages.
   - Builds tree structure, extracts keywords/embeddings.
   - Computes edges with similarities.

2. **Graph Loading (enhanced_graphrag.py)**:
   - Loads nodes as entities, edges as relationships.
   - Builds keyword index and NetworkX graph.

3. **Querying (main.py + enhanced_graphrag.py)**:
   - Find relevant URLs: Keyword overlap + embedding similarity.
   - Expand: Add neighbors via graph traversal.
   - Generate: Prompt Gemini with structured context (entities, snippets, relationships).

## Installation

### Prerequisites
- Python 3.8+
- Google Gemini API key (from https://makersuite.google.com/app/apikey)

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/your-org/docbook.git
   cd docbook
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   - Key deps: crawl4ai[all], sentence-transformers, networkx, scikit-learn, summa, spacy, google-genai, h5py, etc.
   - Install spaCy model: `python -m spacy download en_core_web_sm`

3. Set environment variables in `.env`:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

### Basic Crawl and Query
Crawl and start interactive Q&A:
