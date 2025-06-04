import tkinter as tk

root = tk.Tk()
root.title('window')

check = tk.Checkbutton(root, text = "A")
check2 = tk.Checkbutton(root, text = "B")
check.pack()
check2.pack()

root.mainloop()