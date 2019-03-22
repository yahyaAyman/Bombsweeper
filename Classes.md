# Bombsweeper Classes, and Functions 

| Class | Class Description |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Observable.py |  Includes all classes to be observed 
| Observer.py | An object that wishes to be notified when the board changes states. 
| board.py | Generates a board with the given rows and columns 
| Tile.py | Generates a tile which is a cell in a grid
| Start menu GUI.py | Generates the view to display the board

## Classes 

## Board Class

- The Board class is used to keep track of the grid and and change the state of the game. 
- The Board class randomly assigns each Tile a bomb and counts the amount of bombs in the perimeter of each Tile.
- The class also performs clicks and sets the clicked attribute of the Tile to true if it is clicked.

### Board's Functions 

| Function | Function Definitoin |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `generate_bombs()` | randolmly assigns certain tiles a bomb. |
| `click_tile`<br>`(row, column)` | recursively clicks each tile which does not have a bomb in its perimeter, starting from the given Tile. |
| `count_bomb_perimeter()` | Checks the amount of bombs around the perimeter for each Tile, and accordingly sets the Tile's attribute. 
| `defuse_tile`<br>`(row, column)` | Creates a flag on a tile, which makes the Tile unclickable. |
