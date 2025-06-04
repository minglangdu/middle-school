"""
End-of-Year Challenge

Name: Minglang Du
Class: 8-D14
"""

import tkinter as tk
from tkinter.font import Font

root = tk.Tk()
canv = tk.Canvas(root, height = 500, width = 500)
canv.pack()

class Display:
    def __init__(self, character):
        self.char = character
        self.parts = []
        self.x = 0
        self.y = 0
        
    def show(self, x, y):
        global canv
        if (self.parts):
            for part in self.parts:
                canv.move(part, x - self.x, y - self.y)
        else:
            self.parts.append(canv.create_rectangle(x, y, x + 175, y + 75, fill = "gray"))
            self.parts.append(canv.create_text(x + 85, y + 10, text = self.char.name, font = Font(size=11), fill = "black"))
            self.parts.append(canv.create_text(x + 45, y + 30, text = f"HP ({self.char.current_hit_points}/{self.char.max_hit_points})", font = Font(size=9), fill="red"))
            self.parts.append(canv.create_text(x + 130, y + 30, text = f"STAM {self.char.stamina}", font = Font(size=9), fill = "brown"))
            self.parts.append(canv.create_text(x + 85, y + 60, text = f"{'Active' if self.char.active else 'Inactive'}", font = Font(size=9), fill = ("green" if (self.char.active) else "red")))
            try:
                self.parts.append(canv.create_text(x + 45, y + 45, text = f"MANA ({self.char.current_mana}/{self.char.max_mana})", font = Font(size = 7), fill = "blue"))
                self.parts.append(canv.create_text(x + 130, y + 45, text = f"FOC {self.char.magical_focus}", font = Font(size = 7), fill = "blue"))
            except:
                pass
            
        self.x = x
        self.y = y

class Character:
    def __init__(self, name, hp, stamina):
        self.name = name
        self.max_hit_points = hp
        self.current_hit_points = hp
        self.stamina = stamina
        self.active = True
        self.abilities = []
        self.disp = Display(self)
        
    def display(self, x, y):
        self.disp.show(x, y)
        
    def display_info(self):
        return f"""{self.name}: HP ({self.current_hit_points}/{self.max_hit_points}); STAM {self.stamina}; {'Active' if self.active else 'Inactive'}"""
        
    def take_damage(damage):
        self.current_hit_points = max(self.current_hit_points - damage, 0)
        if (self.current_hit_points == 0 and self.active):
            self.active = False
            print("Defeat")
            
    def apply_healing(healing):
        if (self.active):
            self.current_hit_points = min(self.current_hit_points + healing, self.max_hit_points)
            print(f"""New HP: {self.current_hit_points}""")
            
    def add_ability(self, ability):
        self.abilities.append(ability)
        
    def activate_ability(self, ability_number):
        self.abilities[ability_number].activate()
        
    def activate_abilities(self):
        for i in range(len(self.abilities)):
            self.activate_ability(i)
            
class Mage(Character):
    def __init__(self, name, hp, stamina, max_mana, magical_focus):
        super().__init__(name, hp, stamina)
        self.max_mana = max_mana
        self.current_mana = max_mana
        self.magical_focus = magical_focus
    
    def display_info(self):
        return f"""{self.name}: HP ({self.current_hit_points}/{self.max_hit_points}); STAM {self.stamina}; MANA ({self.current_mana}/{self.max_mana}); FOC {self.magical_focus}; {"Active" if (self.active) else "Inactive"}"""
        
    def attack(self):
        if (self.current_mana < 5):
            print("Not enough mana.")
            return
        print(f"""{self.name} uses {self.magical_focus} to cast a spell.""")
        self.current_mana -= 5
        print(f"""Mana is now at {self.current_mana}/{self.max_mana}""")
        
    def battle_cry(self):
        print("Mage battle cry")
        
class Acolyte(Mage):
    def __init__(self, name, hp, stamina):
        super().__init__(name, hp, stamina, 25, "hemomancy")
        self.training_level = 0
        
    def display_info(self):
        return f"""{self.name}: HP ({self.current_hit_points}/{self.max_hit_points}); STAM {self.stamina}; MANA ({self.current_mana}/{self.max_mana}); TRAIN {self.training_level}; {"Active" if (self.active) else "Inactive"}"""
    
    def train(self):
        self.training_level += 1
        self.max_mana += 5
        print(f"""Training level: {self.training_level}/10; Mana: ({self.current_mana}/{self.max_mana})""")
        if (self.training_level >= 10 and self.__class__ == Acolyte):
            # magical focus already assigned
            self.__class__ = Mage
            print("Acolyte has become a Mage!")
        print(self.display_info())

class Warrior(Character):
    def __init__(self, name, hp, stamina):
        super().__init__(name, hp, stamina)
        
    def attack(self):
        if (self.stamina < 5):
            print("Not enough stamina.")
            return
        print(f"""{self.name} swings a sword. """)
        self.stamina -= 5
        print(f"""Stamina is now at {self.stamina}""")
    
    def battle_cry(self):
        print("Warrior battle cry")
        
class Archer(Character):
    def __init__(self, name, hp, stamina):
        super().__init__(name, hp, stamina)
        
    def attack(self):
        if (self.stamina < 10):
            print("Not enough stamina.")
            return
        print(f"""{self.name} fires an arrow. """)
        self.stamina -= 10
        print(f"""Stamina is now at {self.stamina}""")
    
    def battle_cry(self):
        print("You can't hear the archer's battle cry since it is a stealth archer build")
        
class Ability:
    def __init__(self, name):
        self.name = name
        
    def activate(self):
        pass
    
class Heal(Ability):
    def __init__(self):
        super().__init__("Heal")
        
    def activate(self):
        print("Heal does nothing since that hasn't been implemented yet. ")
        
class Fireball(Ability):
    def __init__(self):
        super().__init__("Fireball")
        
    def activate(self):
        print("Fireball does nothing since that hasn't been implemented yet. ")
        
def simulate_battle(party):
    for char in party.members:
        char.battle_cry()
        char.attack()
        char.activate_abilities()
     
class Party:
    def __init__(self, name, *member):
        self.name = name
        self.members = member
        
    def add(self, *member):
        self.members.extend(member)
        
    def remove(self, membername):
        new = []
        for member in self.members:
            if member.name != membername:
                new.append(member)
        self.members = new
        
    def display_info(self):
        print(f"Info for Party \"{self.name}\":")
        for member in self.members:
            print(member.display_info())
            
    def disp(self, x, y):
        for member in self.members:
            member.display(x, y)
            y += 75
            
    def get(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None
     
party = Party("The Order of the Stick", Mage("Black Mage", 10, 5, 30, "fire"), Warrior("Roy", 20, 10), Archer("Bob", 10, 20), Acolyte("Joe", 10, 5))
party.get("Black Mage").add_ability(Heal())
party.get("Black Mage").add_ability(Fireball())
party.get("Bob").add_ability(Heal())
simulate_battle(party)
for i in range(10):
    party.disp(50, 50)
    canv.after(500, party.get("Joe").train)
party.disp(50, 50)