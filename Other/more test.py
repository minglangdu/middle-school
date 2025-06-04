import tkinter as tk
import math
import random

root = tk.Tk()
canv = tk.Canvas(height = 500, width = 500)
canv.pack()

class Neuron:
    def __init__(self, wsize, bias):
        self.weights = [random.randint(0, 10) for x in range(wsize)]
        self.bias = bias
        self.value = random.randint(0, 10)
class Layer:
    def __init__(self, namount, nsize):
        self.neurons = [Neuron(nsize, 0) for x in range(namount)]
colors = ["red", "pink", "grey", "light green", "green", "green"]
class Network:
    def __init__(self):
        sizes = [5, 8, 10, 10, 8, 2, 0]
        self.layers = [Layer(sizes[x], sizes[x + 1])
                       for x in range(len(sizes) - 1)]
        self.locs = []
        self.setlocs()
        self.makenodes()
        self.makeedges()
    def setlocs(self):
        for i in range(len(self.layers)):
            x = 25 + 75 * i
            ns = self.layers[i].neurons
            mid = 25 + 50 * (len(ns) - 1) / 2
            tem = []
            for j in range(len(ns)):
                y = 50 * j - mid + 275
                tem.append([x, y + 7.5])
            self.locs.append(tem)
    def makenodes(self):
        for i in range(len(self.layers)):
            x = 25 + 75 * i
            ns = self.layers[i].neurons
            mid = 25 + 50 * (len(ns) - 1) / 2
            for j in range(len(ns)):
                y = 50 * j - mid + 275
                col = colors[round(ns[j].value / (len(colors) - 1))]
                canv.create_rectangle(x, y, x + 15, y + 15, fill=col)
                canv.create_text(x + 7.5, y + 7.5, text=ns[j].value)
    def makeedges(self):
        self.locs.append([]) # stop out of bounds
        for i in range(len(self.locs)):
            for j in self.locs[i]:
                for k in self.locs[i + 1]:
                    ns = self.layers[i].neurons
#                    col = colors[round(ns[j].weights[k]
#                                       / (len(colors) - 1))]
                    col = "red"
                    canv.create_line(j[0], j[1], k[0], k[1], fill = col)

tick = 0

def update():
    global tick
    tick += 1
    tick %= 5000
    if (tick % 100 == 0):
        canv.create_rectangle(0, 0, 600, 600, fill="white")
        net.makeedges()
        net.makenodes()
    canv.after(1, update)

net = Network()
canv.after(1, update)