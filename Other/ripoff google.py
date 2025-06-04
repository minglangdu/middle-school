import tkinter as tk
import copy

info = {"geometry dash":
        ["gd", "gmd", "me"],
        "me":
        ["geometry dash", "ayden"],
        "ayden":
        ["battle cats", "noel", "gambling"],
        "battle cats":
        ["cat", "food", "cat food"],
        "noel":
        ["toyota", "cybertruck", "shresth"],
        "shresth":
        ["prophecy jar", "battle cats", "fish"],
        "prophecy jar":
        ["hocus pocus"],
        "toyota":
        ["car", "good"],
        "cybertruck":
        ["car", "bad"],
        "car":
        ["toyota", "cybertruck"],
        "gambling":
        ["food", "ayden"]}



root = tk.Tk()

title = tk.Label(root, text="Ripoff Google", font=("Comic Sans MS", 20, "bold"))
title.grid(row = 1, column = 2, padx = 50, pady = 10)

strinvar = tk.StringVar()
search = tk.Entry(root,textvariable=strinvar)
search.grid(row = 2, column = 2, padx = 50, pady = 10)

submit = tk.Button(root, text="Search", width = 15)
submit.grid(row = 3, column = 2, padx = 50, pady = 10)

subtitle = None;

labels = []
searchkey = ""

def searchsearch(event):
    widget1 = event.widget
    searchf(widget1.cget("text"))

def process(event):
    global searchkey
    for label in labels:
        label.destroy()
    global subtitle
    if subtitle:
        subtitle.destroy()
    dat = search.get()
    if (dat == ""):
        return
    found = set()
    dat = dat.lower()
    if (searchkey != ""):
        dat = searchkey
    for key in info.keys():
        if dat in key or key in dat:
            found.add(key)
            for i in info[key]:
                if i not in found:
                    found.add(i)
        else: 
            for i in info[key]:
                if dat in i or i in dat:
                    found.add(key)
                    break
    found.discard(dat)
    subtitle = tk.Label(root, text="Results", width = 15, font=("Times New Roman", 20, "bold"))
    subtitle.grid(row = 4, column = 2, padx = 50, pady = 15)
    for key in found:
        cop = copy.deepcopy(key)
        labels.append(tk.Label(root, text=key, width = 15, height = 1, font=("Times New Roman", 12, "underline"), fg="blue"))
        labels[len(labels) - 1].grid(row=4 + len(labels), column = 2)
        labels[len(labels) - 1].bind("<Button-1>", searchsearch)
        # lambda doesn't work as of now; defaults to end
    strinvar.set(searchkey)
    searchkey = ""
    
def searchf(keyword):
    global searchkey
    searchkey = keyword
    strinvar.set(searchkey)
    process(None)

submit.bind("<Button-1>", process)

root.mainloop()