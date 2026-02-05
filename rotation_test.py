
import pygame, time
import car_class
import math

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
#Initalize pygame
pygame.init()

# Disable mouse cursor/visibility
pygame.mouse.set_visible(False)

#setting screen dimensions and full screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.FULLSCREEN)

#clock for locking frames per second
clock = pygame.time.Clock()
FPS = 60
##################################

#TEST MAP
bg_test = pygame.image.load("base_bana.png")

###################

#STATES
game = "running"
#############################

#Create car sprite and car class
car_1_sprite = pygame.image.load(r"assets\cars\car_1_top.png").convert_alpha()
car_1 = car_class.Car(SCREEN_WIDTH, SCREEN_HEIGHT, car_1_sprite)
#car_1 = pygame.image.load(r"assets\cars\car_player1.png")

#Car1 position
car_1_x = 100
car_1_y = 100

#Car1 speed
car_speed = 10
########################

#explosion effects

t_blast_unscaled = pygame.image.load(r"assets\kaboom.png").convert_alpha()
t_blast = pygame. transform. scale(t_blast_unscaled, (int(t_blast_unscaled.get_width() * 0.02), int(t_blast_unscaled.get_height() * 0.02)))


kaboom_sound = pygame.mixer.Sound(r"assets\audio\sfx\yafonoob-oh-no-the-car-exploded-10632.mp3")
exp_sound = False
exp_time = 2000
exp_start = 0
##########################################################33

#Setting display to "汽车联盟 (Chinatown)" == League of Cars (Chinatown)
pygame.display.set_caption("汽车联盟 (Chinatown)")

#Game loop

while game == "running":
#shortcut for pygame.key.get_pressed()
    keys = pygame.key.get_pressed()
#Keybinds 
    if keys[pygame.K_DOWN] and car_1.car_y < (SCREEN_HEIGHT - 64):
        #car_1.car_y = car_1.car_y + car_1.speed
        pass

    car_1_x_int = int((math.cos(car_1.rad) * car_1.speed) + car_1.car_x)
    car_1_y_int = int((math.sin(car_1.rad) * car_1.speed) + car_1.car_y)
    #print(bg_test.get_at((car_1_x_int,car_1_y_int)))


    if keys[pygame.K_UP] and (car_1.car_y < SCREEN_HEIGHT):
        if bg_test.get_at((car_1_x_int,car_1_y_int)) != (255,255,255,255):
            car_1.movement()
         #car_1.car_y = car_1.car_y - car_1.speed

    if bg_test.get_at((car_1_x_int,car_1_y_int)) == (255,255,255,255):
        car_1.explosion = True
    
    #if bg_test.get_at((car_1_x_int,car_1_y_int)) == 
#Car rotation, rotates when key is held down
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: car_1.direction = 1
            if event.key == pygame.K_LEFT: car_1.direction = -1
#Car rotation, stops rotation when let go of key        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT: car_1.direction = 0
            if event.key == pygame.K_LEFT: car_1.direction = 0
#end game
        if event.type == pygame.QUIT:
            game = "not running"
            pygame.quit()
            exit()




    car_1.update()
#    car_1.update()

    blast_rect = t_blast.get_rect(center=car_1.rect.center)

    screen.fill((0,0,0,))
    #test

    screen.blit(bg_test, (0,0))

#################
    if car_1.explosion:
        screen.blit(t_blast, blast_rect)
        if not exp_sound:
            kaboom_sound.play()
            exp_start = pygame.time.get_ticks()
            exp_sound = True
    elif exp_sound != True:
        screen.blit(car_1.sprite, car_1.rect)

    if car_1.explosion == True and exp_sound == True and ((pygame.time.get_ticks() - exp_start) > 2000):
        #spawnar bilen igen, ändrar rotation till korrekt rotation för startpositionen.
        car_1.angle = -90
        car_1.respawn(SCREEN_WIDTH, SCREEN_HEIGHT)
        car_1.explosion = False; exp_sound = False

    pygame.display.update()

    clock.tick(FPS)

exit()