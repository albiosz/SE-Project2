

# Possible errors
In the file `currency_converter_pb2_grpc.py` the imports are generated incorrectly, because the generated code is in another package

The import should look like this
```python
from . import currency_converter_pb2 as currency__converter__pb2
```
