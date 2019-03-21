# Bombsweeper

## How to Play 

Bombsweeper contains the same rules as the classic minesweeper game.  The objective of the game is to clear all the non bomb tiles from the board so only the tiles containing a bomb remain.

To uncover a tile, simply click on it.  Once a tile is clicked on, one of three things will happen: 
1. The tile uncovers a number.  The number is a visual repersentation of the amount of bombs within a one block radius of the clicked tile.
2. The tile uncovers a blank spot.  If a blank spot is uncovered all adjacent blank spots and numbers are also uncovered.
3. The tile uncovers a bomb.  If a bomb is uncovered then the player loses the game.

The flag button allows the user to place a flag on tiles that they know to be a bomb.  A tile with a flag is unclickable to avoid accidental clicks.  If you made a mistake you can unflag a tile to make it clickable again by using the flag button again.

The game finishes and the player wins if the only remaining tiles on the board contain bombs.

## Tips

Use the flag button to flag tiles that you know are bombs.

If a tile is labled "1" and there is already a tile within the radius that is known to be a bomb, then all the others are safe and can be clicked.

If a tile contains a number "n" and there are only "n" remaining covered tiles within the radius, then all tile can be flagged and counted as a bomb.

# Installation
## For Windows:
1. Download Python 3.6 [here](https://www.python.org/downloads/release/python-368/)
2. Pick the appropriate version for your PC and install it. Make sure the "Add python 3.6 to PATH" option selected so so that pip will work for you from the command line.
3. Type this in command line:
```

$ py -m pip install -U pygame --user

```
4. Clone this github repo.
```

$ git clone https://github.com/jangra99/Bombsweeper.git

```
5. Navigate to where you cloned the repo.
6. Go into the src folder and run Start menu GUI.py.
7. Enjoy the game!
## For Mac:
1. Open a command terminal.
2. Install Homebrew and prepare it for use.
```

$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ echo export PATH='/usr/local/bin:$PATH' >> ~/.bash_profile
$ brew update
$ brew doctor

```
3. Install Python 3.
```

$ brew install python3

```
4. Install Mercurial.
```

$ brew install mercurial

```
5. Install all the dependencies for Pygame.
```

$ brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
$ brew tap homebrew/headonly
$ brew install --HEAD smpeg

```
6. Install pygame.
```

$ sudo pip3 install hg+http://bitbucket.org/pygame/pygame

```
7. Clone this github repo.
```

$ git clone https://github.com/jangra99/Bombsweeper.git

```
8. Navigate to where you cloned the repo.
9. Go into the src folder and run Start menu GUI.py.
10. Enjoy the game!
## For Linux:
1. Open a terminal window, then install python by entering the following commands:
```

$ sudo apt-get update
$ sudo apt-get install python3.6

```
2. Install pygame.
```

$ sudo apt-get install python-pygame.

```
3. Clone this github repo.
```

$ git clone https://github.com/jangra99/Bombsweeper.git

```
4. Navigate to where you cloned the repo.
5. Go into the src folder and run Start menu GUI.py.
6. Enjoy the game!
# Authors
Davinder Jangra, Kyle Jang, Yahya Ayman, Daniel Costantino, and Hani Ghasempoor

# License

Licensed under [MIT License](https://tasdikrahman.mit-license.org/)
