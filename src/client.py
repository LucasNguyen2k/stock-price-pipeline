import requests

class StockPriceClient:
    BASE_URL = "https://api.example.com/prices"

    def fetch(self, symbols):
        if not symbols:
            raise ValueError("symbol list can not be empty")

        params ={"symbols": ",".join(symbols)}
        response = requests.get(self.BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        return response.json()


class StockClient:
    def fetch_prices(self, symbols):
        """
        Fetch raw price data for given stock symbols
        """
        raise NotImplementedError
