import logging
from fastapi import FastAPI
from sentence_transformers import SentenceTransformer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
def load_model():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    logger.info(f"Loading model {model_name}")
    SentenceTransformer(model_name)
    logger.info("Model loaded")

@app.get("/health")
def health():
    return {"status": "OK"}
