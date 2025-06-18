# Short Long Short
# Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.

# Examples
# These examples should all print True
# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

# PEDAC

# Understand the Problem
# Inputs:
    # Two strings
# Outputs:
    # Return the result of concatenating the shorter string, the longer string, and the shorter string again
# Requirements:
    # A function with two parameters for strings
    # Determine the length of the strings
    # Return the result of the concatenation

# Are there any other rules that I missed? Any implicit?
# Pay close attention to the example, including formatting
    # Takes an empty string
# Is there an input to validate?
    # If not a string, output that it's invalid

# Mental Model:
    # Make a function that takes two strings as arguments. Determine which string is shorter. Return the result of the concatenation.

# Example/Test Case:
    # Inputs:
        # 'dog', 'go'
    # Outputs:
        # godoggo

# Data Structure:
    # None

# Algorithm:
    # Given two strings of different lengths (string1, string2)
    # If string1 is longer
        # Return string2 + string1 + string2
    # Else return string1 + string2 + string1

# Manual test:
    # string1 = 'dog', string2 = 'go'
    # 'godoggo'

# Code:
def short_long_short(string1, string2):
    try:
        if len(string1) > len(string2):
            return (string2 + string1 + string2)
        else:
            return (string1 + string2 + string1)
    except TypeError:
        return 'Oops. Not a string.'

print(short_long_short('dog', 'go'))
print(short_long_short('dog', 'go') == 'godoggo')