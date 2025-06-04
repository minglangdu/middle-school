"""
Worksheet # 8: Data Structure Use Cases
Student Code
Python Level 3

Name: Minglang Du
Section: 8-D14
"""

# Uncomment any provided print statements as needed to verify results.


"""
Part 1
"""

print('\n *** Problem 1 *** ')

# Create a data structure containing your top 3 favorite animals in order,
# then replace your third favorite with a new one. Which data structure did
# you use, and why?

fav_animals = ['toaster', 'bread', 'breadstick']
fav_animals[2] = 'dwarf'

print(fav_animals)

# I used a list because it lists things in order, needed for a top 3, and
# allows you to change it. 

print('\n *** Problem 2 *** ')

# Unpack the data structure from #1 into 3 separate variables.

fav_anim_1, fav_anim_2, fav_anim_3 = fav_animals

print(fav_anim_1, fav_anim_2, fav_anim_3)


print('\n *** Problem 3 *** ')

# Define a 2D data structure to represent an empty chess board (an 8×8 grid),
# where 0s represent empty squares. Why did you choose that data structure?

chess_board = [[0] * 8 for i in range(8)]

for row in chess_board:
    print(row)

# I used a list because it can be changed, can store other lists, and can
# represent a 2d matrix

print('\n *** Problem 4 *** ')

# You’re creating a game and want to represent a player’s position in a 2D grid
# using a data structure that should not be mutable. Create a data structure to
# hold that information and explain why you chose it.

player_position = (5, 3125)

print(player_position)

# I chose a tuple because it is immutable, fitting the question's constraints
