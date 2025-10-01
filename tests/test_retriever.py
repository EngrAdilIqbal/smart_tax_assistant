import pytest
from src.retriever import RuleRetriever

def test_retrieve_non_listed_major():
    retriever = RuleRetriever("data/capital_gains_rules.json")
    query = {"asset_type": "non-listed company", "ownership_percentage": 6}
    results = retriever.retrieve(query)

    assert isinstance(results, list)
    assert len(results) > 0
    assert any("non-listed" in r["asset_type"].lower() for r in results)

def test_retrieve_listed_minor():
    retriever = RuleRetriever("data/capital_gains_rules.json")
    query = {"asset_type": "listed company", "ownership_percentage": 1, "market_value": 800_000_000}
    results = retriever.retrieve(query)

    assert isinstance(results, list)
    assert len(results) > 0
    assert any("listed" in r["asset_type"].lower() for r in results)

def test_retrieve_invalid_asset_type():
    retriever = RuleRetriever("data/capital_gains_rules.json")
    query = {"asset_type": "crypto coins", "ownership_percentage": 50}
    results = retriever.retrieve(query)
    assert results == []
