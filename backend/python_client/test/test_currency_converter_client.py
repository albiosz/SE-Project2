import pytest
import sys
import os

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# try:
from currency_converter_client import CurrencyConverterClient
# except ImportError:
#     pytest.skip("Generated gRPC modules not found. Run generate_proto.py first.", allow_module_level=True)

# Skip tests if server is not running
def is_server_running(host="localhost", port=8081):
    """Check if the gRPC server is running by attempting to open a socket connection"""
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.close()
        return True
    except (socket.error, socket.timeout):
        return False

# Skip all tests if server is not running
pytestmark = pytest.mark.skipif(
    not is_server_running(), 
    reason="Currency converter gRPC server is not running on localhost:8081"
)

@pytest.fixture
def client():
    """Create a client and close it after the test"""
    client = CurrencyConverterClient()
    yield client
    client.close()

class TestCurrencyConverterClient:
    
    def test_convert(self, client):
        """Test currency conversion with real server"""
        result = client.convert("USD", "EUR", 1000)
        assert isinstance(result, int)
        assert result > 0
    
    def test_get_available_currencies(self, client):
        """Test getting available currencies with real server"""
        currencies = client.get_available_currencies()
        
        assert isinstance(currencies, list)
        assert len(currencies) > 0
        
        common_currencies = ["USD", "EUR"]
        for currency in common_currencies:
            assert currency in currencies, f"Expected {currency} to be available"
    
    @pytest.mark.parametrize("from_currency,to_currency,amount", [
        ("USD", "EUR", 1000),  # 10 USD to EUR
        ("EUR", "USD", 1000),  # 10 EUR to USD
        ("USD", "GBP", 2000),  # 20 USD to GBP
    ])
    def test_convert_various_currencies(self, client, from_currency, to_currency, amount):
        """Test converting various currency combinations"""
        result = client.convert(from_currency, to_currency, amount)
        
        assert isinstance(result, int)
        assert result > 0
        
        print(f"Converted {amount} {from_currency} cents to {result} {to_currency} cents") 