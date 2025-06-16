# Isn't it Odd?

# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

# PEDAC
# input: one int
# output: True, False
# make requirements explicit:
    # write a function with a single argument
    # return True when absolute value is odd
    # return False otherwise

# are there any other rules that I missed?

# Mental model:
    # Given an integer, return True if the absolute value of the integer is odd. Otherwise, return False.

# Validation:
    # inputs: 
        # an integer, example: 10
    # outputs:
        # False (the absolute value is 10)

# Data Structure:
    # None?

# Algorithm:
    # Given an integer as a function argument
    # Get the absolute value of the integer
    # Determine if the integer is odd
        # If the integer is odd, return True
        # If not, return False

# Code:
def is_odd(int_num):
    if abs(int_num) % 2 != 0:
        return True
    return False