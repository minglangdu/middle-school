"""
Worksheet # 14: Additional Widgets
Student Code
Grade 8 (Python Level 3)

Student Name: Minglang
Class Section (if any): 8-D14
"""

print('\n <<< Part 1 >>>')

print('\n *** Problem 1 *** ')

"""
The following code attaches a scrollbar to a Listbox in Tkinter, but it's not
working correctly. Identify in what way the scrollbar is not working and why,
and then fix the issue.
"""
print("See GUI window.")

import tkinter as tk

root = tk.Tk()
root.title("Problem 1")
root.geometry("350x300")

listbox = tk.Listbox(root)
scrollbar = tk.Scrollbar(root)

scrollbar.config(command=listbox.yview)
# this line was not added to link the scrolling of the listbox with the scrollbar.
listbox.config(yscrollcommand=scrollbar.set) 

for i in range(100):
    listbox.insert(tk.END, i)

listbox.grid(row=0, column=0)
scrollbar.grid(row=0, column=1, sticky="ns")

root.mainloop()


print('\n *** Problem 2 *** ')

"""
Describe the purpose of the yscrollcommand and command attributes when linking
a scrollbar with a Text widget in Tkinter. Why are both needed?
"""

"""
Answer:
Yscrollcommand and command are used in conjunction to link a text widget and scrollbar.
Yscrollcommand is set by the text widget to use the scrollbar as a scroll controller,
and command is used to set the function of the scrollbar to controlling the text box.
Thus, neither command can be used on its own as it requires the other to function
correctly. 
"""
print("Answer in comment.")


print('\n *** Problem 3 *** ')

"""
Write a Python script to include a Tkinter window with a Text widget and a
Button widget. The Text widget should have the following properties:

a. Width of 40 characters and height of 10 lines.
b. Background color is light gray, and the text color is blue.
c. Default text that reads "Enter your text here." is inserted at the beginning.

Include a button labeled "Clear Text". When this button is clicked, it should
clear all text from the Text widget.
"""
print("See GUI window.")

root = tk.Tk()
text = tk.Text(root, width=40, height=10, bg="light gray", fg="blue")
text.insert(tk.END, "Enter your text here.")
text.grid(row = 0, column = 0, columnspan = 3, sticky="ew", padx=5, pady=5)
def clear():
    text.delete("1.0", tk.END)
button = tk.Button(root, command=clear, text="Clear")
button.grid(row = 1, column = 0, padx=5, pady=5)
#root.mainloop()


print('\n *** Problem 4 *** ')

"""
Modify the program you created in Problem 3 by adding another button labeled
"Submit Text" (on the same row and to the right of the "Clear Text" button).
Clicking this button should output the contents of the Text widget to the
console. Test this by entering text of your own into the Text field and then
clicking "Submit Text".
"""
print("See GUI window.")

def submit():
    print(text.get("1.0", tk.END))
button2 = tk.Button(root, command=submit, text="Submit")
button2.grid(row=1, column=1, padx = 5, pady = 5)
#root.mainloop()

print('\n *** Problem 5: Challenge Problem *** ')

"""
Modify the code from problem 4 to add the following features:

a. Clicking on the Text field for the first time should automatically clear
   the widget so that the user can begin typing into a blank field. This
   should only happen the first time the user clicks in the field.
   
b. Every time the user clicks Submit Text, the text in the widget should be 
   saved in a data structure (instead of immediately printing to console) and
   then cleared from the Text widget.
   
c. Add a button called "Retrieve Text" to print to the console all the text
   messages submitted so far.

"""
print("See GUI window.")

clicked = False
submits = []
def onclcl(event):
    global clicked
    if (clicked):
        return
    text.delete("1.0", tk.END)
    clicked = True
text.bind("<Button-1>", onclcl)
def submit2():
    submits.append(text.get("1.0", tk.END))
    text.delete("1.0", tk.END)
def retrieve():
    print("----")
    for i in submits:
        print(i, "----", sep="\n")
button2.configure(command=submit2)
button3 = tk.Button(root, text="Retrieve", command=retrieve)
button3.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()

