import pygame, time
import car_class
import math, sys

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

#screen = (pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))
#Initalize pygame

pygame.init()

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

text3 = font.render("Fullscreen", True, (0,0,0))
text3_rect = text3.get_rect()
#text3_rect = te

text4 = font.render("Windowed fullscreen", True, (0,0,0))
#startup screen

startup = True

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("League Of Cars (Chinatown) - Startup")


while startup:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = "not running"
            pygame.quit()
            exit()

    screen.fill((240,240,240))
    screen.blit(text, (70,100))
    screen.blit(text2, (70, 150))

    pygame.display.update()
    clock.tick(FPS)
