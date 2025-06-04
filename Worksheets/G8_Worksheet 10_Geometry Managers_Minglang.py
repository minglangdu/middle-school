"""
Worksheet # 10: Geometry Managers
Student Code
Python Level 3

Student Name: Minglang
Class Section (if any): 8-D14

See the Word/hard copy document for this worksheet for visual
examples of the desired tkinter windows for each problem.
"""

print('\n *** Problem 1 *** ')

"""
Given the code snippet below, identify and fix the errors and fill in
any missing code to ensure both labels appear in the tkinter window.
"""
print("See GUI window.")

import tkinter as tk

root = tk.Tk()
root.title("P1")

label1 = tk.Label(text="First Label")
label2 = tk.Label(text="Second Label")
label1.pack()
label2.pack()


print('\n *** Problem 2 *** ')

"""
Write a script that creates a window titled "Problem 2" with two buttons,
"Hello" and "Goodbye", arranged side by side using the grid() method.
Comment out any previous tkinter code to allow this code to run.
"""
print("See GUI window.")

p2 = tk.Tk()
p2.title("Problem 2")

h = tk.Button(p2, text="Hello")
g = tk.Button(p2, text="Goodbye")

h.grid(row = 0, column = 0)
g.grid(row = 0, column = 1)

print('\n *** Problem 3 *** ')

"""
Write a tkinter program that creates an entry widget and a button
labeled "Submit". Place them in a window using the grid() geometry
manager so that the entry widget is in the first row and spans the
first three columns, and the button is in the second row and column.
Comment out any previous tkinter code to allow this code to run.
"""
print("See GUI window.")

p3 = tk.Tk()
p3.title("Problem 3")

en = tk.Entry(p3)
su = tk.Button(p3, text = "Submit")
en.grid(row = 1, column = 0, columnspan = 3)
su.grid(row = 2, column = 2)

print('\n *** Problem 4 *** ')

"""
The following code intends to place an entry widget and a button
side by side, but they are not displayed correctly. Identify and
fix the issue.
"""
print("See GUI window.")

import tkinter as tk

rt = tk.Tk()
rt.title("P4")

entry = tk.Entry(rt)
submit_btn = tk.Button(rt, text="Submit")

entry.grid(row = 0, column = 0)
submit_btn.grid(row=0, column=1)


print('\n *** Problem 5 *** ')

"""
Write a tkinter program to create three labels displaying the text "Top",
"Middle", and "Bottom". Use the pack() geometry manager to arrange the labels
vertically, adding 10 pixels of vertical padding between each using pady.
"""
print("See GUI window.")

p5 = tk.Tk()
p5.title("Problem 5")

top = tk.Label(p5, text = "Top")
middle = tk.Label(p5, text = "Middle")
bottom = tk.Label(p5, text = "Bottom")

top.pack(pady = 10)
middle.pack(pady = 10)
bottom.pack(pady = 10)

#####

root.mainloop()
p2.mainloop()
p3.mainloop()
rt.mainloop()
p5.mainloop()