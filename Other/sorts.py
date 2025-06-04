import random
import tkinter as tk
from tkinter.font import Font

#########CONSTANTS########

TEXTPAD = 25
COLPAD = 10

COLSIZE = 10
COLHEIGHT = 420
SIZE = 500

SZ = 50

DICE = 7
RUNS = 100

##########################

ssort = 0
ss = 0
sorting = False

root = tk.Tk()
root.title("Sorting Algorithms - WIP")
canv = tk.Canvas(root, width = SIZE, height = SIZE)
canv.pack()

values = [x for x in range(1, SZ + 1)]

def shuf():
    global values
    values = [x for x in range(1, SZ + 1)]
    random.shuffle(values)
    canv.after(5, sort)
    canv.after(1, display)

def sort():
    global ssort
    ssort %= 2
    if ssort == 0:
        print("Selection Sort")
        canv.after(500, sel)
                
    if ssort == 1:
        print("Bubble Sort")
        
    ssort += 1

def sel():
    global ss
    if ss >= SZ:
        canv.after(1, display)
        canv.after(1000, shuf)
        return
    
    a = ss
    for j in range(ss, SZ):
        if values[a] >= values[j]:
            a = j
    values[a], values[ss] = values[ss], values[a]

    ss += 1
    canv.after(1, display)
    canv.after(500, sel)

def display():
    global values
    canv.create_rectangle(0, 0, SIZE, SIZE, fill="white")
    canv.create_rectangle(0, COLHEIGHT, SIZE, COLHEIGHT + 1)
    for i in range(SZ):
        
        m = max(values)
        for j in range(values[i]):
            canv.create_rectangle(i * COLSIZE, COLHEIGHT - COLHEIGHT * (values[i] / m), COLPAD + i * COLSIZE, COLHEIGHT, fill = "blue")
        
canv.after(5, shuf)
canv.after(1, display)