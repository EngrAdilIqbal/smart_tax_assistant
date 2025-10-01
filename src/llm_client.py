# src/llm_client.py
import os
import openai
from src.config import OPENAI_API_KEY, LLM_MODEL

openai.api_key = OPENAI_API_KEY

def chat_completion(prompt: str, model: str = LLM_MODEL, max_tokens: int = 500, temperature: float = 0.2) -> str:
    """
    Sends a prompt to the LLM and returns the response text.
    """
    try:
        resp = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a tax assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Error calling LLM: {e}"
