# Stock Price Data Pipeline

## Overview
A Python automation pipeline that fetches stock price data from an external API,
normalizes and validates the data, and exports it for downstream usage.

## Components
- client.py: Fetches raw stock data from external APIs
- processor.py: Normalizes raw responses into a standard schema
- validator.py: Validates required fields and data types
- exporter.py: Exports processed data to files

## Target Schema

| Field | Type | Description |
|-----|-----|-------------|
| symbol | string | Stock ticker |
| price | float | Current price |
| currency | string | Currency code |
| timestamp | string | ISO-8601 UTC time |
