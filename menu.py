import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Menu")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Menu states
options = ["Start", "Multiplayer", "Credits", "Quit"]
selected = 0
show_credits = False

while True:
    screen.fill(BLACK)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if show_credits:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    show_credits = False
            else:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % 4
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 4
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        print("Start Game")
                    elif selected == 1:
                        print("Multiplayer")
                    elif selected == 2:
                        show_credits = True
                    elif selected == 3:
                        pygame.quit()
                        sys.exit()
    
    if show_credits:
        # Draw credits screen
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
        # Draw main menu
        font = pygame.font.SysFont(None, 80)
        title = font.render("RACE GAME", True, GREEN)
        screen.blit(title, (250, 100))
        
        # Draw menu options
        font = pygame.font.SysFont(None, 60)
        for i, option in enumerate(options):
            color = GREEN if i == selected else WHITE
            text = font.render(option, True, color)
            screen.blit(text, (300, 220 + i * 70))
    
    pygame.display.flip()
    clock.tick(60)