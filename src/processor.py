class PriceProcessor:
    def normalize(self, raw_data):
        """
        Convert raw API response into standardized schema.
        """
        if not isinstance(raw_data, dict):
            raise TypeError("raw_data must be a dict")

        records = []

        for symbol, payload in raw_data.items():
            if not isinstance(payload, dict):
                continue    # skip malformed entry

            record = {
                "symbol": symbol,
                "price": payload.get("price"),
                "currency": payload.get("currency"),
                "timestamp": payload.get("timestamp"),
            }
            records.append(record)

        return records



    

"""
we’ll assume raw data looks like this:
raw_data = {
    "AAPL": {
        "price": 150.12,
        "currency": "USD",
        "timestamp": "2025-01-01T00:00:00Z"
    },
    "MSFT": {
        "price": 320.50,
        "currency": "USD",
        "timestamp": "2025-01-01T00:00:00Z"
    }
}

"""
