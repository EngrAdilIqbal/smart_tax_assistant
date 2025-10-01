import pytest
from src.slot_filling import extract_slots

def test_extract_major_shareholder_by_percentage():
    user_input = "I sold 6% shares of a non-listed company last year"
    slots = extract_slots(user_input)
    assert "asset_type" in slots
    assert slots["asset_type"].lower() == "non-listed company"
    assert "ownership_percentage" in slots
    assert slots["ownership_percentage"] == 6

def test_extract_minor_shareholder_listed():
    user_input = "I sold 1% shares of a listed company worth KRW 800M"
    slots = extract_slots(user_input)
    assert slots["asset_type"].lower() == "listed company"
    assert slots["ownership_percentage"] == 1
    assert "market_value" in slots
    assert slots["market_value"] == 800_000_000

def test_extract_holding_period():
    user_input = "I held the shares for 3 years before selling"
    slots = extract_slots(user_input)
    assert "holding_period" in slots
    assert slots["holding_period"] == 3

def test_handles_ambiguous_input():
    user_input = "I sold some shares"
    slots = extract_slots(user_input)
    assert isinstance(slots, dict)
    assert len(slots) == 0  # nothing confidently extracted
