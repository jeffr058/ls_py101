# UTF-16 String Value
# Write a function that determines and returns the UTF-16 string value of a string passed in as an argument. The UTF-16 string value is the sum of the UTF-16 values of every character in the string. (You may use ord to determine the UTF-16 value of a character.)

# Examples
# # These examples should all print True
# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

# # The next three lines demonstrate that the code
# # works with non-ASCII characters from the UTF-16
# # character set.
# OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
# print(utf16_value(OMEGA) == 937)
# print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)

# PEDAC

# Understand the Problem
# Inputs:
    # A string
# Outputs:
    # UTF-16 string value of the string
# Requirements:
    # Write a function
    # UTF-16 string value is the sum of UTF-16 values of every char in the string
    # Use the ord function to determine the UTF-16 value of each char 

# Are there any other rules that I missed? Any implicit?
# Pay close attention to the example, including formatting
# Are there inputs to validate? Edge cases?

# Mental Model:
    # Determine the UTF-16 value of each character in a given string. Compute the sum of the UTF-16 values. Return the result.

# Example/Test Case:
    # Inputs:
        # 'Four score'
    # Outputs:
        # 984

# Data Structure:
    # None
# Types to note:
    # None

# Algorithm:
    # Given a string
    # Set total_sum to 0
    # For each char of the string
        # Set total_sum to total_sum plus the UTF-16 value of char
    # Return total_sum

# Manual test:
    # total_sum = 0
    # each value added during the loop: 
    # 70, 111, 117, 114, 32, 115, 99, 111, 114, 101
    # total_sum = 984 

# Code:
def utf16_value(string):
    total_sum = 0

    for char in string:
        total_sum += ord(char)
    
    return total_sum

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)