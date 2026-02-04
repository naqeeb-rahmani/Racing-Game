import pygame, time
import car_class

#大斯坦制作公司tm
#RTN продакшн

#Day 1: Get atleast 1 car, which should be able to move -done
#Day 2: Create a class for the cars - done
#Day 3: Fix movement - done
#Day 4: Fix collision - work in progress

#SCREEN
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#screen = (pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),

pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
##################################

#TEST BACKGROUND
bg_test = pygame.image.load("base_bana.png")

###################


#STATES
game = "running"
#############################

#CARS

car_1_sprite = pygame.image.load(r"assets\cars\car_1_top.png").convert_alpha()

car_1 = car_class.Car(SCREEN_WIDTH, SCREEN_HEIGHT, car_1_sprite)

#car_1 = pygame.image.load(r"assets\cars\car_player1.png")

car_1_x = 100
car_1_y = 100

car_speed = 10
########################



pygame.display.set_caption("汽车联盟 (Chinatown)")



pygame.display.update()

while game == "running":

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] and car_1.car_y < (SCREEN_HEIGHT - 64):
        #car_1.car_y = car_1.car_y + car_1.speed
        pass

    if keys[pygame.K_UP] and car_1.car_y > 0:
        car_1.movement()
         #car_1.car_y = car_1.car_y - car_1.speed

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: car_1.direction = 1
            if event.key == pygame.K_LEFT: car_1.direction = -1
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT: car_1.direction = 0
            if event.key == pygame.K_LEFT: car_1.direction = 0

        if event.type == pygame.QUIT:
            game = "not running"



    car_1.update()
#    car_1.update()

    screen.fill((0,0,0,))
    #test

    screen.blit(bg_test, (0,0))

#################
    screen.blit(car_1.sprite, car_1.rect)



    pygame.display.update()

    clock.tick(60)

exit()