"""
Worksheet # 13: Event Handling Logic
Student Code
Python Level 3

Student Name: Minglang
Class Section (if any): 8-D14
"""
          
print('\n *** Problem 1 *** ')

"""
The following code is supposed to print the position of a mouse click on the
label, but it's not working. Find, fix, and explain the error.
"""
print("See GUI window.")

import tkinter as tk

def get_position(event):
    print("Clicked at:", event.x, event.y)

root = tk.Tk()
root.title("Problem 1")
root.geometry("350x80")

label = tk.Label(root, text="Click anywhere on this label", width=60, height=20)
label.pack()
label.bind("<Button-1>", get_position)

root.mainloop()


print('\n *** Problem 2 *** ')

"""
Write a program where two labels change their background color to green when the
mouse hovers over them. Bind both events to the same function.
"""
print("See GUI window.")

root = tk.Tk()

lab1 = tk.Label(root, text="1")
lab2 = tk.Label(root, text="2")
lab1.pack()
lab2.pack()
def change(event):
    event.widget.configure(bg="green")
def revert(event):
    event.widget.configure(bg="white")
lab1.bind("<Enter>", change)
lab1.bind("<Leave>", revert)
lab2.bind("<Enter>", change)
lab2.bind("<Leave>", revert)
root.mainloop()

print('\n *** Problem 3 *** ')

"""
Modify this code to display the selected item from the listbox in the label.
"""
print("See GUI window.")

import tkinter as tk

# Define a function to bind to a listbox selection event here:


root = tk.Tk()
root.title("Problem 3")
root.geometry("350x350")

listbox = tk.Listbox(root)
for item in ["Apple", "Banana", "Cherry"]:
    listbox.insert(tk.END, item)
listbox.pack()

def getl(event):
    val = listbox.get(listbox.curselection()[0])
    print(val)
    label.configure(text=val)

label = tk.Label(root, text="Select an item:")
label.pack()

listbox.bind("<<ListboxSelect>>", getl)

# Add an event binding for a listbox selection here:


root.mainloop()


