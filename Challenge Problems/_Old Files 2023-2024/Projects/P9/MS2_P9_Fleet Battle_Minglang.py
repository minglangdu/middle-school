"""
Name: Minglang Du
Program: Fleet Battle, Base
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
            if (x < 0 or x >= len(other[0])) or (y < 0 or y >= len(other)):
                print("out of bounds!")
                return False # return error
            if (other[y][x] != '~'):
                print("ship overlap!")
                return False # return error
            other[y][x] = char
    return other # return modified list

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
                    new = c
                    printb(c)
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
    new[0][0] = "M"
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
    

def win(board): # check if win condition
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] != "~":
                return False
    return True # won! :)

print("""--------------------------------------------------------
Welcome to the Fleet Battle Game!
--------------------------------------------------------
Base Level Version:
This version of the game has no AI capabilities. It
needs two human players to play against each other.
--------------------------------------------------------
""")

p1 = place(p1, 1) # place ships
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
    b = prompt(p2, h2, p1, 2)
    
    if not b:
        break
    p1 = b[1] # same as other.
    h2 = b[2]
    