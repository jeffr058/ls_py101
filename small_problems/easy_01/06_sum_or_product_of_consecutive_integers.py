# Sum or Product of Consecutive Integers
# Write a program that asks the user to enter an integer greater than 0, then 
# asks whether the user wants to determine the sum or the product of all 
# numbers between 1 and the entered integer, inclusive.

# Example 1
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.

# Example 2
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.

# PEDAC

# Understand the Problem
# Inputs:
    # An integer > 0
    # Choice between sum and product
# Outputs:
    # Sum or product of all numbers between 1 and the entered number, inclusive
# Requirements:
    # Get input for integer
    # Get input for desired result
    # Convert string input to integer
    # The range is from 1 to the entered number
    # Compute operation on all numbers in the range, inclusive
    # (Implicit) Print the result 

# Are there any other rules that I missed?
    # Input for sum or product choice is 's' or 'p'

# Mental Model:
    # Get the number and desired result (sum or product). Convert the entered 
    # string input to an integer and compute the appropriate operation on all 
    # numbers in the range, including the entered number. Print the result.

# Example/Test Case:
    # Inputs:
        # 6, s
        # 7, p
    # Outputs:
        # 21
        # 5040

# Data Structure:
    # A range
# Types to note:
    # Numeric string to integer

# Algorithm:
    # Get the number, convert it to an integer, and assign it to integer
    # Get the desired result and assign it to sum_or_product

    # If sum_or_product is 's'
        # Set sum_or_product = 'sum'
        # Set result = 0
    # Else if sum_or_product is 'p'
        # Set sum_or_product = 'product'
        # Set result = 1
    
    # For each number in a range from 1 to integer + 1
        # If sum_or_product = 'sum'
            # Set result += number
        # else if sum_or_product = 'product'
            # Set result *= number
    # Print result

# Manual test:
    # integer = 6
    # sum_or_product = 's'
    # sum_or_product = 'sum'
    # result = 0
    # result = 21
    # The sum of the integers between 1 and 6 is 21.

    # integer = 7
    # sum_or_product = 'p'
    # sum_or_product = 'product'
    # result = 1
    # result = 5040
    # The product of the integers between 1 and 7 is 5040.

# Code:
integer = int(input('Please enter an integer greater than 0: '))
sum_or_product = input('Enter "s" to compute the sum, '
                       'or "p" to compute the product: ')

if sum_or_product == 's':
    sum_or_product = 'sum'
    result = 0
if sum_or_product == 'p':
    sum_or_product = 'product'
    result = 1

for number in range(1, integer + 1):
    if sum_or_product == 'sum':
        result += number
    if sum_or_product == 'product':
        result *= number

print(f'The {sum_or_product} of the integers between 1 and {integer} is '
      f'{result}.')