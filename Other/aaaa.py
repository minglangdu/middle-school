import tkinter
import time
import math

root = tkinter.Tk()

class Object:
    def __init__(self, x, y, width, height, canvas):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + width
        self.width = width
        self.height = height
        self.canvas = canvas
        self.id = self.draw()
    def within_x(self, x1, x2):
        if self.x1 <= x2 and self.x1 >= x1 or \
           self.x2 <= x2 and self.x2 >= x1 or \
           x1 <= self.x2 and x1 >= self.x1 or \
           x2 <= self.x2 and x2 >= self.x1:
            return True
        return False
    def within_y(self, y1, y2):
        if self.y1 <= y2 and self.y1 >= y1 or \
           self.y2 <= y2 and self.y2 >= y1 or \
           y1 <= self.y2 and y1 >= self.y1 or \
           y2 <= self.y2 and y2 >= self.y1:
            return True
        return False
    def is_overlap(self, x1, y1, x2, y2): # TODO
        if self.within_x(x1, x2) and self.within_y(y1, y2):
            return True
        return False
    def draw(self):
        # placeholder drawer
        return self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = "white")
    def move(self):
        pass
    
    def update(self): # don't touch
        self.move()
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
        

class Player(Object):
    def __init__(self, x, y, width, height, canvas):
        super().__init__(x, y, width, height, canvas)
        self.xvel = 0
        self.yvel = 0
        self.canvas.bind_all('<Key>', self.k)
        self.last = time.time()
        
    def k(self, e):
        a = e.keysym
        if a == "w" and self.yvel >= -2:
            self.yvel -= 1
        if a == "a" and self.xvel >= -2:
            self.xvel -= 1
        if a == "d" and self.xvel <= 2:
            self.xvel += 1
        if a == "s" and self.yvel <= 2:
            self.yvel += 1
    def draw(self):
        return self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = "red")
    def move(self):
        if time.time() - self.last > 0.05:
            self.last = time.time()
            self.xvel *= 0.8
            self.yvel *= 0.8
            self.x1 += self.xvel
            self.y1 += self.yvel
            # check for overlap, then run
            for i in self.canvas.objects.keys():
                if i == "player":
                    continue
                a = self.canvas.objects[i]
                if self.is_overlap(a.x1, a.y1, a.x2, a.y2):
                    if i == "bord1" or i == "bord2":
                        self.xvel *= -1
                    if i == "bord3" or i == "bord4":
                        self.yvel *= -1
                    self.x1 -= self.xvel
                    self.y1 -= self.yvel
                    return
            self.canvas.move(self.id, self.xvel, self.yvel)

class Game(tkinter.Canvas):
    def __init__(self, root):
        super().__init__()
        self.pack()
        self.objects = []
        self.init_objs()
        self.after(1, self.update)
    
    def init_objs(self):
        self.create_rectangle(0, 0, 500, 500, fill = "black")
        obj = Player(100, 150, 10, 10, self)
        
        left = Object(50, 70, 5, 150, self)
        right = Object(210, 70, 5, 50, self)
        top = Object(60, 110, 250, 10, self)
        bottom = Object(60, 250, 250, 10, self)
        self.objects = {"player":obj, "bord1":left, "bord2":right, \
                        "bord3":top, "bord4":bottom}
    
    def update(self):
        for obj in self.objects.values():
            obj.update()
        
        self.after(1, self.update)


if __name__ == "__main__": 
    game = Game(root)
    root.mainloop()
