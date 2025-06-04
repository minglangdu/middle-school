"""
Worksheet # 6: Dictionaries
Student Code
Python Level 3

Name: Minglang Du
Section: 8-D14
"""

# Uncomment any provided print statements as needed to verify results.


print('\n *** Problem 1 - Creating and Accessing Dictionaries *** ')

# 1a. Create an empty dictionary named book_record and print it.

print('\n(1-a)')

book_record = {}
print(book_record)

# 1b. Now add the following title and author to the book_record dictionary:
#     'Title': 'To Kill a Mockingbird', 'Author': 'Harper Lee'.
#     Print the book_record dictionary.

print('\n(1-b)')

book_record['Title'] = 'To Kill a Mockingbird'
book_record['Author'] = 'Harper Lee'
print(book_record)

# 1c. Create a dictionary named class_students with the following keys and
#     values: 'John': 12, 'Emily': 13, 'Alex': 14.

print('\n(1-c)')

class_students = dict(John=12, Emily=13, Alex=14)
print(class_students)  # Output: {'John': 12, 'Emily': 13, 'Alex': 14}


print('\n *** Problem 2 - Dictionary Methods *** ')

# 2a. Use the get() method to retrieve the age of 'Daniel' from the
#     class_students dictionary. If 'Daniel' is not present, it should return
#     'Student not found.'

print('\n(2-a)')

age = class_students.get('Daniel', 'Student not found.')

print(age)  # Output: 'Student not found.'


# 2b. Remove 'Emily' from the class_students dictionary using the pop() method.
#     Print the returned value and the updated dictionary.

print('\n(2-b)')

print(class_students.pop('Emily'), class_students)

print(class_students)