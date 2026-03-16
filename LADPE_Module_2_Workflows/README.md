# Module 2: Retrieval Augmented Generation (RAG)

Reference materials for Module 2 — covering RAG fundamentals, embeddings, and vector databases.

---

## 2.1 Introduction to RAG

### Key Concepts
- **RAG** — a technique that augments LLM responses with retrieved external knowledge to reduce hallucinations and provide up-to-date information
- **RAG Pipeline**: Encoding > Indexing > Query Encoding > Similarity Search > Retrieval > Prompt Augmentation > Generation
- **Document Processing**: ingestion, parsing, chunking, and cleaning/preprocessing
- **Chunking Strategies**: page/paragraph/sentence splitting, recursive chunking, fixed-size with overlap, semantic chunking

### Links from Slides
- Images from [Unstract](https://unstract.com/blog/pdf-hell-and-practical-rag-applications/) illustrating PDF parsing challenges (scanned documents, multi-column layouts, watermarks, forms)

### Further Reading
- [Lewis et al. — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020)](https://arxiv.org/abs/2005.11401) — The original RAG paper
- [LangChain — RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/) — Step-by-step guide to building a RAG pipeline
- [Flowise — RAG with Flowise](https://docs.flowiseai.com/tutorials/rag) — Building RAG applications with Flowise
- [LangChain — Text Splitters](https://python.langchain.com/docs/concepts/text_splitters/) — Implementations of various chunking strategies
- [Greg Kamradt — Semantic Chunking (Video)](https://www.youtube.com/watch?v=8OJC21T2SL4) — Visual explanation of semantic chunking
- [ChunkViz](https://www.chunkviz.com/) — Visualizing Chunks
- [Pinecone - Chunking Strategies for LLM Applications](https://www.pinecone.io/learn/chunking-strategies/) - Chunking Strategies with Pinecone
- [Datacamp - Chunking Strategies for AI and RAG Applications](https://www.datacamp.com/blog/chunking-strategies) - Datacamp blog on Chunking Strategies for AI and RAG Applications

---

## 2.2 Understanding Embeddings

### Key Concepts
- **Embeddings** — vector representations that capture semantic meaning of text
- **Similarity Metrics**: Cosine Similarity (angle-based), Dot Product (magnitude-sensitive), Euclidean Distance (straight-line distance)
- When vectors are normalised, Cosine Similarity and Dot Product produce identical results
- The embedding model (retriever) and the LLM (generator) are two separate models in a RAG system

### Links from Slides
- [Mai Khoi Tieu - Retrieval Augmented Generation (RAG) with Vector Databases](https://tieukhoimai.me/blog/rag-with-vector-db) - Blog write-up on RAG with VectorDBs
- [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — Compare embedding models on standard benchmarks
- [OpenAI Embedding Pricing](https://platform.openai.com/docs/pricing#embeddings) — Current pricing for OpenAI embedding models
- [Google Gemini Embedding Pricing](https://ai.google.dev/gemini-api/docs/pricing#gemini-embedding) — Current pricing for Gemini embedding models

### Further Reading
- [Hugging Face — Embedding Models](https://huggingface.co/models?library=transformers&sort=trending&search=embedding) — Popular open-source library for generating embeddings
- [OpenAI — Embeddings Guide](https://platform.openai.com/docs/guides/embeddings) — Overview of OpenAI's embedding models and usage
- [Pinecone — What are Embeddings?](https://www.pinecone.io/learn/vector-embeddings/) — Beginner-friendly explanation with visuals
- [Jay Alammar — The Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/) — Visual walkthrough of embedding fundamentals
- [Serkan Özal - Vector Search For AI](https://medium.com/@serkan_ozal/vector-similarity-search-53ed42b951d9) - Introduction to various similarity search algorithms
- [IBM - What is Vector Search?](https://www.ibm.com/think/topics/vector-search) - IBM article on What is Vector Search?

---

## 2.3 Vector Indexes and Databases

### Key Concepts
- **Vector Store vs. Vector Index**: a store is a full database (storage, metadata, CRUD); an index is the data structure enabling fast search
- **Flat (Brute Force) Index** — 100% recall but O(n) query time; suitable for <50K vectors
- **Approximate Nearest Neighbours (ANN)**: trade small accuracy loss for large speed gains
  - **LSH (Locality Sensitive Hashing)** — hash-based bucketing using random hyperplanes
  - **HNSW (Hierarchical Navigable Small World)** — graph-based multi-layer structure with near-logarithmic query time and >95% recall
  - Other: IVF-PQ, k-d Tree, Annoy
- **Metadata Filtering** — pre-filtering or post-filtering results by metadata (date, category, permissions)
- **Hybrid Search** — combining keyword search (BM25/sparse) with semantic search (dense vectors) via score fusion

### Links from Slides
- [Infracloud - What are Vector Databases? A Beginner's Guide](https://www.infracloud.io/blogs/vector-databases-beginners-guide/) - Vector Databases Landscape
- [Superlinked — Vector Database Comparison](https://superlinked.com/vector-db-comparison) — Interactive comparison of vector database features

### Further Reading
- [Pinecone - Hierarchical Navigable Small Worlds (HNSW)](https://www.pinecone.io/learn/series/faiss/hnsw/) - How HNSW works
- [Pinecone - Locality Sensitive Hashing (LSH): The Illustrated Guide](https://www.pinecone.io/learn/series/faiss/locality-sensitive-hashing/) - How LSH works
- [Pinecone - Product Quantization: Compressing high-dimensional vectors by 97%](https://www.pinecone.io/learn/series/faiss/product-quantization/) - How PQ works
- [Pinecone — Vector Database Overview](https://www.pinecone.io/learn/vector-database/) — Beginner-friendly intro to vector databases
- [FAISS GitHub Repository](https://github.com/facebookresearch/faiss) — Facebook AI's library for efficient similarity search (supports Flat, IVF, HNSW, PQ)
- [Chroma](https://www.trychroma.com/) — Open-source embedding database, easy to get started
- [Weaviate — Vector Indexing Guide](https://weaviate.io/developers/weaviate/concepts/vector-index) — Explains HNSW and other indexing mechanisms
- [Qdrant](https://qdrant.tech/) — Open-source vector database with filtering and hybrid search
- [Milvus](https://milvus.io/) — Scalable open-source vector database for production workloads
- [Malkov & Yashunin — HNSW Paper (2018)](https://arxiv.org/abs/1603.09320) — The original HNSW algorithm paper
