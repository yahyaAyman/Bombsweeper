import pygame
from pygame import *
from tkinter import Tk, Button
import os
import sys

height_window = 700
width_window = 700
##origin = Tk()

window = pygame.display.set_mode((width_window,height_window))
pygame.display.set_caption ("BombSweeper")
background = pygame.image.load("bomb.jpeg")
background= pygame.transform.scale(background, (750,750))
window.blit(background, (0,0))
options_pos = (100,100)
beginner_pos = (120,150)
intermediate_pos = (120,180)
professional_pos = (120, 210)
quit_pos = (100, 250)

    
def main():
    pygame.init() ##Initializes the pygame module
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

    ##Setting up text position on window
    window.blit(game_name, (100,50))
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
##                print(str(beginner_pos[0]) +" and "+ str(beginner_pos[1]))
                if (mouseX >= 102 and mouseX <= 419)and (mouseY >=112 and mouseY <= 130):
                    window.blit(background,(0,0))
                    window.blit(options, options_pos)
                    window.blit(beginner,beginner_pos)
                    window.blit(intermediate,intermediate_pos )
                    window.blit(professional,  professional_pos)
                    pygame.display.flip()
                    counter += 1

                if mouseX >= 120 and mouseX <= 206 and counter == 1 and mouseY >= 156 and mouseY <= 168:
                    print("beginner")

                if mouseX >= 120 and mouseX<= 244 and counter == 1 and mouseY >= 187 and mouseY <= 198:
                    print("Intermediate")

                if mouseX>= 120 and mouseX <= 240 and counter == 1 and mouseY >=215 and mouseY <=230:
                    print("Professional")

    

if __name__ == '__main__':
    main()
