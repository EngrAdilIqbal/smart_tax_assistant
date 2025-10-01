import pytest
from src.pipeline import TaxAssistantPipeline

def test_pipeline_major_non_listed():
    pipeline = TaxAssistantPipeline()
    user_input = "I sold 6% shares of a non-listed company last year"
    response = pipeline.run(user_input)

    assert isinstance(response, str)
    assert "major shareholder" in response.lower()
    assert "capital gains tax" in response.lower()
    assert "form" in response.lower()

def test_pipeline_minor_listed():
    pipeline = TaxAssistantPipeline()
    user_input = "I sold 1% shares of a listed company worth KRW 800M"
    response = pipeline.run(user_input)

    assert isinstance(response, str)
    assert "minor shareholder" in response.lower() or "exempt" in response.lower()

def test_pipeline_ambiguous_input():
    pipeline = TaxAssistantPipeline()
    user_input = "I sold some shares"
    response = pipeline.run(user_input)

    assert isinstance(response, str)
    assert response.strip().endswith("?")  # should ask clarifying question
