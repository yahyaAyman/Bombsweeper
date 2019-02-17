def click(self, row, column):
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
