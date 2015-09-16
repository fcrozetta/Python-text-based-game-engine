import numpy

class Board(object):
    """Creates a Matrix board"""
    def __init__(self, height,width):
        self.board = numpy.empty(shape=(height,width))

