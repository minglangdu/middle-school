"""
Quiz #5: Chapter 11
Student Code
Python Level 2

***
Students: copy this file from LabCommons into your H:\ drive and
replace "Student Code" in the file name with your user name
(e.g., MS2_Quiz4_JohnD.py). Rename a file by selecting it and
pressing F2. The file must be closed to do this.

You will NOT print out this Python script file for the quiz, but
you must save it in your H:\ drive so that your teacher may refer
to it when grading the quiz if needed.

"""

print('\n*** Problem 1 ***\n') 

# Write a line of code to assign a variable scores to a 5-element
# list that contains 75, 82, 91, 87, and 93 as elements (items):

scores = [75, 82, 91, 87, 93]
# Code to test Problem 1:
print(scores, '\n')


# For use with problems 4 and 5:
player_a = ['Stephen', 'Curry', ['age', 34], ['MVP', True]]


print('\n*** Problem 4 ***\n') 

# Write a statement to assign the variable name to a string formed
# from the first two items of player_a with a space between them.
# You must construct that string by accessing player_a:
name_a = player_a[0] + ' ' + player_a[1]


# Code to test Problem 4:
print(name_a, '\n')


print('\n*** Problem 5 ***\n')

# Write code below to print the two items 'MVP' and True in player_a
# You must do this by accessing player_a, not just by printing 'MVP'
# and True directly:


print(player_a[3][0], player_a[3][1])


# For use with problems 6 through 9:
users = ['BobC', 'AvaS1', 'IraL', 'DevG2']


print('\n*** Problem 6 ***\n')

# Uncomment and test this code, and explain the result on your 
# quiz paper:
#users = users + 'JoyC'
#print('users:', users, '\n')


print('\n*** Problem 7 ***\n')

# Comment the code in #6 again, and then uncomment and test the 
# code below. Explain the result on your quiz paper:
#users.extend('JoyC')
#print('users:', users, '\n')


print('\n*** Problem 8 ***\n')

# Comment the code in #7 again, and then write code to properly 
# add 'JoyC' to users, at the end of the list:
users.append('JoyC')
# Code to test Problem 8:
print('users:', users, '\n')


print('\n*** Problem 9 ***\n')

# Write code to loop over the users list, get the capitalized form
# of each string there (using the upper() method), and print the
# capitalized string on its own line:

for user in users:
    a = user.upper()
    print(a)