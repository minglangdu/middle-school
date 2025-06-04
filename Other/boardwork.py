import tkinter as tk

root = tk.Tk()
root.title("Winter Activity List")
#root.geometry("200x300")
root.resizable(False, False)

label = tk.Label(root, text="Winter Activity List")
label.grid(row=0,column=1, pady = 5)
label.configure(fg="blue", bg="light blue", font=("Comic Sans MS", 25, "italic", "bold"))

listbox = tk.Listbox(root)
listbox.grid(row=1, column=0, columnspan = 3, padx = 5)

def add1():
    pass
def rem1():
    pass
def cle1():
    pass

add = tk.Button(root, text="Add", command=add1, bg="green", height=2, width=7)
add.grid(row=2, column = 0, pady = 5, padx = 5)
add.configure(font=("Times New Roman", 15, "bold"), cursor="circle")
# cursor="watch" is really fun

rem = tk.Button(root, text="Remove", command=rem1, bg="yellow", height=2, width=7)
rem.grid(row=2, column = 1, pady = 5, padx = 5)
rem.configure(font=("Times New Roman", 15, "bold"), cursor="circle")

cle = tk.Button(root, text="Clear", command=cle1, bg="red", height=2, width=7)
cle.grid(row=2, column = 2, pady = 5, padx = 5)
cle.configure(font=("Times New Roman", 15, "bold"), cursor="circle")

print("mouseover on add is " + add.cget("cursor"))