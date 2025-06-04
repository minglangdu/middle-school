import tkinter as tk
import random
from tkinter.font import Font

# base class for all objects that can be updated in the canvas
class Obj:
    def __init__(self, x, y, length, width, canv, draw = True):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.canv = canv
        self.parts = []
        self.stopped = False
        self.canv.objs.append(self) # allow Obj to be discoverable by parent canvas
        if draw:
            self.draw()
    def draw(self):
        # when canv draws, an id is created for the part drawn.
        # this stores that id in an array "parts"
        self.parts.append(self.canv.create_rectangle(self.x, self.y, self.x + self.length, self.y + self.width, fill="black"))
        
    def update(self):
        pass # intentionally left blank

    def move(self, x, y):
        # update canvas location of parts and internal location
        for p in self.parts:
            self.canv.move(p, x, y)
        self.x += x
        self.y += y
    
    def c_point(self, x, y):
        # checks if a point is inside the object. Useful for buttons
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.length
        y2 = self.y + self.width
        return (x >= x1 and x <= x2) and (y >= y1 and y <= y2)
    
    def c_rect(self, o):
        # checks if another objects is inside the object. Useful for checking hits
        if not o:
            return False
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.length
        y2 = self.y + self.width
        ox1 = o.x
        oy1 = o.y
        ox2 = o.x + o.length
        oy2 = o.y + o.width
        return (min(ox2, x2) - max(ox1, x1) >= 0) and (min(oy2, y2) - max(oy1, y1) >= 0)

class Unit(Obj):
    # base class for all combatants
    def __init__(self, x, y, canv, attr):
        self.isunit = True # so that units don't try to attack other objects
        # various attributes to distinguish units
        self.speed = attr["speed"]
        self.damage = attr["damage"]
        self.crit = attr["crit"] # chance for critical hit out of 100
        self.health = attr["health"]
        self.cd = attr["cooldown"]
        self.cost = attr["cost"]
        # attack cooldown
        self.cooldown = self.cd
        # dead units float into the sky like in the original Battle Cats
        self.dead = False
        self.checkhit = Obj(x, y, 35, 35, canv, draw = False) # use its collision detection to check for hits
        # unit attacks forwards or backwards depending on alignment
        if (self.issquare):
            self.checkhit.move(-15, 0)
        else:
            self.checkhit.move(15, 0)
        # call parent Obj constructor
        super().__init__(x, y, 35, 35, canv)
        
    def move(self, x, y):
        # same as move but checkhit is also moved
        for p in self.parts:
            self.canv.move(p, x, y)
        self.x += x
        self.y += y
        try:
            self.checkhit.move(x, y)
        except:
            pass
        
    def draw(self): # default square is drawn
        self.parts.append(self.canv.create_rectangle(self.x, self.y, self.x + self.length, self.y + self.width, fill="white"))
        
    def update(self):
        # delete loose ends if no longer used
        if (self.stopped):
            try:
                del self.checkhit
            except:
                pass
            return
        # float into sky if dead
        if (self.dead):
            self.move(0, -5)
            for part in self.parts:
                self.canv.itemconfig(part, fill="gray")
            if (self.y < -100):
                self.stopped = True
            return
        # check if dead
        if (self.health <= 0):
            self.dead = True
        # stand in place to hit
        if (self.hit()):
            return
        # move towards the opponent's base
        if (self.issquare):
            self.move(-1 * self.speed, 0)
        else:
            self.move(self.speed, 0)
    
    def hit(self):
        # check if cooldown is past yet
        if (self.cooldown > 0):
            self.cooldown = max(self.cooldown - 1, 0)
            return True # stay in place to try to keep hitting
        cur = self.damage # current damage
        num = random.randint(1, 100)
        crithit = False
        if num <= self.crit: # critical hit check
            crithit = True
            cur *= 2
        # check if an object is hit
        for obj in self.canv.objs:
            if (obj == self):
                continue
            try:
                if (type(obj) == ""):
                    continue
                if (not obj.stopped and obj.issquare != self.issquare):
                    if (self.checkhit.c_rect(obj)):
                        self.cooldown = self.cd
                        obj.health -= cur
                        obj.flash() # flash red to show damage
                        if (crithit): # show critical hit message
                            Crit(self.x, self.y, self.canv, self.issquare)
                        return True
            except Exception as e:
                pass
        
        if ((self.issquare and self.x < 50) or (not self.issquare and self.x > 420)):
            # damage other base
            self.cooldown = self.cd 
            if (self.issquare):
                self.canv.other -= cur
            else:
                self.canv.hp -= cur
            self.canv.after(50, self.forw)
            # show damage
            self.canv.showdamage(self.issquare)
            if (crithit):
                Crit(self.x, self.y, self.canv, self.issquare)
            return True
        
        return False
        
    def forw(self):
        # move forward to show it is attacking
        if (self.issquare):
            self.move(-10, 0)
        else:
            self.move(10, 0)
        self.canv.after(150, self.back)
        
    def back(self):
        # reset and go backwards
        if (self.issquare):
            self.move(10, 0)
        else:
            self.move(-10, 0)
            
    def flash(self):
        # flash red to show damage
        self.canv.itemconfig(self.parts[0], fill = "red")
        self.canv.after(150, self.unflash)
        
    def unflash(self):
        # reset
        self.canv.itemconfig(self.parts[0], fill = "white")
        
# the following is self-explanatory - several units and their attributes

class Square(Unit):
    def __init__(self, x, y, canv, attr = {"speed":1, "damage":20, "crit":30,
                                           "health":150, "cooldown":15, "cost":100}):
        self.issquare = True
        super().__init__(x, y, canv, attr)
        
class Tank(Square):
    def __init__(self, x, y, canv, attr={"speed":0.5, "damage":25, "crit":40,
                                         "health":230, "cooldown":20, "cost":150}):
        super().__init__(x, y, canv, attr)
        
    def draw(self):
        self.parts.append(self.canv.create_rectangle(self.x - 15, self.y - 15, self.x + self.length, self.y + self.width, fill="green"))
    
    def unflash(self):
        self.canv.itemconfig(self.parts[0], fill = "green")
        
# heals squares around it
class Heal(Square):
    def __init__(self, x, y, canv, attr={"speed":0.5, "damage":0, "crit":0,
                                         "health":1, "cooldown":100, "cost":150}):
        super().__init__(x, y, canv, attr)
        
    def draw(self):
        self.parts.append(self.canv.create_rectangle(self.x + 15, self.y + 15, self.x + self.length, self.y + self.width, fill="yellow"))
    
    def unflash(self):
        self.canv.itemconfig(self.parts[0], fill = "yellow")
        
    # custom update to allow healing
    def update(self):
        # delete loose ends if no longer used
        if (self.stopped):
            try:
                del self.checkhit
            except:
                pass
            return
        # float into sky if dead
        if (self.dead):
            self.move(0, -5)
            for part in self.parts:
                self.canv.itemconfig(part, fill="gray")
            if (self.y < -100):
                self.stopped = True
            return
        # check if dead
        if (self.health <= 0):
            self.dead = True
        # change: instead of attacking, heal squares
        if (self.cooldown > 0):
            self.cooldown = max(self.cooldown - 1, 0)
        for obj in self.canv.objs:
            if (obj == self):
                continue
            try:
                if (type(obj) == ""):
                    continue
                if (not obj.stopped and obj.issquare == self.issquare):
                    if (abs(obj.x - self.x) < 15):
                        self.cooldown = self.cd
                        obj.health += 5
                        print("Heal square healed square!")
                        return
            except Exception as e:
                pass
        # move towards the opponent's base
        if (self.issquare):
            self.move(-1 * self.speed, 0)
        else:
            self.move(self.speed, 0)
    
class Circle(Unit):
    def __init__(self, x, y, canv):
        attr = {
            "speed":2,
            "damage":6,
            "crit":50,
            "health":160,
            "cooldown":15,
            "cost":75
        }
        self.issquare = False
        super().__init__(x, y, canv, attr)
    def draw(self):
        self.parts.append(self.canv.create_oval(self.x, self.y, self.x + self.length, self.y + self.width, fill = "blue"))
        
    def unflash(self):
        self.canv.itemconfig(self.parts[0], fill = "blue")

class Oval(Unit):
    def __init__(self, x, y, canv):
        attr = {
            "speed":3,
            "damage":10,
            "crit":0,
            "health":20,
            "cooldown":12,
            "cost":15
        }
        self.issquare = False
        super().__init__(x, y, canv, attr)
    def draw(self):
        self.parts.append(self.canv.create_oval(self.x, self.y, self.x + self.length, self.y + self.width / 2, fill = "cyan"))

    def unflash(self):
        self.canv.itemconfig(self.parts[0], fill = "cyan")
        
class Rectangle(Unit):
    def __init__(self, x, y, canv):
        attr = {
            "speed":0.7,
            "damage":15,
            "crit":75,
            "health":100,
            "cooldown":15,
            "cost":175
        }
        self.issquare = False
        super().__init__(x, y, canv, attr)
        
    def draw(self):
        self.parts.append(self.canv.create_rectangle(self.x, self.y - 30, self.x + self.length, self.y + self.width, fill="orange"))
    
    def unflash(self):
        self.canv.itemconfig(self.parts[0], fill = "orange")
        
class Triangle(Unit):
    def __init__(self, x, y, canv):
        attr = {
            "speed":5,
            "damage":200,
            "crit":0,
            "health":30,
            "cooldown":6,
            "cost":10
        }
        self.issquare = False
        super().__init__(x, y, canv, attr)
        
    def draw(self):
        self.parts.append(self.canv.create_polygon(self.x + self.length / 2, self.y, self.x, self.y + self.width, self.x + self.length, self.y + self.width, fill = "purple"))

    def unflash(self):
        self.canv.itemconfig(self.parts[0], fill = "purple")

class Boss(Unit):
    def __init__(self, x, y, canv):
        attr = {
            "speed":0.8,
            "damage":200,
            "crit":0,
            "health":3500,
            "cooldown":6,
            "cost":10
        }
        self.issquare = False
        super().__init__(x, y, canv, attr)
        
    def draw(self):
        self.parts.append(self.canv.create_polygon(self.x + self.length / 2, self.y, self.x, self.y + self.width, self.x + self.length, self.y + self.width, fill = "purple"))

    def unflash(self):
        self.canv.itemconfig(self.parts[0], fill = "yellow")
# critical hit message

class Crit(Obj):
    def __init__(self, x, y, canv, issquare):
        self.issquare = issquare
        super().__init__(x, y, 0, 0, canv)
        self.speed = -7

    def update(self):
        if (self.stopped):
            return
        # moves up at decreasing speeds
        self.speed = self.speed / (1.2)
        self.move(0, self.speed)
        if (self.speed > -0.2):
            self.move(0, -500)
            self.stopped = True
            return
        
    def draw(self):
        if self.issquare:
            self.parts.append(self.canv.create_text(self.x, self.y, text = "CRITICAL HIT", font = Font(size = 10), fill = "green"))
        else:
            self.parts.append(self.canv.create_text(self.x, self.y, text = "CRITICAL HIT", font = Font(size = 10), fill = "red"))