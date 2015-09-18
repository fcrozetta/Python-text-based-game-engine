from enum import Enum

class Attributes(Enum):
    attack=0
    defense=1
    health=2
    mana=3

class Item(object):
    """Creates Items"""
    def __init__(self, id,title,description='No description',weight=1):
        self.id = id
        self.title = title
        self.description = description
        self.weight = weight
        self.attributes = {}