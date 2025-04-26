import grpc
import sys
import os

# Add the current directory to the path so we can import the generated modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import currency_converter_pb2
    import currency_converter_pb2_grpc
except ImportError:
    print("Error: Generated gRPC modules not found. Run generate_proto.py first.")
    sys.exit(1)

class CurrencyConverterClient:
    def __init__(self, host="localhost", port=8081):
        """Initialize client with host and port for gRPC server"""
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = currency_converter_pb2_grpc.CurrencyConverterStub(self.channel)

    def convert(self, from_currency, to_currency, amount):
        """
        Convert an amount from one currency to another
        
        Args:
            from_currency (str): Source currency code (e.g., 'USD')
            to_currency (str): Target currency code (e.g., 'EUR')
            amount (int): Amount in cents to convert
            
        Returns:
            int: Converted amount in cents
        """
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

    def get_available_currencies(self):
        """
        Get list of available currencies
        
        Returns:
            list: List of currency codes
        """
        request = currency_converter_pb2.GetAvailableCurrenciesRequest()
        
        try:
            response = self.stub.GetAvailableCurrencies(request)
            return response.currencies
        except grpc.RpcError as e:
            print(f"RPC failed: {e.code()}, {e.details()}")
            raise

    def close(self):
        """Close the gRPC channel"""
        self.channel.close()

def main():
    # Example usage
    client = CurrencyConverterClient()
    
    try:
        # Get available currencies
        print("Fetching available currencies...")
        currencies = client.get_available_currencies()
        print(f"Available currencies: {currencies}")
        
        # Convert 1000 cents (10 USD) to EUR
        print("\nConverting 1000 cents (10 USD) to EUR...")
        result = client.convert("USD", "EUR", 1000)
        print(f"Converted 1000 cents (10 USD) to {result} cents EUR")
    
    except grpc.RpcError as e:
        print(f"RPC Error: {e.details()}")
        print("Is the gRPC server running?")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    main() 