# Tyler Stiefvater
# UWYO COSC 1010
# Submission Date: 11/06/24
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert_to_number(string):
    try:
        number = int(string)
        return number
    except ValueError:
        try:
            if string.count('.') == 1:
                number = float(string)
                return number
            else: 
                return False
        except ValueError:
            return False            


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, x_lower, x_upper):
    if not isinstance(x_lower, int) or not isinstance(x_upper, int):
        return False

    y_values = []
    for x in range(x_lower, x_upper + 1):
        y = m * x + b
        y_values.append(y)
    return y_values

while True:
    m = input("Enter the slope, type q to quit: ")
    if m.lower() == 'q':
        break
    b = input("Enter the y-intercept: ")
    x_lower = input("Enter the lower x value: ")
    x_upper = input("Enter the upper x value: ")

    m = convert_to_number(m)
    b = convert_to_number(b)
    x_lower = convert_to_number(x_lower)
    x_upper = convert_to_number(x_upper)    

    if m is False or b is False or x_lower is False or x_upper is False:
        print("Invalid input, please enter numbers only")
    else:
        result = slope_intercept(m, b, x_lower, x_upper)
        print("y-values:", result)


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None

    sqrt_discriminant = discriminant**0.5
    root1 = (-b + sqrt_discriminant)/(2 * a)  
    root2 = (-b - sqrt_discriminant)/(2 * a)
    return root1, root2  

while True:
    a = input("Enter the coefficient of a, type q to quit: ")
    if a.lower() == 'q':
        break
    b = input("Enter the coefficient of b: ")
    c = input("Enter the coefficient of c: ")

    a = convert_to_number(a)
    b = convert_to_number(b)
    c = convert_to_number(c)
    if a is False or b is False or c is False:
        print("Invalid, please enter numbers")
    else:
        result = quadratic_formula(a, b, c)
        print("Roots:", result)

