import pygame, time

#Day 1: Get atleast 1 car, which should be able to move 

#SCREEN
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = (pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))
##################################

#STATE
game = "running"
#############################

#CARS
car_1 = pygame.image.load(r"assets\cars\car_player1.png")

########################

pygame.init()


pygame.display.set_caption("Racing-Game")


screen.blit(car_1, (100,100))

pygame.display.update()

while game == "running":

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = "not running"


        
