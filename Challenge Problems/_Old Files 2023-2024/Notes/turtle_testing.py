import turtle
import random
import time
import math

screen = turtle.Screen()
screen.setup(width=0.93, height=0.93, startx=0, starty=0)
screen.bgcolor("black")

class randwalk(turtle.Pen):
    def __init__(self):
        self.colors = ["blue", "green", "red", "yellow", "purple", "brown", "white"]
        super().__init__()
        self.width(5)
        self.speed(1e9)
        self.setpos(random.randint(-400, 400), random.randint(-400, 400))
        self.pendown()
        self.pencolor("white")
        self.update()
    def update(self):
        if (random.randint(0, 12) == 1):
            self.penup()
        else:
            self.pendown()
        if (random.randint(0, 5) == 0):
            self.pencolor(random.choice(self.colors))
        if (random.randint(0, 5) == 0):
            self.pendown()
            try:
                self.setpos(random.randint(-100 + self.position()[0], 100 + self.position()[0]), random.randint(-100 + self.position()[1], 100 + self.position()[1]))
            except:
                pass
        else:
            self.right(random.randint(0,359))
            a = random.randint(1, 12)
            for i in range(a):
                self.right(random.randint(-30, 30))
                try:
                    forw = random.randint(25, math.floor(200 / a))
                    if forw:
                        self.forward(forw)
                except:
                    pass
        

class filler(turtle.Pen):
    def __init__(self):
        self.colors = ["blue", "green", "red", "yellow", "purple", "brown", "white"]
        super().__init__()
        self.width(5)
        self.speed(1e9)
        self.setpos(random.randint(-400, 400), random.randint(-400, 400))
        self.pendown()
        self.update()
    def update(self):
        self.pencolor("white")
        self.penup()
        try:
            self.setpos(random.randint(-100 + self.position()[0], 100 + self.position()[0]), random.randint(-100 + self.position()[1], 100 + self.position()[1]))
        except:
            pass
        self.fillcolor()

objs = []
for i in range(7):
    objs.append(randwalk())
for i in range(10):
    objs.append(filler())
while 1:
    for i in objs:
        i.update()