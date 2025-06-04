"""
Project #2
Student: Minglang
Class: C6
Grade: 7

ENHANCEMENTS:
Level 1
Level 2
Level 3
Level 4
Level 5
"""

import turtle
import math
import time
from random import randrange, seed

# random seed
setseed = input("Random seed? (Y/n) (default random)").lower() == "n"
if setseed:
    seed(input("Input seed: "))
else:
    seed("")
# setup screen
screen = turtle.Screen()
# screen dimensions
screen.setup(width=0.50, height=0.93, startx=0, starty=0)
# screen colormode

screen.colormode(255)
screen.bgcolor((0,0,0))

# create turtle
grace = turtle.Turtle()
grace.speed(math.inf)
turtle.delay(0)
# save position and heading
saved_pos = [0, 0]
saved_h = 0

# helping functions
def magnet(t):
    # save position and heading
    global saved_pos, saved_h
    saved_pos = t.pos()
    saved_h = t.heading()

def move(t):
    # move to saved position and heading
    t.pu()
    t.setpos(saved_pos)
    t.seth(saved_h)
    t.pd()

def arm(t, s1, s2, t1, t2, num_segments, width, color, rtt):
    # create two arms 
    magnet(t)
    for i in range(1, num_segments + 1):
        seg1 = s1 + i * 10 + 15
        seg2 = s2 + i * 10 + 15
        turn1 = t1 + i * 10
        turn2 = t2 + i * 10
        # ENHANCEMENT 1: Curves
        if i % 2 == 0: # so that the num of segments is not doubled
            for i in range(8):
                # turtle makes smaller turns to give illusion of curves
                t.fd(seg1 / 8)
                t.rt(turn1 / 8)
        else:
            for i in range(8):
                t.fd(seg2 / 8)
                t.lt(turn2 / 8)
    move(t)

def mandala(t, s1, s2, t1, t2, num_arms, num_segments, width, color):
    turts = []
    for i in range(num_arms):
        t11 = turtle.Turtle()
        t11.width(width)
        t11.pencolor(color)
        t11.rt((360 / num_arms) * i)
        turts.append(t11)
    for i in range(1, num_segments + 1):
        seg1 = s1 + i * 10 + 25
        seg2 = s2 + i * 10 + 25
        turn1 = t1 + i * 4
        turn2 = t2 + i * 4
        #arm(t, s1, s2, t1, t2, num_segments, width, color, (360 / num_arms) * i)
        for j in range(num_arms):
            # ENHANCEMENT 1: Curves
            print("move turtle " + str(j))
            if i % 2 == 0: # so that the num of segments is not doubled
                for i in range(8):
                    # turtle makes smaller turns to give illusion of curves
                    turts[j].fd(seg1 / 8)
                    turts[j].rt(turn1 / 8)
            else:
                for i in range(8):
                    turts[j].fd(seg2 / 8)
                    turts[j].lt(turn2 / 8)
    turts = []
    for i in range(num_arms):
        t11 = turtle.Turtle()
        t11.width(width)
        t11.pencolor(color)
        t11.rt((360 / num_arms) * i)
        turts.append(t11)
    for i in range(1, num_segments + 1):
        seg1 = s1 + i * 10 + 25
        seg2 = s2 + i * 10 + 25
        turn1 = t1 + i * 4
        turn2 = t2 + i * 4
        #arm(t, s1, s2, t1, t2, num_segments, width, color, (360 / num_arms) * i)
        for j in range(num_arms):
            # ENHANCEMENT 1: Curves
            print("move turtle " + str(j))
            if i % 2 == 0: # so that the num of segments is not doubled
                for i in range(8):
                    # turtle makes smaller turns to give illusion of curves
                    turts[j].fd(seg1 / 8)
                    turts[j].lt(turn1 / 8)
            else:
                for i in range(8):
                    turts[j].fd(seg2 / 8)
                    turts[j].rt(turn2 / 8)

def randmand():
    width = randrange(1, 5)
    color = (randrange(0, 256), \
            randrange(0, 256), \
            randrange(0, 256))
    
    s1 = randrange(3, 30)
    s2 = randrange(3, 30)
    t1 = randrange(10, 91)
    t2 = randrange(10, 91)
    arms = randrange(2, 13)
    segs = randrange(3, 7)
    mandala(grace, s1, s2, t1, t2, arms, segs, width, color) # ENHANCEMENT 3: Randomness
    
    grace.pencolor((0, 0, 0))
    grace.width(5)
    grace.ht()
    time.sleep(1)
    mandala(grace, s1, s2, t1, t2, arms, segs, 7, (0, 0, 0)) # ENHANCEMENT: ANIMATION
    

# main code
i = 0
while 1:
    print(i)
#    if i % 5 == 1:
#        # this is constant
#        grace.width(5)
#        grace.pencolor("black")
#        grace.pencolor((75, 255, 25))
#        mandala(grace, 55, 55, 3125, 3125, 5, 5, 5, (75, 255, 25))
#        
#        grace.pencolor((0, 0, 0))
#        grace.ht()
#        time.sleep(1)
#        mandala(grace, 55, 55, 3125, 3125, 5, 5, 5, (0, 0, 0))
        
#    else:
    randmand()
    i += 1