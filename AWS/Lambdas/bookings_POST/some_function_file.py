
from lambda_function import lambda_handler

test_event = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}

def some_function():
    return lambda_handler(test_event, None)


some_function()

