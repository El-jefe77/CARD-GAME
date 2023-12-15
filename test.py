import pygame
from sys import exit

#initialize pygame
pygame.init()
#creation of empty tab and size selection 
screen = pygame.display.set_mode((1080,800))
pygame.display.set_caption("Card game")

#set frame rate for an even speed across devices 
clock = pygame.time.Clock()              

#functions that help to close the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
