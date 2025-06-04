import copy

LENGTH = 2
HEIGHT = 2
PLAYER_CHAR = "@"

rooms = {
    "default":[
        ["#", ".", ".", "#"],
        ["."] * 4,
        ["."] * 4,
        ["#", ".", ".", "#"]
    ],
    "ud": [
        ["#", ".", ".", "#"]
        ] * 4,
    "dl": [
        ["#"] * 4,
        [".", ".", ".", "#"],
        [".", ".", ".", "#"],
        ["#", ".", ".", "#"]
        ],
    "lr": [
        ["#"] * 4,
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        ["#"] * 4
    ],
    "dr": [
        ["#"] * 4,
        ["#", ".", ".", "."],
        ["#", ".", ".", "."],
        ["#", ".", ".", "#"],
        ],
    "ul": [
        ["#", ".", ".", "#"],
        [".", ".", ".", "#"],
        [".", ".", ".", "#"],
        ["#"] * 4
        ],
    "ur": [
        ["#", ".", ".", "#"],
        ["#", ".", ".", "."],
        ["#", ".", ".", "."],
        ["#"] * 4
        ]
}

class Room:
    def __init__(self, x, y, type="default"):
        # top left: x y
        self.x = x
        self.y = y
        self.map = rooms[type]
        
def print_room(pc, map):
    print("Room coords:", pc[0][0], pc[0][1])
    for i in range(4):
        for j in range(4):
            if (j == pc[1][0] and i == pc[1][1]):
                print(PLAYER_CHAR, end="")
            else:
                print(map[pc[0][0]][pc[0][1]].map[i][j], end = "")
        print()
        
def move_player(thing, action):
    coord = copy.deepcopy(thing)
    if (action == 'up'):
        coord[1][1] -= 1
    elif (action == 'down'):
        coord[1][1] += 1
    elif (action == 'left'):
        coord[1][0] -= 1
    elif (action == 'right'):
        coord[1][0] += 1
    else:
        print("Invalid movement.")
    
    if (coord[1][1] <= -1):
        if (coord[0][1] <= 0):
            coord[0][1] = HEIGHT - 1
        else:
            coord[0][1] -= 1
        coord[1][1] = 3
    elif (coord[1][1] >= 4):
        if (coord[0][1] >= HEIGHT - 1):
            coord[0][1] = 0
        else:
            coord[0][1] += 1
        coord[1][1] = 0
    elif (coord[1][0] <= -1):
        if (coord[0][0] <= 0):
            coord[0][0] = LENGTH - 1
        else:
            coord[0][0] -= 1
        coord[1][0] = 3
    elif (coord[1][0] >= 4):
        if (coord[0][0] >= LENGTH - 1):
            coord[0][0] = 0
        else:
            coord[0][0] += 1
        coord[1][0] = 0
        
    if (map[coord[0][0]][coord[0][1]].map[coord[1][0]][coord[1][1]] == "#"):
        print("Collided with a wall.")
        return [[-100, -100], [-100, -100]]
    else:
        return coord
        
map = [[Room(4 * x, 4 * y) for x in range(LENGTH)] for y in range(HEIGHT)]
pc = [[0, 0], [1, 1]]
while (1):
    print_room(pc, map)
    a = input("Move the player: ").lower()
    if a == 'quit':
        break
    new = move_player(pc, a)
    if (new == [[-100, -100], [-100, -100]]):
        pass
    else:
        pc = new
    del new