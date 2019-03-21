"Class which represents the tile that will be on the board."

class Tile:
    """ A tile on the Bombsweeper board.

    Attributes:

    @param Boolean bomb: True if this tile is a bomb, False if it is not a bomb.
    @param Boolean defused: True if this tile is a bomb and is defused, False otherwise.
    @param Boolean clicked: True if this tile has been clicked on, False otherwise.
    @param int bomb_num: Represents the number of bombs around this tile.

    """
    def __init__(self, bomb, bomb_num, defused = False, clicked = False):
        self.bomb = bomb
        self.defused = defused
        self.clicked = clicked
        self.bomb_num = bomb_num
        self.position_x = 0
        self.position_y = 0

    """ Returns whether this tile is a bomb or not."""
    def get_bomb(self):
        return self.bomb

    """ Sets whether this tile is a bomb or not."""
    def set_bomb(self, is_bomb):
        self.bomb = is_bomb

    """Returns whether this tile has been defused or not."""
    def get_defused(self):
        return self.defused

    """Sets whether this tile has been defused or not."""
    def set_defused(self, is_defused):
        self.defused = is_defused

    """Returns whether this tile has been clicked or not."""
    def get_clicked(self):
        return self.clicked

    """Returns the number of bombs around this tile."""
    def get_bomb_num(self):
        return self.bomb_num

    """Sets the number of bombs around this tile."""
    def set_bomb_num(self, bomb_num):
        self.bomb_num = bomb_num

    """Sets whether this tile has been click or not."""
    def click(self):
        if self.clicked:
            self.clicked = False
        else:
            self.clicked = True
