# Lesson 4: Alternatives and the Open-Source Ecosystem - Videos

This repository contains 7 practical video demos for Lesson 4, covering environment setup, Docker quickstart, embedding inference, batching and resource logging, FAISS indexing and retrieval, comparison of local vs cloud embeddings, and RAG end-to-end integration.

## Structure

- `video-1-setup-local-python-env/` : Prepare local Python environment and install dependencies
- `video-2-docker-cpu-gpu-quickstart/` : Run local model in Docker (CPU & GPU)
- `video-3-load-sentence-transformers-notebook/` : Load a Sentence-Transformers model and run single-batch inference
- `video-4-batch-inference-resource-logging/` : Batch inference with latency measurement and resource logging
- `video-5-build-faiss-index-knn-retrieval/` : Build FAISS index and run k-NN queries
- `video-6-compare-local-vs-cloud-embeddings/` : Compare local vs cloud embeddings and compute top-5 overlap
- `video-7-local-rag-integration/` : Replace cloud embeddings with local FAISS-based retrieval and run end-to-end RAG pipeline

## Setup

1. Install Python dependencies for each video folder, for example:
   ```bash
   cd video-1-setup-local-python-env
   pip install -r requirements.txt
   ```
2. For videos using Docker, ensure you have Docker and optionally NVIDIA Container Toolkit installed.
3. Copy the example environment file and set any required variables:
   ```bash
   cp .env.example .env
   ```
4. Follow each video's `README.md` for detailed reproducible steps.

---
