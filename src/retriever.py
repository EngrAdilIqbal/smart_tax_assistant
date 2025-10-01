# src/retriever.py
import numpy as np
import json
import logging
from sklearn.metrics.pairwise import cosine_similarity

logging.basicConfig(level=logging.INFO)

class Retriever:
    """
    Retriever class for RAG: fetches relevant tax rules from precomputed embeddings.
    """
    def __init__(self, embedding_path="./data/embeddings.npy", metadata_path="./data/metadata.json"):
        # Load embeddings
        try:
            self.embeddings = np.load(embedding_path)
            logging.info(f"Loaded embeddings from {embedding_path}")
        except FileNotFoundError:
            logging.error(f"Embeddings file not found: {embedding_path}")
            raise

        # Load metadata
        try:
            with open(metadata_path, "r", encoding="utf-8") as f:
                self.metadata = json.load(f)
            logging.info(f"Loaded metadata from {metadata_path}")
        except FileNotFoundError:
            logging.error(f"Metadata file not found: {metadata_path}")
            raise

        if len(self.embeddings) != len(self.metadata):
            logging.warning(
                f"Embeddings length ({len(self.embeddings)}) != metadata length ({len(self.metadata)})"
            )

    def retrieve(self, query_embedding: np.ndarray, top_k: int = 5):
        """
        Retrieve top_k relevant rules based on cosine similarity.
        """
        if query_embedding.ndim == 1:
            query_embedding = query_embedding.reshape(1, -1)

        sims = cosine_similarity(query_embedding, self.embeddings)[0]
        top_indices = sims.argsort()[-top_k:][::-1]
        results = [self.metadata[i] for i in top_indices]

        logging.info("Top retrieved rules:")
        for i, r in enumerate(results, 1):
            logging.info(f"{i}. {r}")
        return results


if __name__ == "__main__":
    # Quick test
    retriever = Retriever()
    # Example: load a sample query embedding
    query_embedding = np.load("./data/sample_query.npy")
    retriever.retrieve(query_embedding, top_k=5)
