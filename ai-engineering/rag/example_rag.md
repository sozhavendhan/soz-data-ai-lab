# RAG example (outline)

Retrieval-Augmented Generation (RAG) basic steps:

1. Prepare a corpus and split into passages.
2. Compute embeddings for each passage and store them in a vector index (FAISS, Milvus, etc.).
3. Given a user query, retrieve top-k relevant passages.
4. Feed retrieved passages + query to the LLM with an instruction to ground its answers on the passages.

This repo contains links and small examples to get started; adapt the storage and embedding provider to your environment.
