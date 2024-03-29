import pygame
from pygame import *
import os
import math
import sys
from Observer import *
from board import *
from Tile import *
import time
pygame.init()

WIDTH= 58
HEIGHT = 58
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
MARGIN = 10


height_window = 700
width_window = 700


while mixer.music.get_busy():
    time.Clock().tick(10)

window = pygame.display.set_mode((width_window,height_window))
pygame.display.set_caption ("BombSweeper")
background = pygame.image.load("img/bomb.jpeg")
background= pygame.transform.scale(background, (750,750))
window.blit(background, (0,0))
options_pos = (100,100)
beginner_pos = (120,150)
intermediate_pos = (120,180)
professional_pos = (120, 210)
quit_pos = (100, 250)
back_pos = (100,330)
game_name_pos = (100,50)
main_col = (0,0,0)

class View(Observer):    
    def main(self):
         ##Initializes the pygame module
        pygame.display.update()
        pygame.display.flip()
        play = True
        main_col = (0,0,0)
        difficutly_col = (114,111,117)
        main_options_font = pygame.font.SysFont("arialblack", 25)
        font = pygame.font.SysFont("arialblack", 18)
        game_name = main_options_font.render ("BombSweepr", 1 , main_col)
        options = main_options_font.render("Choose Game difficulty" ,1, main_col)
        beginner = font.render("Beginner", 1, difficutly_col)
        intermediate = font.render("Intermediate", 1,difficutly_col)
        professional = font.render("Professional", 1, difficutly_col)
        quit_game = main_options_font.render("Quit", 1, main_col)
        back = main_options_font.render("Back", 1,main_col)

        ##Setting up text position on window
        window.blit(game_name, game_name_pos)
        window.blit(options, options_pos)

        window.blit(quit_game, quit_pos)

        ##putting all the text on window together
        pygame.display.flip()
        counter = 0
        ##game loop
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    sys.exit()
            
                if event.type ==  pygame.MOUSEBUTTONUP:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    print("X: " + str(mouseX) + " and Y:  " + str(mouseY))
                    if (mouseX >= 102 and mouseX <= 419)and (mouseY >=112 and mouseY <= 130) and counter ==0:
                        window.blit(background,(0,0))
                        window.blit(options, options_pos)
                        window.blit(beginner,beginner_pos)
                        window.blit(intermediate,intermediate_pos )
                        window.blit(professional,  professional_pos)
                        window.blit(back, back_pos)
                        pygame.display.flip()
                        counter += 1

                    if mouseX>= 98 and mouseX<= 162 and mouseY >= 260 and mouseY <= 275 and counter ==0:
                        pygame.display.quit()
                        sys.exit()
                    

                    if mouseX >= 120 and mouseX <= 206 and counter == 1 and mouseY >= 156 and mouseY <= 168:
                        difficulty = "Beginner Difficulty"
                        counter +=1
                        return self.playGame(difficulty)
                
                    if mouseX >= 120 and mouseX<= 244 and counter == 1 and mouseY >= 187 and mouseY <= 198:
                        difficulty = "Intermediate Difficulty"
                        counter+=1
                        return self.playGame(difficulty)

                    if mouseX>= 120 and mouseX <= 240 and counter == 1 and mouseY >=215 and mouseY <=230:
                        difficulty = "Professional Difficulty"
                        counter+= 1
                        return self.playGame(difficulty)


                    if mouseX >= 102 and mouseX <=168 and counter ==1 and mouseY >= 340 and mouseY <= 357:
                        window.blit(background,(0,0))
                        window.blit(game_name, game_name_pos)
                        window.blit(options, options_pos)
                        window.blit(quit_game, quit_pos)
                        pygame.display.flip()
                        counter-=1
                                

    def playGame(self, difficulty):
        clock = pygame.time.Clock()
        pygame.display.set_caption(difficulty)

        game_board = Board(10,10)
        game_board.generate_bombs()
        game_board.count_bomb_perimeter()
        game_board.attach(self)
        print(game_board)
        """
        grid = []x
    
        for row in range(10):    
            grid.append([])
            for column in range(10):
                grid[row].append(0)  
        """
        done = False
        window.fill(BLACK)
        for row in range(10):
            for column in range(10):
                pygame.draw.rect(window, WHITE, [(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
        while not done:
            #window.fill(BLACK)
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    done = True  
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    #grid[row][column] = 1
                    game_board.grid[row][column].position_x = pos[1]
                    game_board.grid[row][column].position_y = pos[0]
                    game_board.click_tile(row, column)
                    #print(game_board)
                    print("Click ", pos, "Grid coordinates: ", row, column)

                         
            clock.tick(30)
            pygame.display.flip()
            pygame.display.update()
            
    def update(self, game_board):
        window.fill(BLACK)
        for row in range(10):
            for column in range(10):
                color = WHITE
                if game_board.grid[row][column].get_clicked() and game_board.grid[row][column].get_bomb():
                    color = RED
                    pygame.draw.rect(window, color, [(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
                    #If bomb is clicked, show all other bombs.
                    for row2 in range(10):
                        for column2 in range(10):
                            if game_board.grid[row2][column2].get_bomb():
                                game_board.click_tile(row2, column2)
                    #time.sleep(3)
                    #pygame.quit()
                elif game_board.grid[row][column].get_clicked():
                    color = GREEN
                    pygame.draw.rect(window, color, [(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
                    main_options_font = pygame.font.SysFont("arialblack", 25)
                    options = main_options_font.render( str(game_board.grid[row][column].get_bomb_num()),1, RED)
                    window.blit(options, ((MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN)  )
                else:
                    pygame.draw.rect(window, color, [(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                    
           

if __name__ == '__main__':
    x = View()
    x.main()
