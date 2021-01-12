import time
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60 #frames per second
fpsClock = pygame.time.Clock()

#set up the window
DISPLAYSURF = pygame.display.set_mode((550, 550), 0, 32)
pygame.display.set_caption('Animation')


WHITE = (255, 255, 255)
catImg = pygame.image.load("cat.png")
catx = 10
caty = 10
direction = 'diagonal'

soundObj = pygame.mixer.Sound('beeps.wav')
soundObj.play()

time.sleep(1)
soundObj.stop()

#run the game loop
while True:
    DISPLAYSURF.fill(WHITE)
    print(direction)

    if direction == 'diagonal':
        catx += 5
        caty += 5
        
        if catx == 490:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'diagonalleft'
    elif direction == 'diagonalleft':
        catx -= 5
        caty += 5
        if catx == 10:
            direction = 'up1'
    elif direction == 'up1':
        caty -= 5
        print(caty)
        print(catx)
        if caty == 10 and catx == 10:
            direction = 'diagonal'
    
            
    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()