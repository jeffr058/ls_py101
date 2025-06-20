# Leap Years (Part 2)
# In the previous exercise, we assumed that the Gregorian calendar has been in continuous use since the year 1. However, the Gregorian calendar wasn't adopted until much later; prior to that, much of the world used the Julian calendar, which observed leap year every 4 years.

# In 1752, England, Ireland, and the British colonies all switched to the Gregorian calendar. Update the function from the previous exercise so it uses the Julian calendar prior to 1752, and the Gregorian calendar starting in 1752.

# PEDAC

# Understand the Problem
# Inputs:
    # An integer > 0
# Outputs:
    # True if leap year
    # False if not leap year
# Requirements:
    # Prior to 1752, leap years were every 4 years
    # Starting in 1752, leap years followed Gregorian calendar rules:
        # If the year is divisible by 400, it is a leap year.
        # If the year is divisible by 100 but not by 400, it is not a leap year.
        # If the year is divisible by 4 but not by 100, it is a leap year.
        # All other years are not leap years. 
    # Update the existing function
# Are there any other rules that I missed? Any implicit?
# Pay close attention to the example, including formatting
# Are there inputs to validate? Edge cases?

# Mental Model:
    # Given an integer greater than 0, if it is less than 1752, leap years are determined by whether the number is divisible by 4. If the number is 1752 or greater, leap years are determined by the Gregorian calendar rules. Return True if the number is a leap year, False if not.

# Example/Test Case:
    # Inputs:
        # 100
        # 801
        # 1700
        # 1900
    # Outputs:
        # True
        # False
        # True
        # False

# Data Structure:
    # None
# Types to note:
    # None

# Algorithm:
    # Given an integer year that is greater than 0
    # If year is less than 1752
        # If year is divisible by 4
            # Return True
    # Else if year is divisible by 400
        # Return True
    # Else if year is divisible by 100
        # Return False
    # Else return whether year is divisible by 4 or not
            
# Manual test:
    # 100 < 1752; 100 % 4 == 0 evaluates as True
    # 801 < 1752; 801 % 4 == 0 evaluates as False
    # 1700 < 1752; 1700 % 4 == 0 evaluates as True
    # 1900 > 1752; 1900 % 400 == 0 evaluates as False

# Code:
def is_leap_year(year):
    if year < 1752:
        return year % 4 == 0
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

# Solution with helper functions for practice:
# def julian_calendar(year):
#     return (year < 1752) and (year % 4 == 0)

# def gregorian_calendar(year):
#     if year >= 1752:
#         if year % 400 == 0:
#             return True
#         elif (year % 4 == 0) and (year % 100 != 0):
#             return True
#     return False

# def is_leap_year(year):
#     return julian_calendar(year) or gregorian_calendar(year)

# print(julian_calendar(100))  # True
# print(julian_calendar(801))  # False
# print(julian_calendar(1700))  # True
# print(julian_calendar(1900))  # False
# print()
# print(gregorian_calendar(100))  # False
# print(gregorian_calendar(801))  # False
# print(gregorian_calendar(1700))  # False
# print(gregorian_calendar(1900))  # False
# print()
print(is_leap_year(100))  # True
print(is_leap_year(801))  # False
print(is_leap_year(1700))  # True
print(is_leap_year(1900))  # False
print()
# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)