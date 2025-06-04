"""
Quiz #2: Chapter 8
Problem Code for Students
Python Level 2
"""

print ('\n *** Problem 2 ***')

import turtle

joe = turtle.Turtle()
bob = turtle.Turtle()
bob.pu()
bob.rt(90)
bob.fd(100)
bob.pd()

# This is supposed to draw a hexagon using the turtle
# passed into the parameter turt:
def hexagon(turt):
    for i in range(6):
        turt.fd(100)
        turt.rt(60)

hexagon(joe)

def starburst(radius):
    for i in range(6):
        bob.fd(radius)
        bob.rt(60)
        bob.bk(radius)
    bob.fd(radius)
        
starburst(100)