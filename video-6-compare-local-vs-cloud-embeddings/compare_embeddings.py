import json
import argparse
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def load_cloud_embeddings(path):
    with open(path) as f:
        data = json.load(f)
    ids = [item["id"] for item in data]
    embs = np.array([item["embedding"] for item in data], dtype="float32")
    return ids, embs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local_index", type=str, required=True)
    parser.add_argument("--cloud", type=str, required=True)
    parser.add_argument("--queries", type=str, required=True)
    parser.add_argument("--k", type=int, default=5)
    parser.add_argument("--out", type=str, default="results.json")
    args = parser.parse_args()

    index = faiss.read_index(args.local_index)
    cloud_ids, cloud_embs = load_cloud_embeddings(args.cloud)
    dim = cloud_embs.shape[1]

    with open(args.queries) as f:
        queries_data = json.load(f)
    query_ids = [q["id"] for q in queries_data]
    query_embs = np.array([q["embedding"] for q in queries_data], dtype="float32")

    faiss.normalize_L2(query_embs)
    D_local, I_local = index.search(query_embs, args.k)
    index_cloud = faiss.IndexFlatIP(dim)
    faiss.normalize_L2(cloud_embs)
    index_cloud.add(cloud_embs)
    faiss.normalize_L2(query_embs)
    D_cloud, I_cloud = index_cloud.search(query_embs, args.k)

    results = []
    for qi, qid in enumerate(query_ids):
        local_top5 = [cloud_ids[i] for i in I_local[qi]]
        cloud_top5 = [cloud_ids[i] for i in I_cloud[qi]]
        overlap = len(set(local_top5).intersection(set(cloud_top5)))
        percent = overlap / args.k * 100
        results.append({
            "query_id": qid,
            "local_top5": local_top5,
            "cloud_top5": cloud_top5,
            "overlap_count": overlap,
            "overlap_percentage": percent
        })
    with open(args.out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved comparison results to {args.out}")

if __name__ == "__main__":
    main()
