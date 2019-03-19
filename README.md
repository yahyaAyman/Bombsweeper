# Bombsweeper

How to Play:

Bombsweeper contains the same rules as the classic minesweeper game.  The objective of the game is to clear all the non bomb tiles from the board so only the tiles containing a bomb remain.

To uncover a tile, simply click on it.  Once a tile is clicked on, one of three things will happen: 
1. The tile uncovers a number.  The number is a visual repersentation of the amount of bombs within a one block radius of the clicked tile.
2. The tile uncovers a blank spot.  If a blank spot is uncovered all adjacent blank spots and numbers are also uncovered.
3. The tile uncovers a bomb.  If a bomb is uncovered then the player loses the game.

The flag button allows the user to place a flag on tiles that they know to be a bomb.  A tile with a flag is unclickable to avoid accidental clicks.  If you made a mistake you can unflag a tile to make it clickable again by using the flag button again.

The game finishes and the player wins if the only remaining tiles on the board contain bombs.

Tips: 

Use the flag button to flag tiles that you know are bombs.

If a tile is labled "1" and there is already a tile within the radius that is known to be a bomb, then all the others are safe and can be clicked.

If a tile contains a number "n" and there are only "n" remaining covered tiles within the radius, then all tile can be flagged and counted as a bomb.

# Installation
For Windows:
1. Download Python 3.6 [here](https://www.python.org/downloads/release/python-368/)
2. Pick the appropriate version for your PC and install it. Make sure the "Add python 3.6 to PATH" option selected so so that pip will work for you from the command line.
3. Type this in command line:
'''

py -m pip install -U pygame --user

'''
4. To verify that pygame works, try running the included game:
'''

python3 -m pygame.examples.aliens

'''

For Mac:
1. Download Python 3.6 [here](https://www.python.org/downloads/release/python-368/)
2. Pick the appropriate version for your PC and install it. 
3. Create a virtualenv called 'anenv' and use it:
'''

python3 -m virtualenv anenv
. ./anenv/bin/activate

'''
4. Run this command so the pygame window can get focus.
'''

python -m pip install venvdotapp
venvdotapp
python -m pip install pygame

'''
5. To verify that pygame works, try running the included game:
'''

python -m pygame.examples.aliens

'''

# License

Licensed under [MIT License](https://tasdikrahman.mit-license.org/)
