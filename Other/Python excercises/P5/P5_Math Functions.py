# The cookies were stolen by the neighbor's Eurasian magpie

import math

# Minglang Du
# January 5, 2023
# Project 5: Math Functions

# Problem 1

def vol_sphere(r):
    """
    Find the volume of a sphere.
    
    Arguments:
    r - radius of sphere, float
    
    Return:
    print
    """
    print("volume of sphere: " + str(round((((4/3) * math.pi * (r ** 3))) * 10) / 10) + " units")

# Problem 2

def cel_to_fah(celsius):
    """
    Convert degrees celsius to degrees fahrenheit.
    
    Arguments:
    celsius - temperature, float
    
    Return:
    print
    """
    print("temperature: " + str((celsius * (9 / 5)) + 32) + " degrees fahrenheit")
    
# Problem 3    

def ft_in_to_cm(feet, inches):
    """
    Convert feet and inches into centimeters.
    
    Arguments:
    feet - length, int
    inches - length, int
    
    Return:
    print
    """
    feet_cm = round(feet * 12 * 2.54)
    inches_cm = round(inches * 2.54)
    print("centimeters, rounded: " + str(feet_cm + inches_cm))
    
# Problem 4    

def invest_value(start_value, years, int_rate):
    """
    Calculate the value of an investment.
    
    Arguments:
    start_value - original value of investment, int
    years - years waited, int
    int_rate - percent interest rate, int (0 < int_rate <= 100)
    
    Return:
    print
    """
    print("End value: " + str(round(start_value * ((1 + (int_rate / 100)) ** years))) + " dollars")
    
def main():
    """In function to satisfy pylint."""
    vol_sphere(2)
    cel_to_fah(10)
    ft_in_to_cm(5, 3)
    invest_value(20000, 30, 5)
    
if __name__ == "__main__":
    main()
    
# output
"""
volume of sphere: 33.5 units
temperature: 50.0 degrees fahrenheit
centimeters, rounded: 160
End value: 86439 dollars
"""