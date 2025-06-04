"""
Worksheet # 13: Event Handling Logic
Student Code
Python Level 3

Student Name: Minglang Du
Class Section (if any): 8-D14
"""
          



print('\n *** Problem 4 *** ')

"""
Explain why special variables like StringVar are used in Tkinter and give an
example of where you might use one.
"""
print("Answer in comment.")

"""
Answer: 
These special variables are used in tkinter because they provide direct access to specific
parts of widgets. For example, when using StringVar in an entry object, you can not only
access the text in the entry at a low level, you can also easily set the text. 
"""


print('\n *** Problem 5 *** ')

"""
The following code is supposed to change the label text when the user
types "Hello" in the entry. Instead, nothing happens even when "Hello"
is typed in the entry widget. Find and fix the error.
"""
print("See GUI window.")

import tkinter as tk

def update_label(event):
    if entry_var.get() == "Hello":
        label2.config(text="Greeting detected!")

root = tk.Tk()
root.title("Problem 5")
root.geometry("400x100")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var)

label1 = tk.Label(root, text="'Hello' there!")
label2 = tk.Label(root, text="")

label1.pack()
entry.pack()
label2.pack()

entry.bind("<KeyRelease>", update_label)
root.mainloop()


print('\n *** Problem 6: Challenge Problem *** ')

"""
Create a Tkinter application with two checkbuttons labeled "Bold" and "Italic".
There should also be a label displaying some text. When a checkbutton is
selected, the corresponding style (bold or italic) should be applied to the
label's text. If both are selected, the text should be both bold and italic.

To make a font both bold and italic, the style string (the third element of the
font tuple) should be "bold italic", e.g.,

    label = tk.Label(root, text="Special Font Label", 
                     font=("Arial", 12, "bold italic"))
                 
Note: When you associate an IntVar with a checkbutton, the IntVar becomes a flag
for the checkbutton's status. It holds the value 1 when the checkbutton is
checked, indicating a 'True' state. Conversely, when the checkbutton is
unchecked, the IntVar is set to 0, representing a 'False' state. (In Python,
non-zero values are treated as True in conditions, and 0 is treated as
False.) Thus, you can use the IntVar value directly in conditional statements
to determine the state of the checkbutton.
"""
print("See GUI window.")

root = tk.Tk()
label = tk.Label(root, text="Special Font Label", font=("Arial", 12, ""))
label.pack()
bv = tk.IntVar()
iv = tk.IntVar()
def change():
    f = ""
    if (bv.get()):
        f += "bold "
    if (iv.get()):
        f += "italic"
    label.configure(font=("Arial", 12, f))
bold = tk.Checkbutton(root, text="Bold", variable=bv, command=change)
ital = tk.Checkbutton(root, text="Italic", variable=iv, command=change)
bold.pack()
ital.pack()
root.mainloop()

print('\n *** Problem 7: Challenge Problem *** ')

"""
Create a tkinter application where selecting a fruit from a set of radiobuttons
updates a label to display the possible colors for that fruit. The label should
change in real-time to report the colors associated with each fruit.

Steps (these don’t necessarily reflect the correct order of the code):
1. Create a dictionary to map some fruits to their possible colors (e.g.,
   "Apple" would map to a string "red, green, yellow, white"; "Banana" would
   map to "yellow, red, pink, purple"; etc.)
2. Set up a tkinter window with a group of radiobuttons for the different fruits
   (e.g., Apple, Banana, Cherry).
3. Create a StringVar to link to the radiobuttons, storing the value of the
   selected radiobutton (its fruit name as a string, e.g., "Apple").
4. Add a label that starts off blank/empty.
5. Implement a function to update the label's text whenever any fruit's
   radiobutton is selected, listing the possible colors for that fruit.
6. Assign each radiobutton's command attribute to the function from step 5.
"""
print("See GUI window.")

fruits = {
    "Apple":["red", "green", "white"],
    "Banana":["yellow","red","pink","purple"],
    "Blueberries":["blue", "violet", "dark blue"],
    "Cherry":["red", "redder"]
}
root = tk.Tk()
apvar = tk.StringVar()
bavar = tk.StringVar()
blvar = tk.StringVar()
chvar = tk.StringVar()
label1 = tk.Label(root, text="")
label1.pack()
def apchange2():
    a = fruits[apvar.get()]
    st = ""
    for i in a:
        st += i + " "
    label1.configure(text=st)
def bachange2():
    a = fruits[bavar.get()]
    st = ""
    for i in a:
        st += i + " "
    label1.configure(text=st)
def blchange2():
    a = fruits[blvar.get()]
    st = ""
    for i in a:
        st += i + " "
    label1.configure(text=st)
def chchange2():
    a = fruits[chvar.get()]
    st = ""
    for i in a:
        st += i + " "
    label1.configure(text=st)
ap = tk.Radiobutton(root, textvariable=apvar, value=1, command=apchange2)
ba = tk.Radiobutton(root, textvariable=bavar, value=2, command=bachange2)
bl = tk.Radiobutton(root, textvariable=blvar, value=3, command=blchange2)
ch = tk.Radiobutton(root, textvariable=chvar, value=4, command=chchange2)
apvar.set("Apple")
bavar.set("Banana")
blvar.set("Blueberries")
chvar.set("Cherry")
ap.pack()
ba.pack()
bl.pack()
ch.pack()
root.mainloop()