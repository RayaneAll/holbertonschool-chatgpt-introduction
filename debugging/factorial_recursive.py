import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Vérification que l'argument a été passé
if len(sys.argv) < 2:
    print("Erreur : Tu dois fournir un argument pour calculer le factoriel.")
else:
    try:
        # Convertir l'argument en entier
        number = int(sys.argv[1])
        result = factorial(number)
        print(f"Le factoriel de {number} est {result}.")
    except ValueError:
        print("Erreur : L'argument doit être un entier valide.")
