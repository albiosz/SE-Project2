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

## Running the example

```bash
python currency_converter_client.py
```

Note: The gRPC server must be running for the client to work. 