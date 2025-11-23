# Docbook Improvement Plan

This document outlines a comprehensive plan to improve the `docbook` tool, focusing on software engineering best practices, CLI experience, agent integration, and advanced GraphRAG capabilities.

## 1. Software Design & Architecture

### **Current Issues**
- **Monolithic Scripts**: `deepcrawl.py` and `graphrag.py` mix logic, data definitions, and execution.
- **Hardcoded Dependencies**: Service instantiation happens inside classes.
- **Print Debugging**: Extensive use of `print()` instead of structured logging.
- **Global State**: Reliance on global variables and top-level execution code.

### **Proposed Refactoring**
1.  **Package Structure**:
    ```text
    docbook/
    ├── src/
    │   └── docbook/
    │       ├── __init__.py
    │       ├── cli.py            # Entry point (Typer)
    │       ├── config.py         # Pydantic settings
    │       ├── core/             # Core logic
    │       │   ├── graph.py      # Graph data structures
    │       │   └── storage.py    # HDF5/Database IO
    │       ├── crawler/          # Crawling logic
    │       │   └── deepcrawl.py
    │       ├── rag/              # RAG & Retrieval logic
    │       │   ├── graphrag.py
    │       │   └── embeddings.py
    │       └── agent/            # Agentic interfaces
    │           └── tools.py
    ├── pyproject.toml            # Dependency management
    └── README.md
    ```

2.  **Dependency Injection**:
    - Pass `LLMClient`, `EmbeddingModel`, and `Storage` instances into classes rather than creating them inside.
    
3.  **Configuration Management**:
    - Use `pydantic-settings` to manage `.env` and CLI args.
    
4.  **Logging**:
    - Replace `print` with standard `logging` or `structlog` for better observability.

## 2. CLI Experience (The "Good CLI" Goal)

Switch from `argparse` to **Typer** or **Click** for a modern, composable CLI with rich help and auto-completion.

### **Proposed Commands**
```bash
# Crawl a documentation site
docbook crawl https://docs.example.com --name "example-docs" --depth 2 --output ./data

# Query the knowledge graph via CLI
docbook ask "How do I configure auth?" --kg ./data/example-docs_kg.h5

# Start an API server for agents
docbook serve --kg ./data/example-docs_kg.h5 --port 8000

# Inspect graph stats
docbook inspect ./data/example-docs_kg.h5
```

## 3. Minimal Coding Agent

To enable a "minimal coding agent that can fetch docs content," we need to expose the Knowledge Graph (KG) as a **Tool** that an LLM can call.

### **Design**
1.  **Tool Interface**: Define a standard Python interface `DocsTool`:
    - `search(query: str) -> List[Node]`
    - `read_node(url: str) -> str`
    - `get_related(url: str) -> List[Node]`

2.  **Agent Loop**:
    - Use a lightweight ReAct (Reasoning + Acting) loop.
    - **Prompt**: "You are a coding assistant. Use `search_docs` to find API references. Read the content before writing code."
    - **Implementation**:
    ```python
    class DocAgent:
        def __init__(self, kg_path):
            self.rag = load_graphrag(kg_path)
            
        def solve(self, task):
            # 1. Plan
            # 2. Call rag.retrieve_and_generate() or specific lookup tools
            # 3. Generate Code
    ```

## 4. Advanced GraphRAG Architecture (Research-Backed)

Current implementation uses a basic "Keyword + Semantic" retrieval on a tree structure. We can improve this with recent research findings.

### **A. Hybrid Construction (NLP + LLM)**
Instead of relying solely on LLMs for extraction (slow/expensive) or simple TextRank (low context), use a hybrid approach:
-   **Fast Entity Extraction**: Use **GliNER** (Generalist Model for Named Entity Recognition) or **Spacy** to extract entities (Functions, Classes, Constants) from code blocks and text.
-   **LLM refinement**: Only use LLM to summarize complex relationships between high-level entities.

### **B. Community Summarization (Microsoft GraphRAG style)**
-   **Cluster Nodes**: Use **Leiden** or **Louvain** algorithms to detect communities of related nodes (e.g., "Authentication Module", "Database Drivers").
-   **Hierarchical Summaries**: Generate summaries for these clusters.
-   **Retrieval**: Match query against *cluster summaries* first, then drill down to specific nodes. This answers "global" questions (e.g., "How is error handling structured?") better than simple similarity search.

### **C. Agentic Graph Traversal (Graph-of-Thoughts)**
Instead of a single retrieval step:
1.  **Start**: Search entry nodes (high similarity).
2.  **Navigate**: The Agent sees the node's content and its *outgoing edges* (links).
3.  **Decide**: The Agent decides whether to:
    -   Stop and answer.
    -   Follow a link ("This mentions `AuthConfig`, let me check that node").
    -   Backtrack.
This mimics how a human reads documentation (following hyperlinks).

### **D. Improved Embedding Strategy**
-   **Code-Aware Embeddings**: Use models trained on code (e.g., `jina-embeddings-v2-base-code` or `unixcoder`) for code snippets, rather than generic text embeddings (`all-MiniLM`).
-   **Late Interaction (ColBERT)**: If performance allows, use ColBERT-style token-level interaction for higher precision fetching.

## 5. Implementation Roadmap

1.  **Refactor**: Move current code into `src/` structure and switch to `Typer`.
2.  **Upgrade Graph**: Modify `deepcrawl` to use **GliNER** for better entity tagging during crawl.
3.  **Agent API**: Create the `DocsTool` class and a simple `docbook serve` endpoint.
4.  **Advanced RAG**: Implement "Community Summarization" as a post-processing step after crawling.

