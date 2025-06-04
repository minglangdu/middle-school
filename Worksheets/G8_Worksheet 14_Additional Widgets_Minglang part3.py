"""
Worksheet # 14: Additional Widgets
Student Code
Grade 8 (Python Level 3)

Student Name: Minglang Du
Class Section (if any): 8-D14
"""




print('\n *** Problem 10 *** ')

"""
Create a Tkinter GUI application with a menu bar containing two main menu items:
"Actions" and "Settings". Under "Actions", add two options: "Greet" and "Close".

The "Greet" option should display a message box saying "Hello, multiverse!"

The "Close" option should close the application.

Under "Settings", add an option "Info" that displays an informational message:
    "In another universe, this is where you would change the settings!"
"""
print("See GUI window.")

import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
main = tk.Menu(root)
def p10():
    messagebox.showinfo("Hi","Hello, multiverse!")
def p10a():
    messagebox.showinfo("Settings","In another universe, this is where you would change the settings!")
actions = tk.Menu(root)
actions.add_command(label="Greet", command=p10)
actions.add_command(label="Close", command=root.destroy)
settings = tk.Menu(root)
settings.add_command(label="Info", command=p10a)
main.add_cascade(label="Actions", menu=actions)
main.add_cascade(label="Settings", menu=settings)
root.config(menu=main)
root.mainloop()

print('\n *** Problem 11: Challenge Problem *** ')
"""
Create a Tkinter GUI application where users can input numbers and view them in
a Listbox. The application should have an entry field, a button to add numbers,
a Listbox with a scrollbar to display the numbers, and two menu options,
"Show Sum" and "Show Average", under a "Calculate" menu in a top menu bar.

The program should validate the input as a floating-point number and update the
Listbox with each new number added.

To check whether an input string can be converted into a valid floating-point 
number, use the provided is_float() function, which returns True if its string 
argument is a float and False otherwise.

Use messageboxes to output any error messages (e.g., the user enters an invalid
input--not a floating-point number) and the results of calculations.
"""
print("See GUI window.")

# Provided: is_float function to check if a string can be converted to a float
def is_float(string):
    # Check if the string starts with a minus sign
    if string.startswith("-"):
        string = string[1:]  # Remove the minus sign for further checks
    # Replace one decimal point and check if the rest of the string is numeric:
    return string.replace(".", "", 1).isnumeric()
nums = []
root = tk.Tk()
lb = tk.Listbox(root)
lb.grid(row = 1, column = 1, rowspan = 4, padx = 5, pady = 5, sticky = "nsew")
sv = tk.StringVar()
en = tk.Entry(root, textvariable=sv)
en.grid(row = 1, column = 3, padx = 5, pady = 5)
def submit():
    dat = sv.get()
    if (is_float(dat)):
        lb.insert(tk.END, dat)
        nums.append(float(dat))
    else:
        messagebox.showerror("Invalid Input", "Your input needs to be a float!")
sb = tk.Button(root, command = submit, text = "submit")
sb.grid(row = 2, column = 3, padx = 5, pady = 5)
cb = tk.Scrollbar(root)
cb.grid(row = 1, column = 2, rowspan = 4, padx = 5, pady = 5, sticky = "ns")
lb.config(yscrollcommand=cb.set)
cb.config(command=lb.yview)
def showsum():
    messagebox.showinfo("Sum", f"The sum of these numbers is {sum(nums)}")
def showaverage():
    messagebox.showinfo("Average", f"The average of these numbers is {float(sum(nums)) / float(len(nums))}")
main = tk.Menu(root)
root.config(menu = main)
calc = tk.Menu(root)
main.add_cascade(label="Calculate", menu = calc)
calc.add_command(label = "Show Sum", command=showsum)
calc.add_command(label = "Show Average", command=showaverage)
