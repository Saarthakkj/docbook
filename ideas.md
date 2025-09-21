## Practical GraphRAG / KG-RAG Ideas (from arXiv)

Each entry includes the paper link, brief info, how it works, and concrete integration ideas for this repo (see `deepcrawl.py`, `graphrag.py`, `main.py`).

### 1) LEGO-GraphRAG: Modularizing Graph-based Retrieval-Augmented Generation for Design Space Exploration
[arXiv:2411.05844](http://arxiv.org/abs/2411.05844v3)
- **info**: Proposes a modular GraphRAG framework enabling plug-and-play components and ablations across stages (indexing, retrieval, reasoning).
- **how it works**: Decouples graph construction, retrieval, expansion, and generation with configuration-driven choices per module.
- **how to integrate**:
  - Refactor `graphrag.py` `GraphRAGSystem` into clear modules/interfaces: `Retriever`, `GraphExpander`, `Reranker`, `AnswerGenerator` with a config in `main.py`.
  - Add a registry pattern to toggle between keyword vs embedding retrieval in `_find_relevant_urls()` and neighbor strategies in `_expand_context_with_graph()`.

### 2) PolyG: Effective and Efficient GraphRAG with Adaptive Graph Traversal
[arXiv:2504.02112](http://arxiv.org/abs/2504.02112v1)
- **info**: Introduces adaptive traversal that selects expansion paths per query and budget, outperforming fixed BFS/DFS.
- **how it works**: Learns/uses heuristics (e.g., keyword overlap, semantic similarity, node centrality) to choose next-hop neighbors under a token/time budget.
- **how to integrate**:
  - In `GraphRAGSystem._expand_context_with_graph`, add a traversal policy that ranks neighbors by a weighted score of (cosine similarity, common keywords, degree/centrality, depth penalty).
  - Add a retrieval budget (tokens or nodes) in `main.py` args; stop expansion when budget is hit.

### 3) KG-Infused RAG: Augmenting Corpus-Based RAG with External Knowledge Graphs
[arXiv:2506.09542](http://arxiv.org/abs/2506.09542v1)
- **info**: Fuses unstructured retrieval with external KGs to improve grounding and coverage.
- **how it works**: Entity/link detection connects text chunks to KG nodes; combines textual evidence with KG triples during retrieval and generation.
- **how to integrate**:
  - In `deepcrawl.py`, add optional entity linking step (e.g., spaCy NER + simple Wikidata lookup) storing `entities` per node.
  - Extend `GraphRAGSystem._find_relevant_urls` to also retrieve from linked KG neighbors (stored as metadata) and merge with vector/keyword scores.

### 4) KET-RAG: A Cost-Efficient Multi-Granular Indexing Framework for Graph-RAG
[arXiv:2502.09304](http://arxiv.org/abs/2502.09304v2)
- **info**: Reduces cost via multi-granularity indices and routing, querying fine-grained units only when needed.
- **how it works**: Two-stage retrieval: coarse (page/section) → fine (paragraph/snippet) with gating.
- **how to integrate**:
  - During crawl, store multi-granularity chunks (page → section → paragraph) and precompute embeddings per level.
  - Implement two-stage retrieval in `GraphRAGSystem`: first rank pages/sections; only embed/expand into paragraphs for top-K seeds.

### 5) Walk&Retrieve: Zero-shot RAG via Knowledge Graph Walks
[arXiv:2505.16849](http://arxiv.org/abs/2505.16849v2)
- **info**: Uses guided random walks on the KG to gather compact, relevant subgraphs without supervision.
- **how it works**: Starts from seed nodes derived from query terms/entities; performs biased walks to collect paths as context.
- **how to integrate**:
  - Add `walk_based_retrieval(query, seeds, steps, bias)` that samples paths from the NetworkX graph in `graphrag.py`.
  - Use keyword/embedding similarity as transition bias; materialize unique nodes/edges from visited paths into the context.

### 6) Empowering GraphRAG with Knowledge Filtering and Integration
[arXiv:2503.13804](http://arxiv.org/abs/2503.13804v1)
- **info**: Improves GraphRAG by filtering noisy knowledge and integrating signals before generation.
- **how it works**: Node/edge quality estimation; prune or down-weight low-signal parts; integrate multi-source knowledge consistently.
- **how to integrate**:
  - Compute and store a `quality_score` per node/edge (signals: text length, dedup %, similarity to root domain, outbound degree anomalies).
  - During retrieval and expansion, weight scores by `quality_score`; drop nodes below a threshold.

### 7) When to use Graphs in RAG: A Comprehensive Analysis
[arXiv:2506.05690](http://arxiv.org/abs/2506.05690v1)
- **info**: Provides criteria for when GraphRAG beats vanilla RAG (e.g., multi-hop, hierarchical, entity-rich queries).
- **how it works**: Empirical analysis across tasks shows benefits w.r.t. structure and reasoning depth.
- **how to integrate**:
  - Add a routing policy in `main.py`: detect entity density, query length, and estimated hop depth; choose between vector-only, graph-only, or hybrid pipeline.
  - Log decisions to compare outcomes across policies.

### 8) GraphRAG under Fire
[arXiv:2501.14050](http://arxiv.org/abs/2501.14050v3)
- **info**: Evaluates GraphRAG robustness against poisoning/attacks; proposes defenses.
- **how it works**: Identifies attack surfaces (malicious pages, link spam) and mitigation (provenance, trust scoring, anomaly detection).
- **how to integrate**:
  - Track provenance per node (crawl timestamp, domain, referrer). Add a `trust_score` combining domain whitelist/blacklist and anomaly scores.
  - Filter/rerank retrieval by `trust_score`; add simple content sanitization (strip scripts/iframes) in `deepcrawl.py` extraction.

### 9) GraphRAG-Bench: Challenging Domain-Specific Reasoning Benchmark
[arXiv:2506.02404](http://arxiv.org/abs/2506.02404v3)
- **info**: Benchmark focusing on domain-specific, multi-step reasoning for GraphRAG.
- **how it works**: Curates tasks requiring graph traversal, cross-page synthesis, and hierarchical context.
- **how to integrate**:
  - Create a small benchmark YAML/JSON in `output/bench/` with question → gold citations → expected hops from your crawled docs.
  - Add `--eval bench.json` flag in `main.py` to run batch evaluation and record metrics (EM, F1, citation-precision).

### 10) Know3-RAG: Knowledge-aware RAG with Adaptive Retrieval, Generation, and Filtering
[arXiv:2505.12662](http://arxiv.org/abs/2505.12662v1)
- **info**: Iterative pipeline adaptively retrieves, generates, and filters content to reduce hallucinations.
- **how it works**: Uses a control loop: retrieve → generate → evidence-check → refine retrieval.
- **how to integrate**:
  - Add an optional iterative loop in `GraphRAGSystem.retrieve_and_generate`: after first answer, run a verifier that checks citation span overlap; if low, trigger another retrieval round with adjusted seeds.
  - Introduce a lightweight reranker (e.g., cosine + keyword + trust score) before generation.

---

### General quick wins for this codebase
- **Budgeted expansion**: Add `--token_budget` and trim contexts by highest utility-per-token.
- **Neighbor selection**: Blend cosine similarity with `common_keywords` and centrality for picking neighbors.
- **Provenance & trust**: Store `provenance`, `trust_score` in HDF5; use in ranking.
- **Two-stage retrieval**: Coarse (page/section) → fine (paragraph) to cut cost.
- **Evaluation harness**: Batch mode with saved prompts/contexts for reproducibility and metric logging.


