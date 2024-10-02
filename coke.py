Coke = 50  # Initial amount to be paid
Coin = 0

while Coke > 0:  # Keep looping until the amount due is fully paid
    print(f"Amount Due: {Coke}")
    Coin = int(input("Kindly pay for your soda in coins (5, 10, 25): "))

    # Check if the inserted coin is valid
    if Coin in [5, 10, 25]:
        Coke -= Coin  # Subtract the valid coin from the amount due

        # If the amount due reaches 0 or goes negative, break the loop
        if Coke <= 0:
            break
    else:
        print("Invalid coin. Please insert 5, 10, or 25 cents.")

# Output any change owed if the user overpaid
if Coke <= 0:
    print(f"Change Owed: {-Coke}")
