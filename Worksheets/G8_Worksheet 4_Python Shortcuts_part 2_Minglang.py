"""
Worksheet # 4: Python Shortcuts
Student Code
Python Level 3
"""

# Uncomment the provided print statements as you complete each problem
# to verify results.
print('\n\n*** Problem 5: F-string Formatting *** ')

# 5a.  You are given the variables price = 9.99, qty = 3, item = "burger",
#      and restaurant = "Joe's Diner". Using F-string formatting with 
#      those variables, create and output a string that says:
#
#          3 burgers at Joe's diner costs $29.97.

print('\n(5-a)')

price = 9.99
qty = 3
item = "burger"
restaurant = "Joe's Diner"
sentence = f"{qty} {item}s at {restaurant} costs {price * qty}."

print(sentence) 

# 5b.  Import pi from the math module. hen, print pi to 2 decimal places, 
#      T4 decimal places, and in scientific notation with 2 decimal places
#      using F-string formatting.

from math import pi

print('\n(5-b)')

formatted_string = f"{pi:.2f} {pi:.4f} {pi:.2e}"

print(formatted_string)  # Output: 3.14, 3.1416, 3.14e+00

# 5c.  You're given a variable day = 1. Use F-string formatting to print the
#      day with a leading zero if the day is a single digit.

print('\n(5-c)')
day = 1
formatted_day = f"{'0' + str(day) if abs(day) < 10 else day:<}"

print(formatted_day)  # Output: 01




"""
Part 2: Challenge Problems
"""

print('\n\n*** Problem 6: Conditional (Ternary) Expressions *** ')

# 6a. Given a variable temperature = 85, write a one-line conditional (ternary)
#     expression to print "It's hot" if temperature is above 79, otherwise 
#     print "It's cold".

print('\n(6-a)')

temperature = 85

print(f"""{"It's hot" if temperature > 79 else "It's cold"}""")
# 6b. Using a conditional expression, assign the value "positive" to a variable
#     called sign if a given number num is greater than zero, "negative" if
#     it's less than zero, and "zero" if it's equal to zero.

print('\n(6-a)')

num = 10  # you can change this value to test with different numbers

sign = f"{'positive' if num > 0 else 'negative' if num < 0 else 'zero'}"

print(sign)  # Output: positive


print('\n\n*** Problem 7: List Comprehensions *** ')

# 7a. Using a list comprehension, generate a list of the cubes of all integers
#     from 0 to 10, but only if the cube is less than 500.

print('\n(7-a)')

cubes = [x ** 3 for x in range(10) if x ** 3 < 500]

print(cubes)  # Output: [0, 1, 8, 27, 64, 125, 216, 343]

# 7b. Given a list of names, use a list comprehension to create a new list
#     that contains only those names that start with the letter 'A'.

print('\n(7-b)')

names = ['Adi', 'Andrew', 'Carney']

a_names = [name for name in names if name[0].lower() == 'a']

print(a_names)  # Output: ['Adi', 'Andrew']

# 7c. Given a list of numbers, use a list comprehension with a conditional
#     expression to create a new list called parity that contains the string 
#     "even" for every even number and "odd" for every odd number in the
#     original list.

print('\n(7-c)')

numbers = [11, 42, 23, 84, 110]

parity = [('even' if x % 2 == 0 else 'odd') for x in numbers]

print(parity)  # Output: ['odd', 'even', 'odd', 'even', 'even']
print()