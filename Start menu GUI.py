import pygame
from pygame import *
from tkinter import Tk, Button
import os

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
    difficutly = (114,111,117)
    main_options_font = pygame.font.SysFont("arialblack", 25)
    font = pygame.font.SysFont("arialblack", 18)
    game_name = main_options_font.render ("BombSweepr", 1 , main_col)
    options = main_options_font.render("Choose Game difficulty" ,1, main_col)
    beginner = font.render("Beginner", 1, difficutly)
    intermediate = font.render("Intermediate", 1,difficutly)
    professional = font.render("Professional", 1, difficutly)
    quit_game = main_options_font.render("Quit", 1, main_col)

    ##Setting up text position on window
    window.blit(game_name, (100,50))
    window.blit(options, options_pos)
##    window.blit(beginner,beginner_pos)
##    window.blit(intermediate,intermediate_pos )
##    window.blit(professional,  professional_pos)
    window.blit(quit_game, quit_pos)

    ##putting all the text on window together
    pygame.display.flip()

    ##game loop
    while play:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                return exit()
            
            if event.type ==  pygame.MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()
                print(str(mouseX) + " and " + str(mouseY))
                print(str(beginner_pos[0]) +" and "+ str(beginner_pos[1]))
                if (mouseX >= (options_pos[0] and 120) )and (mouseY <= (options_pos[1] and 400)):
                    window.blit(background,(0,0))
                    window.blit(options, options_pos)
                    window.blit(beginner,beginner_pos)
                    window.blit(intermediate,intermediate_pos )
                    window.blit(professional,  professional_pos)
                    pygame.display.flip()






if __name__ == '__main__':
    main()
