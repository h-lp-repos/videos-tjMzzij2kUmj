import numpy as np
import faiss
import json
import argparse

def main():
    parser = argparse.ArgumentParser(description="FAISS indexing and k-NN retrieval demo")
    parser.add_argument("--embeddings", type=str, default="../video-3-load-sentence-transformers-notebook/embeddings.npz")
    parser.add_argument("--corpus", type=str, default="corpus.json")
    parser.add_argument("--k", type=int, default=5)
    parser.add_argument("--output", type=str, default="knn_results.json")
    args = parser.parse_args()

    data = np.load(args.embeddings)
    embeddings = data["embeddings"].astype("float32")
    with open(args.corpus, "r") as f:
        corpus = json.load(f)
    ids = [doc["id"] for doc in corpus]

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    faiss.normalize_L2(embeddings)
    index.add(embeddings)
    print(f"Built index with {index.ntotal} vectors")

    queries = embeddings[:3]
    faiss.normalize_L2(queries)
    D, I = index.search(queries, args.k)
    results = []
    for i, (dists, inds) in enumerate(zip(D, I)):
        results.append({
            "query_id": ids[i],
            "neighbor_ids": [ids[j] for j in inds],
            "distances": dists.tolist()
        })
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved results to {args.output}")

if __name__ == "__main__":
    main()
