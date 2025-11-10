# Video 6: Compare Local vs Cloud Embeddings

## Objective
Compute top-5 overlap between local and cloud embeddings for a set of queries and save results.

The embeddings in `cloud_baseline.json` were generated using:
```python
corpus = [
    {"id": "doc1", "text": "This is the first document."},
    {"id": "doc2", "text": "This is the second document."},
]
```

The query embeddings in `queries.json` were generated using:
```python
queries = [
    {"id": "query1", "text": "first document"},
    {"id": "query2", "text": "first text example"},
    {"id": "query3", "text": "second example"},
]
```

## Steps

1. Inspect the comparison script:
   ```bash
   cat compare_embeddings.py
   ```

2. Run the script for top-5 overlap:
   ```bash
   python compare_embeddings.py --local_index ../video-5-build-faiss-index-knn-retrieval/index.faiss \
       --cloud cloud_baseline.json --queries queries.json --k 5 --out results_top5.json
   ```

3. (Optional) Run the script for top-2 overlap (demonstrates two-document corpus):
   ```bash
   python compare_embeddings.py --local_index ../video-5-build-faiss-index-knn-retrieval/index.faiss \
       --cloud cloud_baseline.json --queries queries.json --k 2 --out results_top2.json
   ```

4. Review results:
   ```bash
   cat results_top5.json
   cat results_top2.json
   ```

## Troubleshooting

- **Dimension mismatch**: ensure local index and cloud embeddings have the same embedding size.
- **Silent failures**: add `--verbose` to debug loading issues.
