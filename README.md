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
