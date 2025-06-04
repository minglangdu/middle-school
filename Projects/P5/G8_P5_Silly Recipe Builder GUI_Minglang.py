"""
Project 5: Silly Recipe Builder (GUI)
Solution Code - Base Version
Grade 8 (Python Level 3)

Instructions:
1. Complete the missing parts of this program.
2. Follow the comments to set up the GUI components and implement functionality.
3. Test your program to ensure it works as described in the project handout.
"""

# [PROVIDED] Import required modules
import tkinter as tk
from tkinter import messagebox
import random

# [PROVIDED] Define global variables for column dimensions and padding for
# uniform spacing:
col0_width = 15
col1_width = 20
col2_width = 11
col3_width = 11
x_pad = 5
y_pad = 10

# [PROVIDED] Global variable to remember which recipe template is currently
# in use (1 to 5); starts as 1
template_number = 1

# -----------------------------------------------------------------------------
# Step 1: Create a recipe template. (6 points - 2 points per line of code)
# -----------------------------------------------------------------------------
# TODO: Add a recipe template to template_to_recipe(), similar to the existing
#       recipe templates in the function.
#
# [PROVIDED] Most of the function is written for you. This function takes a
#   template number (1-5) and a list of ingredients (each with a name, quantity,
#   and unit) and returns a silly recipe string. As provided, the function only
#   has 4 recipe templates. You will add the 5th.
# -----------------------------------------------------------------------------
def template_to_recipe(template_number, ingredients):
    """
    Returns a short recipe string based on the chosen template (1 to 5)
    and the ingredients list.
    
    Parameters:
    - template_number (int): Specifies which recipe template to use (1 through 5).
    - ingredients (list): A list of 3 sublists, each containing the details of
        one ingredient.Each sublist should follow the format:
          [ingredient_name (str), quantity (str), unit (str)]
        Example: [["flour", "2", "cups"],
                  ["sugar", "1", "cup"],
                  ["milk", "0.5", "liter"]]
    """
    recipe_templates = [
        # Recipe Template 1
        f"Stir the {ingredients[0][1]} {ingredients[0][2]} of {ingredients[0][0]} into a bowl "
        f"with the {ingredients[1][1]} {ingredients[1][2]} of {ingredients[1][0]}, and "
        f"garnish with the {ingredients[2][1]} {ingredients[2][2]} of {ingredients[2][0]}.",
        
        # Recipe Template 2
        f"Spread the {ingredients[0][1]} {ingredients[0][2]} of {ingredients[0][0]} over the "
        f"{ingredients[1][1]} {ingredients[1][2]} of {ingredients[1][0]} and sprinkle with "
        f"{ingredients[2][1]} {ingredients[2][2]} of {ingredients[2][0]}.",
        
        # Recipe Template 3
        f"Mix the {ingredients[0][1]} {ingredients[0][2]} of {ingredients[0][0]} and "
        f"{ingredients[1][1]} {ingredients[1][2]} of {ingredients[1][0]} together and "
        f"top with {ingredients[2][1]} {ingredients[2][2]} of {ingredients[2][0]}.",
        
        # Recipe Template 4
        f"Squeeze the {ingredients[0][1]} {ingredients[0][2]} of {ingredients[0][0]} and "
        f"{ingredients[1][1]} {ingredients[1][2]} of {ingredients[1][0]} into a bowl and "
        f"drop in the {ingredients[2][1]} {ingredients[2][2]} of {ingredients[2][0]}.",
        
        # TODO: Add Recipe Template 5 below. Be creative!
        f"Boil the {ingredients[0][1]} {ingredients[0][2]} of {ingredients[0][0]} in a pot while"
        f"chopping the {ingredients[1][1]} {ingredients[1][2]} of {ingredients[1][0]} up. Mix with the"
        f"{ingredients[2][1]} {ingredients[2][2]} of {ingredients[2][0]}."
    ]
    # template_num ranges from 1-5, so subtract 1 for zero-based indexing
    return recipe_templates[template_number - 1]

# -----------------------------------------------------------------------------
# Step 2: Set Up the Main Window (3 points - 1 point per line of code)
# -----------------------------------------------------------------------------
# TODO: Initialize the main tkinter window. Configure its title and dimensions.
#       You may need to adjust the window dimensions later to ensure all 
#       widgets are fully visible.
# -----------------------------------------------------------------------------
root = tk.Tk()
root.title("Silly Recipe Builder GUI")
root.geometry("600x325")

# [PROVIDED] Add column headers for ingredient information
ingredients_heading_label = tk.Label(root, text="Ingredient Name", width=col1_width)
qty_heading_label = tk.Label(root, text="Quantity", width=col2_width)
units_heading_label = tk.Label(root, text="Units", width=col3_width)

ingredients_heading_label.grid(row=0, column=1, padx=x_pad, pady=y_pad)
qty_heading_label.grid(row=0, column=2, padx=x_pad, pady=y_pad)
units_heading_label.grid(row=0, column=3, padx=x_pad, pady=y_pad)

# -----------------------------------------------------------------------------
# Step 3: Set Up Variables for Input Fields (9 points - 1 point per line)
# -----------------------------------------------------------------------------
# TODO: Create variables to store user input for the ingredient name, quantity,
#       and unit.
# For each ingredient (e.g., Ingredient 1):
# 1. Create one variable for the name, one for the quantity, and one for the unit.
# 2. Each variable should be a StringVar() as they will hold string data (even 
#    the quantity will be treated as a string for simplicity).
# 3. Remember to repeat this process for Ingredient 2 and Ingredient 3.
# -----------------------------------------------------------------------------

name1 = tk.StringVar()
amts1 = tk.StringVar()
unit1 = tk.StringVar()

name2 = tk.StringVar()
amts2 = tk.StringVar()
unit2 = tk.StringVar()

name3 = tk.StringVar()
amts3 = tk.StringVar()
unit3 = tk.StringVar()

# -----------------------------------------------------------------------------
# Step 4: Create and Place Widgets for Ingredient Entry
# -----------------------------------------------------------------------------
# (36 points - 2 points per widget creation, 1 point per grid placement)
#
# TODO: Set up labels and entry fields for the three ingredients (name,
#       quantity, units).
#
# Example:
#   - Row 1: Ingredient 1 (Label + Entry fields for name, quantity, unit)
#   - Row 2: Ingredient 2 (Label + Entry fields for name, quantity, unit)
#   - Row 3: Ingredient 3 (Label + Entry fields for name, quantity, unit)
# -----------------------------------------------------------------------------

lab1 = tk.Label(root, text = "Ingredient 1", width = col0_width)
nent1 = tk.Entry(root, width = col1_width, textvariable = name1)
qent1 = tk.Entry(root, width = col2_width, textvariable = amts1)
uent1 = tk.Entry(root, width = col3_width, textvariable = unit1)

lab1.grid(row = 1, column = 0, padx = x_pad, pady = y_pad)
nent1.grid(row = 1, column = 1, padx = x_pad, pady = y_pad)
qent1.grid(row = 1, column = 2, padx = x_pad, pady = y_pad)
uent1.grid(row = 1, column = 3, padx = x_pad, pady = y_pad)


lab2 = tk.Label(root, text = "Ingredient 1", width = col0_width)
nent2 = tk.Entry(root, width = col1_width, textvariable = name2)
qent2 = tk.Entry(root, width = col2_width, textvariable = amts2)
uent2 = tk.Entry(root, width = col3_width, textvariable = unit2)

lab2.grid(row = 2, column = 0, padx = x_pad, pady = y_pad)
nent2.grid(row = 2, column = 1, padx = x_pad, pady = y_pad)
qent2.grid(row = 2, column = 2, padx = x_pad, pady = y_pad)
uent2.grid(row = 2, column = 3, padx = x_pad, pady = y_pad)


lab3 = tk.Label(root, text = "Ingredient 1", width = col0_width)
nent3 = tk.Entry(root, width = col1_width, textvariable = name3)
qent3 = tk.Entry(root, width = col2_width, textvariable = amts3)
uent3 = tk.Entry(root, width = col3_width, textvariable = unit3)

lab3.grid(row = 3, column = 0, padx = x_pad, pady = y_pad)
nent3.grid(row = 3, column = 1, padx = x_pad, pady = y_pad)
qent3.grid(row = 3, column = 2, padx = x_pad, pady = y_pad)
uent3.grid(row = 3, column = 3, padx = x_pad, pady = y_pad)



# -----------------------------------------------------------------------------
# Step 5: Implement the Recipe Logic (make_recipe function)
# -----------------------------------------------------------------------------
# (15 points - 1 point per get() statement / 2 points per further line of code)
#
# [PROVIDED] A basic framework for this function is provided.
#
# TODO: Complete this function to handle button clicks for generating and 
# updating recipes. In the process, it must:
#   1. Collect ingredient data from input fields.
#   2. Generate the recipe using `template_to_recipe()`.
#   3. Display the generated recipe in the text widget.
#
# Note: When you first start coding a function, it may need to refer to a
# widget that you may not have created yet. You can always pick the name of
# that widget in the function and then use that name when you create that 
# widget later in the program.
# -----------------------------------------------------------------------------

def make_recipe():
    """
    Helper function to gather ingredient data and generate the recipe text
    based on the current template_number. Updates the recipe_text widget.
    """

    # TODO: Get ingredient data from input fields of the GUI and save the data 
    # in the ingredients list. Replace the strings below with get() statements.
    ingredients = [
        [nent1.get(), qent1.get(), uent1.get()],
        [nent2.get(), qent2.get(), uent2.get()],
        [nent3.get(), qent3.get(), uent3.get()],
    ]
    
    # TODO: Use template_to_recipe() to build the silly recipe
    global template_number
    recipe = template_to_recipe(template_number, ingredients)
    # TODO: Display the recipe in the text widget
    tex.delete("1.0", tk.END)
    tex.insert(tk.END, recipe)


# -----------------------------------------------------------------------------
# Step 6: Implement Wrapper Functions for the Buttons (6 points - 2 per line)
# -----------------------------------------------------------------------------
# In this step, you will define one of two functions to handle the two recipe
# buttons. Each function is a "wrapper" that calls the make_recipe() helper.
#
# TODO: For on_generate_new_recipe(), pick a random number from 1 to 4, assign
#       it to the global template_number variable, and then call make_recipe().
#
# [PROVIDED] The on_update_recipe() wrapper function is defined for you.
# -----------------------------------------------------------------------------

def on_generate_new_recipe():
    """
    Button handler: pick a new random template_number, then generate the recipe.
    """
    global template_number
    template_number = random.randint(1, 5)
    make_recipe()

def on_update_recipe():
    """
    Button handler: keep the current template_number, but use any updated
    ingredient data.
    """
    make_recipe()
    
# -----------------------------------------------------------------------------
# Step 7: Buttons for New Recipe and Update (8 points - 2 points per line)
# -----------------------------------------------------------------------------
# TODO: 
#  1. Create two buttons:
#     - "Generate New Recipe": Generates a new recipe using a random template
#     - "Update Recipe": Updates the current recipe using the current template
#        but applying any changes in the ingredient fields
#  2. When creating each button, bind it to the `make_recipe()` function using
#     the command parameter.
#  3. Place each button using grid.
# -----------------------------------------------------------------------------

genrec = tk.Button(root, text = "Generate New Recipe", command = on_generate_new_recipe)
updrec = tk.Button(root, text = "Update Recipe", command = on_update_recipe)
genrec.grid(row = 4, column = 1, padx = x_pad, pady = y_pad)
updrec.grid(row = 4, column = 2, padx = x_pad, pady = y_pad)

# -----------------------------------------------------------------------------
# Step 8: Create a Recipe Output Area - Text Widget (4 points - 2 per line)
# -----------------------------------------------------------------------------
# TODO: Set up a Text widget to display the generated recipe. This widget
#       should span multiple columns for better visibility.
# TIP: Add the wrap=tk.WORD argument when creating the Text widget to force 
#      text it contains to wrap to the next line only at the end of a word.
# -----------------------------------------------------------------------------
tex = tk.Text(root, wrap = tk.WORD, width = col0_width + col1_width + col2_width + col3_width, height = 5)
tex.grid(row = 5, column = 0, columnspan = 3, padx = x_pad, pady = y_pad)

# [PROVIDED] Intro message
intro_string = """
Welcome to the Silly Recipe Builder!

Fill in up to three ingredient names, quantities, and units in the designated fields and then click:

'Generate New Recipe' to display a random recipe using the ingredients, or

'Update Recipe' to update the current/most recent recipe with any changes to the entered values.
"""

# -----------------------------------------------------------------------------
# Step 9: Show an Introductory Messagebox (2 points)
# -----------------------------------------------------------------------------
# TODO: Display a messagebox with the title "Introduction" and the contents of
#       intro_string as the body.
# -----------------------------------------------------------------------------
messagebox.showinfo("Introduction", intro_string)

# [PROVIDED] Ensure the main window regains focus after the messagebox is
# closed and then start the tkinter event loop to run the GUI.
root.focus_force()  
root.mainloop()

# -----------------------------------------------------------------------------
# Remaining point values out of 100:
# -----------------------------------------------------------------------------
# Code Formatting & Comments: 5 points
# Working recipe output: 6 points
# -----------------------------------------------------------------------------