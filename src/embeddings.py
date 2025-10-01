import os
import json
import numpy as np
import openai
import logging
from src.config import OPENAI_API_KEY, EMBEDDING_MODEL, EMBEDDINGS_PATH, METADATA_PATH

CACHE_PATH = "./data/embedding_cache.json"

openai.api_key = OPENAI_API_KEY
logging.basicConfig(level=logging.INFO)

# Load or initialize embedding cache
if os.path.exists(CACHE_PATH):
    with open(CACHE_PATH, "r", encoding="utf-8") as f:
        embedding_cache = json.load(f)
else:
    embedding_cache = {}

def build_embeddings_from_json(json_path: str):
    """Build embeddings for a JSON knowledge base and save to file."""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    texts = [json.dumps(record, ensure_ascii=False) for record in data]
    embeddings = []
    metadata = []

    for idx, text in enumerate(texts, 1):
        if text in embedding_cache:
            emb_vector = embedding_cache[text]
        else:
            resp = openai.embeddings.create(
                model=EMBEDDING_MODEL,
                input=text
            )
            emb_vector = resp.data[0].embedding
            embedding_cache[text] = emb_vector
            # Update cache file incrementally
            with open(CACHE_PATH, "w", encoding="utf-8") as f:
                json.dump(embedding_cache, f, ensure_ascii=False, indent=2)

        embeddings.append(emb_vector)
        metadata.append(data[idx-1])
        if idx % 10 == 0 or idx == len(texts):
            logging.info(f"Processed {idx}/{len(texts)} rules...")

    embeddings = np.array(embeddings)
    np.save(EMBEDDINGS_PATH, embeddings)
    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    logging.info(f"Saved embeddings to {EMBEDDINGS_PATH}")
    logging.info(f"Saved metadata to {METADATA_PATH}")

def get_text_embedding(text: str) -> np.ndarray:
    """
    Returns embedding for a single query string.
    Uses caching to avoid repeated API calls.
    """
    if text in embedding_cache:
        logging.info("Using cached embedding for query.")
        emb_vector = embedding_cache[text]
    else:
        logging.info("Generating new embedding via OpenAI API...")
        resp = openai.embeddings.create(
            model=EMBEDDING_MODEL,
            input=text
        )
        emb_vector = resp.data[0].embedding
        embedding_cache[text] = emb_vector
        # Update cache file
        with open(CACHE_PATH, "w", encoding="utf-8") as f:
            json.dump(embedding_cache, f, ensure_ascii=False, indent=2)

    return np.array(emb_vector)
