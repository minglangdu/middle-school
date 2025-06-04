"""
Worksheet # 11: Configuring Widgets
Student Code
Python Level 3

Student Name: Minglang
Class Section (if any): D-14
"""

print('\n *** Problem 1 *** ')

"""
Write tkinter code with the following graphical elements:

a. Create a label with the text, "Welcome to my colorful world!"
   with the following settings:
     i. a blue background
     ii. a yellow foreground (font)
     iii. font Arial, size 12, bold
b. Create a button with the text "Click me to change the label
   color!"
c. When the button is clicked, it should change the label's
   configuration settings to the following:
     i. a green background
     ii. a pink font
     iii. (font remains unchanged)
"""
print("See GUI window.")

import tkinter as tk

root = tk.Tk()
lab = tk.Label(root, text="Welcome to my colorful world!")
lab.configure(bg="blue",fg = "yellow", font=("Arial", 12, "bold"))
def change():
    lab.configure(bg="green", fg="pink")
but = tk.Button(root, text="Click me to change the label color!", command=change)
lab.pack()
but.pack()


print('\n *** Problem 2 *** ')

"""
Copy-paste and modify the code in Problem 1 so that clicking the button changes
the appearance of the label from a to b to c and then back to a (detailed
below). Use some of the properties below in your conditionals to check the
label's current state.

   a. blue background + yellow font
   b. green background + pink font
   c. red background + white font
   
Comment out previous tkinter code or close previous GUI windows as needed.
"""
print("See GUI window.")

cyclocyc = [("blue", "yellow"), ("green", "pink"), ("red", "white")] # TPLL reference lol
cycle = 0

root2 = tk.Tk()
lab2 = tk.Label(root2, text="Welcome to my colorful world!")
lab2.configure(bg="blue",fg = "yellow", font=("Arial", 12, "bold"))
def change2():
    global cycle
    cycle += 1
    cycle %= 3
    lab2.configure(bg=cyclocyc[cycle][0], fg=cyclocyc[cycle][1])
but = tk.Button(root2, text="Click me to change the label color!", command=change2)
lab2.pack()
but.pack()

print('\n *** Problem 3 *** ')

"""
Create a similar program to that in Problem 2, but display only a single 
button with the text "This is a dynamic font button!" that cycles through 
the following font settings when clicked:

    a. Arial, 12, bold font
    b. Georgia, 11, italic font
    c. Comic Sans MS, 12, underline font

Note that cget() returns a widget's font settings as a string of the font name,
font size, and font style, e.g. "Arial 12 bold". To get just one of those three
values, you must first use split() to separate the string into a list of its
words. Then, get the desired element of that string:

    font_data = widget_name.cget("font")
    font_name = font_data.split()[0]

Comment out previous tkinter code or close previous GUI windows as needed.
"""
print("See GUI window.")

fonts = [("Arial", 12, "bold"), ("Georgia", 11, "italic"), ("Comic Sans MS", 12, "underline")]
cyc = 0
def change():
    global cyc
    cyc += 1
    cyc %= 3
    dyn.configure(font=fonts[cyc])
dyn = tk.Button(root2, text="This is a dynamic font button!", font=("Arial", 12, "bold"), command=change)
dyn.pack()


print('\n *** Problem 4 *** ')

"""
Write a Python tkinter program to create a window of size 400x200 pixels. Inside
this window, add a Button widget with the text "Increase Window Size" and set
its width to 25 characters and height to 2 lines. After clicking the button, the
window should resize to 800x400 pixels.

Comment out previous tkinter code or close previous GUI windows as needed.
"""
print("See GUI window.")

root3 = tk.Tk()
root3.geometry("400x200")

def inc():
    root3.geometry("800x400")

increase = tk.Button(root3, text="Increase Window Size", width=25, height= 2, command = inc)
increase.pack()


print('\n *** Problem 5 *** ')

"""
Create a tkinter application with a window size of 600 x 300. Add
three buttons side-by-side labeled:

"Cursor: Hand", "Cursor: Heart", and "Cursor: Arrow".

a. When the "Cursor: Hand" button is clicked, the cursor should
   change to a hand (for the entire root window).
b. When the "Cursor: Heart" button is clicked, the cursor should
   change to a heart (for the entire root window).
c. When the "Cursor: Arrow" button is clicked, it should go back
   to the default arrow cursor (for the entire root window).
   
To set the cursor for the entire root window, configure root as you
would any other widget. For example:

    root.config(cursor="pirate")

Comment out previous tkinter code or close previous GUI windows as needed.
"""
print("See GUI window.")

root4 = tk.Tk()
root4.config(cursor="shuttle")

def chand():
    root4.config(cursor="hand2")
def cheart():
    root4.config(cursor="heart")
def carrow():
    root4.config(cursor="arrow")

hand = tk.Button(root4, text="Cursor: Hand", command=chand)
heart = tk.Button(root4, text="Cursor: Heart", command=cheart)
arrow = tk.Button(root4, text="Cursor: Arrow", command=carrow)
hand.pack()
heart.pack()
arrow.pack()



# mainloops

root.mainloop()
root2.mainloop()
root3.mainloop()
root4.mainloop()