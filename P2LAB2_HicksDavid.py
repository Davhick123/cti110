# David Hicks
# 3/9/25
# P2LAB2 - Vehicle MPG Calculator
# This program calculates the fuel consumption based on user input for different vehicles.

# Create dictionary with vehicle MPG values
mpg_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get dictionary keys
keys = mpg_dict.keys()
print("Available vehicles:", keys)

# Get user input for vehicle selection
vehicle = input("Enter the vehicle to see it's mpg: ")

# Check if vehicle exists in dictionary
if vehicle in mpg_dict:
    mpg = mpg_dict[vehicle]
    print(f"The  Prius gets {mpg} mpg.")
    
    # Get user input for miles to drive
    miles = float(input("How many miles will you drive the Prius: "))
    
    # Calculate gallons needed
    gallons_needed = miles / mpg
    
    # Display result
    print(f"You will need {gallons_needed:.2f} gallons of gas.")
else:
    print("Vehicle not found. Please enter the name exactly as shown.")