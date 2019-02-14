import pygame
from pygame.locals import *
##from tkinter import *
##from tkinter import Menu
##
##class Button:
##    def __init__(self,name):
##        self.name = name
##        tk = tkinter()
##        #creating screen area for buttons
##        self.screen.grid(row = 0, coloumn = 0, columnspan=4, padx=5, pady=5)
##        self.screen.configure(state='normal')
##
##        # create buttons using method createButtone by the tkinter module
##    def createButton(name:str)->"BUTTON":
##        return tk.createButton(name)


def main():

    #Instantiating the size and the pygame module
    pygame.init()
    height_window = 700
    width_window = 700
    window = pygame.display.set_mode((width_window,height_window))
    pygame.display.set_caption ("BombSweeper")


    background = pygame.Surface(window.get_size())
    backgroud = background.convert()
    background.fill((0,250,0))

##    window.blit(background,(0,0))
##    col1 = (255,255,255)
##    col2 = (0,220,0)
##    newfont = pygame.font.SysFont("monospace",20)
##    beginner = newfont.render("Beginner", True,col1,col2)
##    intermediate = newfont.render("Intermediate", True,col1,col2)
##    professional = newfont.render("Professional",True,col1,col2)


##    beginner_rect = beginner.get_rect()
##    beginner_rect.center = (width_window//2,height_window/2)
##    intermediate_rect = intermediate.get_rect()
##    intermediate_rect.center = ((width_window+20)//2, (height_window +20)//2)
##    professional_rect = professional.get_rect()
##    professional_rect.center = ((width_window+40)//2, (height_window + 40)//2)
##    
##    window.blit(beginner, (100,100))
    
##    b1 = self.createButton("Beginner")
##    b2 = self.createButton("Intermediate")
##    
##
##    buttons = [b1,b2,b3]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type ==QUIT:
                running = False
                pygame.quit()
                
                return exit()
     
        
            window.blit(background, (0,0))
            pygame.display.flip()
            pygame.display.update()
        




if __name__ == '__main__':
    main()

