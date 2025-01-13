#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Check if an argument is provided
if len(sys.argv) < 2:
    print("Usage: ./factorial_recursive.py <number>")
else:
    # Read input from the command line argument
    f = factorial(int(sys.argv[1]))

    # Output the result
    print(f)
