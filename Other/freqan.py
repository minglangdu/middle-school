import random
import tkinter as tk
from tkinter.font import Font

#########CONSTANTS########

TEXTPAD = 25
COLPAD = 15

COLSIZE = 15
COLHEIGHT = 420
SIZE = 500

START = 7
END = 42
SZ = END - START + 1

DICE = 7
RUNS = 100

##########################

root = tk.Tk()
root.title("Frequency Analysis")
canv = tk.Canvas(root, width = SIZE, height = SIZE)
canv.pack()

columns = [str(x) for x in range(START, END + 1)]
values = [0 for x in range(START, END + 1)]

def change():
    global values
    values = [0 for x in range(START, END + 1)]
    for i in range(10000):
        val = 0
        for j in range(DICE):
            val += random.randint(1, 6)
        values[val - START] += 1
    canv.after(1000, display)

def display():
    global values
    canv.create_rectangle(0, 0, SIZE, SIZE, fill="white")
    canv.create_rectangle(0, COLHEIGHT, SIZE, COLHEIGHT + 1)
    for i in range(SZ):
        canv.create_text(TEXTPAD + i * COLSIZE, COLHEIGHT + TEXTPAD, text = columns[i], font = Font(size=15))
        canv.create_rectangle(COLPAD + i * COLSIZE, 0, COLPAD + 1 + i * COLSIZE, 500)
        
        m = max(values)
        for j in range(values[i]):
            canv.create_rectangle(5 + i * COLSIZE, COLHEIGHT - COLHEIGHT * (values[i] / m), COLPAD - 5 + i * COLSIZE, COLHEIGHT, fill = "blue")
    canv.after(1, change)
        
canv.after(1, display)