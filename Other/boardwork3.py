import tkinter as tk

root = tk.Tk()

#listb = tk.Listbox(root)
#listb.grid(row=1, column = 1, padx=5, pady=5, sticky = "ew")
#for i in range(100):
#    listb.insert(i, str(i))
#
#scrollbar = tk.Scrollbar(root)
#scrollbar.grid(row = 1, column = 2, sticky="ns", padx=5, pady=5)
#listb.config(yscrollcommand=scrollbar.set)
#scrollbar.config(command=listb.yview)

textw = tk.Text(root, height=30, width=40)
textw.grid(row = 0, column = 0, padx=15, pady=15, sticky="nsew", columnspan = 2)
textw.insert(tk.END, "Cursor will start at end")
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row = 0, column = 2, sticky="ns", padx=15, pady=15)
scrollbar.config(command=textw.yview)
textw.config(yscrollcommand=scrollbar.set)
content = textw.get("1.0", tk.END)
print(content)
#textw.delete("1.0", tk.END)