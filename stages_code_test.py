import pygame, sys
import car_class


pygame.init()
pygame.mixer.init()

#Day 1: Get atleast 1 car, which should be able to move 
#Day 2:

#SCREEN
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#screen = (pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

menu_music = (r"C:\Users\tor.blom\Racing-Game\assets\audio\music\Blippy Trance.mp3")
main_music = (r"C:\Users\tor.blom\Racing-Game\assets\audio\music\Shenyang.mp3")

pygame.mixer.music.load(menu_music)
pygame.mixer.music.play()

clock = pygame.time.Clock()
##################################

#TEST BACKGROUND
bg_test = pygame.image.load("base_bana.png")

################### Texts

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Menu states
options = ["Start", "Multiplayer", "Credits", "Quit"]
selected = 0
show_credits = False
#STATES
game = True
#############################

#CARS

car_1_sprite = pygame.image.load(r"assets\cars\car_1_top.png").convert_alpha()

car_1 = car_class.Car(SCREEN_WIDTH, SCREEN_HEIGHT, car_1_sprite)

#car_1 = pygame.image.load(r"assets\cars\car_player1.png")

car_1_x = 100
car_1_y = 100

car_speed = 10
########################

class GameState():
    def __init__(self):
        self.state = "menu"

    # Menu states
    options = ["Start", "Multiplayer", "Credits", "Quit"]
    selected = 0
    show_credits = False

    def menu(self):
        pygame.display.set_caption("Simple Menu")
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if self.show_credits:
                    if event.key in (pygame.K_ESCAPE, pygame.K_RETURN):
                        self.show_credits = False
                else:
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.selected == 0:
                            self.state = "main_game"
                        elif self.selected == 2:
                            self.show_credits = True
                        elif self.selected == 3:
                            pygame.quit()
                            sys.exit()

        if self.show_credits:
            font = pygame.font.SysFont(None, 80)
            title = font.render("CREDITS", True, YELLOW)
            screen.blit(title, (280, 100))

            font = pygame.font.SysFont(None, 50)
            names = ["Made by:", "", "Naqeeb", "Reem", "Tor", "", "Press ESC to go back"]
            for i, name in enumerate(names):
                color = GREEN if name in ["Naqeeb", "Reem", "Tor"] else WHITE
                text = font.render(name, True, color)
                screen.blit(text, (320, 200 + i * 50))
        else:
            font = pygame.font.SysFont(None, 80)
            title = font.render("RACE GAME", True, GREEN)
            screen.blit(title, (250, 100))

            font = pygame.font.SysFont(None, 60)
            for i, option in enumerate(self.options):
                color = GREEN if i == self.selected else WHITE
                text = font.render(option, True, color)
                screen.blit(text, (300, 220 + i * 70))

        pygame.display.update()

    def main_game(self):
        pygame.display.set_caption("汽车联盟 (Chinatown)")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
            car_1.update()
#    car_1.update()

            screen.fill((0,0,0,))
    #test

            screen.blit(bg_test, (0,0))

#################
            screen.blit(car_1.sprite, car_1.rect)



            pygame.display.update()

    



    def state_manager(self):
        if self.state == "menu":
            self.menu()
        if self.state == "main_game":
            self.main_game()
        


pygame.display.set_caption("汽车联盟 (Chinatown)")

game_state = GameState()

while game:
    game_state.state_manager()

    clock.tick(60)
