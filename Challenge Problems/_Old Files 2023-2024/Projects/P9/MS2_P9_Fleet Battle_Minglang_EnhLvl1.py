"""
Name: Minglang Du
Program: Fleet Battle, Enhancement Level 1
Class: 7-C6
"""
import sys
import random


p1 = [["~"] * 8 for x in range(8)]
p2 = [["~"] * 8 for x in range(8)]
ships = [["Mega-carrier", 6], ["Carrier", 5], ["Battleship", 4], ["Submarine", 3], ["Destroyer", 2]] # list of ships
def printb(board):
    print("y/x", end=" ") 
    for i in range(len(board[0])):
        print(i,end="") # top row
    print()
    for i in range(len(board)):
        print(" " + str(i), end="  ") #side row
        for j in board[i]:
            print(j,end="")
        print()

def check(board, x, y, dir, length, char):
    sx, sy, ex, ey = -1, -1, -1, -1 # check if ship is valid
    # sx and sy: start coord; ex, ey end coord
    other = board[:]
    if dir == 0: # North
        ex = x + 1
        ey = y + 1
        sx = x
        sy = y - length + 1
    elif dir == 1: # South
        sx = x
        sy = y
        ex = x + 1
        ey = y + length
    elif dir == 2: # East
        sy = y
        sx = x
        ey = y + 1
        ex = x + length
    else: # West
        ey = y + 1
        ex = x + 1
        sy = y
        sx = x - length + 1
    for x in range(sx, ex): # loop through ship
        for y in range(sy, ey):
            if (x < 0 or x >= len(board[0])) or (y < 0 or y >= len(board)):
                #print("out of bounds!")
                return False # return error
            if (board[y][x] != '~'):
                #print("ship overlap!")
                return False # return error
    return [sx, sy, ex, ey] 

def make(board, sx, sy, ex, ey, char):
    other = board[:]
    for x in range(sx, ex):
        for y in range(sy, ey):
            other[y][x] = char
    return other

def place(board, player): # place ships
    input("Player " + str(player) + ", when ready to place, press ENTER.")
    new = board[:]
    print("Your board so far...")
    printb(new)
    for ship in ships: # place each ship in ship list
        print("Active player, place your " + ship[0] + ".")
        flag = False
        x, y = 0, 0
        dir = -1
        while not flag: # flag is only true when correct placement
            try:
                b = input("Input starting coordinates: ").strip().split()
                x = int(b[0])
                y = int(b[1])
                if (y >= len(board) or y < 0 or x >= len(board[0]) or x < 0):
                    raise SyntaxError("out of bounds") 
                if (new[y][x] != '~'):
                    raise SyntaxError("overlap")
            except: # invalid
                print("Invalid. Try again.")
                continue
            try: 
                l = ['N', 'S', 'E', 'W']
                b = input("Input direction(N, S, E, W): ")[0]
                if b in l:
                    dir = l.index(b)
                else:
                    raise SyntaxError("invalid direction")
                c = check(new, x, y, dir, ship[1], ship[0][0])
                if c:
                    new = make(new, c[0], c[1], c[2], c[3], ship[0][0])
                    printb(new)
                    flag = True
                else: 
                    raise SyntaxError("check returned false")
            except:# invalid
                print("Invalid. Try again.")
                continue
    print("\n" * 50) 
    return new

def autoplace(board, player):
    new = board[:]
    for ship in ships:
        while 1:
            x = random.randrange(0, 8)
            y = random.randrange(0, 8)
            flag = False
            for i in range(4):
                c = check(new, x, y, i, ship[1], ship[0][0])
                if c:
                    new = make(new, c[0], c[1], c[2], c[3], ship[0][0])
                    flag = True
                    break
            if flag:
                print("Placed Player " + str(player) +"'s " + ship[0])
                break
                
    return new

def shoot(board, hit): # shoot at a ship
    new = board[:] # player
    newh = hit[:] # hit list
    outcome = ""
    while 1:
        try: # same as place function
            b = input("Input coordinates: ").strip().split()
            x = int(b[0])
            y = int(b[1])
            if (y >= len(board) or y < 0 or x >= len(board[0]) or x < 0):
                raise SyntaxError("bad")
            if (hit[y][x] != "?"):
                raise SyntaxError("more bad")
            outcome = board[y][x]
            new[y][x] = "~"
            if (outcome == "~"):
                newh[y][x] = "m"
            else:
                newh[y][x] = "H"
            return [outcome, new, newh]
        except:
            print("Invalid. Try again.")
            continue

def prompt(shi, hits, opship, player): # prompt each player to place
    while 1:
        input("Player " + str(player) + ", press ENTER to shoot at a ship!")
        break # stops showing ships until player consents
    print("Your ships...")
    printb(shi)
    print("Opponent's ships (H is hit, m is miss)..")
    printb(hits)
    ret = shoot(opship, hits)
    print("\n" * 50)
    if ret[0] == '~':
        print("You missed.")
    else:
        print("HIT!!!", file=sys.stderr)
        e = ""
        for ship in ships:
            if ship[0][0] == ret[0]:
                e = ship[0]
        print("You hit the opponent's " + e + "!")
        if (win(opship)):
            print("PLAYER " + str(player) + " WINS!!!!!", file=sys.stderr)
            return None
    
    return ret

def autoshoot(board, hit):
    moves = []
    for y in range(len(hit)):
        for x in range(len(hit[0])):
            if hit[y][x] == "?":
                moves.append([x, y])
    shoot = random.choice(moves)
    outcome = board[shoot[1]][shoot[0]]
    newh = hit[:]
    new = board[:]
    if outcome == "~":
        newh[shoot[1]][shoot[0]] = "m"
        print("The AI missed. ")
    else:
        newh[shoot[1]][shoot[0]] = "H"
        print("The AI hit!")
        e = ""
        for ship in ships:
            if ship[0][0] == outcome:
                e = ship[0]
        print("It hit your " + e + "!")
        if win(board):
            print("AI WINS!")
            return None
    new[shoot[1]][shoot[0]] = "~"
    return [outcome, new, newh]

def win(board): # check if win condition
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] != "~":
                return False
    return True # won! :)

print("""--------------------------------------------------------
Welcome to the Fleet Battle Game!
--------------------------------------------------------
Enhanced Level 1 Version:
This version of the game has AI capabilities. It
needs two human players or just one to play.
--------------------------------------------------------
""")

ai = 0
if input("Players, do you want to play against an ai? (y/n)") == "y":
    print("Okay, playing against an ai. ")
    ai = 1
else:
    print("Okay, not playing against ai.")

if input("Player 1, enter y for autoplace: ") == "y":
    p1 = autoplace(p1, 1)
else:
    p1 = place(p1, 1)
if ai or input("Player 2, enter y for autoplace: ") == "y":
    p2 = autoplace(p2, 2)
else:
    p2 = place(p2, 2)

h1 = [["?"] * 8 for x in range(8)] # hit list
h2 = [["?"] * 8 for x in range(8)]
print("You are now ready to guess coordinates. Player 1 goes first.")
while 1: # hitting list
    a = prompt(p1, h1, p2, 1) 
   
    if not a: # break if won
        break
    p2 = a[1] # update values
    h1 = a[2]
    if not ai:
        b = prompt(p2, h2, p1, 2)
    else:
        b = autoshoot(p1, h2)
    if not b:
        break
    p1 = b[1] # same as other.
    h2 = b[2]
    
