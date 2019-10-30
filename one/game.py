"""#################################IMPORTS###############################"""
import pygame
from pygame.locals import *

"""##################################VARS################################"""
width, height = 640, 480

"""##################################INIT################################"""
pygame.init()
screen=pygame.display.set_mode((width, height))

# 3 - Load images
player = pygame.image.load("C:/Users/icyst/OneDrive/Pictures/NoreenSundaySchoolPictures/2007Noreen")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player, (100,100))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 
