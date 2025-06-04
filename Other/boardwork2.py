import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="asdf")
label.pack()
button = tk.Button(root, text="Click")
button.pack()
def change(ev):
    label.configure(text="asdasd")
button.bind("<Button-1>", change)
root.mainloop()