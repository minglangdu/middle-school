"""
Project #2
Student: Minglang
Class: C6
Grade: 7
"""

import turtle
import math

# setup
screen = turtle.Screen()
# set screen dimensions
screen.setup(width=0.50, height=0.93, startx=0, starty=0)
# create turtle
grace = turtle.Turtle()
grace.speed(math.inf)
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

def arm(t, seg_size, turn_size, num_segments):
    # create two arms 
    magnet(t)
    for i in range(1, num_segments + 1):
        seg = seg_size + i * 10 + 15
        turn = turn_size + i * 10
        if i % 2 == 0: # so that the num of segments is not doubled
            t.fd(seg)
            t.rt(turn)
        else:
            t.fd(seg)
            t.lt(turn)
    move(t)
    # near same as above, but rt and lt are swapped
    for i in range(1, num_segments + 1):
        seg = seg_size + i * 10 + 15
        turn = turn_size + i * 10
        if i % 2 == 0:
            t.fd(seg)
            t.lt(turn)
        else:
            t.fd(seg)
            t.rt(turn)

def mandala(t, seg_size, turn_size, num_arms, num_segments):
    for i in range(num_arms):
        arm(t, seg_size, turn_size, num_segments)
        move(t)
        # turn degree = 360 / num_turns
        t.rt(360 / num_arms)

# main code
grace.width(1)
mandala(grace, 10, 40, 36, 6)
grace.width(3)
mandala(grace, 0.25, 60, 8, 10)
grace.width(5)
mandala(grace, 2, 90, 4, 15)
grace.width(7)
mandala(grace, 50, 10, 8, 10)
grace.ht() # hide turtle