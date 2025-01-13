class Minesweeper:
    # ... autres méthodes de la classe ...

    def play(self):
        try:
            while True:
                # Exemple de boucle de jeu
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                # Logique du jeu ici...
                print(f"You entered coordinates: ({x}, {y})")
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        finally:
            print("Game terminated.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
