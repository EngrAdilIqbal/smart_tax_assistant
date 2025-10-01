# Smart Tax Assistant

**Smart Tax Assistant** is an AI-driven application that provides structured, actionable tax guidance based on user queries. It leverages advanced Large Language Models (LLMs) and vector embeddings to interpret tax-related text and return step-by-step recommendations in a professional, enterprise-ready format.

---

## Features

* **Natural Language Understanding**: Extracts structured information (slots) from user queries, such as share percentage, company type, asset type, holding period, transaction year, and country.
* **Knowledge Retrieval**: Retrieves relevant tax rules from a structured knowledge base using semantic embeddings.
* **Dynamic Prompting**: Constructs detailed prompts for LLMs with structured tables and bullet-point instructions for clear, actionable advice.
* **Batch Processing**: Supports multiple queries in a single run for efficiency in demo scenarios.
* **Embedding Caching**: Avoids redundant API calls for repeated queries, speeding up response time during demonstrations.
* **Step-by-Step Guidance**: Outputs professional, bullet-pointed instructions, including calculations, applicable forms, deadlines, and references.

---

## Technology Stack & Models

* **LLM (Language Model)**: OpenAI GPT model (e.g., GPT-4) is used for generating tax guidance.

  * **Reason for choice**: GPT-4 provides highly coherent, structured, and context-aware responses, making it suitable for professional financial guidance applications.
* **Embeddings**: OpenAI embeddings (text-embedding-3-large) for semantic similarity search.

  * **Reason for choice**: These embeddings provide accurate semantic understanding of tax rules and queries, enabling relevant retrieval from knowledge base.
* **Python**: Core language for data processing, API calls, and application logic.
* **NumPy & JSON**: For embeddings storage, vector calculations, and metadata handling.

> ⚠️ **Security Note**: The OpenAI API key has been removed from this repository for security purposes.
> Before running the project, create a `.env` file or set environment variables with your key:
>
> ```bash
> OPENAI_API_KEY=your_openai_api_key_here
> ```

---

## Installation & Setup

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd smart_tax_assistant
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key in `.env` or environment variables.

5. Run the demo:

   ```bash
   python run_demo.py
   ```

   * You can enter **multiple queries** separated by a semicolon (`;`) in a single run.
   * Type `exit` to quit.

---

## Example Runs

### Single Query via Pipeline

```bash
python -m src.pipeline --query "I sold 10% SME shares last year."
```

Output:

```
INFO:root:Loaded embeddings from ./data/embeddings.npy
INFO:root:Loaded metadata from ./data/metadata.json
INFO:root:Slots extracted: {'share_percentage': 10, 'company_type': 'SME', 'asset_type': 'SME Shares', 'holding_period': 'unknown', 'transaction_year': 'previous year', 'country': 'unknown'}
INFO:root:Generating new embedding via OpenAI API...
INFO:root:Top retrieved rules: ...
INFO:root:Retrieved 5 rules

--- Assistant Response ---

1. Determine Holding Period: Identify how long you held the SME shares to determine tax treatment.
2. Calculate Taxable Gain: Selling price minus purchase price.
3. Apply Tax Rate: 50% if held ≥5 years, else 20%.
4. Prepare Tax Forms: Form 84-SME if ≥5 years, else Form 84.
5. Submit Forms: May 1–31 following year.
6. Keep Records: Maintain transaction documents for audits.
```

---

### Multiple Queries via Demo

```bash
python run_demo.py
```

User input:

```
I sold 5% shares of a non-listed company last year; I inherited SME shares from my uncle; I gifted 10% listed stock this year
```

Output:

```
--- Query 1 ---
Slots extracted: {'share_percentage': 5, 'company_type': 'non-listed', 'asset_type': 'Unlisted Stock', ...}
Assistant Response: Step-by-step guidance including forms Form 84, deadlines May 1–31.

--- Query 2 ---
Slots extracted: {'share_percentage': None, 'company_type': 'SME', 'asset_type': 'SME Shares', ...}
Assistant Response: Special SME exemption rules, tax rates, and filing instructions.

--- Query 3 ---
Slots extracted: {'share_percentage': 10, 'company_type': 'listed', 'asset_type': 'Listed Stock', ...}
Assistant Response: Gift tax guidance, applicable forms, submission deadlines.
```

---

## Project Structure

```
smart_tax_assistant/
│
├── data/
│   └── capital_gains_rules.json       # Knowledge base (50+ tax rules)
│
├── src/
│   ├── __init__.py
│   ├── config.py                      # Loads API keys & settings from .env
│   ├── embeddings.py                  # Embed JSON rules into vector DB
│   ├── retriever.py                   # Query vector DB to retrieve relevant tax rules
│   ├── slot_filling.py                # Extract structured slots (asset, holding period, etc.)
│   ├── prompt_builder.py              # Build final prompt for LLM (with slots + retrieved rules)
│   ├── llm_client.py                  # Wrapper around LLM API (chat/completions)
│   ├── pipeline.py                    # Orchestration: slot filling → retrieval → LLM response
│   └── utils.py                       # Helper functions (logging, parsing, etc.)
│
├── tests/
│   ├── __init__.py
│   ├── test_slot_filling.py           # Unit tests for slot extraction
│   ├── test_retriever.py              # Tests for vector DB retrieval
│   ├── test_pipeline.py               # End-to-end pipeline test
│   ├──conftest.py               
│
│
├── requirements.txt                   # Dependencies (openai, chromadb, faiss, python-dotenv, pytest, etc.)
├── run_demo.py                        # CLI script: run assistant with sample user queries
├── .env                               # Stores API_KEY, MODEL_NAME, DB_PATH, etc. (not committed to GitHub)

```

---

## Future Work & Industrial-Scale Considerations

1. **Scalability & Optimization**

   * Move embeddings to a **vector database** (e.g., Pinecone, Milvus) for faster retrieval.
   * Batch LLM calls and implement **async processing** for multiple queries.

2. **Model Optimization**

   * Fine-tune LLMs for domain-specific tax data.
   * Optimize embeddings for latency-sensitive applications.

3. **Enhanced Slot Extraction**

   * Advanced NLP (spaCy, HuggingFace Transformers) for robust slot detection.

4. **Security & Compliance**

   * Store API keys securely (e.g., AWS Secrets Manager).
   * Add logging and monitoring for enterprise-grade reliability.

5. **UI & User Experience**

   * Web interface or chatbot integration.
   * Visual summaries of tax rules and deadlines.

6. **Testing & CI/CD**

   * Unit tests for slot extraction, embedding retrieval, and prompt generation.
   * CI/CD pipeline for automated deployment.

---

## Author

**Adil Iqbal**
Senior Machine Learning Engineer

Expertise in applied NLP, LLMs, AgenticAI, embeddings, retrieval systems, and building structured AI pipelines suitable for enterprise applications.
