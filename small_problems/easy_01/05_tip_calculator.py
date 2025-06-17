# Tip Calculator
# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

# Example
# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00

# PEDAC

# Understand the Problem
# Inputs:
    # Bill amount
    # Tip rate
# Outputs:
    # Tip amount
    # Total bill amount
# Requirements:
    # Get the bill amount and tip rate. Compute the tip. Print the tip amount. Print the total bill amount.

# Are there any other rules that I missed?
    # The output amounts are expected to include '$' and cents.

# Mental Model:
    # Ask the user for bill amount and tip rate. Compute the tip and output the tip amount and the total bill amount.

# Example/Test Case:
    # Inputs:
        # Bill amount: 180
        # Tip rate: 20
    # Outputs:
        # Tip amount: $36.00
        # Total bill amount: $216.00

# Data Structure:
    # None
# Types to note:
    # String from inputs
    # Floats for calculations

# Algorithm:
    # Get the bill amount, coerce it to float, and assign it to bill_amount
    # Get the tip rate, coerce it to float, divide by 100, and assign the quotient to tip_rate
    # Multiply bill_amount by tip_rate and assign the product to tip_amount
    # Add tip_amount to bill_amount and assign the sum to total_amount
    # Print tip_amount
    # Print total_amount

# Manual test:
    # bill_amount = 180.0
    # tip_rate = 0.2
    # tip_amount = 36.0
    # total_amount = 216.0
    # The tip is $36.00
    # The total is $216.00

# Code:
bill_amount = float(input('What is the bill? '))
tip_rate = float(input('What is the tip percentage? ')) / 100

tip_amount = bill_amount * tip_rate
total_amount = bill_amount + tip_amount

print(f'The tip is ${tip_amount:.2f}')
print(f'The total is ${total_amount:.2f}')