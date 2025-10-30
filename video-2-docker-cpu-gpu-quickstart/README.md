# Video 2: Docker CPU & GPU Quickstart

## Objective
Demonstrate launching a local container that exposes a model-serving endpoint for inference, showing both CPU and GPU variants.

## Steps

1. Inspect Docker Compose files:
   ```bash
   cat docker-compose.cpu.yml docker-compose.gpu.yml
   ```
2. Build and start CPU container:
   ```bash
   docker-compose -f docker-compose.cpu.yml up --build -d
   docker ps
   ```
3. (Optional) Build and start GPU container:
   ```bash
   docker-compose -f docker-compose.gpu.yml up --build -d
   docker logs <container_id>
   ```
4. Health check:
   ```bash
   curl http://localhost:8000/health
   ```

## Troubleshooting

- **Docker build fails**: use a lightweight model tag or increase disk space.
- **GPU not available**: install NVIDIA Container Toolkit and ensure `runtime: nvidia`.
