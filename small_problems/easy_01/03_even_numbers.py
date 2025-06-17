# Even Numbers
# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the even numbers?

# PEDAC

# Understand the Problem:
# Inputs:
    # A range of numbers from 1 to 99
# Outputs: 
    # All even numbers
# Requirements: 
    # Print one number on each line
    # Inclusive of 99

# Are there any other rules that I missed?

# Mental Model:
    # Iterate through a range of numbers, printing only the even numbers, one on each line.

# Example/Test Case:
    # Inputs:
        # 1, 99
    # Outputs:
        # 2
        # 4
        # 6
        # ...
        # 98

# Data Structure:
    # A range

# Algorithm:
    # Given a range of 1 to 99
    # Iterate through a range from 1 to 99
        # If the number is even
            # Print the number

# Code:
for num in range(1, 99):
    if num % 2 == 0:
        print(num)

# Bonus:
# No, if you have to start at 1, you have to skip over that start value first.