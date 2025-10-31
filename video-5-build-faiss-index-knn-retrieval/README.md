# Video 5: FAISS Indexing & k-NN Retrieval

## Objective
Index the produced embeddings into a FAISS index, save the index to disk, and perform top-5 k-NN queries.

## Steps

1. Load embeddings and corpus mapping:
   ```bash
   cat corpus.json
   ```
2. Run the retrieval script (this will build the index and save it as `index.faiss`):
   ```bash
   python retrieval_integration.py --embeddings ../video-3-load-sentence-transformers-notebook/embeddings.npz --corpus corpus.json --k 5 --output knn_results.json
   ```
3. Review index and results:
   ```bash
   ls index.faiss knn_results.json
   cat knn_results.json
   ```

## Troubleshooting

- **Dtype mismatch**: ensure embeddings are float32 and normalized.
- **Memory error**: use chunked adds or IndexIVFFlat for larger datasets.
