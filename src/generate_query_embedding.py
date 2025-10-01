# src/generate_query_embedding.py
import numpy as np
from src.config import OPENAI_API_KEY
from openai import OpenAI

# Initialize client
client = OpenAI(api_key=OPENAI_API_KEY)

query_text = "I sold 5% shares of a non-listed company last year."

# Create embedding
resp = client.embeddings.create(
    model="text-embedding-3-small",
    input=query_text
)

# Access embedding correctly
query_embedding = np.array(resp.data[0].embedding)

# Save to file
np.save("./data/sample_query.npy", query_embedding)
print("[INFO] Saved sample_query.npy")
