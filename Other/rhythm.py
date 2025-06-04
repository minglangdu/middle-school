import tkinter
from tkinter.font import Font
from base import *
import random

root = tkinter.Tk()
root.title("Random Rhythm Game")

colors = ["blue", "red", "yellow", "green", "purple", "pink", "orange", "light green"]
score = 0

class Rhythm(Game):
    def __init__(self, root):
        super().__init__(500, 500, root)
        self.over = False
        self.cooldown = 700
        self.speed = 16
        self.color = random.choice(colors)
        self.blocks = 5
        self.totblocks = 5
        self.destroyed = 0
        self.init()
        self.after(1, self.update())
    def init(self):
        self.score = self.create_text(230, 20, text=f"Score: {str(score)}", fill = "green", font = Font(size=15))
    def cust(self):
        self.itemconfig(self.score, text=f"Score: {str(score)}")
        if self.over:
            root.destroy()
        if self.blocks < 1 and self.tick % 5000 != 0:
            return
        elif self.destroyed >= self.totblocks:
            self.destroyed = 0
            self.blocks = random.randint(9, 15)
            self.totblocks = self.blocks
            self.cooldown = random.randint(600, 800)
            self.speed = random.randint(11, 16)
            self.color = random.choice(colors)
            bg = self.color
            while (self.color == bg):
                bg = random.choice(colors)
            self.create_rectangle(0, 0, 500, 500, fill = bg)
            self.score = self.create_text(230, 20, text=f"Score: {str(score)}", fill = self.color, font = Font(size=15))
        if self.tick % self.cooldown == 0:
            Bar(500, random.randint(50, 450), self.speed, self.color, self)
            self.blocks -= 1
        
class Bar(Obj):
    def __init__(self, x, y, sped, color, canv):
        self.stopped = False
        self.sped = sped
        self.col = color
        super(). __init__(x, y, 50, 50, canv)
    def onclick(self):
        if (not self.stopped):
            self.canv.destroyed += 1
        self.stopped = True 
        Effect(self.y, self.canv)
        global score
        score += 1
        self.kys()
    def draw(self):
        bord = self.canv.create_rectangle(self.x, self.y, self.x + self.l, self.y + self.w, fill=self.col)
        self.parts.append(bord)
    def update(self):
        if (self.stopped):
            return
        self.move(-1 * self.sped, 0)
        if (self.x < 0):
            self.stopped = True
            self.canv.over = True


class Effect(Obj):
    def __init__(self, y, canv):
        self.stopped = False
        self.speed = 10
        self.color = colors[0]
        super().__init__(-500, y, 500, 50, canv)
    def update(self):
        if (self.stopped):
            return
        self.color = random.choice(colors)
        for i in self.parts:
            self.canv.itemconfig(i, fill=self.color)
        self.speed *= 1.25
        self.move(self.speed, 0)
        if (self.x > 1000):
            self.stopped = True
            

menu = tkinter.Menu(root)
menu.add_command(label="End", command = root.destroy)
root.config(menu=menu)

game = Rhythm(root)
root.mainloop()