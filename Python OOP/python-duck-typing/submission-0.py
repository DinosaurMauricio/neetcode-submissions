class SpiderMan:
    def attack(self) -> str:
        return "Web Shooter!"
    
    def defend(self) -> str:
        return "Spider Sense!"

# TODO: Create the BlackWidow class with attack() and defend() methods

class BlackWidow:
    def attack(self):
        return "Widow's Bite!"

    def defend(self):
        return "Acrobatic Dodge!"



def battle_sequence(obj):

    print(obj.attack())
    print(obj.defend())


# TODO: Create the battle_sequence() function



# Don't modify the code below
spider_man = SpiderMan()
black_widow = BlackWidow()

battle_sequence(spider_man)
battle_sequence(black_widow)
