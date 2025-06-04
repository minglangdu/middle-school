import tkinter
"""
Working as a standalone game engine
of sorts, this module does difficult
work in the background, such as
garbage collection of deleted objects
while the main modules are able to
handle less work.
This is built less for the computer
fair and more for use in other games.
"""
class Game(tkinter.Canvas):
    def __init__(self, length, width, root):
        super().__init__(width=length, height=width)
        self.over = False
        self.root = root # root use for special scenarios
        self.pack() # draw self onto the root
        self.x = 0 # get the x and y of the mouse
        self.y = 0
        self.bind_all('<Button-1>', self.onclick)
        self.bind_all('<Motion>', self.store)
        self.bind_all('<Key>', self.onkey)
        self.buttons = []
        self.objs = []
        self.dest = [] # items marked for deletion
        self.tick = 0
        self.length = length
        self.width = width
        if __name__ == "__main__":
            self.init()
            self.after(1, self.update)
        
    def init(self): # testing
        def f():
            print("asdf")
        b = Button(100, 100, 75, 75, self, "print(\"asdf\")", f)
        self.buttons.append(b)
        c = Obj(300, 300, 75, 75, self)
        self.objs.append(c)
        
    def onclick(self, _):
        for b in self.buttons:
            if (b.c_point(self.x, self.y)):
                b.func()
                return
        for obj in self.objs:
            if (obj.c_point(self.x, self.y)):
                obj.onclick()
                return
    
    def onkey(self, e):
        key = e.keysym
        for obj in self.objs:
            if not obj:
                continue
            obj.onkey(key)
    
    def store(self, e):
        self.x = e.x
        self.y = e.y
        
    def cust(self):
        pass # custom updates
        
    def update(self):
        if (self.over):
            return
        self.cust()
        if self.tick % 10 == 0:
            for obj in self.objs:
                if obj:
                    obj.update()
            for b in self.buttons:
                b.update()
        for i in range(len(self.objs)):
            if i >= len(self.objs):
                break
            if self.objs[i] in self.dest: # garbage collection algorithm which mitigates objects
                del self.objs[i]
        self.tick = (self.tick + 1) % 100000 # refresh every 100 seconds
        self.after(1, self.update)
        
class Obj: # the base class for all things drawn on canvas
    def __init__(self, x, y, length, width, canv, pack=True, inv = False):
        self.inv = inv
        self.x = x
        self.y = y
        self.l = length
        self.w = width
        self.canv = canv
        self.stop = False
        self.parts = []
        self.coll = False
        self.enem = False
        self.attr = []
        if pack:
            self.draw()
            self.canv.objs.append(self)
        
    def onclick(self):
        pass
        
    def c_point(self, x, y):
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.l
        y2 = self.y + self.w
        return (x >= x1 and x <= x2) and (y >= y1 and y <= y2)
    
    def c_rect(self, o):
        if not o:
            return False
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.l
        y2 = self.y + self.w
        ox1 = o.x
        oy1 = o.y
        ox2 = o.x + o.l
        oy2 = o.y + o.w
        return (min(ox2, x2) - max(ox1, x1) >= 0) and (min(oy2, y2) - max(oy1, y1) >= 0)
        
    def draw(self):
        bord = None
        if (self.inv):
            bord = self.canv.create_rectangle(self.x, self.y, self.x + self.l, self.y + self.w, fill="white", outline = "white")
        else:
            bord = self.canv.create_rectangle(self.x, self.y, self.x + self.l, self.y + self.w, fill="black")
        self.parts.append(bord)
        
    def move(self, x, y):
        if self.canv.over:
            return
        for i in self.parts:
            self.canv.move(i, x, y)
        self.x += x
        self.y += y
            
    def update(self):
        pass
    
    def onkey(self, key):
        pass
    
    def kys(self):
        for i in self.parts:
            self.canv.delete(i)
        self.canv.dest.append(self)
        self.ondeath()
        self.stop = True
    def ondeath(self):
        pass
    
class Button(Obj): # an example of an inheriting class of object
    def __init__(self, x, y, length, width, canv, text, func):
        self.func = func
        self.text = text
        self.isenem = False
        super(). __init__(x, y, length, width, canv)
    def draw(self):
        bord = self.canv.create_rectangle(self.x, self.y, self.x + self.l, self.y + self.w, fill="cyan")
        self.parts.append(bord)
        txt = self.canv.create_text(self.x + self.l / 2, self.y + self.w / 2, text=self.text)
        self.parts.append(txt)

if __name__ == "__main__": # run if not in module
    root = tkinter.Tk()
    game = Game(500, 500, root)
    root.mainloop()