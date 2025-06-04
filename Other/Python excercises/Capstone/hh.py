"""
Human Hamlet - Capstone Project
by Minglang
"""
import random
import sys

x = 0
y = 0

grid = [['soil'] * 20 for x in range(15)]
build = []
rend = [[''] * 20 for x in range(15)]
humans = [[1, 1, []]]

def graphic(x, y):
    global grid, rend
    a = grid[y][x]
    for human in humans:
        if human[0] == x and human[1] == y:
            rend[y][x] = '☻'
            return
    if a == 'soil':
        b = random.choice(['.', ',', '`', '*'])
    elif a == 'wall':
        if grid[y + 1][x] == 'wall' and grid[y - 1][x] == 'wall' and grid[y][x + 1] == 'wall' and grid[y][x - 1] == 'wall':
            b = 'O'
        elif grid[y + 1][x] == 'wall' and grid[y - 1][x] == 'wall':
            b = '|'
        elif grid[y][x + 1] == 'wall' and grid[y][x - 1] == 'wall':
            b = '='
        else:
            b = '#'
    elif a == 'floor':
        b = '+'
    else:
        b = '?'
    rend[y][x] = b

def update(xx, yy):
    global x, y, grid, rend
    x = xx
    y = yy
    a = grid[yy][xx]
    graphic(xx, yy)
    if a in ['soil', 'wall']:
        pass
    elif a == 'asdf':
        pass #placeholder

def conv():
    global grid
    asdf = []
    for y in range(len(grid)):
        asdf.append([])
        for x in range(len(grid[0])):
            if grid[y][x] in ['wall']:
                asdf[y].append(True)
            else:
                asdf[y].append(False)
    return asdf

def pathfind(x1, y1, x2, y2, pathgrid, path):
    path = []
    y3 = max(y1, y2)
    y4 = min(y1, y2)
    x3 = max(x1, x2)
    x4 = min(x1, x2)
    for i in range(y4, y3 + 1):
        path.append([x1, i])
    for i in range(x4, x3 + 1):
        path.append([i, y2])
    return path

def people():
    global humans
    new = []
    for i in range(len(humans)):
        human = humans[i]
        x = human[0]
        y = human[1]
        pathgrid = conv()
        if len(human[2]) == 0:
            if grid[y][x][0] == 'b':
                grid[y][x] = grid[y][x][1:]
            if len(build) > 0:
                human[2] = pathfind(x, y, build[0][0], build[0][1], pathgrid, [])
                del build[0]
            else:
                human[2] = pathfind(x, y, 5, 5, pathgrid, [])
        human[2][0].append(human[2])
        new.append(human[2][0])
        del human[2][0]
    humans = new[:]

while True:
    for yy in range(len(grid)):
        for xx in range(len(grid[0])):
            update(xx, yy)
    people()
    for yy in range(len(grid)):
        for xx in range(len(grid[0])):
            a = rend[yy][xx]
            if a == '?':
                print('_', end = '', file = sys.stderr)
            else:
                print(a, end = '')
        print()
    print(len(build))
    print("Input what you want to do.")
    print("build: place a building")
    print("[return]: do nothing")
    ty = input()
    if ty == 'build':
        while 1:
            try:
                x1, y1, x2, y2 = [int(x) for x in input('x1, y1, x2, y2: ').split()]
                building = input('Enter building: ')
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        grid[y - 1][x - 1] = 'b' + building
                        build.append([x - 1, y - 1])
                break
            except:
                print("Enter x and y again. ")