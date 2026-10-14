class Hero:
    def __init__(self, name: str, power: int):
        self.name = name
        self.health = 100
        self.power = power
    
    def attack(self) -> int:
        return self.power

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

# TODO: Implement the Warrior and Mage classes

class Warrior(Hero):

    @property
    def attack(self):
        return self.power + 10

class Mage(Hero):
    def __init__(self,name, power):
        super().__init__(name,power)
        self.health = 80
        
    @property
    def attack(self):
        return self.power + 20
# TODO: Implement the battle function


def show_attack(hero):
    print(f"{hero.name} attacks with {hero.attack} damage!")


# Do not modify the following code
warrior = Warrior("Bob", 20)
mage = Mage("Alice", 15)

show_attack(warrior)  
show_attack(mage)    
