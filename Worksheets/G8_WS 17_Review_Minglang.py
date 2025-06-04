# Minglang Du
# 8-D14

"""
Problem 1
"""

class Character:
    def __init__(self, name, hp, stamina):
        self.name = name
        self.max_hit_points = hp
        self.current_hit_points = hp
        self.stamina = stamina
        self.active = True
        self.abilities = []
        
    def display_info(self):
        print(f"{self.name}: HP ({self.current_hit_points}/{self.max_hit_points}); STAM {self.stamina}; {'Active' if self.active else 'Inactive'}")
        
    def take_damage(damage):
        self.current_hit_points = max(self.current_hit_points - damage, 0)
        if (self.current_hit_points == 0 and self.active):
            self.active = False
            print("Defeat")
            
    def apply_healing(healing):
        if (self.active):
            self.current_hit_points = min(self.current_hit_points + healing, self.max_hit_points)
            print(f"New HP: {self.current_hit_points}")
            
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
        print(f"""{self.name}: HP ({self.current_hit_points}/{self.max_hit_points}); STAM {self.stamina}; MANA ({self.current_mana}/{self.max_mana}); FOC {self.magical_focus}; {"Active" if (self.active) else "Inactive"}""")
        
    def attack(self):
        if (self.current_mana < 5):
            print("Not enough mana.")
            return
        print(f"{self.name} uses {self.magical_focus} to cast a spell.")
        self.current_mana -= 5
        print(f"Mana is now at {self.current_mana}/{self.max_mana}")
        
    def battle_cry(self):
        print("Mage battle cry")
        
class Warrior(Character):
    def __init__(self, name, hp, stamina):
        super().__init__(name, hp, stamina)
        
    def attack(self):
        if (self.stamina < 5):
            print("Not enough stamina.")
            return
        print(f"{self.name} swings a sword. ")
        self.stamina -= 5
        print(f"Stamina is now at {self.stamina}")
    
    def battle_cry(self):
        print("Warrior battle cry")
        
class Archer(Character):
    def __init__(self, name, hp, stamina):
        super().__init__(name, hp, stamina)
        
    def attack(self):
        if (self.stamina < 10):
            print("Not enough stamina.")
            return
        print(f"{self.name} fires an arrow. ")
        self.stamina -= 10
        print(f"Stamina is now at {self.stamina}")
    
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
        
def simulate_battle(characters):
    for char in characters:
        char.battle_cry()
        char.attack()
        char.activate_abilities()
        
characters = [Mage("Black Mage", 10, 5, 30, "fire"), Warrior("Roy", 20, 10), Archer("Bob", 10, 20)]
characters[0].add_ability(Heal())
characters[0].add_ability(Fireball())
characters[2].add_ability(Heal())
simulate_battle(characters)