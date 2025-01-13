#!/usr/bin/python3

def main():
    try:
        balance = 0.0  # Initialisation du solde
        while True:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
            if action == "deposit":
                try:
                    amount = float(input("Enter the amount to deposit: "))
                    if amount <= 0:
                        print("Please enter a positive amount.")
                    else:
                        balance += amount
                        print(f"${amount:.2f} deposited. New balance: ${balance:.2f}")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            elif action == "withdraw":
                try:
                    amount = float(input("Enter the amount to withdraw: "))
                    if amount <= 0:
                        print("Please enter a positive amount.")
                    elif amount > balance:
                        print("Insufficient funds.")
                    else:
                        balance -= amount
                        print(f"${amount:.2f} withdrawn. New balance: ${balance:.2f}")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            elif action == "balance":
                print(f"Your current balance is: ${balance:.2f}")
            elif action == "exit":
                print("Exiting the checkbook. Goodbye!")
                break
            else:
                print("Invalid action. Please choose from deposit, withdraw, balance, or exit.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Checkbook program terminated.")

if __name__ == "__main__":
    main()
