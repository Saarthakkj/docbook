
# DocBook: GraphRAG Documentation Assistant
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Saarthakkj/docbook)


A Python-based system that crawls documentation websites using Crawl4AI, builds a knowledge graph with embeddings and relationships, and provides intelligent question-answering capabilities using Retrieval-Augmented Generation (RAG) powered by Google's Gemini API.

## Project Overview

DocBook is designed to create an intelligent assistant for any documentation website. It performs a deep crawl of the target site, extracts content, builds a structured knowledge graph with semantic embeddings, and enables natural language querying of the documentation using an enhanced GraphRAG implementation.

Key technical aspects:
- **Crawling**: Uses Crawl4AI for asynchronous, depth-limited crawling with content extraction.
- **Graph Construction**: Builds a hierarchical graph with nodes representing pages, including metadata like depth, keywords (extracted via TextRank), and embeddings (using Sentence Transformers).
- **RAG System**: Combines keyword matching, semantic similarity (cosine similarity on embeddings), and graph traversal for context retrieval, followed by generation using Gemini API.
- **Persistence**: Saves knowledge graphs as HDF5 for efficient storage and reuse, avoiding repeated crawls.

## Features

- **Asynchronous Deep Crawling**: BFS-based crawling with configurable max depth and pages, skipping 404 errors.
- **Keyword Extraction**: Uses TextRank (from summa library) with fallback to frequency-based method for robustness.
- **Embeddings**: Generates vector embeddings using 'all-MiniLM-L6-v2' model from Sentence Transformers.
- **Knowledge Graph**: Directed graph with NAVIGATES_TO relationships, including common keywords and semantic similarity scores.
- **Multi-Method Retrieval**: Combines keyword indexing, semantic similarity, and graph expansion for relevant context.
- **Interactive Q&A**: Command-line interface for querying with 'quit' to exit.
- **HDF5 Storage**: Efficient binary format for storing large graphs with metadata, embeddings, and hierarchical structure.

## Architecture and Technical Details

### Core Components

1. **deepcrawl.py**:
   - **GraphNode dataclass**: Represents nodes with url, content, depth, keywords, embedding, and children list.
   - **Graph dataclass**: Contains nodes dict, edges list, and metadata dict with total_nodes, max_depth, root_url.
   - **Deep crawling**: Uses BFS strategy with AsyncWebCrawler, configurable depth/page limits.
   - **Keyword extraction**: Primary method uses TextRank via `extract_keywords_textrank()`, fallback to frequency-based analysis.
   - **Embeddings**: Creates embeddings using SentenceTransformer('all-MiniLM-L6-v2').
   - **Edge computation**: Calculates semantic similarity as ratio of common keywords between parent-child nodes.
   - **HDF5 persistence**: `save_graph_hdf5()` stores graph in hierarchical format with metadata, nodes (with embeddings/keywords), and edges.
   - **Graph utilities**: `print_graph_structure()` for visualization, `find_parent_node()` for tree traversal.

2. **graphrag.py**:
   - **EnhancedEntity**: Dataclass with source_urls, keywords, content_snippet, embedding, depth, score.
   - **EnhancedRelationship**: Dataclass with source, target, source_urls, common_keywords, semantic_similarity.
   - **EnhancedGraphRAGSystem**: Main RAG class with:
     - Initialization with Graph object and Gemini API key
     - SentenceTransformer model loading for embeddings
     - NetworkX DiGraph construction for graph operations
     - Keyword index (defaultdict) mapping keywords to URL lists
     - `load_from_kg_json()`: Creates entities from GraphNodes, relationships from edges
     - `retrieve_and_generate()`: Main query method combining retrieval and generation
     - `_find_relevant_urls()`: Multi-score ranking (keyword overlap + cosine similarity)
     - `_expand_context_with_graph()`: Graph traversal to add neighbor nodes (top 2 per seed)
     - `_generate_enhanced_answer()`: Constructs detailed prompt with context sections for LLM

3. **main.py**:
   - **CLI argument parsing**: Required args (--url, --output_dir, --name), optional (--max_depth, --max_pages).
   - **Graph persistence check**: Looks for existing `{name}_kg.h5` file to avoid re-crawling.
   - **Crawling workflow**: If no existing graph, runs `deepcrawl.deep_crawl()` and saves with `save_graph_hdf5()`.
   - **Graph loading**: Uses `load_graph_hdf5()` to reconstruct Graph object from HDF5.
   - **RAG initialization**: Creates EnhancedGraphRAGSystem from loaded graph.
   - **Interactive loop**: Continuous Q&A interface with error handling and 'quit' command.
   - **Debug utilities**: `debug_save_process()` and `inspect_saved_graph()` for troubleshooting.

### How It Works (Step-by-Step)

1. **Crawling Phase**:
   - BFS traversal starting from root URL with depth/page limits
   - Content extraction to markdown, keyword extraction via TextRank
   - Embedding generation for each page's content
   - Parent-child relationship establishment with similarity scoring

2. **Graph Construction**:
   - Nodes stored as GraphNode objects with full content and metadata
   - Edges contain semantic similarity scores and common keywords
   - HDF5 storage with hierarchical structure: /metadata, /nodes, /edges

3. **RAG System Loading**:
   - Graph reconstruction from HDF5 into memory
   - Entity creation from nodes, relationship mapping from edges
   - NetworkX graph building for efficient traversal
   - Keyword index construction for fast lookup

4. **Query Processing**:
   - Keyword matching and embedding similarity scoring
   - Graph expansion to include relevant neighbors
   - Context compilation with entities, relationships, and content snippets
   - LLM generation with structured prompt including instructions and context

## Installation

### Prerequisites
- Python 3.8+
- uv (fast Python package manager and environment tool)
- Google Gemini API key (from https://ai.dev/apikey)

### Steps (using uv)
1. Clone the repository:
   ```
   git clone https://github.com/your-org/docbook.git
   cd docbook
   ```

2. Install uv (if not already installed):
   ```
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Create and activate a virtual environment:
   ```
   uv venv .venv
   . .venv/bin/activate
   ```

4. Install dependencies with uv:
   ```
   uv pip install -r requirements.txt
   ```

5. Set environment variables in `.env`:
   ```
   gemini_api_key=your_api_key_here
   ```
