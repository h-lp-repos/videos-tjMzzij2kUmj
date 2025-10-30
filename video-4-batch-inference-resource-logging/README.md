# Video 4: Batch Inference & Resource Logging

## Objective
Measure per-batch latency (p50/p95), wall-clock time, and peak memory usage using `psutil`, and produce a `metrics.json` file.

## Steps

1. Inspect the script:
   ```bash
   cat time_inference.py
   ```
2. Run the script:
   ```bash
   python time_inference.py
   ```
3. Review the generated metrics:
   ```bash
   cat metrics.json
   ```

## Troubleshooting

- **psutil memory issues**: use `tracemalloc` or `/proc/meminfo` fallback on Linux.
- **High first-batch latency**: drop the first measurement when computing percentiles.
