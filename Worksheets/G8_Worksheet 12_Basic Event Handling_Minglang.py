"""
Worksheet # 12: Basic Event Handling
Student Code
Python Level 3

Student Name: Minglang
Class Section (if any): 8-D14
"""
          
print('\n *** Problem 1 *** ')

"""
Write tkinter code to create a button that alternates between red and blue
backgrounds when clicked. The foreground (text) should be white.
"""
print("See GUI window.")

import tkinter as tk
root = tk.Tk()
root.title("Worksheet 12")

but = tk.Button(root, text="Alternating Button", fg = "white", bg="red")
but.pack()

def prob1(event):
    if (but.cget("bg") == "red"):
        but.configure(bg="blue")
    else:
        but.configure(bg="red")
but.bind("<Button-1>", prob1)

print('\n *** Problem 2 *** ')

"""
Write a tkinter script where pressing any key changes the text of a Label widget
to "Key Pressed". Use bind() to bind your function to the root window.
(Sometimes, keypress detection is done for specific widgets, but in this case,
we just want to detect the keypress whenever the window is active.)
"""
print("See GUI window.")

lab = tk.Label(root, text = "I detect keypresses!")
lab.pack()
keypresses = 0
def prob2(event):
    global keypresses
    keypresses += 1
    lab.configure(text = "I detected " + str(keypresses) + " keypresses!")
root.bind('<Key>', prob2)

print('\n *** Problem 3 *** ')

"""
Create a GUI with a label that changes its text to "Mouse Hovering" when the
mouse hovers over it and reverts back to "Hover over me" when the mouse leaves.
"""
print("See GUI window.")

hov = tk.Label(root, text="Hover over me")
hov.pack()
def prob3e(event):
    hov.configure(text="Mouse Hovering!!!")
def prob3l(event):
    hov.configure(text="Hover over me")
hov.bind("<Enter>", prob3e)
hov.bind("<Leave>", prob3l)

print('\n *** Problem 4 *** ')

"""
Write tkinter code to create a label with a width of 30 columns and a height of
10 rows. The label should display "Double Clicked!" when double-clicked.
"""
print("See GUI window. Double-click in the label to activate text.")

#double-button-1
doub = tk.Label(root, width = 30, height = 10, text="Double Click!", font=("Arial", 25, ""))
doub.pack()
def prob4(event):
    doub.configure(text="Double Clicked!", font=("Times New Roman", 30, "bold"))
doub.bind("<Double-Button-1>", prob4)

print('\n *** Problem 5 *** ')

"""
Create a tkinter label with a width of 60 columns and a height of 30 rows. The
label should update to show the current mouse position (x, y) whenever the mouse
moves over it. Remember that a mouse event object has two attributes, event.x
and event.y, that report the current coordinates of the mouse.
"""
print("See GUI window.")

root2 = tk.Tk()

def prob5(event):
    mpos.configure(text="(" + str(event.x) + ", " + str(event.y) + ")")

mpos = tk.Label(root2, width = 60, height = 30, text="(?, ?)", font=("Times New Roman", 40, ""))
mpos.pack()
mpos.bind("<Motion>", prob5)


print('\n *** Problem 6: Challenge Problem *** ')

"""
Write Python tkinter code with two buttons and a label sandwiched between them,
all on the same line, placed using grid().

The left button should have the text "-" and the right button should have the
text "+". The label should start off displaying 0.

That label's display value should decrease by 1 whenever the "-" button is
clicked and whenever the minus key "-" on the keyboard is pressed. (Bind the
<KeyPress-minus> event code to root.)

Meanwhile, the label's value should increase by 1 whenever the "+" button is
clicked or whenever the "+" key is pressed. (Bind the <KeyPress-plus> event
code to root.)

Hints:
1. A label's text attribute is a string, so you must do conversions
   back and forth between string and integer types to increment/
   decrement and update the value.
2. Assigning a button's command attribute to a function does not
   pass an event object to the function. However, using bind() to
   bind an event to a function does pass an event object to that
   function. If you use the same function for both, you may get an
   error. You can resolve this by either:
      a. using only bind() for buttons instead of the command attribute, or
      b. making the function's event parameter optional with a default value of
         None so that it works with both the command attribute and bind(), or
      c. defining separate functions to assign to each button's command
         attribute and bind() events (the least efficient choice).
"""
print("See GUI window.")

root3 = tk.Tk()

value = 0

minus = tk.Button(root3, text="-")
plus = tk.Button(root3, text="+")
num = tk.Label(root3, text="0")
minus.grid(row = 0, column = 0, padx = 5, pady = 5)
num.grid(row = 0, column = 1, padx = 10, pady = 5)
plus.grid(row = 0, column = 2, padx = 5, pady = 5)
def add(event):
    global value
    value += 1
    num.configure(text= str(value))
def subtract(event):
    global value
    value -= 1
    num.configure(text= str(value))
root3.bind("<KeyPress-minus>", subtract)
root3.bind("<KeyPress-plus>", add)
minus.bind("<Button-1>", subtract)
plus.bind("<Button-1>", add)
    
#############

root.mainloop()
root2.mainloop()
root3.mainloop()