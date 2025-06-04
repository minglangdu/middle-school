"""
Worksheet # 17: Class Design in Python
Student Code
Grade 8

Name: Minglang Du
Class Section (if more than one G8 class): 8-D14
"""

print('\n *** Problem 1 *** ')

"""
In your own words, what does polymorphism allow us to do in object-oriented
programming?
"""

print("Answer in the comment.")

"""
Polymorphism allows us to run a function for objects of classes regardless of what type of object they are.
For example, if we use polymorphism to cause all children of a Bird class to inherit a stub function lay_eggs,
we are allowing all the child classes to run lay_eggs regardless of what type they are. 

"""


print('\n *** Problem 2 *** ')

"""
Given a Bird class with a stub method called lay_eggs(), describe how you 
would implement polymorphism to allow any subclass of Bird to lay eggs without
knowing whether that subclass builds a nest first, lays eggs in a scrape
in the ground, lays them in another bird's nest, etc.
"""

print("Answer in the comment.")

"""
I would, for each subclass of Bird, create a lay_eggs function to override the stub function
defined in bird, so that the different ways to lay eggs are implemented uniquely in each
animal. 

"""


print('\n *** Problem 3 *** ')

# You are given the Bird class below. First, note that you DON'T need to
# explicitly define an __init__() constructor for a class if you don't have 
# any attributes that need to be assigned or methods that need to be run
# at object creation.

class Bird:
    def lay_eggs(self):
        pass

# Your task is to implement polymorphism in the manner you described in 
# Problem 2. Create three subclasses for Bird using the following
# information about different birds' egg-laying methods:

# a. Sparrow - builds a nest in a tree and lays its eggs there
# b. Plover - lays eggs in a scrape on the ground
# c. Cuckoo - lays its eggs in another bird's nest

class Sparrow(Bird):
    def lay_eggs(self):
        print("Sparrow builds a nest in a tree and lays its eggs there")
        
class Plover(Bird):
    def lay_eggs(self):
        print("Plover lays eggs in a scrape on the ground")
        
class Cuckoo(Bird):
    def lay_eggs(self):
        print("Cuckoo lays its eggs in another bird's nest")

# Run your own test cases demonstrating the polymorphism at work.

sp = Sparrow()
pl = Plover()
cu = Cuckoo()

sp.lay_eggs()
pl.lay_eggs()
cu.lay_eggs()
