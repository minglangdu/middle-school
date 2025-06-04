"""
Worksheet # 3: Python Review
Solutions
Python Level 3

(For Publications use: Document Code 09-969.146-24)

Name: Minglang Du
Section: 8-D14
"""

"""
Part 2: Collections and Iterables
"""

print('\n *** Problem 8 *** ')

# a. Create a list named numbers containing the numbers 10 to 15.
# b. Use a loop to double each number in the list.
# c. Print the modified list.

# Create a list of numbers
numbers = list(range(10, 16))
# Use a loop to double each number in the list
for i in range(len(numbers)):
    numbers[i] *= 2
# Print the modified list
print(numbers)


print('\n *** Problem 9 *** ')

# The code below attempts to capitalize the first letter of the string location.
# Identify and fix the error in the code.

location = 'osaka'
location = location.upper()
print(location)  # Output should be 'Osaka'


print('\n *** Problem 10 *** ')
print('See comments in code.')

# Identify which of the following are iterables in Python: list, dictionary,
# integer, string, tuple. Define iterable.

# Answer: 


print('\n *** Problem 11 *** ')
print('See comments in code.')
# Of those items in Problem 10 that are iterables, which are mutable? Explain.

# Answer: 


"""
Challenge Problem for Part 2
"""

print('\n *** Problem 12 *** ')

# a. Create a string variable named string1 containing the word 'Challenger'.
# b. Write a loop to reverse the string without using slicing.
# c. Print the reversed string.

# Create a string variable
string1 = ''
# Write a loop to reverse the string

# Print the reversed string
print(reversed_string)