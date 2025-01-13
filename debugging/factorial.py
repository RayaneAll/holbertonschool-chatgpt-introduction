#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Check if an argument is provided
if len(sys.argv) < 2:
    print("Usage: ./factorial.py <number>")
else:
    f = factorial(int(sys.argv[1]))
    print(f)
