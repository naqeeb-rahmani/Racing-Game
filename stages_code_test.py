import pygame, sys, car_class

#爱泼斯坦制片公司tm
#Блят продукция partners & co

pygame.init()

#Day 1: Get atleast 1 car, which should be able to move 
#Day 2:

#SCREEN
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#screen = (pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



clock = pygame.time.Clock()
##################################

#TEST BACKGROUND
bg_test = pygame.image.load("base_bana.png")

###################


#STATES
game = True
#############################

#CARS

car_1 = car_class.Car(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.image.load(r"assets\cars\car_1_top.png")
)

#car_1 = pygame.image.load(r"assets\cars\car_player1.png")

car_1_x = 100
car_1_y = 100

car_speed = 10
########################

class GameState():
    def __init__(self):
        self.state = "main_game"

    def menu(self):
        screen.blit(bg_test, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_1.car_x > 0:
            car_1.car_x = car_1.car_x - car_1.speed

        if keys[pygame.K_RIGHT] and car_1.car_x < (SCREEN_WIDTH - 64):
            car_1.car_x = car_1.car_x + car_1.speed

        if keys[pygame.K_DOWN] and car_1.car_y < (SCREEN_HEIGHT - 64):
            car_1.car_y = car_1.car_y + car_1.speed

        if keys[pygame.K_UP] and car_1.car_y > 0:
            car_1.car_y = car_1.car_y - car_1.speed

        screen.fill((0,0,0,))
        screen.blit(bg_test, (0,0))
        screen.blit(car_1.sprite, (car_1.car_x, car_1.car_y))

        pygame.display.update()

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main_game()
        


pygame.display.set_caption("汽车联盟 (Chinatown)")

game_state = GameState()

while game:
    game_state.menu()

    clock.tick(60)
