from enum import Enum

class Interactions(Enum):
    open = 0,
    close = 1,
    climb = 2

class Furniture(object):
    """Create a new generic Furniture"""
    def __init__(self, id,name,description):
        self.id = id # Identification (unique)
        self.name = name # User frinedly name
        self.description = description # user frinedly description of Furniture
        self.isBlocking = False # is this Furniture blocking the player passage?
        self.isOpen = False # is the Furniture Open? Always false for furnitures that cannot be opened
        self.isInteractive = False # can players interact with this furniture?
        self.interactions = []


class Stair(Furniture):
    """Create a Stair"""
    def __init__(self, id, name, description,destination):
        super().__init__(id, name, description)
        self.destination = destination # Where does the player go?
        self.interactions.append(Interactions.climb)
        
        

