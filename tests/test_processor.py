import pytest
from src.processor import PriceProcessor

@pytest.fixture
def processor():
    return PriceProcessor()

def test_normalize_valid_data(processor):
    
    raw_data = {
        "AAPL": {
            "price": 150.0,
            "currency": "USD",
            "timestamp": "2025-01-01T00:00:00Z"
        }
    }
    records = processor.normalize(raw_data)

    assert len(records) == 1
    assert records[0]["symbol"] == "AAPL"
    assert records[0]["price"] == 150.0

def test_non_dict_data_raises(processor):
    with pytest.raises(TypeError):
        processor.normalize("invalid")

def test_malformed_payload_is_skipped(processor):

    raw_data = {
        "AAPL": "invalid_payload",
        "MSFT": {
            "price": 300.0,
            "currency": "USD",
            "timestamp": "2025-01-01T00:00:00Z"
        }
    }

    records = processor.normalize(raw_data)
    assert len(records) == 1
    assert records[0]["symbol"] == "MSFT"



