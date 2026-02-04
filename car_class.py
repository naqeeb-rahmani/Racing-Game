
import pygame, math

class Car:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, sprite):
        self.car_x = SCREEN_WIDTH / 2
        self.car_y = (SCREEN_HEIGHT / 2) + 300

        self.angle = -90
        self.direction = 0     #direction 1 = right, direction -1 = left and 0 means straight
        self.rotating_speed = 5

        self.rad = 0

        self.speed = 5

        self.original_sprite = sprite
        self.sprite = self.original_sprite

        self.explosion = False

        #self.rect = self.sprite.get_rect(center=(self.car_x, self.car_y))


    def rotation(self):
        if self.direction == 1:
            self.angle -= self.rotating_speed
        elif self.direction == -1:
            self.angle += self.rotating_speed

        self.sprite = pygame.transform.rotozoom(self.original_sprite, self.angle, 1)

        self.rect = self.sprite.get_rect(center=(self.car_x, self.car_y))

    def movement(self):

        self.rad = math.radians(self.angle + 90) # +90 because it was off by 90 degrees

        self.car_x += (math.cos(self.rad) * self.speed) #speed is the hypotenuse
        self.car_y -= (math.sin(self.rad) * self.speed)
    

    def update(self):
        self.rotation()
