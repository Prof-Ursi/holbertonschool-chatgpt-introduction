#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

# Check if an argument is provided
if len(sys.argv) != 2:
    print("Usage: python script_name.py <number>")
    sys.exit(1)

# Convert the argument to an integer and calculate factorial
try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Please provide a valid integer as an argument.")
    sys.exit(1)