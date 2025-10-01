# src/pipeline.py
import logging
import argparse
from src.slot_filling import extract_slots
from src.retriever import Retriever
from src.prompt_builder import build_prompt
from src.llm_client import chat_completion
from src.embeddings import get_text_embedding

logging.basicConfig(level=logging.INFO)

class TaxAssistantPipeline:
    def __init__(self):
        self.retriever = Retriever()

    def run(self, user_input):
        # 1. Extract slots
        slots = extract_slots(user_input)
        logging.info(f"Extracted slots: {slots}")

        # 2. Get query embedding (uses caching)
        query_emb = get_text_embedding(user_input)

        # 3. Retrieve top rules
        rules = self.retriever.retrieve(query_emb)
        logging.info(f"Retrieved {len(rules)} rules")

        # 4. Build LLM prompt
        prompt = build_prompt(user_input, slots, rules)

        # 5. Get LLM response
        answer = chat_completion(prompt)
        return answer

# --- CLI support ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Smart Tax Assistant pipeline.")
    parser.add_argument('--query', type=str, required=True, help="Tax-related query")
    args = parser.parse_args()

    pipeline = TaxAssistantPipeline()
    response = pipeline.run(args.query)
    print("\n--- Assistant Response ---\n")
    print(response)
