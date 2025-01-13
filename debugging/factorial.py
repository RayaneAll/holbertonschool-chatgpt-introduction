#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if len(sys.argv) < 2:
    print("Erreur : Tu dois fournir un argument pour calculer le factoriel.")
else:
    try:
        number = int(sys.argv[1])
        f = factorial(number)
        print(f"Le factoriel de {number} est {f}.")
    except ValueError:
        print("Erreur : L'argument fourni doit être un entier.")