import grpc
import sys
import os

# Add the current directory to the path so we can import the generated modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import generated_client.currency_converter_pb2 as currency_converter_pb2
    import generated_client.currency_converter_pb2_grpc as currency_converter_pb2_grpc
except ImportError:
    print("Error: Generated gRPC modules not found. Run generate_proto.py first.")
    sys.exit(1)

class CurrencyConverterClient:
    def __init__(self, host="localhost", port=8081):
        """Initialize client with host and port for gRPC server"""
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = currency_converter_pb2_grpc.CurrencyConverterStub(self.channel)

    def convert(self, from_currency: str, to_currency: str, amount: int) -> int:
        request = currency_converter_pb2.ConvertRequest(
            from_currency=from_currency,
            to_currency=to_currency,
            amount=amount
        )
        
        try:
            response = self.stub.Convert(request)
            return response.amount
        except grpc.RpcError as e:
            print(f"RPC failed: {e.code()}, {e.details()}")
            raise

    def get_available_currencies(self) -> list[str]:
        request = currency_converter_pb2.GetAvailableCurrenciesRequest()
        
        try:
            response = self.stub.GetAvailableCurrencies(request)
            available_currencies = list(response.currencies)
            return available_currencies
        except grpc.RpcError as e:
            print(f"RPC failed: {e.code()}, {e.details()}")
            raise

    def close(self):
        """Close the gRPC channel"""
        self.channel.close()
