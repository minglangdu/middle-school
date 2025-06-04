import tkinter as tk
from tkinter.font import Font
import random
import copy

## CONSTANTS ##

WIDTH = 1100
HEIGHT = 150

SIZE = 20
PADX = 50
PADY = 50
CELLSIZE = 50

TXPADX = 25
TXPADY = 25
TXSIZE = 15
INDSIZE = 10

DELAY = 1500

###############

root = tk.Tk()
root.geometry("+100+300")
canv = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canv.pack()

li = list(range(1, SIZE + 1))
random.shuffle(li)

part = -1
id = 0
indices = [[0, len(li)]]

def showlist():
    if (len(indices) == 0):
        canv.after(DELAY, end)
        return
    
    canv.create_rectangle(0, 0, WIDTH + 5, HEIGHT + 5, fill = "white")
    new = li[indices[0][0]:indices[0][1]]
    print("Shown list:", new)
    for i in range(len(new)):
        x = PADX + CELLSIZE * i
        canv.create_rectangle(x, PADY, x + CELLSIZE, PADY + CELLSIZE, fill = "white")
        canv.create_text(x + TXPADX, PADY + TXPADY, text = str(new[i]), font = Font(size = TXSIZE))

def issorted():
    if (len(indices) == 0):
        canv.after(DELAY, end)
        return
    try:
        cur = li[indices[0][0]]
        for i in range(indices[0][0] + 1, indices[0][1]):
            if (li[i] < cur):
                return False
            cur = li[i]
        return True
    except:
        return True

# inefficient because im bad
def part1():
    global part, id, li
    if (len(indices) == 0):
        canv.after(DELAY, end)
        return
    print(f"doing indices between {indices[0][0]} and {indices[0][1]}")
    showlist()
    if (issorted()):
        del indices[0]
        print("already sorted, skipping")
        canv.after(DELAY, part1)
        return
    part = li[min(indices[0][1] - 1, len(li) - 1)]
    print("partition value is ", part)
    x = PADX + CELLSIZE * (indices[0][1] - 1)
    id = canv.create_text(x + TXPADX, TXPADY, text = "Partition", font = Font(size = INDSIZE))
    canv.after(DELAY, part2)
    
def part2():
    global part, id, li
    if (len(indices) == 0):
        canv.after(DELAY, end)
        return
    canv.move(id, 0, -200)
    a = []
    b = []
    new = li[indices[0][0]:indices[0][1]]
    for i in new:
        if i == part:
            continue
        if i < part:
            a.append(i)
        else:
            b.append(i)
    l = len(a)
    a.extend(b)
    li = a
    showlist()
    indices.append([indices[0][0], indices[0][0] + l])
    indices.append([indices[0][0] + l, min(indices[0][1], len(li))])
    del indices[0]
    canv.after(DELAY, part1)

def end():
    print("Ending list:", li)
    showlist()

showlist()
canv.after(DELAY, part1)