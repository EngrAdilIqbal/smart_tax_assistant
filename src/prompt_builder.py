# src/prompt_builder.py

def build_prompt(user_input, slots, rules):
    """
    Build dynamic prompt for LLM: includes slots and retrieved rules in a structured table.
    Instructions added for LLM to provide bullet-pointed, actionable guidance.
    """
    prompt = "You are a highly knowledgeable smart tax assistant. Provide clear, structured, bullet-pointed guidance based on the user's input and applicable tax rules.\n\n"
    prompt += f"User Query: {user_input}\n\n"
    
    # Slots
    prompt += "Identified Slots:\n"
    for k, v in slots.items():
        prompt += f"- {k}: {v}\n"

    # Retrieved rules in table format
    prompt += "\nRelevant Tax Rules (structured table):\n"
    prompt += f"{'Asset Type':<20} | {'Holding Period':<15} | {'Tax Treatment':<35} | {'Rate Rules':<20} | {'Forms':<25} | {'Deadline':<20}\n"
    prompt += "-"*140 + "\n"
    for r in rules:
        forms_str = ", ".join(r['forms'])
        prompt += f"{r['asset_type']:<20} | {r['holding_period']:<15} | {r['tax_treatment']:<35} | {r['rate_rules']:<20} | {forms_str:<25} | {r['deadline']:<20}\n"

    # Bullet-pointed instruction for LLM
    prompt += "\nInstructions for response:\n"
    prompt += "- Provide a step-by-step answer in bullet points.\n"
    prompt += "- Include actionable advice, calculations, applicable forms, deadlines, and references.\n"
    prompt += "- Use a professional and easy-to-follow format.\n"
    prompt += "- Base your response strictly on the identified slots and retrieved rules.\n"

    return prompt

# Example usage:
if __name__ == "__main__":
    user_input = "I sold 5% shares of a non-listed company last year."
    slots = {
        "share_percentage": 5,
        "company_type": "non-listed",
        "asset_type": "Unlisted Stock",
        "holding_period": "unknown",
        "transaction_year": "unknown",
        "country": "unknown"
    }
    rules = [
        {
            "asset_type": "Unlisted Stock",
            "holding_period": "< 1 year",
            "tax_treatment": "Major shareholder classification",
            "rate_rules": "25% flat on gains",
            "forms": ["Form 84", "Major Shareholder Report"],
            "deadline": "May 1–31 following year"
        },
        {
            "asset_type": "Unlisted Stock",
            "holding_period": ">= 1 year",
            "tax_treatment": "Long-term deduction applies",
            "rate_rules": "20% after deductions",
            "forms": ["Form 84", "Major Shareholder Report"],
            "deadline": "May 1–31 following year"
        }
    ]
    
    prompt_text = build_prompt(user_input, slots, rules)
    print(prompt_text)
