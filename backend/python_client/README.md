# Currency Converter Python Client

This is a Python client for the Currency Converter gRPC service.

## Setup

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Generate Python code from the .proto file:
```bash
python generate_proto.py
```
This will create two files:
- `currency_converter_pb2.py`: Contains message classes
- `currency_converter_pb2_grpc.py`: Contains client and server classes

## Usage

```python
from currency_converter_client import CurrencyConverterClient

# Create client (default connects to localhost:8081)
client = CurrencyConverterClient()

try:
    # Get available currencies
    currencies = client.get_available_currencies()
    print(f"Available currencies: {currencies}")
    
    # Convert 1000 cents (10 USD) to EUR
    result = client.convert("USD", "EUR", 1000)
    print(f"Converted 1000 cents (10 USD) to {result} cents EUR")

finally:
    # Always close the connection
    client.close()
```

You can also specify a different host and port:

```python
client = CurrencyConverterClient(host="example.com", port=50051)
```

## Running the Tests

**Important**: Tests require a running gRPC server on localhost:8081.

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run a specific test file
pytest test_currency_converter_client.py
```

If the gRPC server is not running, tests will be skipped with an appropriate message. 