"""
Worksheet # 3: Python Review
Solutions
Python Level 3

(For Publications use: Document Code 09-969.146-24)

Name: Minglang Du
Section: 8-D14
"""

"""
Part 1: Loops
"""

# Uncomment the provided print statements as you complete each problem
# to verify results.


print('\n *** Problem 1 *** ')

# Write a for loop that prints the integers from 0 to 20 but skips
# printing odd numbers by using a continue statement.

for i in range(0, 21):
    if i % 2 != 0:
        continue
    print(i, end = ' ')


print('\n *** Problem 2 *** ')

# Implement the task in #1 without a continue -- just add an
# argument to range().
for i in range(0, 21, 2):
    print(i, end = ' ')

print('\n *** Problem 3 *** ')

# Write Python code that asks for a positive integer input and prints a
# countdown from that number down to 1, inclusive. If the user inputs a
# non-positive integer, the program should print an error message and ask for
# another input. Use two while loops for this problem — one for the error
# checking and another one for the countdown.
a = 0
while 1:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        print("Invalid input.")
    else:
        break
while a > 0:
    print(a, end = ' ')
    a -= 1

print('\n *** Problem 4 *** ')

# This Python program is meant to calculate the factorial of a given number.
# However, it currently results in an infinite loop due to a bug. Fix the bug
# and add a comment in your code identifying the problem and how your fix
# solved it.

n = int(input("Enter a number: "))
factorial = 1

# This bug caused an infinite loop because the
# end statement in the while loop was never
# reached. This was solved by decrementing n. 

while n > 1:
    factorial = factorial * n
    n -= 1

    
print("The factorial is", factorial)


print('\n *** Problem 5 *** ')

# Write a Python program that randomly chooses a secret number between 1 and 5
# (inclusive), and asks the user to guess the number. The game should continue
# until the user guesses the correct number. Implement this using a while loop
# and a break statement.
import random

ans = random.randint(1, 5)
while 1:
    guess = int(input("Guess a number between 1 and 5: "))
    if (guess == ans):
        print("Correct!")
        break
    else:
        print("Incorrect")



"""
Challenge Problems for Part 1
"""

print('\n *** Problem 6 *** ')

# Write a program that builds a sequence of numbers. The program should start
# by printing 1 and then add 4 to the previous number in each subsequent step.
# The program should stop just before it reaches or exceeds 100.
i = 1
while i < 100:
    print(i, end = ' ')
    i += 4



print('\n *** Problem 7 *** ')

# The program is supposed to print all odd numbers from 1 to 20, but it is
# only printing 1 and then hanging/freezing. Fix the bug and add a comment in
# your code identifying the problem and how your fix solved it.

# Buggy code (uncomment to test):

i = 0
while i < 20:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)
               # Once i becomes 2 (an even number), this line is never reached.
               # The if-condition is always met and the continue statement just
               # keeps executing, continuing the loop indefinitely.
               # ^ what they said


