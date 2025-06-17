# Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.

# PEDAC
# input: (from user) starting value, ending value
# output: odd numbers from the given starting value through ending value
# make requirements explicit:
    # print one number per line
    # include the ending value if odd

# are there any other rules that I missed?

# Mental model:
    # Given a starting value and an ending value, print one odd number per line. If the ending value is odd, include it as an output.

# Validation:
    # inputs:
        # -99, -1 
        # -5, 22
        # 0, 1000
        # 100, 199
    # outputs: (each integer printed per line)
        # -99, -96, -93...-1
        # -5, -3, -1, 1, 3...21
        # 1, 3, 5...999
        # 101, 103, 105...199

# Data Structure:
    # A range

# Algorithm (and manual non-code testing):
    # Given a starting value and ending value as a range of numbers
        # starting, ending values: -5, 21
    # If the starting value is not odd, add 1
    # Else if the starting value is odd, do nothing
    # For each number in a range that starts at the starting value, ends at the stop value +1, and step at a value of 2
        # Print the number
            # print(-5)

# Code:
def print_odd_nums(num1, num2):
    if num1 % 2 == 0:
        num1 += 1

    for num in range(num1, num2 + 1, 2):
        print(num)

print_odd_nums(-99, -1)
print_odd_nums(-5, 22)
print_odd_nums(0, 1000)
print_odd_nums(100, 199)