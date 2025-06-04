import tkinter
from base import *
import math
import random
"""
This module allows for customization on the
game's separate attributes. For example, the
'Bends' module adds a different track for
the sqares and can also customize the types
of sqares that come.
"""



class Map:
    def __init__(self):
        for i in range(len(self.dirs)):
            self.dirs[i][0] *= (1 / max(max(abs(self.dirs[i][1][0]), abs(self.dirs[i][1][1])), 0))
            # compensate for high speed by dividing by the max speed.
        self.pos = ['red', 'blue', 'green', 'yellow', 'heal', 'click'] # possible sqares
    
    def draw(self, canv):
        pass
    
    def upd_aux(self, sq, mult=1): 
        idx = len(self.dirs)
        for i in range(len(self.dirs) - 1, -1, -1):
            if (sq.prog < self.dirs[i][0]):
                idx = i # find the path the sqare is on.
        if (idx >= len(self.dirs)):
            if (not sq.stop):
                sq.canv.health -= 1
            sq.kys()
            sq.stop = True
            sq.canv.shake = 20 # shake screen when leak
        else:
            sq.prog += 1 * mult
            sq.move(self.dirs[idx][1][0] * mult, self.dirs[idx][1][1] * mult)
        return sq.speed * mult
    
    def upd(self, sq, mult=1): # move a sqare forwards
        b = mult * sq.speed # multiplier
        a = math.floor(b)
        sign = b / abs(b)
        for i in range(int(abs(a) / 3)): # move sqare forward a / 3 steps of 3
            self.upd_aux(sq,mult=sign * 3)
        self.upd_aux(sq, mult=sign * abs(b % 1))
            
    def wave(self, w): # generate a wave
        pos = self.pos # possible enemies
        if (w <= 20):
            ans = []
            if (w == 0):
                ans = ['red', ' '] * 5
            elif (w % 10 == 0):
                ans = ['boss']
                for i in range(random.randint(2, 5)):
                    ans.append('')
                ans *= math.ceil(w / 20)
            else:
                for i in range(random.randint(math.ceil(0.5 * w), math.floor(1.5 * w))):
                    ans.append(random.choice(pos))
                    if (random.randint(1, 3) == 3):
                        ans.append('')
            return ans
        else:
            return 'end'
            
            
ms = [] # list of maps

# all maps
class Basic(Map):
    def __init__(self):
        self.dirs = [[412, [0, 0.5]], [888, [0.5, 0]]]
        super().__init__()
    
    def draw(self, canv):
        canv.create_rectangle(0, 0, 500, 500, fill="light green")
        canv.create_rectangle(500, 0, 700, 500, fill='gray')
        canv.create_rectangle(0, 500, 700, 700, fill='beige')
        Road(0, 0, 50, 400, canv)
        Road(0, 400, 500, 450, canv)
    
    
class Bends(Map):
    def __init__(self):
        self.dirs = [[412, [0, 0.5]], [812, [0.5, 0]], [1012, [0, -0.5]], [1088, [0.5, 0]]]
        super().__init__()
    def draw(self, canv):
        canv.create_rectangle(0, 0, 500, 500, fill="light green")
        canv.create_rectangle(500, 0, 700, 500, fill='gray')
        canv.create_rectangle(0, 500, 700, 700, fill='beige')
        Road(0, 0, 50, 400, canv)
        Road(0, 400, 460, 450, canv)
        Road(410, 450, 460, 210, canv)
        Road(460, 210, 500, 250, canv)
        
# sqare path indicator
class Road(Obj):
    def __init__(self, x, y, x2, y2, canv):
        self.isenem = False
        super().__init__(x, y, x2 - x, y2 - y, canv)
    def draw(self):
        a = self.canv.create_rectangle(self.x, self.y, self.x + self.l, self.y + self.w, fill="brown")
        self.parts.append(a)
        
# add maps to potential maps
ms.append(Basic())
ms.append(Bends())