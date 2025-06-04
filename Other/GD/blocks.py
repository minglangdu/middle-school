from base import *
import sys

class Cube(Obj):
    def __init__(self, x, y, canv, mode = "wave"):
        super().__init__(x, y, 50, 50, canv)
        self.dy = 0 # velocity y
        self.touch_ground = False
        self.holding = False
        # modes: cube ship ufo wave
        self.mode = mode
        self.canv.bind_all("<Up>", self.hold)
        self.canv.bind_all("<KeyRelease-Up>", self.stophold)
    def update(self):
        if (self.mode !="wave"):
            self.dy -= 0.1
        self.touch_ground = False
        for i in self.canv.objs: # check if colliding
            if i.coll and self.c_rect(i):
                self.touch_ground = True
        if self.touch_ground:
            self.dy = max(0, self.dy)
        
        if (self.holding and not self.mode == "ufo"):
            self.jump()
        
        
        
        self.move(0, -1 * self.dy)
        for i in self.canv.objs:
            if i is self:
                continue
            if self.c_rect(i):
                if i.enem:
                    print("game over!")
                    self.canv.over = True
                    self.canv.root.quit()
                    sys.exit()
#                     self.canv.restart()
                elif i.coll:
                    self.dy = 0
                    up = 0
                    while (self.c_rect(i)):
                        self.move(0, -1)
                        up += 1
                    if (up >= 30):
                        self.move(0, up)
                    elif (up >= 10):
                        self.move(0, up)
                        print("game over!")
                        self.canv.over = True
                        self.canv.root.quit()
                        sys.exit()
#                        self.canv.restart()
                    self.move(0, 1)
                elif 'jump' in i.attr:
                    self.dy = 6
                
    def hold(self, _):
        self.holding = True
        if (self.mode == "wave"):
            self.jump()
        
    def stophold(self, _):
        self.holding = False
        if (self.mode == "wave"):
            self.dy = -4
    
    def jump(self):
        for i in self.canv.objs:
            if i is self:
                continue
            if self.c_rect(i):
                if 'jumporb' in i.attr:
                    self.dy = 6
        if (self.mode == "cube"):
            if self.touch_ground:
                print("a")
                self.dy = 4
        elif (self.mode == "ship"):
            self.dy = min(self.dy + 0.2, 4)
        elif (self.mode == "ufo"):
            self.dy = 4
        elif (self.mode == "wave"):
            self.dy = 4
    def draw(self):
        bord = self.canv.create_rectangle(self.x, self.y, self.x + self.l, self.y + self.w, fill="green")
        empt = self.canv.create_rectangle(self.x + 5, self.y + 5, self.x + self.l - 5, self.y + self.w - 5,
                                            fill = "light blue")
        insi = self.canv.create_rectangle(self.x + 15, self.y + 15, self.x + self.l - 15, self.y + self.w - 15,
                                          fill = "light green")
        self.parts.append(bord)
        self.parts.append(empt)
        self.parts.append(insi)

class Spike(Obj):
    def __init__(self, x, y, canv):
        super().__init__(x - 10, y - 30, 10, 30, canv)
        self.enem = True
    def update(self):
        self.move(self.canv.speed * -1, 0)
    def draw(self):
        bord = self.canv.create_polygon((self.x - 10, self.y + 40),
                                        (self.x + 40, self.y + 40),
                                        (self.x + 15, self.y - 10))
        self.parts.append(bord)
        if self.canv.hitbox:
            hitbox = self.canv.create_rectangle(self.x, self.y, self.x + 10, \
                                                self.y - 30, outline="red")
            self.parts.append(hitbox)

class Block(Obj):
    def __init__(self, x, y, canv):
        self.canv = canv
        self.x = x
        self.y = y
        self.l = 50
        self.w = 50
        self.parts = []
        self.coll = True
        self.draw()
        self.canv.objs.append(self)
        
    def draw(self):
        a = Obj(self.x, self.y - 50, 50, 50, self.canv)
        a.coll = True
        self.parts.append(a)
        
    def update(self):
        for i in self.parts:
            i.move(-self.canv.speed, 0)
            
    def move(self, x, y = 0):
        for i in self.parts:
            i.move(x, y)
    
    def onkey(self, e):
        pass

class Under(Block):
    def __init__(self, x, y, canv):
        self.enem = False
        self.attr = []
        super().__init__(x, y, canv)
    def update(self):
        self.move(self.x - self.canv.player.x)
    def draw(self):
        a = Obj(self.x, self.y - 50, 50, 50, self.canv, inv = True)
        a.coll = True
        self.parts.append(a)
        
class Jump(Obj): # jump pad
    # btw nice on making it to friday
    # thanks
    def __init__(self, x, y, canv):
        super().__init__(x, y, 50, 10, canv)
        self.attr.append('jump')
        
    def update(self):
        self.move(self.canv.speed * -1, 0)
        
    def draw(self):
        bord = self.canv.create_rectangle(self.x - 20, self.y, self.x + 30, self.y + 10,
                                          fill = "yellow")
        self.parts.append(bord)

class Orb(Obj):
    def __init__(self, x, y, canv):
        super().__init__(x, y, 50, 50, canv)
        self.attr.append('jumporb')
        # btw nice on making it to friday
        # thanksgiving is close
    def update(self):
        self.move(self.canv.speed * -1, 0)
        
    def draw(self):
        bord = self.canv.create_oval(self.x, self.y, self.x + 50, self.y + 50, fill="yellow")
        self.parts.append(bord)
        if self.canv.hitbox:
            hitbox = self.canv.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, outline = "red")
            self.parts.append(hitbox)
