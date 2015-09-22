import sys
import os
from BoardGame import Board, Character,Item, Furniture

def main():
    tutorial_char = Character.Character('dummy')
    tutorial_map = Board.Board(4,4)
    tutorial_tile = Board.Tile('tile1')    
    table = Furniture.Furniture('t1','table','this is a fucking table')
    stairs = Furniture.Stair('s1','stairs','this is a fucking stair',1)


    tutorial_tile.objects.append(table)
    tutorial_tile.objects.append(stairs)
    tutorial_map.board[0][0] = tutorial_tile

    
    print(stairs.destination)

if __name__ == "__main__":
    sys.exit(int(main() or 0))
