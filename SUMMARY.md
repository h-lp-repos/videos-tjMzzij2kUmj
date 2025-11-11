# Repository Summary

This repository contains demo materials for *Lesson 4: Alternatives and the Open-Source Ecosystem* video series. Each `video-<n>-*` folder includes self-contained code, sample data, and instructions for one demo.

## Top-level files and folders

- `.env.example`: example environment variables file (do not commit secrets)
- `.gitignore`: common files and folders to ignore
- `README.md`: high-level overview
- `video-1-setup-local-python-env/`
- `video-2-docker-cpu-gpu-quickstart/`
- `video-3-load-sentence-transformers-notebook/`
- `video-4-batch-inference-resource-logging/`
- `video-5-build-faiss-index-knn-retrieval/`
- `video-6-compare-local-vs-cloud-embeddings/`
- `video-7-local-rag-integration/`

## Folder details

### video-1-setup-local-python-env/
- `README.md`: setup Python venv or conda and install dependencies
- `requirements.txt`: dependencies (sentence-transformers, faiss-cpu, psutil, numpy)
- `run_local_embeddings.py`: script to verify model import and inference

### video-2-docker-cpu-gpu-quickstart/
- `README.md`: Docker (CPU & GPU) quickstart instructions
- `Dockerfile`, `docker-compose.cpu.yml`, `docker-compose.gpu.yml`: container configs
- `app.py`: example model-serving application
- `requirements.txt`: Python dependencies for container

### video-3-load-sentence-transformers-notebook/
- `README.md`: instructions for Jupyter notebook demo
- `local_embedding_inference.ipynb`: notebook to load model and encode text
- `requirements.txt`: notebook dependencies

### video-4-batch-inference-resource-logging/
- `README.md`: batch timing and memory logging demo
- `time_inference.py`: timing wrapper script
- `metrics.json`: sample output with p50/p95 latency and peak memory
- `requirements.txt`: dependencies (psutil)

### video-5-build-faiss-index-knn-retrieval/
- `README.md`: FAISS indexing and k‑NN retrieval demo
- `corpus.json`: sample corpus with document IDs and text
- `retrieval_integration.py`: build/save index and run queries
- `requirements.txt`: dependencies (faiss-cpu)

### video-6-compare-local-vs-cloud-embeddings/
- `README.md`: comparison of local vs cloud embeddings
- `cloud_baseline.json`: sample cloud embeddings baseline
- `compare_embeddings.py`: script to compute top‑5 overlap
- `queries.json`: sample queries for comparison
- `requirements.txt`: dependencies

### video-7-local-rag-integration/
- `README.md`: local RAG integration demo instructions
- `generator_stub.py`: stub generator for end-to-end demo
- `retrieval_integration.py`: modified retrieval code using FAISS
- `queries.json`: sample queries for RAG demo
- `run_output.json`: sample run output with retrieved IDs and generated answers
- `requirements.txt`: dependencies (sentence-transformers, faiss-cpu)

## Running demos

Each video folder has detailed steps in its `README.md`. From the repo root:

```bash
cd video-1-setup-local-python-env
# follow instructions to create env, install deps, and run scripts
```

Repeat for other video folders (`video-2-...` through `video-7-...`).

*Note*: There is no unified test suite; the demos produce artifact files (embeddings.npz, index.faiss, metrics.json, results.json, run_output.json) as checkpoints for verification.
