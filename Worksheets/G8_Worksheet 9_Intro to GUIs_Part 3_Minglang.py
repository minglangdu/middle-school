"""
Worksheet # 9: Introduction to GUI programming
Student Code
Python Level 3

(For Publications use: Document Code 09-969.181-24)
"""



"""
Part 3: Tkinter Widgets: Checkbuttons, Radiobuttons, Listboxes
Problems 8 - 10
"""

print('\n *** Problem 8 *** ')

print("Output will be a GUI window.")
"""
Create a tkinter window titled "Problem 8". Add two checkbuttons labeled
"Option A" and "Option B". Place them in the window using the pack() geometry
manager.
"""

import tkinter as tk

p8 = tk.Tk()
p8.title("Problem 8")

c1 = tk.Checkbutton(p8, text="Option A")
c2 = tk.Checkbutton(p8, text="Option B")
c1.pack()
c2.pack()


print('\n *** Problem 9 *** ')

print("Output will be a GUI window.")
"""
Create a tkinter window titled "Problem 9". Add three radiobuttons labeled
"Choice 1", "Choice 2", and "Choice 3" with the values 1, 2, and 3,
respectively. Place them in the same "Problem 9" window using the pack()
geometry manager.
"""

p9 = tk.Tk()
p9.title("Problem 9")

r1 = tk.Radiobutton(p9, text = "Choice 1", value = 1)
r2 = tk.Radiobutton(p9, text = "Choice 2", value = 2)
r3 = tk.Radiobutton(p9, text = "Choice 3", value = 3)

r1.pack()
r2.pack()
r3.pack()

print('\n *** Problem 10 *** ')

print("Output will be a GUI window.")
"""
Create a tkinter window titled "Problem 10". Add a listbox widget and insert
three items labeled "Item 1", "Item 2", and "Item 3". Place the listbox in the
window using the pack() geometry manager.
"""

p10 = tk.Tk()
p10.title("Problem 10")

listb = tk.Listbox(p10)
listb.insert(1, "Item 1")
listb.insert(2, "Item 2")
listb.insert(3, "Item 3")
listb.pack()

######

p8.mainloop()
p9.mainloop()
p10.mainloop()