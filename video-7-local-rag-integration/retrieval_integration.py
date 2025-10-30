import argparse
import json
from sentence_transformers import SentenceTransformer
import faiss

def fetch_local_embeddings(query, index_path):
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    emb = model.encode([query], show_progress_bar=False)
    faiss.normalize_L2(emb)
    index = faiss.read_index(index_path)
    D, I = index.search(emb.astype("float32"), 5)
    return [int(i) for i in I[0]]

def generate_answer(query, retrieved_docs):
    return f"Answer for query: {query} with docs {retrieved_docs}"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--queries", type=str, required=True)
    parser.add_argument("--index", type=str, required=True)
    parser.add_argument("--out", type=str, default="run_output.json")
    args = parser.parse_args()

    with open(args.queries) as f:
        queries_data = json.load(f)
    results = []
    for q in queries_data:
        q_text = q.get("query") or q.get("id")
        docs = fetch_local_embeddings(q_text, args.index)
        ans = generate_answer(q_text, docs)
        results.append({"query": q_text, "retrieved_doc_ids": docs, "generated_answer": ans})
    with open(args.out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved end-to-end outputs to {args.out}")

if __name__ == "__main__":
    main()
