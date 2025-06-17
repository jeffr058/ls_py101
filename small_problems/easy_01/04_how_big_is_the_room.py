# How big is the room?
# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# PEDAC

# Understand the Problem
# Inputs:
    # Length in meters
    # Width in meters
# Outputs:
    # Area in square meters
    # Area in square feet
# Requirements:
    # Get the inputs from the user. Calculate and print the area in both square meters and feet.
# Are there any other rules that I missed?
    # Is it implicit to have the unit of measure following the numbers?
# Mental Model:
    # Using length and width in meters given by the user, calculate the area in meters and convert the area to feet and print both, indicating the unit of measure.

# Example/Test Case:
    # Inputs:
        # length: 10, width: 12
        # length: 500, width: 1000
        # length: 0, width: 0
    # Outputs:
        # First output:
            # Area in meters: 120 square meters
            # Area in feet: 1291.668 square feet
        # Second output:
            # Area in meters: 500000 square meters
            # Area in feet: 5381950 square feet
        # Third output:
            # Invalid entry

# Data Structure:
    # None

# Algorithm:
    # Ask the user for length and width in meters
    # Store the values in length_in_m and width_in_m
        # lenth_in_m = 10, width_in_m = 12
    # While either value is 0, ask for valid input and store the value in the corresponding variable
        # If the new value is valid, move on
    # Calculate the area in meters and store the value in area_in_m
        # area_in_m = 120
    # Convert the area to square feet and store the value in area_in_ft
        # area_in_ft = 1291.668
    # Print the value with "square meters"
        # 120 square meters
    # Print the value with "square feet"
        # 1291.668 square feet

# Code:
M_TO_FT = 10.7639

def area_of_room():
    length_in_m = input('Enter the room length in meters: ')
    width_in_m = input('Enter the room width in meters: ')
    
    while True:
        if length_in_m == '0':
            length_in_m = input('Enter a valid length in meters: ')
        elif width_in_m == '0':
            width_in_m = input('Enter a valid width in meters: ')
        else:
            break

    area_in_m = float(length_in_m) * float(width_in_m)
    area_in_ft = float(area_in_m) * M_TO_FT

    print(f'The area of the room is: {area_in_m} square meters.')
    print(f'The area of the room is: {area_in_ft} square feet.')

area_of_room()