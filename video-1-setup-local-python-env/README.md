# Video 1: Prepare Local Python Environment

## Objective
Create a reproducible Python environment and install the exact dependencies used in lab (Sentence-Transformers, faiss-cpu, psutil, numpy).

## Steps

1. Open terminal in this directory and verify files:
   ```bash
   ls
   ```
2. Create and activate a virtual environment:
   - **venv** (Linux/macOS/Windows PowerShell):
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate    # Unix/macOS
     .\.venv\Scripts\activate    # Windows PowerShell
     ```
   - **conda**:
     ```bash
     conda create -n lesson4 python=3.8
     conda activate lesson4
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Verify imports:
   ```bash
   python run_local_embeddings.py
   ```
   You should see `Environment OK`.

## Troubleshooting

- **Build wheel errors**: install prebuilt `faiss-cpu` wheel or use `conda install -c conda-forge faiss-cpu`.
- **Wrong Python version**: ensure Python 3.8+ is used.
