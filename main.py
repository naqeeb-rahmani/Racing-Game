import pygame, time
import car_class
import math, sys
import os

#大斯坦制作公司tm
#RTN продакшн

#Day 1: Get atleast 1 car, which should be able to move -done
#Day 2: Create a class for the cars - done
#Day 3: Fix movement - done
#Day 4: Fix collision - done
#Day 5: Fixed the car so it slows done when driving on the grass and fixing the gui, as well as menu - in progress...

#SCREEN
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

startup = True
menu = False
game = False
game_mode = None

screen_type = None

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Disable mouse cursor/visibility
pygame.mouse.set_visible(True)


clock = pygame.time.Clock()
FPS = 60

#writing function

font = pygame.font.Font(None , 30)

def write_text(text, text_colour, x, y):
    text = font.render(text, True, text_colour)

    screen.blit(text, (x, y))

#startup screen text
font2 = pygame.font.Font(None, 20)
text = font.render("League Of Cars (Chinatown)", True, (0,0,0))

text2 = font2.render("Screen resolution: 1280 x 720", True, (2,2,2))

col_t3 = (0,0,0)
text3 = font.render("Fullscreen", True, col_t3)
text3_rect = text3.get_rect(topleft=(70, 200))

col_t4 = (0,0,0)
text4 = font.render("Windowed fullscreen", True, col_t4)
text4_rect = text4.get_rect(topleft=(70, 250))
#startup screen

startup = True

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("League Of Cars (Chinatown) - Startup")


#############


while startup:
    mouse_pos = pygame.mouse.get_pos()  
    mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)

    if mouse_rect.colliderect(text3_rect):
        col_t3 = (0, 0, 200)
        text3 = font.render("Fullscreen", True, col_t3)
    elif mouse_rect.colliderect(text4_rect):
        col_t4 = (0, 0, 200)
        text4 = font.render("Windowed fullscreen", True, col_t4)
    else:
        col_t3 = (0, 0, 0); col_t4 = (0, 0, 0)
        text3 = font.render("Fullscreen", True, col_t3)
        text4 = font.render("Windowed fullscreen", True, col_t4)



    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_rect.colliderect(text3_rect):
                    screen_type = "Fullscreen"
                    startup = False
                    menu = True
                elif mouse_rect.colliderect(text4_rect):
                    screen_type = "Windowed fullscreen"
                    startup = False
                    menu = True

        if event.type == pygame.QUIT:
            game = "not running"
            pygame.quit()
            exit()

    screen.fill((240,240,240))
    screen.blit(text, (70,100))
    screen.blit(text2, (70, 150))
    screen.blit(text3, (70, 200))
    screen.blit(text4, (70, 250))

    pygame.display.update()
    clock.tick(FPS)

###############################################


if screen_type == "Fullscreen":
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
elif screen_type == "Windowed fullscreen":
    screen = (pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))
pygame.display.set_caption("League Of Cars (Chinatown)")

#loading in map, sprites and other game mechanics
#map
map = pygame.image.load(r"assets\tiles\Base road plus grass.png")

#start/finish line

goal_start = pygame.image.load(r"assets/tiles/goal.png").convert_alpha()
goal_start_rect = goal_start.get_rect()
goal_start_rect.center = (170 // 2, 170 // 2)

second_trig = pygame.image.load(r"assets/tiles/second_trig.png").convert_alpha()
second_trig_rect = second_trig.get_rect()
second_trig_rect.center = (999 + second_trig_rect.width // 2, 320 + second_trig_rect.height // 2)

laps = 0
count_laps = False

#timer
timer_bg = pygame.image.load(r"assets\ui\timer_back.png").convert_alpha()
timer_bg = pygame.transform.scale(timer_bg, (150, 50))
timer_rect = timer_bg.get_rect()
timer_rect.x, timer_rect.y = 100, 625


Timer_x_pos = timer_rect.x
Timer_y_pos = timer_rect.y

font = pygame.font.Font(None , 40)

#Create car sprite and car class
car_1_sprite = pygame.image.load(r"assets\cars\car_1_top.png").convert_alpha()
car_1 = car_class.Car(SCREEN_WIDTH, SCREEN_HEIGHT, car_1_sprite)

#menu texts
font0 = pygame.font.Font(None, 40)
font = pygame.font.Font(None , 30)
font2 = pygame.font.Font(None, 20)

text = font.render("League Of Cars (Chinatown)", True, (0,0,0))

text2 = font2.render("Screen resolution: 1280 x 720", True, (2,2,2))

col_t3 = (0,0,0)
text3 = font.render("Fullscreen", True, col_t3)
text3_rect = text3.get_rect(topleft=(70, 200))

col_t4 = (0,0,0)
text4 = font.render("Windowed fullscreen", True, col_t4)
text4_rect = text4.get_rect(topleft=(70, 250))


#########################


while menu:
    mouse_pos = pygame.mouse.get_pos()  
    mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)

    screen.fill((255,255,255))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = "not running"
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(FPS)

