"""
Sqares TD 5: Tower Defense with New Ideas
by Minglang

This project aims to implement a recreation
of popular tower defense games now with
several new ideas. This allows it to stay
original.

- Heal squares:
You do not want to pop them, but they can
get into the crossfire. This is used to
encourage players to not use 'bullet hell'
towers. This also solves the problem of lag
from excessive projectiles.
- Click squares:
In order to promote player interaction,
this square is used. It is impervious to
all damage and is undetectable, but can be
destroyed using a simple click of the mouse.
It forces players to pay more attention to
the screen.
- Spawn squares:
They create lesser sqares behind them, meaning
they have to be targeted first. They also split into
two yellow sqares, and serve as a kind of final
boss. They break the repetition of the game.
- Screen shake:
Spices up the gameplay by making risky maneuvers
more intense, capturing the player's attention
as well.
- Diversity:
Sqares can sometimes have differing traits, like
speed, so that the game feels more alive to the
player.
- Garbage collection:
Originally, STD5 was very laggy, with the game
becoming more and more hard to play as time
went on. Now, by deleting all objects not onscreen,
this problem was greatly mitigated. This uses a
list to flag objects for deletion, as directly
deleting them would result in reference errors. 

Pseudocode:
-----------------
create a window using the base module
initialize variables.
draw the map from the map module
create displays for relevant information
create buttons for relevant information
starts mainloop:
    find the player's mouse position
    enable or disable relevant buttons
    if player is clicking:
        place the tower the player selected
        at the stored mouse position
    if wave is on(self.on):
        spawn squares using the map and addons module
        update towers and sqares by moving and shooting them.
-----------------
"""
from base import * # self-made module 1
import tkinter 
import random
from tkinter.font import Font
import sys

# self-made modules
import maps # module 2 needs above code to function
from addons import * # module 3 needs above code to function

class Sqares(Game):
    """
    This class inherits from the Game class (base.py) which inherits from
    tkinter's canvas. It uses the Game class's functionality to regulate
    actions, like towers shooting, and to store information, like money. 
    """
    def __init__(self, length, width, root):
        super().__init__(length, width, root) # runs the Game class's __init__ function
        # the main elements of the game
        self.health = 1e9 # when 0, the game is over
        self.mons = 1e9 # used to buy towers
        self.wav = 1 # indicates player's progress
        # used to create enemies
        self.on = False # False -> placing towers | True -> fighting squares
        self.map = random.choice(maps.ms) # gets a random map from maps.py
        self.wave = None # stores pattern of square colors
        # used to create ui
        self.tow = None # stores tower player selected
        self.shake = 0 # screen shake duration
        # finally create the game.
        self.init() # second phase of initialization
        self.after(1, self.update) # starts internal clock
    
    def init(self):
        self.map.draw(self) # draws a map
        # displays essential variables
        self.score = self.create_text(600, 10, fill='black', text="Wave " + str(self.wav), font=Font(size=15))
        self.lives = self.create_text(600, 30, fill='red', text="♥" + str(self.health), font=Font(size=15))
        self.money = self.create_text(600, 50, fill='green', text="$" + str(self.mons), font=Font(size=15))
        # create features to interact with towers
        self.aaa = self.create_text(100, 515, fill='gray', text=str(self.tow), font=Font(size=15))# name of selected tower
        self.d = self.create_text(200, 555, fill='blue', text="", font=Font(size=15)) # tooltip of tower
        self.c = self.create_text(500, 525, fill='gold', text="", font=Font(size=15)) # cost of tower
        self.b = Button(550, 420, 100, 60, self, "Start", func) 
        self.r = Button(550, 350, 100, 60, self, "Cancel Buy", func2) 
        self.u = Button(100, 625, 100, 50, self, "Upgrade", func3)  
        self.a = Button(300, 625, 100, 50, self, "Deselect", func4) 
        self.s = Button(500, 555, 100, 50, self, "Sell", func5) 
        Tower(515, 105, self, 10, 35, 200, 170, icon=True) # an icon allows someone to select a type of tower.
        TS(655, 105, self, icon=True)
        DG(515, 175, self, icon=True)
        SM(655, 175, self, icon=True)
        # tell game to update buttons when they are pressed
        self.buttons.append(self.b)
        self.buttons.append(self.r)
        self.buttons.append(self.u)
        self.buttons.append(self.a)
        self.buttons.append(self.s)
        # Highlight buttons and towers to new players
        self.create_text(600, 85, fill='black', text="Towers", font=Font(size=15))
        self.create_rectangle(505, 70, 700, 250, width=5)
        self.itemconfig(self.b.parts[0], width=3)
        self.itemconfig(self.b.parts[1], font=Font(size=15))
    
    def cust(self): # custom updates
        # change essential variables
        self.itemconfig(self.score, text="Wave " + str(self.wav))
        self.itemconfig(self.lives, text="♥" + str(self.health))
        self.itemconfig(self.money, text="$" + str(self.mons))
        
        if self.on: # disallow or allow starting a wave based on whether you are in one
            self.itemconfig(self.b.parts[0], fill="light gray") 
        else:
            self.itemconfig(self.b.parts[0], fill="cyan") 
            
        if self.tow: # selecting tower or buying tower?
            self.itemconfig(self.d, text=str(self.tow.desc)) # show tooltip
            self.itemconfig(self.c, text="$" + str(self.tow.price)) # show cost
            
            if self.tow.icon: # disallow or allow based on tower type
                self.itemconfig(self.aaa, text=str(self.tow.name)) # show name
                self.itemconfig(self.r.parts[0], fill="cyan") # allow canceling buy
                self.itemconfig(self.a.parts[0], fill="light gray") # disallow deselecting
                self.itemconfig(self.s.parts[0], fill="light gray") # disallow selling
                self.itemconfig(self.u.parts[0], fill="light gray") # disallow upgrading
                self.itemconfig(self.u.parts[1], text="Upgrade") # remove specific upgrade
            else: 
                self.itemconfig(self.aaa, text=str(self.tow.name) + " | Level " + str(self.tow.lev + 1)) # show name and upgrade
                if self.tow.lev < len(self.tow.upgrc) and self.mons >= self.tow.upgrc[self.tow.lev]: # checks if can upgrade
                    self.itemconfig(self.u.parts[0], fill="cyan") # allow upgrading
                    self.itemconfig(self.u.parts[1], text=self.tow.upgrn[self.tow.lev])
                else:
                    self.itemconfig(self.u.parts[0], fill="light gray") # disallow upgrading
                    self.itemconfig(self.u.parts[1], text="Upgrade") # remove specific upgrade
                self.itemconfig(self.a.parts[0], fill="cyan") # allow deselecting
                self.itemconfig(self.s.parts[0], fill="cyan") # allow selling
                self.itemconfig(self.r.parts[0], fill="light gray") # disallow canceling buy
        else: # not selecting tower or buying tower
            # remove displays
            self.itemconfig(self.aaa, text="")
            self.itemconfig(self.d, text="")
            self.itemconfig(self.c, text="")
            # disable buttons
            self.itemconfig(self.r.parts[0], fill="light gray")
            self.itemconfig(self.u.parts[0], fill="light gray")
            self.itemconfig(self.a.parts[0], fill="light gray")
            self.itemconfig(self.s.parts[0], fill="light gray")
        
        # game end scenarios
        if (self.health <= 0): 
            self.create_rectangle(0, 0, 700, 700, fill="black") # fill screen
            self.create_text(350, 250, fill='red', text="GAME OVER", font=Font(size=50)) # show game over 
            self.after(10000, sys.exit) # quit after a delay
        if self.on and self.tick % 500 == 0: # runs every 500 millisecond if fighting sqares.
            if (self.wave == "end"): # end of game?
                self.create_rectangle(0, 0, 700, 700, fill="light green") # fill screen
                self.create_text(350, 250, fill='blue', text="YOU WON", \
                                      font=Font(size=50)) # show game won
                self.after(10000, sys.exit) # quit after a delay
                return
            
            if (not self.wave or len(self.wave) < 1): # end of wave?
                self.on = False # no longer fighting sqares
                self.wav += 1 # next wave
                return
            a = self.wave.pop() # get sqare to spawn
            # conditionals to spawn sqares
            if (a == "red"):
                Red(23, 0, self)
            elif (a == "blue"):
                Blue(23, 0, self)
            elif (a == "green"):
                Green(23, 0, self)
            elif (a == "yellow"):
                Yellow(23, 0, self)
            elif (a == "heal"):
                Heal(23, 0, self)
            elif (a == "click"):
                Click(23, 0, self)
            elif (a == "boss"):
                Boss(23, 0, self)
        # screen shake
        if (self.shake > 1):
            x = random.randint(675, 725)
            y = random.randint(675, 725)
            self.root.geometry(str(x) + "x" + str(y)) # change screen size
            self.shake -= 1 # remove timer
        elif (self.shake == 1):
            self.root.geometry("700x700") # reset size
            
    def onkey(self, e): # give keyboard input
        key = e.keysym # key pressed
        for obj in self.objs: # relay info to objects
            if not obj:
                continue
            obj.onkey(key)
            
    def onclick(self, _): # give mouse input
        for b in self.buttons: # relay info to buttons
            if (b.c_point(self.x, self.y)):
                b.func(b)
        for obj in self.objs: # relay info to objects
            if (obj and obj.c_point(self.x, self.y)):
                obj.onclick()
        # process of elimination->we are placing towers
        if (self.x >= 500 or self.y >= 500 or not self.tow): # can't place towers 
            return
        # conditional to spawn towers
        if (self.mons >= 170 and self.tow.name == "Tower"):
            Tower(self.x - 20, self.y - 20, self, 10, 35, 200, 170)
            self.mons -= 170
        if (self.mons >= 250 and self.tow.name == "Spike Shooter"):
            TS(self.x - 20, self.y - 20, self)
            self.mons -= 250
        if (self.mons >= 250 and self.tow.name == "Gunner"):
            DG(self.x - 20, self.y - 20, self)
            self.mons -= 250
        if (self.mons >= 950 and self.tow.name == "Super Circle"):
            SM(self.x - 20, self.y - 20, self)
            self.mons -= 950

class Start(Game): # shows the start menu
    def __init__(self, length, width, root):
        super().__init__(length, width, root) # runs the Game class's __init__ function
        self.init() # draws everything
    def init(self):
        self.create_rectangle(0, 0, 700, 700, fill="light gray")
        self.create_text(350, 50, fill='black', text="Sqares TD 5", \
                                      font=Font(size=50))
        self.b = Button(305, 300, 100, 70, self, "Start", self.change) # create a button
        self.t = Button(280, 150, 150, 110, self, "Tutorial", self.tutor1)
        self.buttons.append(self.b)
        self.buttons.append(self.t)
    def change(self):
        self.destroy()
        game = Sqares(700, 700, root)
    
    # tutorial text
    def tutor1(self):
        self.create_rectangle(0, 0, 700, 700, fill="light gray") # clear screen
        self.buttons = [] # stop user from pressing buttons
        self.text = self.create_text(350, 150, fill='green', text="Oh no! Sqares are invading \nyour circular hometown. Here, you want\n to destroy squares that\n appear on the screen. \n Otherwise, you will lose lives.\n When lives reach 0, you lose!", \
                                     font = Font(size=25))
        self.after(5000, self.tutor2)
    def tutor2(self):
        self.itemconfig(self.text, text="To do this, you have to place towers.\nClick on a circle (a tower) in the right sidebar,\nand click on the green grass near the track.")
        self.after(6000, self.tutor3)
    def tutor3(self):
        self.itemconfig(self.text, text="Keep in mind they cannot be placed on brown \nroads or outside. After placing a tower,\n you can press\n the 'start' button in the game sidebar.")
        self.after(6000, self.tutor4)
    def tutor4(self):
        self.itemconfig(self.text, text="I'm going to transport you to the game now. \n Remember these instructions!")
        self.after(3000, self.change)
    def onclick(self, _): # give mouse input
        for b in self.buttons: # relay info to buttons
            if (b.c_point(self.x, self.y)):
                b.func()
    
        
if __name__ == "__main__": # if not imported, run
    root = tkinter.Tk() # tkinter main window
    root.title("Sqares TD by Minglang") 
    game = Start(700, 500, root) # create start menu
    root.mainloop() # main loop
