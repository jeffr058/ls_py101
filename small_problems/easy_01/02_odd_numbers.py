# Odd Numbers
# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# PEDAC
# input: numbers from 1 through 99
# output: each odd number in the range
# make requirements explicit:
    # each odd number must be printed on its own line
    # the last number, 99, needs to be printed

# are there any other rules that I missed?

# Mental model:
    # Given a range of numbers, print only the odd numbers, each on its own line. Include the final number in the range.

# Validation:
    # inputs:
        # 1, 3, 5...99
    # outputs:
        # 1
        # 3
        # 5
        # ...
        # 99

# Data Structure:
    # A range

# Algorithm:
    # Given a range of numbers from 1 to 99
    # Go through the numbers
        # If the number is odd
            # Print the number on its own line
        # If the number is not odd, do nothing

# Code:
for num in range(1, 100, 2):
    print(num)

# Bonus:
Yes. If you use a range with the start at 1 and 2 as the step value, the loop will increment to the next odd number.