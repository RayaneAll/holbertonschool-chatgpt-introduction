#!/usr/bin/python3
import sys

def factorial(n):
    """Calcule récursivement la factorielle de n."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if len(sys.argv) < 2:  # Vérifie qu'un argument est passé
    print(f"Usage: {sys.argv[0]} <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])  # Tente de convertir l'argument en entier
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        sys.exit(1)
    f = factorial(n)
    print(f"The factorial of {n} is {f}.")
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1)
