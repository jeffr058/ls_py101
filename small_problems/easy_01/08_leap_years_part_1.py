# Leap Years (Part 1)
# Write a function that takes any year greater than 0 as input and returns True if the year is a leap year, or False if it is not.

# For simplicity, this exercise assumes that the Gregorian calendar has been in continuous use since the year 1. We'll address that assumption in the next exercise that follows this one.

# To determine whether a given year is a leap year, use the rules of the Gregorian calendar:

# If the year is divisible by 400, it is a leap year.
# If the year is divisible by 100 but not by 400, it is not a leap year.
# If the year is divisible by 4 but not by 100, it is a leap year.
# All other years are not leap years.

# PEDAC

# Understand the Problem
# Inputs:
    # A number greater than 0
# Outputs:
    # True or False
# Requirements:
    # Return True if the integer is a leap year or False if not
    # Follow Gregorian calendar rules:
        # If divisible by 400, is leap year
        # If divisible by 4 but not by 100, is leap year
        # If divisible by 100 but not by 400, is not leap year
        # All other years are not leap years

# Are there any other rules that I missed? Any implicit?
# Pay close attention to the example, including formatting
# Are there inputs to validate? Edge cases?

# Mental Model:
    # Given an integer greater than 0, check which conditions of the Gregorian calendar rules it meets. Return a boolean value based on the result.

# Example/Test Case:
    # Inputs:
        # 400
        # 1452
        # 1853
    # Outputs:
        # True
        # True
        # False

# Data Structure:
    # None
# Types to note:
    # No type conversion needed

# Algorithm:
    # Given an integer greater than 0
    # Set year to the integer
    # If year is divisible by 400
        # return True
    # Else if year is divisible by 4 but not by 100
        # return True
    # Else if year is divisible by 100 but not by 400
        # return False
    # Else return False

# Manual test:
    # True
    # True
    # False

# Code:
def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

print(is_leap_year(400))
print(is_leap_year(1452))
print(is_leap_year(1853))

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)