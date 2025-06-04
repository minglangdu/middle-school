import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

uses = 0

def infobox():
    messagebox.showinfo("Title", "Message")

def errorbox():
    messagebox.showerror("Error Title", "This is an error message")

def questionbox():
    response = messagebox.askyesno("Poll", "Do you like tkinter?")
    if (response):
        messagebox.showinfo(":)", "Good")
    else:
        global uses
        uses += 1
        messagebox.showinfo("-_-", "Bad")
        messagebox.showinfo("Try again", "You've already clicked no " + str(uses) + " times.")
        questionbox()
    
def warningbox():
    messagebox.showwarning("Warning", "This is a warning warning warning warning warning warning linguistic satisfaction")

click = tk.Button(root, text="Click", command=infobox)
error = tk.Button(root, text="Error", command=errorbox)
question = tk.Button(root, text="Question", command=questionbox)
warning = tk.Button(root, text="Warning", command=warningbox)
menu = tk.Menu(root)
file = tk.Menu(root)
menu.add_cascade(label = "File", menu = file)
helpp = tk.Menu(root)
menu.add_cascade(label = "Help", menu = helpp)
menu.add_command(label = "Python help", command = help)
menu.add_command(label = "Exit", command = root.destroy)

root.config(menu = menu)
click.grid(row = 0, column = 0, padx = 15, pady = 5)
error.grid(row = 1, column = 0, padx = 15, pady = 5)
question.grid(row = 2, column = 0, padx = 15, pady = 5)
warning.grid(row = 3, column = 0, padx = 15, pady = 5)


root.mainloop()












### pov linguistic satisfaction ###











