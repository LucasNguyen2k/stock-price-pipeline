import pytest
from src.validator import PriceValidator

@pytest.fixture
def validator():
    return PriceValidator()

def test_valid_record_passes(validator):
    record = {
        "symbol": "AAPL",
        "price": 150.0,
        "currency": "USD",
        "timestamp": "2025-01-01T00:00:00Z"
    }
    assert validator.validate(record) is True
    
def test_missing_field_raises_error(validator):
    record = {"symbol": "AAPL", "price": 100.0}
    
    with pytest.raises(ValueError):
        validator.validate(record)

def test_invalid_price_type(validator):
     record = {
        "symbol": "AAPL",
        "price": "100",
        "currency": "USD",
        "timestamp": "2025-01-01T00:00:00Z"
    }
     with pytest.raises(TypeError):
         validator.validate(record)

def test_non_dict_record(validator):
    with pytest.raises(TypeError):
        validator.validate("not a dict")
