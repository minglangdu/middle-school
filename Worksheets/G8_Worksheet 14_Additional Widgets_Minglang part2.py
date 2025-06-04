"""
Worksheet # 14: Additional Widgets
Student Code
Grade 8 (Python Level 3)

Student Name: Minglang Du
Class Section (if any): 8-D14
"""


print('\n <<< Part 2 >>>')


print('\n *** Problem 6 *** ')

"""
Write code to display an informational message box with the title "Greetings"
and the message "Welcome to Python GUI programming!" This message box should be
triggered by clicking a button.
"""
print("See GUI window.")

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
def greet():
    messagebox.showinfo("Greetings", "Welcome to Python GUI programming!")
p6 = tk.Button(root, text="Welcome", command=greet)
p6.pack()
root.mainloop()

print('\n *** Problem 7 *** ')

"""
The following code is intended to create an error message box, but it has a bug.
Identify and fix the bug.
"""
print("See GUI window.")

import tkinter as tk
from tkinter import messagebox

def error_box(): # bug: button should be replaced with messagebox.
    messagebox.showerror("Error", "This is an error.")

root = tk.Tk()
root.title("Problem 7")
root.geometry("350x50")

button = tk.Button(root, text="Show Error", command=error_box)
button.pack()
root.mainloop()


print('\n *** Problem 8 *** ')

"""
The following code is intended to create a warning message box, but it has a
bug. Identify and fix the bug.
"""
print("See GUI window.")

import tkinter as tk
from tkinter import messagebox

def warning_box(): # bug: showwarning is misspelled
    messagebox.showwarning("Warning", "This is just a test warning.")

root = tk.Tk()
root.title("Problem 8")
root.geometry("350x50")

button = tk.Button(root, text="Show Warning", command=warning_box)
button.pack()

root.mainloop()


print('\n *** Problem 9 *** ')

"""
Write a script to display a message box that asks the user if they enjoy
eating pineapple on pizza. If the user clicks "Yes", display "Me too!" in
another message box. If "No", display "That's OK, it's not for everyone!".

Note: Technically, tkinter message boxes do not require you, the programmer, 
to explicitly create a root window, as modal dialogs like message boxes are
transient interface elements rather than widgets that attach to a window.
However, if you create a messagebox without first creating a root window,
tkinter will implicitly create a root window for you in the background. Thus,
you should still explicitly create a root window in most cases for consistency
and control over how that window looks and behaves.
"""
print("See GUI window.")

root = tk.Tk()
response = messagebox.askyesno("Question", "Do you enjoy pineapple pizza?")
if (response):
    messagebox.showinfo(":)))))))))))))))))))))))))))))))))))))))", "Me too!")
else:
    messagebox.showinfo("-____________-", "That's OK, it's not for everyone!")
    messagebox.showinfo("-____________-", "I take that back your opinions are objectively wrong and will stay wrong")
root.mainloop()
