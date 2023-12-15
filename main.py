import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Card game")
clock = pygame.time.Clock()              
    #this helps to keep a constant tick rate, so that the framerate is constant

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #add elements 
    #update everything 
    pygame.display.update()
    clock.tick(60)
        #frames per second maintained 
    #this is an extra comment 