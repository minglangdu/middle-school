"""
Worksheet # 15: Inheritance
Student Code
Grade 8

Name: Minglang Du
Class Section (if more than one G8 class): 8-D14
"""

print('\n *** Problem 1 *** ')

# Create a class called Bird with attributes name and can_fly, which
# should be True by default. Then, create a subclass called Penguin that
# inherits from Bird but sets can_fly to False by default. Use the provided
# test case to verify that your classes work.


# Provided test case (uncomment to test)
class Bird:
    def __init__(self, name):
        self.name = name
        self.can_fly = True
        
class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name)
        self.can_fly = False


skipper = Penguin("Skipper")
print(skipper.can_fly)



print('\n *** Problem 2 *** ')

# Using the Mammal class provided, create a subclass called Dolphin that adds
# an additional attribute called can_swim and set it to True by default. 
# Then, in the Dolphin class, override the make_sound() method to output
# "click click click click click". Run your own test case.

class Mammal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass
    
class Dolphin(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.can_swim = True
    
    def make_sound(self):
        print("click click click click click")

d = Dolphin("Ann", 5)
d.make_sound()
print(d.can_swim)
 
print('\n *** Problem 3 *** ')

# Create a multi-level inheritance structure: an Animal class at the top, then
# Mammal, and finally a Bat class. The Animal class should be a stub (you can
# just use pass), and the Mammal class should be as above (but modified however
# needed to work with the hierarchy). Make sure the Bat class has an attribute
# nocturnal set to True. Override make_sound() to output "squeak squeak".
# Run your own test case.

class Animal:
    pass
    
class Mammal(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def make_sound(self):
        pass
    
class Bat(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.nocturnal = True
        
    def make_sound(self):
        print("squeak squeak")
        
b = Bat("Beth", 3)
b.make_sound()
print(b.nocturnal)
 
print('\n *** Problem 4 *** ')

# Given the Vehicle class below, create a subclass called Car that inherits
# from Vehicle. The Car class should introduce a new attribute called
# number_of_doors, which is passed as a parameter during object instantiation.
# Create an instance of the Car class and print the brand, model, and number
# of doors. Run your own test case. You may use the following car information
# or choose your own: Toyota Supra (2 doors)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.number_of_doors = doors
        
c = Car("Toyota", "Supra", 2)
print(f"{c.brand} {c.model} ({c.number_of_doors} doors)")

 
print('\n *** Problem 5 *** ')

"""
Imagine you're designing a software system for a bookstore. You decide to
have a base class named Item that represents any item that can be purchased
from the bookstore. This class has attributes like title, price, and item code.

What subclasses would you likely need to define? Explain the advantage of
creating subclasses inheriting from the Item superclass, rather than designing
them as entirely separate classes. What might be some attributes or methods
that are shared? What might be unique to each subclass?
"""

print("Answer in the comment.")

"""
I would create subclasses for the subcategories of items in the store.
As Item already provides attributes and methods for all of these subclasses, it is advantageous to inherit it to avoid repetition.
For example, the title, price, and item code attributes and the buy methods would be shared, while
the expiration dates would be unique to Food classes.

"""

print('\n *** Problem 6 *** ')

# Debug the issues in the Butterfly subclass to correctly instantiate a
# Butterfly object with 4 wings.

# Buggy code (uncomment to test):

class Insect:
    def __init__(self, num_wings):
        self.wings = num_wings

class Butterfly(Insect):
    def __init__(self, wings=4):
        super().__init__(wings)

# Provided test case
monarch = Butterfly()

print(f"A monarch butterfly has {monarch.wings} wings.")



print('\n *** Problem 7: Challenge Problem *** ')

# Given the base class Shape:

class Shape:
    def __init__(self, color="Red"):
        self.color = color

    def describe(self):
        return f"This is a {self.color} shape."

# a. Create a subclass Polygon that inherits from Shape. The Polygon class
#    should introduce an attribute sides which indicates the number of sides
#    the polygon has (e.g., a triangle has 3 sides). Add a method
#    describe_polygon() that returns a string indicating the color of the shape
#    and the number of sides.

class Polygon(Shape):
    def __init__(self, sides, color="Red"):
        super().__init__(color=color)
        self.sides = sides
        
    def describe_polygon(self):
        return f"This is a {self.color} polygon with {self.sides} sides."

# b. Now, create two more subclasses: Triangle and Square. Both should inherit
#    from the Polygon class. The Triangle class should automatically set sides
#    to 3, and the Square class should set sides to 4.

class Triangle(Polygon):
    def __init__(self, typ, color = "Red"):
        super().__init__(3, color=color)
        self.kind = typ
        
    def describe_polygon(self):
        return f"This is a {self.kind} {self.color} triangle with {self.sides} sides."
        
class Square(Polygon):
    def __init__(self, color = "Red"):
        super().__init__(4, color=color)

# c. For an added twist, in the Triangle class, introduce an attribute called 
#    type that specifies the type of triangle ("equilateral", "isosceles", or
#    "scalene") . Override the describe_polygon() method in the Triangle class
#    to include information about the triangle's type.



# Provided test cases (uncomment to test)

tri = Triangle("Blue", "equilateral")
print(tri.describe())           # Output: This is a Blue shape.
print(tri.describe_polygon())   # Output: This is a Blue equilateral triangle
                                #         with 3 sides.

sq = Square("Green")
print(sq.describe())            # Output: This is a Green shape.
print(sq.describe_polygon())    # Output: This is a Green polygon with 4 sides.
