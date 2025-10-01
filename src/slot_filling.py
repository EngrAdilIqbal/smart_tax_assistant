# src/slot_filling.py
import re
import logging

logging.basicConfig(level=logging.INFO)

# Example holding period patterns
HOLDING_PERIOD_PATTERNS = [
    r'(\d+)\s*years?',
    r'(\d+)\s*months?',
    r'less than (\d+)\s*years?',
    r'over (\d+)\s*years?',
    r'more than (\d+)\s*years?',
]

# Example transaction year patterns
YEAR_PATTERNS = [
    r'in (\d{4})',
    r'last year',
    r'this year',
]

# Country detection (optional, for international cases)
COUNTRY_PATTERNS = [
    r'\b(Korea|South Korea|USA|United States|Japan|China)\b',
]

def extract_slots(user_input: str) -> dict:
    """
    Extract structured slots from user input:
    - share_percentage
    - company_type
    - asset_type
    - holding_period
    - transaction_year
    - country (optional)
    """
    slots = {
        "share_percentage": None,
        "company_type": None,
        "asset_type": None,
        "holding_period": "unknown",
        "transaction_year": "unknown",
        "country": "unknown"
    }

    # Extract share percentage
    share_match = re.search(r'(\d+)\s*%', user_input)
    if share_match:
        slots["share_percentage"] = int(share_match.group(1))

    # Determine company type / asset type
    if re.search(r'\bnon[-\s]?listed\b', user_input, re.I):
        slots["company_type"] = "non-listed"
        slots["asset_type"] = "Unlisted Stock"
    elif re.search(r'\blist(ed)?\b', user_input, re.I):
        slots["company_type"] = "listed"
        slots["asset_type"] = "Listed Stock"
    elif re.search(r'\bSME\b', user_input, re.I):
        slots["company_type"] = "SME"
        slots["asset_type"] = "SME Shares"
    elif re.search(r'\binherited\b', user_input, re.I):
        slots["asset_type"] = "Inheritance"
    elif re.search(r'\bgift(ed)?\b', user_input, re.I):
        slots["asset_type"] = "Gifted Shares"

    # Extract holding period
    for pattern in HOLDING_PERIOD_PATTERNS:
        match = re.search(pattern, user_input, re.I)
        if match:
            slots["holding_period"] = match.group(0)
            break

    # Extract transaction year
    for pattern in YEAR_PATTERNS:
        match = re.search(pattern, user_input, re.I)
        if match:
            if match.group(0).lower() == 'last year':
                slots["transaction_year"] = "previous year"
            elif match.group(0).lower() == 'this year':
                slots["transaction_year"] = "current year"
            else:
                slots["transaction_year"] = match.group(1)
            break

    # Extract country
    for pattern in COUNTRY_PATTERNS:
        match = re.search(pattern, user_input, re.I)
        if match:
            slots["country"] = match.group(0)
            break

    logging.info(f"Slots extracted: {slots}")
    return slots

# Test
if __name__ == "__main__":
    queries = [
        "I sold 5% shares of a non-listed company last year.",
        "I sold 10% SME shares in 2022 in Korea.",
        "I inherited unlisted shares from my father.",
        "I gifted 3% listed stock this year."
    ]
    for q in queries:
        extract_slots(q)
