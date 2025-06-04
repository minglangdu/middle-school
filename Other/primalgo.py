# Prim's Algorithm Test

NODE_AMOUNT = 50
NODE_SIZE = 5
CANV_SIZE = 400
MARGIN_SIZE = 25
STEP = 5

import tkinter as tk
import heapq
import random

root = tk.Tk()
canv = tk.Canvas(root, height = CANV_SIZE, width = CANV_SIZE)
canv.pack()

nodes = []
for i in range(NODE_AMOUNT):
    nodes.append([random.randint(MARGIN_SIZE, CANV_SIZE - MARGIN_SIZE),
                random.randint(MARGIN_SIZE, CANV_SIZE - MARGIN_SIZE)])
    x = nodes[i][0]
    y = nodes[i][1]
    canv.create_rectangle(x - NODE_SIZE, y - NODE_SIZE,
                          x + NODE_SIZE, y + NODE_SIZE)
    
dists = []
for i in range(NODE_AMOUNT):
    curdist = []
    for j in range(NODE_AMOUNT):
        dx = nodes[i][0] - nodes[j][0]
        dy = nodes[i][1] - nodes[j][1]
        curdist.append(pow(dx, 2) + pow(dy, 2))
    dists.append(curdist)

node = nodes[i]
q = []
for j in range(len(dists[i])):
    if j != i:
        q.append([dists[i][j], i, j])

heapq.heapify(q)
put = [i]

def step():
    global heapq
    global nodes
    global put
    if (len(put) >= NODE_AMOUNT):
        return
    cur = heapq.heappop(q)
    first = nodes[cur[1]]
    second = nodes[cur[2]]
    if (cur[2] in put):
        return
    canv.create_line(first[0], first[1], second[0], second[1],
                     fill = "red", width = "5")
    put.append(cur[2])
    for i in range(len(dists[cur[2]])):
        if (i != cur[2]):
            heapq.heappush(q, [dists[cur[2]][i], cur[2], i])

def wrap():
    step()
    canv.after(STEP, wrap)
    
canv.after(STEP, wrap)

#while (len(put) < NODE_AMOUNT):
#    cur = heapq.heappop(q)
#    first = nodes[cur[1]]
#    second = nodes[cur[2]]
#    if (cur[2] in put):
#        continue
#    canv.create_line(first[0], first[1], second[0], second[1])
#    put.append(cur[2])
#    for i in range(len(dists[cur[2]])):
#        if (i != cur[2]):
#            heapq.heappush(q, [dists[cur[2]][i], cur[2], i])

