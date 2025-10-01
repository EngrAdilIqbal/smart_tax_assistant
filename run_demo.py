# run_demo.py
import logging
from src.pipeline import TaxAssistantPipeline

logging.basicConfig(level=logging.INFO)

def run_demo():
    pipeline = TaxAssistantPipeline()

    print("=== Smart Tax Assistant Demo ===")
    print("You can enter multiple queries separated by ';' (semicolon).")
    print("Or type 'exit' to quit.")

    while True:
        user_input = input("\nEnter your tax query (or type 'exit'): ").strip()
        if user_input.lower() == 'exit':
            break

        # Split multiple queries using semicolon
        queries = [q.strip() for q in user_input.split(";") if q.strip()]
        for idx, query in enumerate(queries, 1):
            print(f"\n--- Query {idx} ---")
            try:
                response = pipeline.run(query)
                print("\n--- Assistant Response ---")
                print(response)
            except Exception as e:
                logging.error(f"Error processing query '{query}': {e}")

if __name__ == "__main__":
    run_demo()
