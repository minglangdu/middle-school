"""
Worksheet # 4: Python Shortcuts
Student Code
Python Level 3
"""

# Uncomment the provided print statements as you complete each problem
# to verify results.

"""
Part 1
"""

print('\n*** Problem 1: Multiple Assignment *** ')

# 1a. Assign values 5, 10, and 15 to variables a, b, and c respectively in a
#     single line.

print('\n(1-a)')

a, b, c = 5, 10, 15

print('a is', a, '\nb is', b, '\nc is', c, )

# 1b. Now swap the values between variables a and c using the 
#     multiple assignment feature of Python.

print('\n(1-b)')
print("\nBefore swap, a is", a, "and c is", c)

a, c = c, a

print("After swap, a is", a, "and c is", c)

# 1c. You can also use multiple assignment to assign individual variables
#     to elements of a list. Declare four variables w, x, y, z, and assign 
#     them values from the list [2, 4, 6, 8] using a single line of code.

print('\n(1-c)')

w, x, y, z = [2, 4, 6, 8]

print("\nThe values of w, x, y, z are, respectively,", w, x, y, z)


print('\n\n*** Problem 2: Augmented Assignment *** ')

# 2a. Given a = 5 and b = 10, use the -= operator to subtract b from a.

print('\n(2-a)')

a = 5
b = 10
a -= b
print("Before augmented assignment, a is", a,
      "and b is", b)

print("After augmented assignment, a is", a,
      "and b is", b)

# 2b. Given list1 = [1, 2, 3] and list2 = [4, 5, 6], use
#     augmented assignment to concatenate list2 to list1.

print('\n(2-b)')

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("\nBefore augmented assignment, list1 is", list1,
      "and list2 is", list2)
list1 += list2
print("After augmented assignment, list1 is", list1,
      "and list2 is", list2)

# 2c. Define a variable c = 20. Use an augmented assignment operator to
#     multiply c by 3.

print('\n(2-c)')

c = 20
print("\nBefore augmented assignment, c is", c)
c *= 3
print("After augmented assignment, c is", c)


print('\n\n*** Problem 3: From-Import Statement *** ')

# 3a. Import the math module and use it to print the square root of 81.

print('\n(3-a)')

import math
print(math.sqrt(81))
# 3b. Now use the from-import statement to import the sqrt function
#     from the math module and calculate the square root of 64.

print('\n(3-b)')

from math import sqrt
print(sqrt(81))

# 3c. Use the from-import statement to import the date object from the 
#     datetime module. The date object has a method called today() that
#     returns today's date. Sample call: date.today(). Print today's date.

print('\n(3-c)')

from datetime import date

print(date.today())

print('\n\n*** Problem 4: Line Continuation *** ')

# 4a. Given that a, b, c, d, e, f = 2, 3, 5, 7, 11, 13, write an if statement
#     to check the following condition using implicit line continuation:
#   (a < b and c > d) or (e < f and b + c > d) or (d - e > f and a * c < b * d)
#     Your if statement should output "condition met" if the condition is true.

print('\n(4-a)')

a, b, c, d, e, f = 2, 3, 5, 7, 11, 13

if ((a < b and c > d) or
    (e < f and b + c > d) or
    (d - e > f and a * c < b * d)):
    print("condition met")


# 4b. Write the same conditional using explicit line continuation.

print('\n(4-b)')

a, b, c, d, e, f = 2, 3, 5, 7, 11, 13
if (a < b and c > d) or \
    (e < f and b + c > d) or \
    (d - e > f and a * c < b * d):
    print("condition met")

# 4c.  Imagine you're trying to calculate the distance between two points in
#      3D space. The formula for this is
#
#          sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
#
#      Your points are p1 = (2, 4, 6) and p2 = (5, 9, 3). Write the calculation
#      in one line, then split the statement using implicit line continuation 
#      to improve readability.

print('\n(4-c)')

p1 = [2, 4, 6]
p2 = [5, 9, 3]

# Calculate in one line
dist = sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

# Using line continuation for better readability
distance = sqrt((p2[0] - p1[0])**2 + \
           (p2[1] - p1[1])**2 + \
           (p2[2] - p1[2])**2)

print ("\nDistance between", p1, "and", p2, "is", distance)
