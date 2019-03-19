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
        for i in range((self.row-1)*(self.column-1)):
            column = random.randint(0, self.column-1)
            row = random.randint(0, self.row-1)
            if not self.grid[row][column].bomb:
                self.grid[row][column].bomb = True;
                
    def click_tile(self, row, column):
        self.grid[row][column]                      #set clicked true for later recursive calls
        if self.grid[row][column].bomb:             #if bomb was clicked
            return -1
        elif self.grid[row][column].bomb_num:       #if labeled tile was clicked
            return self.grid[row][column].bomb_num
        else:                                       #if a blank tile was clicked
            if row == 0:                            #if tile is on top row
                R = (0 , 1)
            elif row == self.row - 1:               #on bottom row
                R = (-1 , 0)
            else:                                   #middle rows
                R = (-1, 0, 1)                      
            if column == 0:                         #leftmost column
                C = (0, 1)                          
            elif column == self.column - 1:         #rightmost column
                C = (-1 , 0)
            else:                                   #middle columns
                C = (-1, 0, 1)
            for i in R:
                for j in C:
                    if not (self.grid[row +i][column + j].bomb or (self.grid[row + i][column + j].bomb_num > 0) or self.grid[row + i][column + j].clicked):
                        click(self, row + i, row + j)
        return 0
    
    def count_bomb_perimeter(self):
        """Check the amount of bombs around the perimeter for each tile
        """
        for i in range(self.row):
            for j in range(self.column):
                count = 0 #represents number of bombs around a given tile
                if i == 0 and j == 0 and not self.grid[i][j].bomb:
                    if self.grid[i][j+1].bomb:
                        count+=1
                    if self.grid[i+1][j+1].bomb:
                        count+=1
                    if self.grid[i+1][j].bomb:
                        count+=1
                    self.grid[i][j].bomb_num = count
                elif j == 0 and i == self.row-1 and not self.grid[i][j].bomb:
                    if self.grid[i-1][j].bomb:
                        count+=1
                    if self.grid[i-1][j+1].bomb:
                        count+=1
                    if self.grid[i][j+1].bomb:
                        count+=1
                    self.grid[i][j].bomb_num = count                    
                elif j == 0 and not self.grid[i][j].bomb:
                    print(str(i) +str(self.row)+" "+ str(j))
                    if self.grid[i][j+1].bomb:
                        count+=1
                    if self.grid[i+1][j+1].bomb:
                        count+=1
                    if self.grid[i+1][j].bomb:
                        count+=1
                    if self.grid[i-1][j].bomb:
                        count+=1
                    if self.grid[i-1][j+1].bomb:
                        count+=1
                    self.grid[i][j].bomb_num = count
                elif j == self.column-1 and i == 0 and not self.grid[i][j].bomb:
                    if self.grid[i][j-1].bomb:
                        count+=1
                    if self.grid[i+1][j-1].bomb:
                        count+=1
                    if self.grid[i+1][j].bomb:
                        count+=1
                    self.grid[i][j].bomb_num = count   
                elif j == self.column-1 and i == self.row-1 and not self.grid[i][j].bomb:
                    if self.grid[i-1][j].bomb:
                        count+=1
                    if self.grid[i-1][j-1].bomb:
                        count+=1
                    if self.grid[i][j-1].bomb:
                        count+=1
                    self.grid[i][j].bomb_num = count                   
                elif j == self.column-1 and not self.grid[i][j].bomb:
                    if self.grid[i][j-1].bomb:
                        count+=1
                    if self.grid[i+1][j].bomb:
                        count+=1
                    if self.grid[i+1][j-1].bomb:
                        count+=1
                    if self.grid[i-1][j].bomb:
                        count+=1
                    if self.grid[i-1][j-1].bomb:
                        count+=1
                    self.grid[i][j].bomb_num = count
                elif i == 0 and not self.grid[i][j].bomb:
                    if self.grid[i][j-1].bomb:
                        count+=1
                    if self.grid[i][j+1].bomb:
                        count+=1
                    if self.grid[i+1][j].bomb:
                        count+=1
                    if self.grid[i+1][j-1].bomb:
                        count+=1
                    if self.grid[i+1][j+1].bomb:
                        count+=1     
                    self.grid[i][j].bomb_num = count
                elif i == self.row-1 and not self.grid[i][j].bomb:
                    if self.grid[i][j-1].bomb:
                        count+=1
                    if self.grid[i][j+1].bomb:
                        count+=1
                    if self.grid[i-1][j].bomb:
                        count+=1
                    if self.grid[i-1][j-1].bomb:
                        count+=1
                    if self.grid[i-1][j+1].bomb:
                        count+=1     
                    self.grid[i][j].bomb_num = count
                elif not self.grid[i][j].bomb:
                    if self.grid[i][j-1].bomb:
                        count+=1
                    if self.grid[i][j+1].bomb:
                        count+=1
                    if self.grid[i+1][j].bomb:
                        count+=1
                    if self.grid[i+1][j-1].bomb:
                        count+=1
                    if self.grid[i+1][j+1].bomb:
                        count+=1     
                    if self.grid[i-1][j].bomb:
                        count+=1
                    if self.grid[i-1][j-1].bomb:
                        count+=1
                    if self.grid[i-1][j+1].bomb:
                        count+=1
                    self.grid[i][j].bomb_num = count 
                    
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
