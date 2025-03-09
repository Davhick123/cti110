# Pseudocode:
# 1. Prompt user to enter travel budget and store it.
# 2. Prompt user to enter travel destination and store it.
# 3. Prompt user to enter expected expenses for:
# 4. Calculate total expenses by adding all three expense values.
# 5. Subtract total expenses from budget to get the remaining budget.
# 6. Display the travel destination, initial budget, total expenses, and remaining budget.
# Get user input
budget = float(input("Enter budget: "))
destination = input("Enter you travel destination: ")
gas = float(input("How much do you think you will spend on gas?: "))
accommodation = float(input("approximately, how much will you need for accommodation/hotel: "))
food = float(input("last, how much wil you need for food. : "))
# Calculate total expenses
total_expenses = gas + accommodation + food
# Calculate remaining budget
remaining_budget = budget - total_expenses
# Display results
print("\n----------- Travel Budget Summary -----------")
print(f"Destination: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")