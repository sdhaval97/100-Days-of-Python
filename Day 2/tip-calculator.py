# Creating a tip calculator using variables

print("Welcome to the tip calculator!")

# Asking the user for the bill amount, tip percentage and number of people

total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give: 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

# computing the split

split_amount = round((total_bill * (1 + 0.01 * tip_percent)) / people, 2)

# printing the amount each one has to pay

print(f"Each person should pay: ${split_amount}")