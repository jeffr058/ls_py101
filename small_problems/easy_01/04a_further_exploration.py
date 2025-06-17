# Further Exploration
# Modify the program to let the user specify the measurement type (meters or feet). Compute the area accordingly and print it and its conversion in parentheses.

# PEDAC

# Understand the Problem
# Inputs:
    # Unit of measure
    # Length in chosen measurement
    # Width in chosen measurement
# Outputs:
    # Area in chosen measurement and conversion
# Requirements:
    # Get the measurement type, length, and width from the user. Print the area in the chosen unit of measure and its conversion in parentheses.

# Are there any other rules that I missed?

# Mental Model:
    # Get the measurement type, length, and width from the user. Compute and print the area in the chosen unit of measure and its conversion in parentheses.

# Example/Test Case:
    # Inputs:
        # feet, 20, 35
        # meters, 7, 14
    # Outputs:
        # 700 (65.03)
        # 98 (1054.86)

# Data Structure:
    # Types to note:
        # String from input
        # Float for calculations

# Algorithm:
    # Set 10.7639 to CONVERSION
    # Get the unit of measure and store in in unit_of_measure
    # Get the length and store it in length
    # Get the width and store it in width
    # Store in area:
        # Product of the length and width converted to number type
    # If unit_of_measure is meters
        # Multiply area with CONVERSION and store it in converted_area
        # Store 'feet' in other_measure
    # Else if unit_of_measure is feet
        # Divide area by CONVERSION and store it in converted_area 
        # Store 'meters' in other_measure
    # Print the rounded area and rounded converted_area in parentheses

# unit_of_measure = 'feet'
# length = '20'
# width = '35'
# area = 700.0
# converted_area = 65.03219...
# output = 500.00 (65.03)

# unit_of_measure = 'meters'
# length = '7'
# width = '14'
# area = 98
# converted_area = 1054.8622
# output = 98.00 (1054.86)

# Code:
CONVERSION = 10.7639
unit_of_measure = input('Please enter "meters" or "feet": ')
length = input('Please enter the room length: ')
width = input('Please enter the room width: ')
area = float(length) * float(width)

if unit_of_measure == 'meters':
    converted_area = area * CONVERSION
    other_measure = 'feet'
elif unit_of_measure == 'feet':
    converted_area = area / CONVERSION
    other_measure = 'meters'

print(f'The area of the room is: {area:.2f} square {unit_of_measure} '
        f'({converted_area:.2f} square {other_measure}).')