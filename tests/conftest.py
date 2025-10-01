import pytest
from src.retriever import RuleRetriever
from src.pipeline import TaxAssistantPipeline

@pytest.fixture(scope="session")
def retriever():
    """Fixture to load the RuleRetriever once per test session."""
    return RuleRetriever("data/capital_gains_rules.json")

@pytest.fixture(scope="session")
def pipeline():
    """Fixture for the end-to-end assistant pipeline."""
    return TaxAssistantPipeline()
