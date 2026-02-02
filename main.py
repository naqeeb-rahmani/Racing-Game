import pygame, time
import car_class


#Day 1: Get atleast 1 car, which should be able to move 

#SCREEN
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#screen = (pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),

pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
##################################

#TEST BACKGROUND
bg_test = pygame.image.load(r"assets\tiles\testbana.png")

###################


#STATES
game = "running"
#############################

#CARS

car_1 = car_class.Car(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.image.load(r"assets\cars\car_player1.png")
)

#car_1 = pygame.image.load(r"assets\cars\car_player1.png")

car_1_x = 100
car_1_y = 100

car_speed = 10
 ########################

pygame.init()


pygame.display.set_caption("Racing-Game")



pygame.display.update()

while game == "running":

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_1.car_x > 0:
        car_1.car_x = car_1.car_x - car_1.speed

    if keys[pygame.K_RIGHT] and car_1.car_x < (SCREEN_WIDTH - 64):
        car_1.car_x = car_1.car_x + car_1.speed

    if keys[pygame.K_DOWN] and car_1_y < (SCREEN_HEIGHT - 64):
        car_1.car_y = car_1.car_y + car_1.speed

    if keys[pygame.K_UP] and car_1_y > 0:
        car_1.car_y = car_1.car_y - car_1.speed


    screen.fill((0,0,0,))
    #test

    screen.blit(bg_test, (0,0))

#################
    screen.blit(car_1.sprite, (car_1.car_x, car_1.car_y))


    pygame.display.update()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = "not running"

exit()

        
