# Video 6: Compare Local vs Cloud Embeddings

## Objective
Compute top-5 overlap between local and cloud embeddings for a set of queries and save results.

## Steps

1. Inspect the comparison script:
   ```bash
   cat compare_embeddings.py
   ```
2. Run the script:
   ```bash
   python compare_embeddings.py --local_index ../video-5-build-faiss-index-knn-retrieval/index.faiss \
       --cloud cloud_baseline.json --queries queries.json --k 5 --out results.json
   ```
3. Review results:
   ```bash
   cat results.json
   ```

## Troubleshooting

- **Dimension mismatch**: ensure local index and cloud embeddings have the same embedding size.
- **Silent failures**: add `--verbose` to debug loading issues.
