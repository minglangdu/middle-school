"""
Worksheet # 15: Object-Oriented Programming
Student Code
Grade 8

Name: Minglang Du
Class Section (if more than one G8 class): 8-D14
"""

print('\n *** Problem 1 *** ')

"""
In the comment below, define Object-Oriented Programming (OOP) 
using your own words.
"""

print("Answer in the comment.")

"""
OOP is a type of writing code that defines many types (or classes) of objects in order to allow for more complex behavior.
For example, to simulate animals using OOP, a class Animal would be defined and multiple objects would be created as instances of that class and could use their attributes and methods to simulate animals.

"""


print('\n *** Problem 2 *** ')

# Given the procedural programming approach below, re-write it using 
# the OOP approach. Run your own test cases for the OOP version.

def get_description(name, age):
    return f"{name} is {age} years old"

# Test cases
student1_name = "Alice"
student1_age = 15

student2_name = "Bob"
student2_age = 16

print(get_description(student1_name, student1_age))
print(get_description(student2_name, student2_age))

# Write the OOP version and its test cases below:

print("-----")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_description(self):
        return f"{self.name} is {self.age} years old"
    
student1 = Student("Alice", 15)
student2 = Student("Bob", 16)

print(student1.get_description())
print(student2.get_description())


print('\n *** Problem 3 *** ')

"""
Explain in your own words the benefits of using the OOP approach. Use your code
from Problem 2 as an example. Identify a scenario where it would be more
beneficial to use the OOP approach.
"""

print("Answer in the comment.")

"""
The OOP approach has many benefits similar to how creating functions has many benefits.
It makes writing attributes and methods for many similar objects much easier by defining classes that streamline the writing of attributes and methods,
similar to how creating functions streamlines the writing of methods and processes. 

"""


print('\n *** Problem 4 *** ')

# Identify and fix the errors in the following code (uncomment to test):
class Elephant:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"The elephant's name is {self.name} and",
              f"it is {self.age} years old")

# Provided test case:
elephant1 = Elephant("Dumbo", 5)
elephant1.description()


print('\n *** Problem 5 *** ')

# Create a class called Circle. The class should have an attribute radius
# initialized during object creation and a method area() that calculates the
# area of the circle. Run your own test case to verify that it works.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * pow(self.radius, 2)
    
circle1 = Circle(51.2)
print(f"circle1 has an area of {circle1.area()}")

print('\n *** Problem 6: Challenge Problem *** ')

# Create a class called Library. This class should have an attribute books that 
# is a list. It should have methods to add a book, remove a book, and list the 
# books. Run your own test cases.


class Library:
    def __init__(self):
        self.books = []
        
    def add(self, book):
        self.books.append(book)
        
    def remove(self, book):
        new = []
        for b in self.books:
            if (b != book):
                new.append(b)
        self.books = new
    def listbooks(self):
        return self.books
    
lib = Library()
lib.add("The Maze Runner")
lib.add("The Necronomicon")
print(lib.listbooks())
lib.remove("This is not a book")
lib.remove("The Maze Runner")
print(lib.listbooks())
lib.add("Yog-Sothoth, the Gate and the Key")
lib.remove("The Necronomicon")
print(lib.listbooks())