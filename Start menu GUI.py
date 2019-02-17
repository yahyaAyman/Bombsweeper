<<<<<<< HEAD
import pygame
from pygame import *
from pygame.locals import *
from tkinter import Tk, Button
import os

height_window = 700
width_window = 700
##origin = Tk()

window = pygame.display.set_mode((width_window,height_window))
pygame.display.set_caption ("BombSweeper")
background = pygame.image.load("bomb.jpg")
background= pygame.transform.scale(background, (750,750))
window.fill((242,27,27))
window.blit(background, (0,0))
def temp_method():
    print("ouch!!")

##beginner_button = Button(origin, text = "Beginner Level", command = temp_method)
##intermediate_button = Button(origin,text = "Intermediate Level", command= temp_method)
##professional_button = Button(origin,text = "Professional Level", command = temp_method)
##beginner_button.pack()
##intermediate_button.pack()
##professional_button.pack()
##origin.mainloop()


class Button:
    """This class is used to create the buttons and display them for the menu"""
    def __init__(self,color, x,y,width,height, text):
        self.color = color
        self.x = x
        self.y= y
        self.width = width
        self.height = height
        self.text = text
        

##    def addRect(self):
##        font_style = pygame.font.SysFont(None,40)
##        button_text = font_style.render(self.text, True, (0xff,0xff,0xff))
##        pygame.draw.rect(window,self.color, (self.x, self.y, self.width, self.height), 20)

def messageStyle(text, textFont, textSize, textColor):
    set_font = pygame.font.Font(textFont, textSize)
    message = set_font.render(text,1,textColor)
    return message

def main_menu():
    checker = True
    start = "Start"

    while checker:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                checker = False
                quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if "Start" == start:
                        print("Start Game")
                    elif start == "quit":
                        pygame.quit()
                        checker = False
                        quit()
                        
##    window.fill((20,20,95))
        title = messageStyle("Start Game", "Retro.ttf", 90, (89,200,150))
        if start =="Start":
            start_message = messageStyle("Start Game" , "Retro.ttf",80, (98,32,200))
        else:
            start_message = messageStyle("Start Game", "Retro.ttf", 70, (0,255,22))
        if start == "quit":
            quitting = messageStyle("Quit", "Retro.ttf", 80, (98,32,200))
        else:
            quitting = messageStyle("Quit", "Retro.ttf", 70, (0,255,22))

        title_place = title.get_rect()
        start_place =start_message.get_rect()
        quit_place = quitting.get_rect()

    #adds the text to the menu option

    window.blit(title, (width_window- height_window)//2, 80)
    window.blit( start_message, (width_window- height_window)//2, 300)
    window.blit( quitting, (width_window- height_window)//2, 370)
    pygame.display.flip()

   
##def repaint():
##    color = (255,30,90)
##    beginner = Button(color, 100,100,100,100, "Beginner")
##    intermediate = Button(color, 20,20,90,90, "Intermediate")
##    professional = Button(color, 80,80,100,100, "Professional")
##    window.fill((0,0,250))
##    beginner.addRect()


    
def main():
    pygame.init() ##Initializes the pygame module
##    repaint()
##    window.draw.text("Hello World", (100,100) , color = (200,200,200), background = ("gray"))
    pygame.display.update()
    pygame.display.flip()
    running = True
    main_col = (0,0,0)
    difficutly = (114,111,117)
    font = pygame.font.SysFont("arialblack", 20)
    game_name = font.render ("BombSweepr", 1 , main_col)
    options = font.render("Choose Game difficulty" ,1, main_col)
    beginner = font.render("Beginner", 1, difficutly)
    intermediate = font.render("Intermediate", 1,difficutly)
    professional = font.render("Professional", 1, difficutly)
    quit_game = font.render("Quit", 1, main_col)
##    newline = font.render("\n", 1, None)
    window.blit(game_name, (100,50))
    window.blit(options, (100,100))
    window.blit(beginner,(120,150))
    window.blit(intermediate, (120,180))
    window.blit(professional, (120,210))
    window.blit(quit_game, (100, 300))

##    word_lst = [beginner,newline,  intermediate, newline,professional]
##    window.blit(intermediate,(200,200))


##    for word in word_lst:
##        window.blit(word, (100,100))
        
    pygame.display.flip()    
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                return exit()
##            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: ##The one just check the left click nothing too special
##                if pygame.mouse.get_pos == beginner_button:
##                    beginner_button.press() #this calls the temp method that is associated with the beginner button
##                    







if __name__ == '__main__':
    main()
    main_menu()
=======
import pygame
from pygame import *
from pygame.locals import *
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
>>>>>>> GUIwindow
