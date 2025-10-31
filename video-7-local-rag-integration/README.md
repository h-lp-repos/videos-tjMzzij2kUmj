# Video 7: Local RAG Integration

## Objective
Integrate local FAISS-based retrieval into a RAG demo, replacing cloud embedding calls, and run 3 end-to-end queries.

## Steps

1. Locate and open the RAG retrieval integration script:
   ```bash
   cat retrieval_integration.py
   ```
2. Replace cloud embedding calls by running local inference + FAISS search.
3. Run the end-to-end script:
   ```bash
   python retrieval_integration.py --queries queries.json --index ../video-5-build-faiss-index-knn-retrieval/index.faiss --out run_output.json
   ```
4. Review outputs:
   ```bash
   cat run_output.json
   ```
5. (Optional) Rollback changes:
   ```bash
   git checkout -- retrieval_integration.py
   ```

## Troubleshooting

- **ID mapping errors**: ensure `retrieved_doc_ids` align with corpus IDs.
- **Missing API key**: use `generator_stub.py` to avoid external dependencies.
