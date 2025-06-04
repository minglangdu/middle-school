import random
from datetime import datetime

name = "Minglang"
date = str(datetime.today().strftime("%M %d %Y"))
print(f"{name}\n MS3_P2_Silly Recipe Builder \n {date}")

print("""
Welcome to the Silly Recipe Builder!

In this program, you will be asked to input three ingredients, including their \
quantities and units. The program will then output a silly recipe based on \
your inputs.

Let's get started!

""") # give greeting

def get_servings(i1, i2, i3, orig, new):
    change = new / orig
    i1[1] *= change
    i2[1] *= change
    i3[1] *= change
    return i1, i2, i3

def template_to_recipe(i1, i2, i3):
    # each parameter has (in order): name, number, unit
    # preprocessed string representing each ingredient
    c1 = f"{i1[1]:.1f} {i1[2]} of {i1[0]}" 
    c2 = f"{i2[1]:.1f} {i2[2]} of {i2[0]}"
    c3 = f"{i3[1]:.1f} {i3[2]} of {i3[0]}"
    # premade list of possible templates
    templates = [f"Squeeze the {c1} and drop it into {c2} and stir with {c3}.",
                 f"Spread the {c1} over a blended mixture of {c2} and {c3}.",
                 f"Boil {c1} and roast the {c2} and {c3} together. Mix well.",
                 f"C-remove the {c1} and use {c2} to fight off a grue.\
As a treat, eat the {c3} and continue on your journey.",
                 f"Shoot {c3} out of a pneumatic cannon into {c1} and {c2}"
                 ]
    # give a random fstring
    return random.choice(templates)

def generate_recipe():
    ing = [] # ingredient list
    for i in range(1, 4): # ask user for ingredients
        name = input(f"Enter the name of ingredient {i}: ")
        while 1:
            try:
                number = int(input("Enter the quantity of \
that you want to use: "))
            except:
                continue
            break
        unit = input("Enter the unit for that quantity (e.g. cups, grams): ")
        ing.append([name, number, unit])
    # get original servings
    while 1:
            try:
                servings = int(input("Enter the number of servings the \
original recipe is meant to serve: "))
            except:
                continue
            break
    print("Here's your silly recipe:\n")
    print(template_to_recipe(ing[0], ing[1], ing[2]), "\n") # prints recipe.
    # get new servings
    while 1:
            try:
                newserv = int(input("Enter the number of servings you want \
to serve: "))
            except:
                continue
            break
    ing = get_servings(ing[0], ing[1], ing[2], servings, newserv)
    print("Here's your sillier recipe:\n")
    print(template_to_recipe(ing[0], ing[1], ing[2]), "\n") # prints recipe.
    
while 1:
    generate_recipe()
    again = input("Would you like to make another recipe (y/n)? ") 
    if again.lower()[0] != "y": # checks if user doesn't want to continue
        break