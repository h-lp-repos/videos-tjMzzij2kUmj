import time
import psutil
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def main(batch_size=32, n_batches=5):
    print(f"Loading model {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)
    print("Model loaded")

    # Sample texts
    texts = ["This is a test sentence." for _ in range(batch_size)]
    latencies = []
    proc = psutil.Process()
    peak_memory = 0
    start_wall = time.perf_counter()
    for _ in range(n_batches):
        t0 = time.perf_counter()
        embeddings = model.encode(texts, batch_size=batch_size)
        t1 = time.perf_counter()
        latencies.append((t1 - t0) * 1000)
        peak_memory = max(peak_memory, proc.memory_info().rss / (1024 * 1024))
    wall_time = time.perf_counter() - start_wall

    lat_sorted = sorted(latencies)
    p50 = lat_sorted[int(0.5 * len(lat_sorted))]
    p95 = lat_sorted[int(0.95 * len(lat_sorted)) - 1]

    metrics = {
        "batch_size": batch_size,
        "p50_ms": round(p50, 2),
        "p95_ms": round(p95, 2),
        "wall_time_s": round(wall_time, 2),
        "peak_memory_mb": round(peak_memory, 2)
    }

    with open("metrics.json", "w") as f:
        import json
        json.dump(metrics, f, indent=2)
    print("Metrics written to metrics.json")


if __name__ == "__main__":
    main()
