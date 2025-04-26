
import lambda_function

event = '"{ body : key1 }"'

def some_function():
    return lambda_function.lambda_handler(event, None)


some_function()

