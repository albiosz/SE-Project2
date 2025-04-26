#!/usr/bin/env python3

import os
import subprocess
import sys

def main():
    # Get the root directory of the project
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Path to the proto file
    proto_file = os.path.join(root_dir, 'CurrencyConverterService', 'src', 'main', 'proto', 'currency_converter.proto')
    
    # Output directory for generated code
    output_dir = os.path.join(root_dir, 'backend', 'python_client')
    
    # Ensure the proto file exists
    if not os.path.exists(proto_file):
        print(f"Error: Proto file not found at {proto_file}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Proto file path: {proto_file}")
    print(f"Output directory: {output_dir}")
    
    # Run protoc command to generate Python code
    cmd = [
        'python', '-m', 'grpc_tools.protoc',
        f'--proto_path={os.path.dirname(proto_file)}',
        f'--python_out={output_dir}',
        f'--grpc_python_out={output_dir}',
        proto_file
    ]
    
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("Successfully generated Python gRPC code")
    else:
        print("Failed to generate Python gRPC code", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main() 