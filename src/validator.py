class PriceValidator:
    REQUIRED_FIELDS = ["symbol", "price", "currency", "timestamp"]

    def validate(self, record):
        """
        Validate a single price record.
        """
        if not isinstance(record, dict):
            raise TypeError("Record must be a dict")

        for field in self.REQUIRED_FIELDS:
            if field not in record:
                raise ValueError(f"Missing required field: {field}")
            
        if not isinstance(record["symbol"], str):
            raise TypeError("symbol must be a string")

        if not isinstance(record["price"], (int, float)):
            raise TypeError("price must be a number")

        if not isinstance(record["currency"], str):
            raise TypeError("currency must be a tring")

        if not isinstance(record["timestamp"], str):
            raise TypeError("timestamp must be a tring")
        
        return True
