# David Hicks
# 4/20/2025
# P5LAB_HicksDavid.py
# This program simulates a customer using a self-checkout machine by calculating change.
# It generates a random amount for the customer to pay and then calculates the change owed.

import random

# Function to dispense the change
def disperse_change(change_owed):
    # Convert change to cents
    cents = round(change_owed * 100)
    
    denominations = {
        "Dollar": 100,
        "Quarter": 25,
        "Dime": 10,
        "Nickel": 5,
        "Penny": 1
    }

    print("Change Owed: ${:.2f}".format(change_owed))
    print("Dispensing Change:")

    for name, value in denominations.items():
        count = cents // value  # Get the count of coins
        cents %= value  # Update remaining cents
        if count > 0:
            print(f"{count} {name + ('s' if count > 1 else '')}")

# Main function to drive the program logic
def main():
    # Generate a random amount for the customer to pay
    total_owed = round(random.uniform(0.01, 100.00), 2)
    
    print(f"Total Owed: ${total_owed:.2f}")
    
    # Prompt user for the amount of money they will pay
    amount_paid = float(input("Enter the amount of money you will put into the self-checkout: $"))
    
    # Check if the user has provided enough money
    if amount_paid < total_owed:
        print("Insufficient funds. You need more money.")
    else:
        # Calculate the change owed to the customer
        change_owed = round(amount_paid - total_owed, 2)
        # Call the function to dispense the change
        disperse_change(change_owed)

# Call the main function to run the program
if __name__ == "__main__":
    main()