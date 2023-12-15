import pygame
from sys import exit

#initialize pygame
pygame.init()
#creation of empty tab and size of the tab
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Card game")
#set frame rate for an even speed across devices 
clock = pygame.time.Clock()              

#creation of surface for display (primary surface) 
test_surface = pygame.Surface((100, 200))
test_surface.fill("red")

#"while true" will create an infinite loop, meaning it will execute it indefinitely until the program is interrupted or terminated
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#creation of surface on top of another surface
    screen.blit(test_surface,(0,0))


    pygame.display.update()
    clock.tick(60)
