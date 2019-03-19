from Tile import * 
import random

class Board:
    """ Generates a board instance which is filled with tile instances 
    """

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.grid = [[Tile(False, 0) for i in range(column)] for j in range(row)]
        
    def generate_bombs(self):
        """ Generates (length-1)*(width-1) bombs randomly in the grid
        """
        for i in range((self.row-1)*(self.column-1) // 5):
            column = random.randint(0, self.column-1)
            row = random.randint(0, self.row-1)
            if not self.grid[row][column].bomb:
                self.grid[row][column].bomb = True;
                
    def click_tile(self, row, column):
        self.grid[row][column].clicked = True #Set clicked true for later recursive calls
        if self.grid[row][column].bomb:             #if bomb was clicked
            return -1
        elif self.grid[row][column].bomb_num:       #if labeled tile was clicked
            return self.grid[row][column].bomb_num
        else :
            R = self.row - 1
            C = self.column -1
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if (0 <= i + row < R) and (0 <= j + column < C) and\
                       (not self.grid[row + i][column + j].clicked or self.grid[row + i][column + j].bomb):
                        self.click_tile(row + i, row + j)
        return 0
    
    def count_bomb_perimeter(self):
        """Check the amount of bombs around the perimeter for each tile
        """
        #inspired by the tutorial
        xdim = self.row
        ydim = self.column
        for i in range(xdim):
            for j in range(ydim):
                count = 0 #represents number of bombs around a given tile
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if (0 <= i + dx < xdim) and (0 <= j + dy < ydim) and self.grid[i+dx][j+dy].bomb:
                            count += 1
                self.grid[i][j].bomb_num = count
                
    def __str__(self):
        for i in range(row):
            for j in range(column):
                print("Row: " + str(i) + ", Column: " + str(j) + ", Has Bomb: " + str(x.grid[i][j].bomb)\
                      + ", Bomb in perimeter: " + str(x.grid[i][j].bomb_num) + ", clicked: " + str (x.grid[i][j].clicked))
        return "board __str__"
                   
if __name__ == '__main__':
    #TESTING PURPOSES
    #edit row and column to make that grid size
    row = 2
    column = 2
    x = Board(row,column) #generate board
    x.generate_bombs() #generate bombs
    x.count_bomb_perimeter() #generate perimeter
    print(x.grid) #print grid which has tiles
    for i in range(row):
        for j in range(column):
            print("Row: " + str(i) + ", Column: " + str(j) + ", Has Bomb: " + str(x.grid[i][j].bomb) + ", Bomb in perimeter: " + str(x.grid[i][j].bomb_num))
