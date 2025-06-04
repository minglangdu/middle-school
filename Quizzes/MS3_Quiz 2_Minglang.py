"""
Quiz # 2: Data Structures
Student Code
Python Level 3

(For Publications use: Document Code 09-969.166-24)

Fill out your name and section below.

Name: Minglang Du
Section: 8-D14
"""

print("\n*** Problem 1 ***")    # 12 points

# Create a tuple called planets that contains the following planets:
# 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'
# (Copy-paste the planet names above to save time.) Print the tuple.

planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
print(planets)

print("\n*** Problem 2 ***")    # 8 points

# Write code to get a slice of the elements including only Jupiter and Saturn
# and assign it into the variable gas_giants.

gas_giants = planets[4:6]

# Uncomment the print when done:
print(gas_giants)


print("\n*** Problem 3 ***")    # 8 points

# You are given the coordinates of three landmarks on a map as tuples
# representing (x, y) coordinates: (3, 4), (6, 1), and (2, 7). Create a tuple
# called landmark_coordinates to store these coordinates.

landmarks_coordinates = ((3, 4), (6, 1), (2, 7))

# Uncomment the print when done:
print(landmarks_coordinates)


print("\n*** Problem 4 ***")    # 10 points

# You have been provided with the tuple book_data which contains information
# about a book in the following order:
#
#     'Title', 'Author', 'Publication Year', 'Genre'

book_data = ('The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy')

# Unpack book_data into individual variables in a single line:

title, author, pub_year, genre = book_data

# Uncomment the print statement to test your unpacking when done:
print(f"{genre} novel {title} was written by {author} and published",
      f"in {pub_year}.")  


print("\n*** Problem 5 ***")    # 22 points

# Create a dictionary named country_capitals with countries as keys and 
# their capitals as values. Include entries for the USA (Washington, D.C.),
# Japan (Tokyo) and the Philippines (Manila). Using the items() method and
# a for loop, print each country and capital (key-value pair) on its own line.

# Create the country_capitals dictionary: [10 points]

country_capitals = {
    "USA":"Washington, D.C.",
    "Japan":"Tokyo",
    "Philippines":"Manila",
}

# Create the loop to print the dictionary's items(): [12 points]

for pair in country_capitals.items():
    print(pair)

print("\n*** Problem 6 ***")    # 16 points

# Given the dictionary of students and their ages below, complete the two print
# statements with calls to get() on the dictionary. Each call to get() should
# retrieve the student's age if the student exists in the dictionary or else
# output "Student not found.":

students = {"John":14, "Amaya":12, "Mario": 13}

# Complete and uncomment the print statements below. [8 points each]
print("Amaya's age:", students.get("Amaya", "Student not found."))
print("Jane's age:", students.get("Jane", "Student not found."))


print("\n*** Problem 7 ***")    # 24 points

# Given the students dictionary from Problem 6:

# (a) Add a student named "Jericho", age 14, into the students dictionary.
# [8 points]


# (b) Retrieve the value of and remove the student "Mario" in the same 
#     statement, printing the result:
# [8 points]


# (c) Add the items from the following dictionary into students using update().
# [8 points]
new_students = {"Nikhil":13, "Nora":14}

students["Jericho"] = 14
print(students.pop("Mario"))
students.update(new_students)

# To check your work, after completing problem 7, the following print should
# output: {'John': 14, 'Amaya': 12, 'Jericho': 14, 'Nikhil': 13, 'Nora': 14}
print(students)
