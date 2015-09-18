import numpy

class Tile(object):
    """create a new Tile for the board"""
    def __init__(self,id,title="tile",description="This is a tile!"):
        self.id = id
        self.title = title
        self.description = description
        self.objects = []
        self.characters = []

class Board(object):
    """Creates a Matrix board"""
    def __init__(self, height,width):
        self.board = numpy.empty(shape=(height,width),dtype=Tile)