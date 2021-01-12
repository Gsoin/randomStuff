import pygame, sys
from pygame.locals import *

pygame.init()

#set up the window
DISPLAYSURF = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('Drawing')

#set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

#draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 50), (236, 180), (56, 180), (0, 50)))
pygame.draw.rect(DISPLAYSURF, RED, (400,400,50,25))
pygame.draw.polygon(DISPLAYSURF, BLUE, ((25,75),(76,90),(250,375),(400,25),(60,540)))
pygame.draw.circle(DISPLAYSURF, BLACK, (600,300), 100)


#run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()