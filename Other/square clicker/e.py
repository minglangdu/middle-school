"""
Square Clicker:
a shameless Cookie Clicker clone
by Minglang

"""
import tkinter
import pickle
from tkinter.font import Font
import os
import time

root = tkinter.Tk()
root.title("Square Clicker by Minglang Du")
# fix farms
effects = []
types = []
dat = {"score":0, "rates":[],\
       "amts":[], "costs":[],\
       "used":[], "clickp":1}

class Upgrades(tkinter.Canvas):
    def __init__(self, root):
        global dat
        global effects
        super().__init__(width = 500, height = 500)
        self.pack()
        self.root = root
        self.bind_all('<Button-1>', self.onclick)
        self.bind_all('<Motion>', self.store) # store mouse motion
        self.x = 0
        self.y = 0
        self.buttons = {}
        
        self.costs = []
        self.builds = 0
        self.types = []
        
        self.init()
        
    def init(self):
        global dat
        back = Button(375, 0, 125, 75, "Exit")
        back.draw(self)
        self.buttons["exit"] = back
        self.upgrade(0, " Doubled\n Programmer", "prog1", 5000, """dat['rates'][1] *= 2""")
        self.upgrade(1, " Better\n Farms", "farm1", 10000, "dat['rates'][2] *= 2")
        self.upgrade(2, " Superclick", "auto1", 2500, """dat['rates'][0] *= 2
dat['clickp'] *= 2""")
        self.upgrade(3, " Hyperclick", "auto2", 25000, """dat['rates'][0] *= 4
dat['clickp'] *= 4""")
        self.upgrade(4, " Mass\n Production", "fact1", 50000, "dat['rates'][4] *= 4")
        self.upgrade(5, " Child\n Labor", "fact2", 75000, "dat['rates'][4] *= 8")
        self.upgrade(6, " Super\n Hyperclick", "auto3", 250000, """dat['rates'][0] *= 8
dat['clickp'] *= 8""")
        self.upgrade(7, " Hyper\n Hyperclick", "auto4", 2500000, """dat['rates'][0] *= 16
dat['clickp'] *= 16""")
        
        self.score = self.create_text(100, 10, fill='black', text=str(dat["score"]), \
                                      font=Font(size=15))
        self.after(1, self.update)
    def update(self):
        global dat, effects
        self.itemconfig(self.score, text=str(dat["score"]))
        i = 0
        for b in self.buttons.keys():
            if b == "exit":
                continue
            if self.itemcget(self.buttons[b].border, "fill") == "black":
                continue
            if dat["score"] < self.costs[i] or dat["used"][i] == True:
                self.itemconfig(self.buttons[b].border, fill="gray")
            else:
                self.itemconfig(self.buttons[b].border, fill="white")
            
            i += 1
        
        self.after(1, self.update)
    
    def upgrade(self, id, name, idname, cost, effect): # effect is a function
        global dat, effects
        amt = 3
        x = id % amt
        y = id // amt
        u = Button(25 + x * 85, 25 + y * 85, 75, 75, name)
        u.draw(self)
        self.buttons[idname] = u
        self.costs.append(cost)
        effects.append(effect)
        self.types.append(idname)
        self.builds += 1
        if len(dat["used"]) <= id:
            dat["used"].append(False)
    def onclick(self, event):
        global dat
        if self.buttons["exit"].check(self.x, self.y):
            self.destroy()
            game = Game(self.root)
        for i in range(self.builds):
            if self.buttons[self.types[i]].check(self.x, self.y):
                if dat["score"] >= self.costs[i] and dat["used"][i] == False:
                    dat["used"][i] = True
                    self.flash(self.buttons[self.types[i]])
                    dat["score"] -= self.costs[i]
                    exec(effects[i])
                    with open("save.squarefile", "wb") as save:
                        pickle.dump(dat, save)
    def store(self, e):
        self.x = e.x
        self.y = e.y
    def flash(self, e):
        b = e.border
        t = e.text
        self.itemconfig(b, fill="black")
        self.itemconfig(t, fill="white")
        self.after(75, self.resetb)
    def resetb(self):
        for e in self.buttons.values():
            b = e.border
            t = e.text
            self.itemconfig(b, fill="white")
            self.itemconfig(t, fill="black")

class Game(tkinter.Canvas):
    def __init__(self, root):
        super().__init__(width = 500, height = 500)
        self.pack()
        self.root = root
        self.bind_all('<Button-1>', self.onclick)
        self.bind_all('<Motion>', self.store) # store mouse motion
        self.x = 0
        self.y = 0
        self.buttons = {}
        self.cps = 0
        self.init()
        self.after(1, self.update)
    def update(self):
        global dat, types
        self.itemconfig(self.score, text=str(dat["score"]))
        self.itemconfig(self.cpsd, text=("CpS: " + str(self.cps)))
        self.itemconfig(self.clickp, text=("Click Power: " + str(dat["clickp"])))
        while len(dat["amts"]) < len(types):
            dat["amts"].append(0)
        while len(dat["costs"]) < len(types):
            dat["costs"].append(1e9)
        while len(dat["rates"]) < len(types):
            dat["rates"].append(0)
        for i in range(len(types)):
            b = types[i]
            if self.itemcget(self.buttons[b].border, "fill") == "black":
                continue
            if dat["score"] < dat["costs"][i]:
                self.itemconfig(self.buttons[b].border, fill="gray")
            else:
                self.itemconfig(self.buttons[b].border, fill="white")
        
        self.after(1, self.update)
        
    def flash(self, e):
        b = e.border
        t = e.text
        self.itemconfig(b, fill="black")
        self.itemconfig(t, fill="white")
        self.after(75, self.resetb)
    
    def onclick(self, event):
        global dat, types
        if self.buttons["square"].check(self.x, self.y):
            dat["score"] += dat["clickp"]
            self.flash(self.buttons["square"])
        for i in range(len(types)):
            if self.buttons[types[i]].check(self.x, self.y):
                if dat["score"] >= dat["costs"][i]:
                    dat["amts"][i] += 1
                    self.flash(self.buttons[types[i]])
                    dat["score"] -= dat["costs"][i]
                    dat["costs"][i] = round(dat["costs"][i] * 11/10)
        if self.buttons["upgrade"].check(self.x, self.y):
            self.destroy()
            game = Upgrades(self.root)
        
    def resetb(self):
        for e in self.buttons.values():
            b = e.border
            t = e.text
            self.itemconfig(b, fill="white")
            self.itemconfig(t, fill="black")
        
    def persec(self):
        global dat, types
        c = 0
        for i in range(len(types)):
            dat["score"] += dat["amts"][i] * dat["rates"][i]
            c += dat["amts"][i] * dat["rates"][i]
        self.cps = c
        
        self.after(1000, self.persec)
        with open("save.squarefile", "wb") as save:
            pickle.dump(dat, save)
    
    def store(self, e):
        self.x = e.x
        self.y = e.y
        
    def building(self, id, name, idname, cost, rate):
        global dat, types
        y = id % 6
        x = id // 6
        build = Button(175 + 150*x, 10 + 50*y, 150, 50, name)
        build.draw(self)
        self.buttons[idname] = build
        types.append(idname)
        dat["rates"].append(rate)
        dat["costs"].append(cost)
        dat["amts"].append(0)
        
    def init(self):
        global dat, types
        types = []
        self.building(0, "Autoclicker", "auto", 15, 1)
        self.building(1, "Programmer", "prog", 100, 10)
        self.building(2, "Farm", "farm", 1100, 30)
        self.building(3, "Mine", "mine", 2520, 75)
        self.building(4, "Factory", "fact", 10000, 176)
        self.building(5, "Bank", "bank", 120000, 589)
        self.building(6, "Temple", "temp", 540000, 1555)
        self.building(7, "Tower", "towr", 1000000, 5743)
        self.building(8, "Rocket", "rock", 3500000, 10953)
        self.building(9, "Lab", "alch", 8700000, 29532)
        self.building(10, "Portal", "port", 12500000, 46352)
        self.building(11, "Prism", "pris", 55500000, 100000)
        
        square = Button(50, 75, 100, 100, "SQUARE")
        square.draw(self)
        upgrade = Button(25, 300, 125, 75, "Upgrade")
        upgrade.draw(self)
        self.buttons["upgrade"] = upgrade
        self.buttons["square"] = square
        if not os.path.isfile('save.squarefile'):
            with open("save.squarefile", "wb") as save:
                pickle.dump(dat, save)
        else:
            with open("save.squarefile", "rb") as save:
                dat = pickle.load(save)
        self.score = self.create_text(100, 10, fill='black', text=str(dat["score"]), \
                                      font=Font(size=15))
        self.cpsd = self.create_text(100, 35, fill='black', text=("CpS: " + str(self.cps)), \
                                      font=Font(size=10))
        self.clickp = self.create_text(100, 60, fill='black', text=("Click Power: " + str(dat["clickp"])), \
                                      font=Font(size=10))
        self.after(1000, self.persec)
        self.after(1, self.update)
        
        
class Button: # not normal tkinter button
    def __init__(self, x, y, width, height, text):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height
        self.text = text
    def draw(self, canvas):
        x = self.x1
        y = self.y1
        self.border = canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="white", outline="black", tag='button')
        self.text = canvas.create_text((x + self.x2) / 2, (y + self.y2) / 2, fill='black', text=self.text, tag='button', font=Font(size=10))
    def check(self, x, y):
        if self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            return True
        return False

game = Game(root)
root.mainloop()

