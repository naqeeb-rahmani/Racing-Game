import pygame, time
import car_class
import math, sys
import os

#Day 1: Get atleast 1 car, which should be able to move -done
#Day 2: Create a class for the cars - done
#Day 3: Fix movement - done
#Day 4: Fix collision - done
#Day 5: Fixed the car so it slows done when driving on the grass and fixing the gui, as well as menu - done
#Day 5 (after school): Made a startup menu, then a menu, and now im working on making a local .txt save file


#checking if there is a save file. If not create one
if not os.path.isfile("save.txt"):
    with open("save.txt", "w") as save:
        save.write("9999")


#SCREEN
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

startup = True
menu = False
game = False
menu_choice = None

screen_type = None

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1' #centers the screen if the player chooses windowed screen in the startup menu

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
lap_time = None
lap1_time = 0
lap2_time = 0
lap3_time = 0
lap_nr = 0
count_laps = False

with open("save.txt", "r") as save:
        personal_best = float(save.readline().strip())

#loading in gui (incl lap.png's)
lap_bg = pygame.image.load(r"assets\ui\Lap back.png")
lap_bg = pygame.transform.scale(lap_bg, (50, 50))
lap0 = pygame.image.load(r"assets\ui\lap 0 av 3v1.png")
lap0 = pygame.transform.scale(lap0, (50, 50))
lap1 = pygame.image.load(r"assets\ui\lap 1 av 3v1.png")
lap1 = pygame.transform.scale(lap1, (50, 50))
lap2 = pygame.image.load(r"assets\ui\lap 2 av 3v1.png")
lap2 = pygame.transform.scale(lap2, (50, 50))
lap3 = pygame.image.load(r"assets\ui\lap 3 av 3v1.png")
lap3 = pygame.transform.scale(lap3, (50, 50))


#timer
pb_bg = pygame.image.load(r"assets\ui\timer_back.png").convert_alpha() #pb = personal best
pb_bg = pygame.transform.scale(pb_bg, (200,50))
pb_bg_rect = pb_bg.get_rect()
pb_bg_rect.x, pb_bg_rect.y = 0, 650
timer_bg = pygame.image.load(r"assets\ui\timer_back.png").convert_alpha()
timer_bg = pygame.transform.scale(timer_bg, (200, 50))
timer_rect = timer_bg.get_rect()
timer_rect.x, timer_rect.y = 200, 650

time_running = False

Timer_x_pos = timer_rect.x
Timer_y_pos = timer_rect.y

font = pygame.font.Font(None , 40)

#Create car sprite and car class
car_1_sprite = pygame.image.load(r"assets\cars\car_1_top.png").convert_alpha()
car_1 = car_class.Car(SCREEN_WIDTH, SCREEN_HEIGHT, car_1_sprite)

#menu texts
menu_font0 = pygame.font.Font(None, 40)
menu_font = pygame.font.Font(None , 30)
menu_font2 = pygame.font.Font(None, 35)

menu_text = menu_font0.render("League Of Cars (Chinatown)", True, (0,0,0))

menu_text2 = font.render("Single player (3 laps)", True, (2,2,2))
text2_rect = menu_text2.get_rect(topleft=(100,250))

col_t3 = (0,0,0)
menu_text3 = menu_font.render("Multiplayer (player vs player)", True, col_t3)
text3_rect = menu_text3.get_rect(topleft=(100,300))

col_t4 = (0,0,0)
menu_text4 = menu_font.render("Settings", True, col_t4)
text4_rect = menu_text4.get_rect(topleft=(100, 350))

col_t5 = (0,0,0)
menu_text5 = menu_font.render("Credits", True, col_t5)
text5_rect = menu_text5.get_rect(topleft=(100, 400))

col_t6 = (0,0,0)
menu_text6 = menu_font.render("Quit", True, col_t6)
text6_rect = menu_text6.get_rect(topleft=(100, 450))

#credits text
cred_text1 = menu_font0.render("THE BIG THREE PRODUCTIONS", True, (50,50,50)); ct1_x = 420; ct1_y = 100 

cred_text2 = menu_font2.render("Programmers:", True, (255,0,0)); ct2_x = 550; ct2_y = 160 

cred_text3 = menu_font.render("Tor", True, (0,0,0)); ct3_x = 620; ct3_y = 210 

cred_text4 = menu_font.render("Naqeeb", True, (0,0,0)); ct4_x = 600; ct4_y = 260 

cred_text5 = menu_font.render("Reem", True, (0,0,0)); ct5_x = 610; ct5_y = 310 

cred_text6 = menu_font2.render("Graphic designer:", True, (0,255,0)); ct6_x = 530; ct6_y = 360 

cred_text7 = menu_font.render("Tindra", True, (0,0,0)); ct7_x = 600; ct7_y = 410 

cred_text8 = menu_font2.render("Musician:", True, (0,0,255)); ct8_x = 575; ct8_y = 460 

cred_text9 = menu_font.render("Antero", True, (0,0,0)); ct9_x = 600; ct9_y = 510 

def cred_animation():
    global ct1_y, ct2_y, ct3_y, ct4_y, ct5_y, ct6_y, ct7_y, ct8_y, ct9_y
    ct1_y -= 1; ct2_y -= 1; ct3_y -= 1; ct4_y -= 1; ct5_y -= 1; ct6_y -= 1; ct7_y -= 1; ct8_y -= 1; ct9_y -= 1
    if ct1_y < -20:
        ct1_y = SCREEN_HEIGHT 
    elif ct2_y < -20:
        ct2_y = SCREEN_HEIGHT 
    elif ct3_y < -20:
        ct3_y = SCREEN_HEIGHT
    elif ct4_y < -20:
        ct4_y = SCREEN_HEIGHT
    elif ct5_y < -20:
        ct5_y = SCREEN_HEIGHT
    elif ct6_y < -20:
        ct6_y = SCREEN_HEIGHT
    elif ct7_y < -20:
        ct7_y = SCREEN_HEIGHT
    elif ct8_y < -20:
        ct8_y = SCREEN_HEIGHT
    elif ct9_y < -20:
        ct9_y = SCREEN_HEIGHT




#########################


while menu:
    mouse_pos = pygame.mouse.get_pos()  
    mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
    if menu_choice == None:
        if mouse_rect.colliderect(text2_rect):
            col_t2 = (0, 0, 200)
            menu_text2 = font.render("Single player (3 laps)", True, col_t2)
        elif mouse_rect.colliderect(text3_rect):
            col_t3 = (0, 0, 200)
            menu_text3 = font.render("Multiplayer (player vs player)", True, col_t3)
        elif mouse_rect.colliderect(text4_rect):
            col_t4 = (0, 0, 200)
            menu_text4 = font.render("Settings", True, col_t4)
        elif mouse_rect.colliderect(text5_rect):
            col_t5 = (0, 0, 200)
            menu_text5 = font.render("Credits", True, col_t5)
        elif mouse_rect.colliderect(text6_rect):
            col_t6 = (0, 0, 200)
            menu_text6 = font.render("Quit", True, col_t6)
        else:
            col_t2 = (0,0,0) ;col_t3 = (0, 0, 0); col_t4 = (0, 0, 0); col_t5 = (0,0,0); col_t6 = (0,0,0)
            menu_text2 = font.render("Single player (3 laps)", True, col_t2)
            menu_text3 = font.render("Multiplayer (player vs player)", True, col_t3)
            menu_text4 = font.render("Settings", True, col_t4)
            menu_text5 = font.render("Credits", True, col_t5)
            menu_text6 = font.render("Quit", True, col_t6)


        screen.fill((255,255,255))
        screen.blit(menu_text, (100,100))
        screen.blit(menu_text2, (100,250))
        screen.blit(menu_text3, (100,300))
        screen.blit(menu_text4, (100,350))
        screen.blit(menu_text5, (100,400))
        screen.blit(menu_text6, (100,450))


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse_rect.colliderect(text2_rect):
                        menu_choice = "Single player"
                    elif mouse_rect.colliderect(text3_rect):
                        menu_choice = "Multiplayer"
                    elif mouse_rect.colliderect(text4_rect):
                        menu_choice = "Settings"
                    elif mouse_rect.colliderect(text5_rect):
                        menu_choice = "Credits"

                    elif mouse_rect.colliderect(text6_rect):
                        exit()
                
            if event.type == pygame.QUIT:
                game = "not running"
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(FPS)

    #single player mode
    elif menu_choice == "Single player":
        if time_running == False:
            start_time = pygame.time.get_ticks()
            time_running = True

            #movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and (car_1.car_y < SCREEN_HEIGHT):
            car_1.movement()
        
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

        car_1.slow_grass(map)

        if car_1.rect.colliderect(second_trig_rect):
            count_laps = True

        if car_1.rect.colliderect(goal_start_rect) and count_laps == True:
            lap_time = (pygame.time.get_ticks() - start_time) / 1000
            with open("save.txt", "r") as save:
                personal_best = float(save.readline().strip())
            if lap_time < personal_best:
                with open("save.txt", "w") as save:
                    save.write(str(lap_time))
                personal_best = lap_time
                
                    
            lap_nr += 1
            count_laps = False
            print(lap_nr)
            start_time = pygame.time.get_ticks()
        if time_running == True:
            end_time = pygame.time.get_ticks()
            write_text(f"TIME:{lap_time}", (255,255,255), timer_rect.x + 16, timer_rect.y +13)
        
        elif time_running == False:
            start_time = pygame.time.get_ticks()
            time_running = True
            count_laps = False
    



        screen.fill((0,0,0,))

        screen.blit(map, (0,0))
        screen.blit(second_trig, (999, 320))

        screen.blit(car_1.sprite, car_1.rect)
        screen.blit(goal_start, (53,100))
        screen.blit(lap_bg, (Timer_x_pos + 200, Timer_y_pos))
        if lap_nr == 0:
            screen.blit(lap0,(Timer_x_pos + 200, Timer_y_pos))
        elif lap_nr == 1:
            lap1_time = lap_time
            screen.blit(lap1,(Timer_x_pos + 200, Timer_y_pos))
        elif lap_nr == 2:
            lap2_time = lap_time
            screen.blit(lap2,(Timer_x_pos + 200, Timer_y_pos))
        elif lap_nr == 3:
            lap3_time = lap_time
            screen.blit(lap3,(Timer_x_pos + 200, Timer_y_pos))
        screen.blit(timer_bg, (Timer_x_pos,Timer_y_pos))
        write_text(f"TIME:{lap_time}", (255,255,255), timer_rect.x + 16, timer_rect.y +13)
        screen.blit(pb_bg, (Timer_x_pos-200,Timer_y_pos)) ###########################################################################################################
        write_text(f"PB:{personal_best}", (255,255,255), pb_bg_rect.x + 16, pb_bg_rect.y +13)

        car_1.respawn(SCREEN_WIDTH, SCREEN_HEIGHT)
        

        pygame.display.update()

        clock.tick(FPS)


    #multiplayer mode
    elif menu_choice == "Multiplayer":
        pass

    #settings
    elif menu_choice == "Settings":
        pass
    
    #credits
    elif menu_choice == "Credits":
        screen.fill((255,255,255))
        screen.blit(cred_text1, (ct1_x,ct1_y)) #ct = credits text
        screen.blit(cred_text2, (ct2_x,ct2_y))
        screen.blit(cred_text3, (ct3_x,ct3_y))
        screen.blit(cred_text4, (ct4_x,ct4_y))
        screen.blit(cred_text5, (ct5_x,ct5_y))
        screen.blit(cred_text6, (ct6_x,ct6_y))
        screen.blit(cred_text7, (ct7_x,ct7_y))
        screen.blit(cred_text8, (ct8_x,ct8_y))
        screen.blit(cred_text9, (ct9_x,ct9_y))

        cred_animation()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_choice = None

        pygame.display.update()
        clock.tick(FPS)

