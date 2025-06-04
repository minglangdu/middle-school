"""
Worksheet # 9: Introduction to GUI programming
Student Code
Python Level 3

(For Publications use: Document Code 09-969.181-24)
"""

"""
Part 1: Introduction to GUIs and Tkinter
Problems 1 - 3
"""

print('\n *** Problem 1 *** ')

print("Answer in the comment.")
"""
In your own words, what is the biggest advantage of a GUI over a text-based,
command-line interface?

The biggest advantage of a GUI over a text-based interface is that it is
more intuitive and easier to understand. While a text-based interface needs
a lot of reading to understand and can be unwieldy, the various elements of
a GUI are easy. For example, when a text entry is seen, we know that we put
text in there, unlike where we need to read in a text-based interface.
"""


print('\n *** Problem 2 *** ')

print("2a. Answer in the comment.")
"""
2a. Explain the purpose of creating a main application window in tkinter.

Creating a main application window creates an object that allows you to
add widgets to it. Therefore, it is the base of everything in a GUI.
"""

print("2b. Output will be a GUI window.")
"""
2b. Write a Python script to create a basic tkinter window and set its title
to "Problem 2". Manually resize the window if needed to verify the window title.
"""
import tkinter as tk
root2 = tk.Tk()
root2.title("Problem 2")



print('\n *** Problem 3 *** ')

print("Answer in the comment.")
"""
Explain the use of import tkinter as tk in your script.

The phrase 'import tkinter as tk' imports the tkinter module under the
abbreviation tk so that it is easier to call. 
"""


"""
Part 2: Tkinter Widgets: Labels, Buttons, Entry Widgets
Problems 4 - 7
"""

print('\n *** Problem 4 *** ')
print("Output will be a GUI window.")

import tkinter as tk
root = tk.Tk()

"""
4a. Create a root window with the title "Problem 4". Define a function named
on_button_print() to print "Yay you clicked me!" to the console. (Later, you
will bind a button to this function.)
"""
root.title('Problem 4')
def on_button_print():
    print("Yay you clicked me!")

    
"""
4b. Create and place a button with the text, "Click me!". Bind it to the
function on_button_print() using the button's command parameter.

You will need to move the call to root.mainloop() below the code for this
sub-problem since code below the loop will not execute until the loop ends
(usually when the GUI window is closed by the user). Therefore, if you want to
add more widgets or make further modifications to the GUI before the window is
displayed and starts interacting with the user, make sure to do so before the
call to root.mainloop().
"""
button = tk.Button(root, text = "Click me!", command = on_button_print)
button.pack()

print('\n *** Problem 5 *** ')
print("Output will be a GUI window.")

"""
5a. Create a tkinter window with the title "Problem 5". Add a label to the 
tkinter window that displays the text "Hello, World!".
"""
root.title('Problem 5')
label = tk.Label(root, text = "Hello, World!")
label.pack()

"""
5b. Add another label with the text:
"Hello, World! This string is longer to demonstrate window resizing."
"""
label.pack()


print('\n *** Problem 6 *** ')

print("6a. Debugging problem--see code.")
"""
Identify and fix the error in the code.
"""
import tkinter as tk
main = tk.Tk()
main.title("Problem 6: Debugging")
button = tk.Button(main, text="Press Me")
button.pack()

print("6b. Answer in the comment.")
"""
Explain why the error occurred and how to avoid it in similar situations.

The error occurred when the button used the wrong window: it used root
instead of main. to solve this clearly check which window you are using
before writing it. 
"""


print('\n *** Problem 7 *** ')

print("Output will be a GUI window.")
"""
Create a tkinter window titled "Problem 7". Add an entry widget to allow user
input and a button that, when clicked, retrieves and prints the input to the
console.
"""

root.title('Problem 7')
entry = tk.Entry(root)
entry.pack()
def retrieve():
    print(entry.get())
button2 = tk.Button(root, text="retrieve", command=retrieve)
button2.pack()

######

root.mainloop()
main.mainloop()
root2.mainloop()