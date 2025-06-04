"""
Worksheet # 8: Data Structure Use Cases
Student Code
Python Level 3

Name: Minglang
Section: 8-D14
"""

# Uncomment any provided print statements as needed to verify results.


"""
Part 2
"""

print('\n *** Problem 5 ***\n')

# In the code block below, find and correct the error that prevents the 
# correct counting of occurrences of each word in the text string.

text = "cat dog cat bird dog cat bird bird"
print("Text:", text)
words = text.split()  # splits the string into words

word_count = {}

for word in words:
    if word not in word_count:
        word_count[word] = 1 
    else:
        word_count[word] += 1

print("Word count:", word_count)


print('\n *** Problem 6 ***')

# Convert the following 5x5 matrix into a dictionary representation.
matrix = [
    [0, 7, 0, 0, 0],
    [0, 0, 0, 6, 0],
    [0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ]

matrix_dict = {}

for i in range(len(matrix)):
    matrix_dict[i] = matrix[i]

print(matrix_dict)


print('\n *** Problem 7 ***')

# Given the nested dictionary nba_players below, add a new player,
# “LeBron James” of the “Lakers” with 4 championship rings, using an assignment
# statement. After adding, print the updated dictionary with each full entry 
# (key and value) on a separate line.

nba_players = {
    ('Curry', 'Stephen') : {'team':'Warriors', 'rings':4},
    ('Thompson', 'Klay') : {'team':'Warriors', 'rings':4},
    ('Brooks', 'Dillon') : {'team':'Rockets','rings':0}
}

nba_players[('James', 'Lebron')] = {'team':'Lakers', 'rings':4}

for i in nba_players:
    print(i, nba_players[i])

print('\n *** Problem 8 ***')

# You’re designing a system to quickly lookup kids’ movie ratings (rated for
# quality on a scale of 1 to 10). Choose the appropriate data structure to
# store a list of movies and their ratings, and demonstrate adding a movie,
# changing a movie’s rating, and removing a movie. Why did you choose that data
# structure? (Sample movies and ratings to include in your data structure:
# "Toy Story": 8.3, "Frozen": 7.5, "Moana": 7.6)

# Answer already made so i changed it a little

# A dictionary is suitable for this because you can easily get
# the rating with only the name of the movie, and it is mutable
# so ratings can be changed, added, or deleted. 

movies = {
    "Toy Story": 8.3,
    "Frozen": 7.5,
    "Moana": 7.6
}

movies["Asdfmovie"] = 7.7
movies["Moana"] = -110
del movies["Toy Story"]

print(movies)


"""
Part 2: Challenge Problems
"""

print('\n *** Problem 9 ***')

# You’re a wildlife researcher in a national park. Every day, you observe
# different animals and note them down. You want to keep track of each type of
# animal and the number of sightings. You need to quickly look up how many
# times an animal has been observed. Choose an appropriate data structure to
# store this data and implement a function to add a sighting for a given animal 
# and another function to look up the number of sightings for an animal.

animal_sightings = {}

def add_sighting(animal):
    if (animal in animal_sightings):
        animal_sightings[animal] += 1
    else:
        animal_sightings[animal] = 1

def get_sightings(animal):
    return animal_sightings[animal]

add_sighting("emu")
add_sighting("emu")
add_sighting("koala")
add_sighting("wallaby")
add_sighting("kangaroo")
add_sighting("koala")

print(animal_sightings)
print("There were", get_sightings("koala"), "koala sightings.")


print('\n *** Problem 10 ***')

# You are developing a software for a restaurant. The restaurant serves various
# dishes, and each dish has a list of ingredients. Customers can order multiple
# dishes. Your task is to create a function get_ingredients() that, given a 
# list of dishes ordered by a customer, returns a list of all ingredients 
# needed for those dishes (including any duplicates in different dishes).

# Choose an appropriate data structure to contain the names of the dishes and
# the set of ingredients each requires. Some suggested dishes and ingredients:
# burger (bun, patty, lettuce, tomato); pizza (dough, tomato sauce, cheese);
# and pasta (pasta, tomato sauce, cheese, basil).

needed = {
    'Pasta': ['noodles', 'sauce'],
    'Burger': ['buns', 'meat'],
    'Pizza' : ['sauce', 'bread']
}

def get_ingredients(lis):
    ans = []
    for i in lis:
        for j in needed[i]:
            ans.append(j)
    return ans

ingredients = get_ingredients(['Pasta', 'Burger', 'Pizza'])
print(ingredients)