"""
Worksheet # 5: Tuples
Student Code
Python Level 3

Name: Minglang Du
Section:  8-D14
"""

# Uncomment any provided print statements as needed to verify results.

"""
Part 1
"""

print('\n *** Problem 1 - Creating Tuples *** ')

# 1a. Write code to create and print a tuple named "cities" with the elements
#     'New York', 'Paris', 'Tokyo', 'London'.

print('\n(1-a)')

cities = 'New York', 'Paris', 'Tokyo', 'London'

print(cities)

# 1b. Write code to create a single-element tuple named "single" with the 
#     element 100 (add a trailing comma). What will happen if you don't  
#     include a trailing comma? Try this as well to test your hypothesis.

print('\n(1-b)')

single = (100,)
unsingle = (100)
print(single, unsingle)

print('\n *** Problem 2 - Accessing Tuple Elements *** ')

# 2a. Write code that creates a tuple named "days" with the elements 
#     'M', 'Tu', 'W', 'Th', 'F'. Then, print the element for 'Tu' using
#     the index number.

print('\n(2-a)')

days = 'M', 'Tu', 'W', 'Th', 'F'

print(days[1])

# 2b. Write code to slice the days tuple to print the weekday abbreviations
#     from Tu to F.

print('\n(2-b)')

print(days[1:])

print('\n *** Problem 3 - Tuple Immutability *** \n')

# 3.  Write code to try to change the third element of the "cities" tuple to
#     'Berlin'. What happens and why? Type your answer as a comment.

# It throws an error because tuples cannot be changed

print('\n *** Problem 4 - Tuple Packing and Unpacking *** ')

# 4a. Write code to create a tuple named "student_scores" by
#     packing the following scores: 85, 90, 78, 92 (no parentheses).



print('\n(4-a)')

student_scores = 85, 90, 78, 92

print(student_scores)  # Output: (85, 90, 78, 92)

# 4b. Write code to unpack the "student_scores" tuple into variables named
#     "math", "science", "english", "history" using multiple assignment. 
#     Then, print the score for English.

print('\n(4-b)')

math, science, english, history = student_scores

print(english)  # Output: 78

# 4c. What will happen if you try to unpack "student_scores" into three
#     variables instead of four? Write code to test your hypothesis.

print('\n(4-c)')
print("Code commented to prevent error. Uncomment to see what happens.")

# It will throw an error because the amount of variables and length don't match

# math, science, english = student_scores


"""
Part 1: Challenge Problem
"""

print('\n *** Problem 5 - Tuple Unpacking, Formatted Output *** \n')

# You are given a student name, their grade, and their average score as a 
# tuple. You need to print this information in a formatted way. Use tuple
# unpacking to get the information from the tuple, then print the information
# in a user-friendly format. Here is an example tuple that you might be given:

student_info = ("John Smith", "8th grade", 92.5)
name, grade, score = student_info
print(f"{name}, who is in {grade}, has an average score of {score}.")

# Here is what the output of your code should look like:
# John Smith, who is in 8th grade, has an average score of 92.5.



