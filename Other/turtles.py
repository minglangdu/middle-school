# this is from worksheet #4

import turtle

def poly(t, size, num_sides):
    t.speed(1e9) # for speed 
    turn = 360 / num_sides
    for i in range(num_sides):
        t.fd(size)
        t.rt(turn)

alice = turtle.Turtle()
bob = turtle.Turtle()
carol = turtle.Turtle()
dave = turtle.Turtle()
emily = turtle.Turtle()
frank = turtle.Turtle()
grace = turtle.Turtle()
harold = turtle.Turtle()
izzy = turtle.Turtle()
john = turtle.Turtle()
kelly = turtle.Turtle()
lawrence = turtle.Turtle()
mindy = turtle.Turtle()
noel = turtle.Turtle() # thank you noel, btw
olive = turtle.Turtle()
percy = turtle.Turtle()
qubert = turtle.Turtle()
ryan = turtle.Turtle()
sandy = turtle.Turtle()
terry = turtle.Turtle()
udhayan = turtle.Turtle()
victor = turtle.Turtle()
wanda = turtle.Turtle()
xavier = turtle.Turtle() # goofy ahh name
yoyo = turtle.Turtle() # also goofy ahh name
zachary = turtle.Turtle()


poly(alice, 40, 3)
poly(bob, 15, 4)
poly(carol, 20, 5)
poly(dave, 25, 6)
poly(emily, 30, 7)
poly(frank, 35, 8)
poly(grace, 30, 9)
poly(harold, 30, 10)
poly(izzy, 30, 11)
poly(john, 30, 12)
poly(kelly, 30, 13)
poly(lawrence, 30, 14)
poly(mindy, 30, 15)
poly(noel, 30, 16)
poly(olive, 30, 17)
poly(percy, 30, 18)
poly(qubert, 30, 19)
poly(ryan, 30, 20)
poly(sandy, 30, 21)
poly(terry, 30, 22)
poly(udhayan, 30, 23)
poly(victor, 30, 24)
poly(wanda, 30, 25)
poly(xavier, 30, 26)
poly(yoyo, 30, 27)
poly(zachary, 31, 28)