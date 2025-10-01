# src/config.py
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Model names
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")

# Paths
EMBEDDINGS_PATH = os.getenv("EMBEDDINGS_PATH", "./data/embeddings.npy")
METADATA_PATH = os.getenv("METADATA_PATH", "./data/metadata.json")
