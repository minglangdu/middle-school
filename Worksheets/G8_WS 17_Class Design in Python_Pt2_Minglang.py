"""
Worksheet # 17: Class Design in Python
Student Code
Grade 8

Name: Minglang Du
Class Section (if more than one G8 class): 8-D14
"""


print('\n *** Problem 4 *** ')

"""
Define 'instance attribute' and 'class attribute' in your own words. Provide
examples of each.
"""

print("Answer in the comment.")

"""
An instance attribute is an attribute that each instance of a class individually
owns and can use. This means that instance attributes can be different among instances
of the same class. For example, if we defined `self.age` in `__init__`, it would be
an instance attribute.

A class attribute is an attribute that is possessed by the class itself, meaning
that instances of the same class MUST have the same class attribute. For example, if we
defined `population` in the class (not in a method) it would be a class attribute. 

"""


print('\n *** Problem 5 *** ')

# Debugging:
# The following code should print the name and age of a specific Dog instance
# and the kind of diet all dogs need. Explain and fix the bug(s) or mistake(s),
# if any.

class Dog:
    diet = "mainly carnivorous"

    def __init__(self, name, age, fav_food=""):
        self.name = name
        self.age = age
        self.fav_food = fav_food

my_dog = Dog("Coco", 10)
print(my_dog.name)
print(my_dog.age)

#my_dog.diet = "shepherd's pie" # My dog loves shepherd's pie!
my_dog.fav_food = "sheperd's pie"
print(my_dog.diet)

print("Explanation part of answer in the comment.")

"""
I removed the line that changed `mydog.diet`. Since `diet` is
a class attribute, it shouldn't be changed to reflect only one
animal. I have created a `fav_food` attribute instead to reflect
one animal's favorite food, since it's an instance attribute.

"""


print('\n *** Problem 6 *** ')

# You're developing a game where players can create magic potions. Each potion
# can have one primary effect (like "Healing", "Invisibility", etc.). Players
# have a limited inventory space for potions, so the total number of potions
# must be tracked.

# You are given the following Potion class and need to modify it to add:
#     a. a class attribute to track the number of potions created
#     b. a class attribute representing the potion inventory space;
#        set this to 10
#     c. a class method to report the available potion inventory space
#     d. code in the constructor to update the potion count, report how 
#        many potions have been made, and report how much inventory space
#        remains for potions

class Potion:
    created = 0
    space = 10
    available = space
    def __init__(self, primary_effect):
        self.primary_effect = primary_effect
        self.update()
    
    @classmethod
    def update(cls):
        cls.created += 1
        cls.available = cls.space - cls.created
        print(f"There have been {cls.created} potions created and {cls.available} potions left.")

# Provided test cases:
potion1 = Potion("Healing")
potion2 = Potion("Invisibility")
potion3 = Potion("Haste")


print('\n *** Problem 7: Challenge Problem *** ')

"""
Suppose we wanted to create an even more universal interface than the lay_eggs()
method in the Bird class from Problem 2--a method that will work for all
animals. Obviously, not all animals lay eggs.

Assuming you had an Animal superclass, how would you go about applying
polymorphism in this case? In the Bird class, would you remove the lay_eggs()
method? Why or why not? Explain and provide code to demonstrate your answer.
"""

print("Explanation part of answer in the comment.")

"""
To apply polymorphism to to Animal, I would use the same methods I used for Bird.
The base function for Animal would `raise` an error intentionally since they can't
lay eggs by default. Then, I would change the function for each class of Bird.

class Animal:
    def lay_eggs(self):
        raise SyntaxError("Cannot lay eggs")
        
class Bird(Animal):
    def lay_eggs(self):
        print("Laid eggs.")
        
class Cuckoo(Bird):
    def lay_eggs(self):
        print("Laid eggs in other bird's nest")

"""
