# Video 3: Single-Batch Inference Notebook

## Objective
Load a Sentence-Transformers model, run inference on a small batch of texts, and save embeddings to disk (`embeddings.npz`).

## Steps

1. Open the notebook:
   ```bash
   jupyter notebook local_embedding_inference.ipynb
   ```
2. Run each cell sequentially:
   - Load model
   - Run inference on sample texts
   - Save embeddings to `embeddings.npz`
3. Verify output:
   ```bash
   ls -lh embeddings.npz
   ```

## Troubleshooting

- **Model download errors**: ensure internet connection or set `LOCAL_FILES_ONLY=True`.
- **Memory issues**: reduce batch size in the notebook.
