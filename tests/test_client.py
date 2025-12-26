import pytest
from unittest.mock import patch
from src.client import StockPriceClient

@patch("src.client.requests.get")
def test_fetch_prices_success(mock_get):
    mock_get.return_value.status_code =200
    mock_get.return_value.json.return_value = {
        "AAPL": {"price": 150, "currency": "USD"}
    }

    client = StockPriceClient()
    data = client.fetch(["AAPL"])

    assert "AAPL" in data
    assert data["AAPL"]["price"] == 150

@patch("src.client.requests.get")
def test_fetch_raises_on_http_error(mock_get):
    mock_get.return_value.raise_for_status.side_effect = Exception("HTTP Error")

    client = StockPriceClient()
    with pytest.raises(Exception):
        client.fetch(["AAPL"])
