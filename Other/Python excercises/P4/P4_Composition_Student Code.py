""" Project #4: Composition

Name: Minglang
Date: December 1, 2022
Class: 6-B1
"""
# output:
"""
1.  People who live in glass houses should lower their blinds.
2.  Get all your ducks in a row before they hatch.
3.  the lazy dog jumped over the quick brown fox
4.  6
5.  Always the bridesmaid, never the
bird in the bush.
"""

# first accepts a string s and an integer x as arguments
# and returns the first x characters of s as a string
def first(s, x):
    return s[:x]

# last accepts a string s and an integer x as arguments
# and returns the last x characters of s as a string
def last(s, x):
    return s[(-x):]

# conc accepts any number of strings as arguments
# and concatenates them together into one string
# and then returns that new string.
# conc is short for "concatenate"
def conc(*args):
    new_string = ''
    for s in args:
        new_string = new_string + s
    return new_string

# After you do some experimentation with the functions to learn how
# they work, you will do Problem 1 together as a class. (If you figure
# out how to do it before the class is done with the experimentation
# phase, you are welcome to do it and move on to the other problems.)

# Afterward, solve the remaining problems by composing the functions,
# passing in any necessary arguments. You can use the shell to continue
# to tinker with the functions to find the solutions. You can also use
# temporary prints to save intermediate steps, making it easier to get
# to the final, complete composition.

# Problem 1
# Compose the functions to turn the following strings into:
# 'People who live in glass houses should lower their blinds.'
# Save it in the variable a.
a1 = 'People who live in glass houses should not throw stones.'
a2 = 'The neighbors never lower their blinds.'
a = conc(first(a1, 38), last(a2, 20))
print('1. ', a)

# Problem 2
# Use the functions to turn the following strings into:
# 'Get all your ducks in a row before they hatch.'
# Save it in the variable b.
b1 = 'Do not count your chickens before they hatch.'
b2 = 'Get all your ducks in a row to make the job easier.'
b = conc(first(b2, 27), last(b1, 19))
print('2. ', b)

# Problem 3
# Use the functions to turn the following string into:
# the lazy dog jumped over the quick brown fox
# Save it in the variable c.
c1 = 'the quick brown fox jumped over the lazy dog'
c = conc(last(c1, 12), first(last(c1, 25), 13), first(c1, 19))
print('3. ', c)

# Problem 4
# Compose functions in a single expression to calculate the factorial
# of the GCD of the ceiling of the square root of 410 and the floor of 
# pi squared. Save the result in the variable result.
# Don't forget to import the math module.

import math

result = math.factorial(math.gcd(math.ceil(math.sqrt(410)), math.floor(math.pi ** 2)))
print('4. ', result)


# Problem 5: Challenge problem
# Use the functions first, last, and conc to turn the following
# strings into:
# 'Always the bridesmaid, never the
# bird in the bush.'
# The string should be on two separate lines as shown.
# Save it in the variable d.
d1 = 'Always the bridesmaid, never the bride.'
d2 = 'A bird in the hand is worth two in the bush.'
d = conc(first(d1, 32), "\n", last(first(d2, 13), 11), last(d2, 6)) 
print('5. ', d)
