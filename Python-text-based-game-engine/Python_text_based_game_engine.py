import sys
import os
from BoardGame import Board, Character,Item

def main():
    sword = Item.Item('wooden sword','wooden flying sword of flying pony from hell','this shit is amazing',30)
    sword.attributes[Item.Attributes.defense] = 12
    print (sword.attributes)
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))
