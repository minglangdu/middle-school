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
Part 2
"""

print('\n *** Problem 6 *** ')

# Define a function find_max() that takes three numbers as parameters and  
# returns the maximum of the three.

# Write your own test cases to test your function.

def find_max(n1, n2, n3):
    if (n1 >= n2 and n1 >= n3):
        return n1
    elif (n2 >= n1 and n2 >= n3):
        return n2
    else:
        return n3

print(find_max(31, 2, 5))


print('\n *** Problem 7 *** ')

# Write a Python function eval_temp(temp) that takes a temperature
# as a parameter and returns 'Hot' if the temperature is above 85
# degrees, 'Warm' if the temperature is between 70 and 85 degrees
# inclusive, 'Cool' if the temperature is between 50 and 70 degrees
# (including 50 but excluding 70), and 'Cold' if the temperature
# is below 50.

# Write your own test cases to check every branch of your conditional,
# including edge cases.

def eval_temp(temp):
    if temp > 85:
        return 'Hot'
    elif temp > 69:
        return 'Warm'
    elif temp > 49:
        return 'Cool'
    else:
        return 'Cold'
    
print(eval_temp(99))
print(eval_temp(55))
print(eval_temp(80))
print(eval_temp(32))

print('\n *** Problem 8 *** ')

# The following code is supposed to check whether a list is sorted
# in ascending order or not, but it’s not working correctly.
# Identify and fix the problem(s). 
#   a.  First, determine when the expected output matches the actual
#       output and when it doesn’t, identify why that happens. 
#   b.  Once you fix that bug, you will likely encounter an error.
#       Fix it if/when it arises. Remember that fixing a bug can
#       reveal other bugs that had previously been hidden.

def is_sorted(list):
    for i in range(len(list) - 1):
        if (list[i] > list[i + 1]):
            return False
    return True

print(is_sorted([1, 2, 3, 4, 5]))  
# Expected output: True

print(is_sorted([1, 3, 2, 5, 4]))  
# Expected output: False


print('\n *** Problem 9 *** ')

# You’re programming a simple game where the player is located in a 2D grid at
# a position with coordinates stored in a list player_coord = [x, y]. The player 
# has three possible actions: 'up', 'down', 'left', 'right'. Each action changes
# the player's position: 'up' decreases the y-coordinate by 1, 'down' increases
# the y-coordinate by 1, 'left' decreases the x-coordinate by 1, and 'right'
# increases the x-coordinate by 1. (This follows the upper-left-origin
# coordinate system common in computing applications, where the coordinates 
# (0, 0) are at the upper left of the coordinate plane/screen.)

# Write a Python function move_player(coord, action) that takes the player’s
# current coordinates in a list and an action (a string) as parameters, and
# returns a new list with the updated coordinates after the action is performed.
# You can assume that the action will always be one of the four valid actions.
# Then, reassign the player’s global coordinate list to the function’s return
# value.


# Test the function. Call move_player() to move the player up, down, left, 
# and right. Print player_coord after each move to verify the results.

player_coord = [0, 0]

def move_player(coord, action):
    if (action == 'up'):
        coord[1] -= 1
    elif (action == 'down'):
        coord[1] += 1
    elif (action == 'left'):
        coord[0] -= 1
    else:
        coord[0] += 1
    return coord
player_coord = move_player(player_coord, 'left')
print(player_coord)
player_coord = move_player(player_coord, 'right')
print(player_coord)
player_coord = move_player(player_coord, 'up')
print(player_coord)
player_coord = move_player(player_coord, 'down')
print(player_coord)