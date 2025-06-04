"""
Worksheet # 1: Python Review
Student Code
Python Level 3

(For Publications use: Document Code 09-969.142-24)

Name: Minglang Du
Section: 8-D14
"""

# Uncomment the provided print statements as you complete each problem
# to verify results.

"""
Part 1
"""

print('\n *** Problem 1 *** ')

# Define a function subtotal(price, qty) that takes an item’s price and
# quantity purchased as parameters and returns the subtotal cost for that
# purchase rounded to two decimal places using the round() function.

def subtotal(price, qty):
    return round(price * qty, 2)

print(subtotal(3.68, 12))


print('\n *** Problem 2 *** ')

# Define a function total_with_tax(subtotal_amt, tax_rate) that takes a
# subtotal purchase amount and a tax rate as a percentage (e.g., 8.25%)
# and calculates the total amount of the purchase including tax.

def total_with_tax(subtotal_amt, tax_rate):
    tax_amt = round(subtotal_amt * tax_rate / 100, 2)
    return subtotal_amt + tax_amt

print(total_with_tax(75, 8.25))


print('\n *** Problem 3 *** ')

# Test the functions from #1 and 2 separately, and then test them together
# by using the result of placing a call to subtotal() as an argument to
# total_with_tax(), as in: total_with_tax(subtotal(…,…), …)

# Assign the result to the variable item_total.

item_total = total_with_tax(subtotal(1.99, 5), 8.25)
print(item_total)


print('\n *** Problem 4 *** ')

# Define a function concat_str() that concatenates two strings together with
# an optional separator, returning the result. The default separator should be
# a single space. Test your function with two strings and no separator provided,
# and again with two strings and a separator of your choice.

def concat_str(s1, s2, sep=""):
    return s1 + sep + s2

print(concat_str('Hello', 'world!'))
print(concat_str('Hello', 'world!', ', '))
print(concat_str('Hello', 'world!', sep = '...'))


print('\n *** Problem 5 *** ')

# The following function is supposed to calculate and return the area of a
# circle given the radius, but it’s not producing the correct result. Identify
# and fix the problem(s).

import math

def circle_area(r):
    area = math.pi * (r ** 2)
    return area

print(circle_area(5))
print(circle_area(99.9))
