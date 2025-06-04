"""
Quiz # 3: Graphical User Interface Programming
Minglang 
Grade 8 (Python Level 3)
"""

import tkinter as tk

print('\n *** Problem 1: Color-Changing Buttons (30 points) *** ')

"""
Task:
- Add a label with the text "Choose font color:". Using the grid geometry 
  manager, place it on the first row, spanning the first two columns.
- Add two buttons labeled "Red" and "Blue". Using the grid geometry
  manager, place each button on the second row. The buttons should only span 
  one column each. On click, each button change the font color of the label.

Pre-filled Code:
- Functions to change label color
- Root window setup and mainloop
"""
print("See GUI window.")

# Pre-filled: Functions to change label color
def change_to_red():
    label.configure(fg="red")

def change_to_blue():
    label.configure(fg="blue")

# Pre-filled: Root window setup
root = tk.Tk()
root.title("Problem 1")
root.geometry("300x200")

label = tk.Label(root, text="Choose font color:")
label.grid(row = 1, column = 1, columnspan = 2)
p1r = tk.Button(root, text = "Red", command = change_to_red)
p1b = tk.Button(root, text = "Blue", command = change_to_blue)
p1r.grid(row = 2, column = 1)
p1b.grid(row = 2, column = 2)

# Students write (10 points): Create and place the label.


# Students write (20 points): Create and place buttons to change label color.


root.mainloop()  # Pre-filled 


print('\n *** Problem 2: Listbox & Scrollbar Synchronization (10 points) *** ')

"""
Task:
- Synchronize the Listbox with the Scrollbar so that scrolling one updates
  the other.

Pre-filled Code:
- The Listbox and Scrollbar have already been created and placed.
- The Listbox has been filled with numbers.
- The root window has been setup and its mainloop is run.
"""
print("See GUI window.")

import tkinter as tk

# Pre-filled: Root window setup
root = tk.Tk()
root.title("Problem 2")
root.geometry("400x400")

# Pre-filled: Listbox and Scrollbar setup
listbox = tk.Listbox(root)
scrollbar = tk.Scrollbar(root)

# Students write (10 points): Synchronize the Listbox and Scrollbar.

listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

# Pre-filled: Fill the listbox with numbers.
for i in range(50):
    listbox.insert(tk.END, i)

# Pre-filled: Place the listbox and scrollbar.
listbox.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

root.mainloop()  # Pre-filled


print('\n *** Problem 3: Keypress Counter with Hover Effects (25 points) ***')
"""
Task:
- Complete the GUI to count keypresses typed into a Text widget.
- A label at the top should display the number of keypresses.
- Add hover effects to the label so it becomes bold when the mouse cursor
  hovers over it (the <Enter> event) and returns to normal when the cursor
  leaves (the <Leave> event).

Pre-filled Code:
- Hover effect functions
- Counter label creation and placement
- Root window setup and mainloop
"""
print("See GUI window.")

# Pre-filled: Hover effect functions
def update_keypress_count(event):
    global keypress_count
    keypress_count += 1
    count_label.configure(text=f"Total Keypresses: {keypress_count}")

def change_label_to_bold(event):
    count_label.configure(font=("Arial", 12, "bold"))

def change_label_to_default(event):
    count_label.configure(font=("Arial", 12, "normal"))

# Pre-filled: Root window setup
root = tk.Tk()
root.title("Problem 3")
root.geometry("400x300")

keypress_count = 0

# Students write (10 points): Create and place the Text widget.

p3t = tk.Text(root, width = 50, height = 8)
p3t.pack(padx = 5, pady = 5)

# Students write (5 points): Bind keypress events in the text widget
# to keypress count update function.

p3t.bind("<Key>", update_keypress_count)

# Pre-filled: Counter label creation and placement
count_label = tk.Label(root, text="Total Keypresses: 0",
                       font=("Arial", 12, "normal"))
count_label.pack()

# Students write (10 points): Bind hover events for the mouse 
# entering and leaving the counter label.

count_label.bind("<Enter>", change_label_to_bold)
count_label.bind("<Leave>", change_label_to_default)

root.mainloop()  # Pre-filled 


print('\n *** Problem 4: Simple Counter with Reset Button (35 points) *** ')
"""
Task:
- Create a GUI that tracks a counter with the following features:
  1. A label to display the current counter value, starting at 0
  2. A button labeled "Increment" that increases the counter by 1 each 
     time it is clicked
  3. A button labeled "Reset" that sets the counter back to 0

Pre-filled Code:
- Functions to increment and reset the counter
- Root window setup and mainloop
"""
print("See GUI window.")

# Pre-filled: Functions to manage counter
def increment_counter():
    global counter
    counter += 1
    counter_label.configure(text=f"Counter: {counter}")

def reset_counter():
    global counter
    counter = 0
    counter_label.configure(text=f"Counter: {counter}")

# Pre-filled: Root window setup
root = tk.Tk()
root.title("Problem 4")
root.geometry("300x200")

# Students write (5 points): Initialize counter variable to 0.

counter = 0

# Students write (10 points): Create and place the label to display the counter.

counter_label = tk.Label(root, text=f"Counter: {counter}")
counter_label.pack()

# Students write (10 points): Create and place the Increment button.

inc = tk.Button(root, text = "Increment", command=increment_counter)
inc.pack()

# Students write (10 points): Create and place the Reset button.

res = tk.Button(root, text = "Reset", command=reset_counter)
res.pack()

root.mainloop()  # Pre-filled 
