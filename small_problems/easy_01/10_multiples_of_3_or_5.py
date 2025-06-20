# Multiples of 3 or 5
# Write a function that computes the sum of all numbers between 1 and some other number, inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.

# Examples
# # These examples should all print True
# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)

# PEDAC

# Understand the Problem
# Inputs:
    # An integer greater than 1 (target_num)
# Outputs:
    # Sum of all numbers (that are multiples of 3 or 5) between 1 and target_num, inclusive
# Requirements:
    # Function
    # Return the sum
    # Only add unique numbers

# Are there any other rules that I missed? Any implicit?
# Pay close attention to the example, including formatting
# Are there inputs to validate? Edge cases?

# Mental Model:
    # Determine the integers between 1 and target_num, inclusive, that are multiples of 3 or 5, and the integers must be unique. Compute and return the sum.

# Example/Test Case:
    # Inputs:
        # 3         # 3
        # 5         # 3, 5
        # 10        # 3, 5, 6, 9, 10
        # 1000      # 3, 5, 6, 9, 10,... 1000
        # 15        # 3, 5, 6, 9, 10, 12, 15
    # Outputs:
        # 3         # 3
        # 8         # 3 + 5 = 8
        # 33        # 3 + 5 + 6 + 9 + 10 = 33
        # 234168    # per provided example
        # 60        # 3 + 5 + 6 + 9 + 10 + 12 + 15 = 60

# Data Structure:
    # List
# Types to note:
    # None

# Algorithm:
    # Given target_num
    # Set multiples to empty list
    # For each number between 1 and target_num, inclusive
    # If number is divisible by 3 or 5
        # Add number to multiples
    # Set sum to the sum of all numbers in multiples
    # Return sum

# Manual test:
    # target_num = 15
    # multiples = []
    # multiples = [3, 5, 6, 9, 10, 12, 15]
    # sum = 60
    # 60

# Code:
def multisum(target_num):
    multiples = []
    for number in range(1, target_num + 1):
        if (number % 3 == 0) or (number % 5 == 0):
            multiples.append(number)
    
    sum_of_multiples = sum(multiples)
    
    return sum_of_multiples

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
print()
print(multisum(15) == 60)