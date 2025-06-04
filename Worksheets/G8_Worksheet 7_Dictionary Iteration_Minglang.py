"""
Worksheet # 7: Dictionary Iteration
Student Code
Python Level 3

Name: Minglang Du
Section: 8-D14
"""

# Uncomment any provided print statements as needed to verify results.


print('\n *** Problem 1 - Basic Dictionary Iteration *** ')

# 1a. You’re organizing a video game tournament and you want to keep track of
#     player scores. Create a dictionary called player_scores with the player
#     names below as keys and their scores as values. Then, using iteration,
#     print out each player’s name and their score in this format:
#
#       Ankur has 550 points.
#       Becca has 800 points.
#       Cid has 400 points. 

print('\n(1-a)')

player_scores = dict(Ankur=550, Becca=800, Cid=400)

for player, score in player_scores.items():
    print(f"{player} has {score} points.")

# 1b. You have a dictionary books_and_authors with books as keys and their
#     authors as values. Using iteration, print out each book and its author
#     on a new line:

print('\n(1-b)')
books_and_authors = {
    "1984": "George Orwell",
    "To Kill a Mockingbird": "Harper Lee",
    "The Great Gatsby": "F. Scott Fitzgerald"
    }

for book, author in books_and_authors.items():
    print(book, author)


print('\n *** Problem 2 - Using View Objects for Iteration *** ')

# You’re running a pizza restaurant and tracking your available ingredients.
# You are given: 

ingredients = {"Pepperoni": 10, "Mushrooms": 15, "Olives": 20, "Anchovies": 5}

# 2a. Use the keys() method to print out each ingredient on a new line.

print('\n(2-a)')
    
for i in ingredients.keys():
    print(i)
    
# 2b. Use the values() method to calculate and print the total quantity of
#     ingredients.

print('\n(2-b)')

print(sum(list(ingredients.values())))

#print("The total quantity of ingredients is", total)

# 2c. Use the items() method to print all ingredient-quantity pairs from the
#     ingredients dictionary in the format "We have 10 pounds of pepperoni."

print('\n(2-c)')

for i, j in ingredients.items():
    print(f"We have {j} pounds of {i.lower()}.")

print('\n *** Problem 3 - Comparing View Objects and Direct Key Iteration ***')

# 3a. Given a dictionary favorite_books with student names as keys and their
#     favorite books as values, write two pieces of code to print out the
#     names of the students: one using direct key iteration and another
#     using the keys() method.

print('\n(3-a)')

favorite_books = {
    "Sam": "1984",
    "Alex": "To Kill a Mockingbird",
    "Jesse": "The Great Gatsby"
    }
for student in favorite_books:
    print(student, end=" ")
print()
for student in favorite_books.keys():
    print(student, end=" ")
    
# 3b. Given the dictionary car_speeds below, write two pieces of code: one
#     using direct key iteration and another using the items() method to print
#     out each car and its speed.

print('\n(3-b)')

car_speeds = {"Sports Car": 200, "SUV": 120, "Truck": 100}

for i in car_speeds:
    print(i, car_speeds[i], end = " ")
print()
for car, speed in car_speeds.items():
    print(car, speed, end = " ")

"""
Challenge Problems
"""

print('\n *** Problem 4 - Swapping Keys and Values *** ')

# Write a function swap_keys_values(d) that takes a dictionary as its argument
# and returns a new dictionary where the keys and values have been swapped.
# Use the following dictionary of planets and their distances from the sun as
# your function argument:

planet_sun_dist = {"Earth": 1, "Mars": 1.52, "Venus": 0.72}

def swap_keys_values(d):
    new_dict = {}
    for i, j in d.items():
        new_dict[j] = i
    return new_dict

print(swap_keys_values(planet_sun_dist))


print('\n *** Problem 5 - Modifying Dictionary During Iteration *** ')

# You’re running a library and have a dictionary of books where keys are book
# titles and values are the number of copies available. Write a program that
# traverses the dictionary and removes any book that has no copies left.

# Important note: Modifying a dictionary while iterating over it is generally
# considered a bad practice because it can lead to unexpected behavior.
# However, you can first make a copy of the dictionary (or its keys) and
# iterate over that while modifying the original dictionary.

# For this problem, first try iterating over the dictionary directly. Then,
# once you’ve seen the result of doing that, save a copy of the keys as a list
# (pass books.keys() as an argument to list() and assign the result into a
# variable). Then, iterate over that list instead.

books = {"1984": 3, "To Kill a Mockingbird": 0,
         "The Great Gatsby": 2, "Moby Dick": 0}
import copy

bcopy = copy.deepcopy(books)

for i in bcopy:
    if bcopy[i] <= 0:
        del books[i]

print(books)  # Should print: {'1984': 3, 'The Great Gatsby': 2}