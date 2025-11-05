class Player():
    def __init__(self,name, level=0, health=100):
        self.name = name
        self.level = level
        self.health = health
    
    def attackPlayer(self):
        pass

    def takeHit(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return self.health
    
    def getStronger(self, lIncrement,hIncrement):
        self.level += lIncrement
        self.health += hIncrement
        if self.health > 100 and self.level >= 10:
            self.health = 100
            self.level = 10
        return (self.level, self.health)
      
    def checkStatus(self):
        return f"Player: {self.name}, Level: {self.level}, Health: {self.health}"
    
class Warrior(Player):
    def __init__(self, name, level, health, rage=0):
        super().__init__(name, level, health)
        self.rage = rage
       
    
    def attackPlayer(self, target, damage, rage_gain):
        self.rage += rage_gain
        target.takeHit(damage)
        return f"{self.name} attacked {target.name} for {damage} damage! Rage is now {self.rage}."
    
    def powerSmach(self, target):
        if self.rage >= 50:
            damage = 50
            self.rage -= 50
            target.takeHit(damage)
            return f"{self.name} performed Power Smash on {target.name} for {damage} damage! Rage is now {self.rage}."
        else:
            return f"{self.name} does not have enough rage to perform Power Smash."
        
    def checkStatus(self):
        base_status = super().checkStatus()
        return f"{base_status}, Rage: {self.rage}"
    
class Mage(Player):
    def __init__(self, name, level, health, mana=100):
        super().__init__(name, level, health)
        self.mana = mana
    
    def castSpell(self, target, spell_damage, spell_mana_cost):
        if self.mana >= spell_mana_cost:
            self.mana -= spell_mana_cost
            target.takeHit(spell_damage)
            return f"{self.name} cast a spell on {target.name} for {spell_damage} damage! Mana is now {self.mana}."
        else:
            return f"{self.name} does not have enough mana to cast the spell."
    
    def checkStatus(self):
        base_status = super().checkStatus()
        return f"{base_status}, Mana: {self.mana}"