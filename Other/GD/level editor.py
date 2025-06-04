import tkinter
from base import *
from blocks import *

test = False

class Editor(Game):
    def __init__(self, root):
        self.hitbox = False # whether spikes have hitboxes
        self.over = False # if game is over
        if test:
            self.speed = 3 # how fast player moves
        else:
            self.speed = 0
        self.offset = 0
        self.yoff = 0
        self.level = []
        super().__init__(500, 500, root)
        self.bind_all('<Key>', self.onkey)
        self.ind = None
        self.init()
        self.after(1, self.update) # begin mainloop
    def init(self):
        if test:
            Under(25, 401, self) # thing player rests on (invisible)
            self.create_rectangle(0, 350, 530, 530, fill = "blue") # ground (fake)
            self.create_rectangle(0, 0, 530, 351, fill = "light blue") # background
            self.player = Cube(25, 300, self)
        else:
            self.create_rectangle(0, 350, 530, 530, fill = "blue") # ground (fake)
            self.create_rectangle(0, 0, 530, 351, fill = "light blue") # background
        for i in self.level: # makes everything
            if i[0] == 0:
                Spike(i[1], i[2], self)
            else:
                Block(i[1], i[2], self)
        self.ind = self.create_rectangle(235, 350, 285, 300, fill = "white")
        
    def onkey(self, e):
        print(e.keysym)
        k = e.keysym
        
        if (k == 'a'):
            self.speed = -5
            self.after(50, self.reset)
            self.offset -= 25
        elif (k == 'd'):
            self.speed = 5
            self.after(50, self.reset)
            self.offset += 25
        elif (k == 'w'):
            self.yoff -= 25
            self.move(self.ind, 0, -25)
        elif (k == 's'):
            self.yoff += 25
            self.move(self.ind, 0, 25)
        elif (k == 'p'):
            print(self.level)
        elif (k == 'k'):
            Spike(255, 343 + self.yoff, self)
            self.level.append([0, 255 + self.offset, 343 + self.yoff])
        elif (k == 'b'):
            Block(235, 350 + self.yoff, self)
            self.level.append([1, 235 + self.offset, 350 + self.yoff])
        elif (k == 'j'):
            Jump(255, 343 + self.yoff, self)
            self.level.append([2, 255 + self.offset, 343 + self.yoff])
        elif (k == 'o'):
            Orb(235, 300 + self.yoff, self)
            self.level.append([3, 235 + self.offset, 300 + self.yoff])
        elif (k == 'minus'):
            file = open("level.txt", "w")
            file.write(str(self.level))
            
    def reset(self):
        self.speed = 0
        
root = tkinter.Tk()
game = Editor(root)
root.mainloop()