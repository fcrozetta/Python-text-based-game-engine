from enum import Enum
    
class Moods(Enum):
    neutral = 0
    happy = 1
    sad = 2
    angry = 3
    calm = 4
    danger = 5

class Interactions(Enum):
    talk = 0
    shop = 1
    attack = 2
    pickpocket = 3

class Races(Enum):
    human = 0
    elf = 1
    dwarf = 2

class Attributes(enumerate):
    hp = 0
    mp = 1
    attack = 2
    defense = 3
    stamina = 4
    stealth = 5
    charisma = 6


class Character(object):
    """Creates a character. this can be used to create player/NPCs"""
    def __init__(self, id,):
        self.id = id #Identification
        self.isInteractable = False # can someone interact with it?
        self.isAlive = True # is it alive?
        self.possibleInteractions = [] # List of possible interactions with character
        self.mood = Moods.neutral # character's mood
        self.speed = 1; # character movement speed
        self.inventory = Inventory("{character}.inventory".format(character=self.id),12,100) # main inventory, by default: slots = 12, max_wheight = 100 
        
        #verbose and simple...
        self.hp = 100
        self.mp = 100
        self.attack = 100
        self.defense = 100
        self.stamina = 100
        self.stealth = 100
        self.charisma = 50


class Inventory(object):
    """Create inventory"""
    def __init__(self, id,slots,max_weight):
        self.id = id
        self.slots = slots
        self.items = []
        self.max_weight = max_weight
        self.total_weight = 0

    def isFull(self):
        """return true if inventory has no empty slots"""
        if self.items.count == self.slots:
            return True;
        else:
            return False

    def isHeavy(self):
        """returns true if sum of all items's weight > mas_weight of the inventory"""
        if self.total_weight > self.max_weight:
            return True
        else:
            return False

    def add(self,item):
        """Add item into inventory if there is a space left"""
        if not self.isFull():
            try:
                self.total_weight += item.weight
            except  :
                self.total_weight += 1
            self.items.append(item)