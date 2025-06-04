import MS71_Minglang_CF as sqares
from MS71_Minglang_CF import *
import tkinter
from tkinter.font import Font
import random
import math
"""
This module creates 'addons' to existing libraries in
the 'sqares' game. For example, the 'Red' class builds
off of the 'Sqare' class and adds specific attributes,
like its color. 
"""

class Sqare(Obj): # base class for sqares
    def __init__(self, x, y, canv, col, sped, health = 1):
        self.color = col # distinguishing characteristic
        self.prog = 0 # progress in map
        self.isenem = True # is enemy?
        self.targ = False
        self.speed = sped + random.randint(-2, 2) # speed affected by randomness
        self.stop = False # check if stopped
        self.health = health
        super().__init__(x, y, 25, 25, canv) # do object initialization
    def draw(self):
        bord = self.canv.create_rectangle(self.x, self.y, self.x + self.l, self.y + self.w,
                                          fill=self.color)
        self.parts.append(bord) # draw sqare and get id
        
    def update(self):
        if (self.stop): # stop if stopped
            return
        self.canv.map.upd(self, mult=1) # move
   
class Tower(Obj): # base class for towers
    def __init__(self, x, y, canv, freq, sped, rang, price, icon=False):
        self.isenem = False # not enemy
        self.lev = 0 # how many upgrades?
        self.check = False # check upgrades if True
        self.upgrc = [100, 200, 150] # upgrade costs
        self.upgrn = ["Fast shots", "Big range", "Faster shots"] # upgrade names
        self.freq = freq # frequency of firing
        self.speed = sped # speed of projectiles
        self.range = rang # detection radius
        self.price = price # cost of tower
        self.icon = icon # is placed tower or just button
        self.name = "Tower" # tooltip
        self.desc = "A tower. What." # tooltip
        self.targ = None
        super().__init__(x, y, 40, 40, canv) # object initialization
        for obj in self.canv.objs:
            if obj and obj.c_rect(self):
                if obj == self:
                    continue
                # if colliding with object, destroy and refund tower
                self.canv.mons += self.price
                self.kys() 
                break
        
    def draw(self):
        circ = self.canv.create_oval(self.x, self.y, self.x + self.l, self.y + self.w,
                                     fill = "green") 
        self.parts.append(circ) # add tower sprite id
        if self.icon:
            self.canv.create_text(self.x + self.l / 2, self.y + self.w / 2, text="CLICK", fill="red")
        
    def update(self):
        if self.icon: # if button, doesn't do anything
            return
        e = self.targ
        if (self.canv.tick % (self.freq * 50) == 0): # shoots every (self.freq * 50) ticks
            e = None # entity shooting at
            delta = [] # difference betweens xs and ys
            dist = 0 # distance from entity
            # find targets
            if self.targ:
                try:
                    aa = self.targ.prog
                    if self.targ.stop:
                        raise SyntaxError
                except:
                    self.targ = None
            for sq in self.canv.objs:
                if sq and not sq.isenem: # disregard non-enemies
                    continue
                delta = [sq.x - self.x, sq.y - self.y] # get differences between xs and ys
                dist = delta[0] ** 2 + delta[1] ** 2 # use pythagorian theorem 
                if dist > self.range ** 2: # ignore things out of detection range
                    continue
                if e == None or e.prog < sq.prog:
                    if not sq.targ:
                        e = sq # set entity to sqare
                        sq.targ = True
                        self.targ = e
                break
            if e: # if found entity
                self.shoot(e, dist)
        self.upgrades() # check for upgrades
              
    def shoot(self, e, dist):
        a = math.sqrt(dist) / 250 * math.sqrt(self.speed) # amount to move sqare
        self.canv.map.upd(e, mult=a) # move sqare
        delta = [e.x - self.x, e.y - self.y] # get difference of sqare and tower in future
        d0 = delta[0] / max(abs(delta[0]), abs(delta[1])) * self.speed
        # normalize dx and multiply by projectile speed
        d1 = delta[1] / max(abs(delta[0]), abs(delta[1])) * self.speed
        # normalize dy and multiply by projectile speed
        Projectile(self.x, self.y, self.canv, d0, d1) # fire projectile
        self.canv.map.upd(e, mult=-1 * a) # reset sqare
              
    def upgrades(self):
        if (self.check): # if new upgrade check
            if (self.lev == 0):
                self.freq += self.freq / 2
            elif (self.lev == 1):
                self.range += self.range / 2
            elif (self.lev == 2):
                self.freq += self.freq / 1.5
            if (self.lev <= 2):
                self.lev += 1
            self.check = False
                
    def onclick(self):
        self.canv.tow = self
        if self.icon:
            self.icon = False
            self.draw() # remove large 'click' text
            self.icon = True

class Projectile(Obj):
    def __init__(self, x, y, canv, dx, dy):
        self.dx = dx # speed is dx and dy
        self.dy = dy
        self.isenem = False # not enemy
        self.stop = False # not stopped
        super().__init__(x, y, 20, 20, canv) # object initialize
        
    def draw(self):
        circ = self.canv.create_oval(self.x, self.y, self.x + self.l, self.y + self.w,
                                     fill = "gray")
        self.parts.append(circ) # is gray circle
    
    def update(self):
        if (self.canv.tick % 50 == 0): # move every few seconds
            self.move(self.dx, self.dy)
        for i in range(len(self.canv.objs)):
            sq = self.canv.objs[i] # check for collisions
            if (self.stop):
                break
            if (sq and (not sq.isenem) and (not sq.nm == "heal")):
                continue
            if (self.c_rect(sq)):
                if (sq.health <= 1):
                    sq.kys()
                else:
                    sq.health -= 1
                self.kys()# destroy both when hit
                self.canv.mons += 5 # gain money from killing sqares
                self.stop = True
                break
        if (self.x < 0 or self.x > 500 or self.y < 0 or self.y > 500):
            self.kys() # destroy when out of bounds
            self.stop = True

class Red(Sqare):
    def __init__(self, x, y, canv):
        super().__init__(x, y, canv, "red", 10)
class Blue(Sqare):
    def __init__(self, x, y, canv):
        super().__init__(x, y, canv, "blue", 20)
    def ondeath(self):
        a = Red(self.x, self.y, self.canv)
        a.prog = self.prog
        b = Red(self.x, self.y, self.canv)
        b.prog = self.prog
        b.update()
class Green(Sqare):
    def __init__(self, x, y, canv):
        super().__init__(x, y, canv, "green", 15)
    def ondeath(self):
        a = Blue(self.x, self.y, self.canv)
        a.prog = self.prog
        b = Blue(self.x, self.y, self.canv)
        b.prog = self.prog
        b.update()
class Yellow(Sqare):
    def __init__(self, x, y, canv):
        super().__init__(x, y, canv, "yellow", 15)
    def ondeath(self):
        a = Green(self.x, self.y, self.canv)
        a.prog = self.prog
        b = Green(self.x, self.y, self.canv)
        b.prog = self.prog
        b.update()
class Heal(Sqare):
    def __init__(self, x, y, canv):
        super().__init__(x, y, canv, 'light green', 7)
        self.isenem = False
        self.nm = 'heal'
    def ondeath(self):
        ds = self.canv.map.dirs
        if (self.prog < ds[len(ds) - 1][0]):
            self.canv.health -= 10 # didn't reach end yet
        else:
            self.canv.health += 10
    
    def draw(self):
        bord = self.canv.create_rectangle(self.x, self.y, self.x + self.l, self.y + self.w,
                                          fill="blue")
        symbol = self.canv.create_text(self.x + self.l / 2, self.y + self.w / 2, fill='green', text="+", \
                                      font=Font(size=25))
        self.parts.append(bord) # draw sqare and get id
        self.parts.append(symbol)
        
class Click(Sqare):
    def __init__(self, x, y, canv):
        super().__init__(x, y, canv, 'light green', 15)
        self.isenem = False
    def onclick(self):
        self.kys()
    
    def draw(self):
        bord = self.canv.create_rectangle(self.x, self.y, self.x + self.l, self.y + self.w,
                                          fill="pink")
        symbol = self.canv.create_text(self.x + self.l / 2, self.y + self.w / 2, fill='black', text="Click Me", \
                                      font=Font(size=5))
        self.parts.append(bord) # draw sqare and get id
        self.parts.append(symbol)
    
class Boss(Sqare):
    def __init__(self, x, y, canv):
        super().__init__(x, y, canv, 'purple', 10, health = 10)
        self.l *= 2
        self.w *= 2
        self.move(-1/2 * self.l, -1/2 * self.w)
    def draw(self):
        bord = self.canv.create_rectangle(self.x, self.y, self.x + self.l * 2, self.y + self.w * 2,
                                          fill="purple")
        symbol = self.canv.create_text(self.x + self.l, self.y + self.w, fill='red', text="X", \
                                      font=Font(size=15))
        self.parts.append(bord) # draw sqare and get id
        self.parts.append(symbol)
    def update(self):
        if (self.stop): # stop if stopped
            return
        self.canv.map.upd(self, mult=1) # move
        if (self.canv.tick % 250 == 0): # spawn new sqares 
            choice = random.randint(0, 9)
            x = self.x + self.l / 2
            y = self.y + self.w / 2
            if (choice == 0):
                a = Green(x, y, self.canv)
            elif (choice == 1):
                a = Blue(x, y, self.canv)
            elif (choice == 2):
                a = Red(x, y, self.canv)
            elif (choice == 3):
                a = Yellow(x, y, self.canv)
            if choice <= 3:
                a.prog = self.prog
    
    def ondeath(self):
        x = self.x + self.l / 2
        y = self.y + self.w / 2
        a = Yellow(x, y, self.canv)
        a.prog = self.prog
        b = Yellow(x, y, self.canv)
        b.prog = self.prog
        b.update()
    
class BT(Tower):
    def __init__(self, x, y, canv, icon=False):
        super().__init__(x, y, canv, 10, 35, 200, 170, icon=icon)
        self.name = "Basic Tower"
        self.desc = "A cheap tower with inaccurate aim."
        self.upgrc = [100, 200, 150] # upgrade costs
        self.upgrn = ["Fast shots", "Big range", "Faster shots"] # upgrade names
    
    def upgrades(self):
        if (self.check): # if new upgrade check
            if (self.lev == 0):
                self.freq += self.freq / 2
            elif (self.lev == 1):
                self.range += self.range / 2
            elif (self.lev == 2):
                self.freq += self.freq / 1.5
            if (self.lev <= 2):
                self.lev += 1
            self.check = False
        
class TS(Tower):
    def __init__(self, x, y, canv, icon=False):
        super().__init__( x, y, canv, 20, 30, 200, 250, icon=icon)
        self.name = "Spike Shooter"
        self.desc = "Shoots projectiles in all 8 directions!"
        self.upgrc = [100, 200, 150] # upgrade costs
        self.upgrn = ["Huge range", "Speedy spikes", "Faster shots"] # upgrade names
    def upgrades(self):
        if (self.check): # if new upgrade check
            if (self.lev == 0):
                self.range *= 2
            elif (self.lev == 1):
                self.speed += self.speed / 2
            elif (self.lev == 2):
                self.freq += self.freq / 1.5
            if (self.lev <= 2):
                self.lev += 1
            self.check = False
    
    def draw(self):
        circ = self.canv.create_oval(self.x, self.y, self.x + self.l, self.y + self.w,
                                     fill = "pink")
        self.parts.append(circ)
        if self.icon:
            self.canv.create_text(self.x + self.l / 2, self.y + self.w / 2, text="CLICK", fill="red")
            
    def update(self):
        if self.icon:
            return
        e = None
        if (self.canv.tick % (self.freq * 50) == 0):
            e = None
            delta = []
            dist = 0
            for sq in self.canv.objs:
                if not sq:
                    continue
                delta = [sq.x - self.x, sq.y - self.y]
                dist = delta[0] ** 2 + delta[1] ** 2
                if dist > self.range ** 2:
                    continue
                if (sq.isenem):
                    e = sq
                    break
        if e:
            Projectile(self.x, self.y, self.canv, self.speed, 0)
            Projectile(self.x, self.y, self.canv, -1 * self.speed, 0)
            Projectile(self.x, self.y, self.canv, 0, self.speed)
            Projectile(self.x, self.y, self.canv, 0, -1 * self.speed)
            Projectile(self.x, self.y, self.canv, self.speed, self.speed)
            Projectile(self.x, self.y, self.canv, -1 * self.speed, self.speed)
            Projectile(self.x, self.y, self.canv, -1 * self.speed, -1 *self.speed)
            Projectile(self.x, self.y, self.canv, self.speed, -1 *self.speed)
        self.upgrades()
        
class DG(Tower):
    def __init__(self, x, y, canv, icon=False):
        super().__init__( x, y, canv, 5, 35, 200, 250, icon=icon)
        self.name = "Gunner"
        self.desc = "Slowly shoots where you direct it."
        self.upgrc = [100, 200, 150] # upgrade costs
        self.upgrn = ["Sharp shots", "Frequent shots", "Faster shots"] # upgrade names
    def upgrades(self):
        if (self.check): # if new upgrade check
            if (self.lev == 0):
                self.speed += self.speed / 1.2
            elif (self.lev == 1):
                self.freq += self.freq / 2
            elif (self.lev == 2):
                self.freq += self.freq / 1.5
            if (self.lev <= 2):
                self.lev += 1
            self.check = False
        
    def update(self):
        if self.icon:
            return
        if (self.canv.tick % (self.freq * 50) == 0):
            sq = self.canv
            delta = [sq.x - self.x, sq.y - self.y]
            d0 = delta[0] / max(abs(delta[0]), abs(delta[1])) * self.speed
            d1 = delta[1] / max(abs(delta[0]), abs(delta[1])) * self.speed
            Projectile(self.x, self.y, self.canv, d0, d1)
        self.upgrades()
        
    def draw(self):
        circ = self.canv.create_oval(self.x, self.y, self.x + self.l, self.y + self.w,
                                     fill = "cyan")
        self.parts.append(circ)
        if self.icon:
            self.canv.create_text(self.x + self.l / 2, self.y + self.w / 2, text="CLICK", fill="red")
class SM(Tower):
    def __init__(self, x, y, canv, icon=False):
        super().__init__( x, y, canv, 2, 35, 500, 950, icon=icon)
        self.name = "Super Circle"
        self.desc = "The purest form of circle. Nothing can rival it."
        self.upgrc = [1e9] # upgrade costs
        self.upgrn = ["No upgrades"] # upgrade names
    def draw(self):
        circ = self.canv.create_oval(self.x, self.y, self.x + self.l, self.y + self.w,
                                     fill = "red")
        self.parts.append(circ)
        if self.icon:
            self.canv.create_text(self.x + self.l / 2, self.y + self.w / 2, text="CLICK", fill="green")

def func(self): # starts a wave
    self.canv.wave = self.canv.map.wave(self.canv.wav)
    self.canv.on = True
def func2(self): # cancels buying a tower
    if not self.canv.tow or not self.canv.tow.icon:
        return # ends if not buying a tower
    self.canv.tow = None
def func3(self): # upgrades a tower
    if not self.canv.tow or self.canv.tow.icon:
        return # ends if not selecting a placed tower
    if self.canv.tow.lev >= len(self.canv.tow.upgrc):
        return # ends if already full upgraded
    if self.canv.mons >= self.canv.tow.upgrc[self.canv.tow.lev]: # checks if can afford
        self.canv.mons -= self.canv.tow.upgrc[self.canv.tow.lev] # subtracts money
        self.canv.tow.check = True # tells tower to check for upgrades
def func4(self): # deselects a placed tower
    if not self.canv.tow or self.canv.tow.icon:
        return # ends if not selecting a placed tower
    self.canv.tow = None 
def func5(self): # sells a placed tower
    if not self.canv.tow or self.canv.tow.icon:
        return # ends if not selecting a placed tower
    self.canv.tow.kys() # destroys tower
    self.canv.mons += self.canv.tow.price # refunds money
    self.canv.tow = None # deselects tower
