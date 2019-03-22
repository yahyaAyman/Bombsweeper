# Bombsweeper Classes, and Functions 

| Class | Class Description |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Start menu GUI.py | Generates the view to display the board
| Observable.py |  Includes all classes to be observed 
| Observer.py | An object that wishes to be notified when the board changes states. 
| board.py | Generates a board with the given rows and columns 
| Tile.py | Generates a tile which is a cell in a grid


## Classes 

## Start Menu Class
- `View` contains all the python source code that is responsible for updating of the game view on the start menu and the game while being played


| Functions | Function Definition |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| main(self) | Starts the game by notifying the view to update itself |
|  playGame(self, difficulty)  | Generates the apropriate update of the game to notify the update method |
| update(self, game_board) | Updates the view of the game as the player interacts with the menu or the game |

## Board Class

- The Board class is used to keep track of the grid and and change the state of the game. 
- The Board class randomly assigns each Tile a bomb and counts the amount of bombs in the perimeter of each Tile.
- The class also performs clicks and sets the clicked attribute of the Tile to true if it is clicked.
### Board's Variables
| Variable | Variable Definition |
|:---------------------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `row` | The amount of rows in the grid |
| `column` | The amount of columns in the grid |
| `grid` | The grid includes column * row Tiles|

### Board's Functions 

| Function | Function Definition |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `generate_bombs()` | randolmly assigns certain tiles a bomb. |
| `click_tile`<br>`(row, column)` | recursively clicks each tile which does not have a bomb in its perimeter, starting from the given Tile. |
| `count_bomb_perimeter()` | Checks the amount of bombs around the perimeter for each Tile, and accordingly sets the Tile's attribute. 
| `defuse_tile`<br>`(row, column)` | Creates a flag on a tile, which makes the Tile unclickable. |

## Tile Class
### Tile's Variables
| Variable | Variable Definition |
|:---------------------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` bomb ` | True if the tile is a bomb, False if it is not a bomb. |
| ` defused ` | True if the tile is a bomb and is defused, False otherwise. |
| ` clicked ` | True if thes tile has been clicked on, False otherwise. |
| ` bomb_num ` | Represents the number of bombs around the tile. |
### Tile's Functions
| Function | Function Definition |
|:--------------------------------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `get_bomb(self)` | Returns whether the tile is a bomb or not. |
| `set_bomb(self, is_bomb) ` | Sets whether the tile is a bomb or not. |
| `get_defused(self)` | Returns whether the tile has been defused or not. |
| `set_defused(self, is_defused)` | Sets whether the tile has been defused or not. |
| `get_clicked(self)` | Returns whether the tile has been clicked or not. |
| `get_bomb_num(self)` | Returns the number of bombs around the tile. |
| `set_bomb_num(self, bomb_num)` | Sets the number of bombs around the tile. |
| `click(self)` | Sets whether the tile has been click or not. |
