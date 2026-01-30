import pygame


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#STATE
game = "running"
#############################

pygame.init

screen = (pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))

pygame.display.set_caption("Racing-Game")





while game == "running":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = "not running"


        
