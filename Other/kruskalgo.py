# Kruskal's Algorithm Test #

NODE_AMOUNT = 40
NODE_SIZE = 5
CANV_SIZE = 400
MARGIN_SIZE = 25
STEP = 1

import tkinter as tk
import heapq
import random
import copy

root = tk.Tk()
canv = tk.Canvas(root, height = CANV_SIZE, width = CANV_SIZE)
canv.pack()

dsu = [x for x in range(NODE_AMOUNT)]
def find(node):
    if dsu[node] == node:
        return node
    res = find(dsu[node])
    dsu[node] = res
    return res
def union(n1, n2):
    f1 = find(n1)
    f2 = find(n2)
    if f1 == f2:
        return
    dsu[f1] = f2

nodes = []
for i in range(NODE_AMOUNT):
    nodes.append([random.randint(MARGIN_SIZE, CANV_SIZE - MARGIN_SIZE),
                random.randint(MARGIN_SIZE, CANV_SIZE - MARGIN_SIZE)])
    x = nodes[i][0]
    y = nodes[i][1]
    canv.create_rectangle(x - NODE_SIZE, y - NODE_SIZE,
                          x + NODE_SIZE, y + NODE_SIZE)
    
edgelist = []
for i in range(NODE_AMOUNT):
    for j in range(i):
        dx = nodes[i][0] - nodes[j][0]
        dy = nodes[i][1] - nodes[j][1]
        edgelist.append([pow(dx, 2) + pow(dy, 2), i, j])

heapq.heapify(edgelist)
newn = [[] for i in range(NODE_AMOUNT)]

def step():
    edge = heapq.heappop(edgelist)
    first = edge[1]
    second = edge[2]
    if (find(first) == find(second)):
        return
    canv.create_line(nodes[first][0], nodes[first][1],
                     nodes[second][0], nodes[second][1],
                     fill = "red", width = "5")
    newn[first].append(second)
    newn[second].append(first)
#    print(first, second)
    union(first, second)
        
def wrap():
    flag = True
    a = find(0)
    for i in range(len(dsu)):
        if find(i) != a:
            flag = False
    if (not len(edgelist) or flag):
        print("Done.")
        print("Getting Diameter")

        d1 = bfs(0)
        d2 = bfs(d1)
        canv.create_rectangle(nodes[d1][0] - NODE_SIZE, nodes[d1][1] - NODE_SIZE,
                          nodes[d1][0] + NODE_SIZE, nodes[d1][1] + NODE_SIZE, fill = "blue", width = 3)
        canv.create_rectangle(nodes[d2][0] - NODE_SIZE, nodes[d2][1] - NODE_SIZE,
                          nodes[d2][0] + NODE_SIZE, nodes[d2][1] + NODE_SIZE, fill = "blue", width = 3)
        getpath(d1, d2)
        return
    step()
    canv.after(STEP, wrap)
    
canv.after(STEP, wrap)

# Get Diameter #

def bfs(node):
    q = [node]
    visit = set()
    ans = node
    while (len(q)):
        for i in range(len(q), 0, -1):
            cur = heapq.heappop(q)
            if (cur in visit):
                continue
            visit.add(cur)
            ans = cur
            for nd in newn[cur]:
                heapq.heappush(q, nd)
    return ans

def getpath(d1, d2):
    q = [[d1]]
    visit = set()
    ans = []
    while (len(q)):
        for i in range(len(q), 0, -1):
            print(len(q))
            cur = heapq.heappop(q)
            print(cur)
            if (cur[len(cur) - 1] in visit):
                continue
            visit.add(cur[len(cur) - 1])
            if (cur[len(cur) - 1] == d2):
                ans = cur
            for nd in newn[cur[len(cur) - 1]]:
                a = copy.deepcopy(cur)
                a.append(nd)
                heapq.heappush(q, a)
                print(a)
                
    print(ans)
    prev = d1
    for node in ans:
        canv.create_line(nodes[prev][0], nodes[prev][1], nodes[node][0], nodes[node][1], fill = "blue", width = "7")
        prev = node
        
            