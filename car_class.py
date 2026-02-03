
import pygame

class Car:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, sprite):
        self.car_x = SCREEN_WIDTH / 2
        self.car_y = SCREEN_HEIGHT / 2

        self.angle = 0
        self.direction = 0     #direction 1 = right, direction -1 = left and 0 means straight
        self.rotating_speed = 1

        self.speed = 10

        self.original_sprite = sprite
        self.sprite = self.original_sprite

        self.rect = self.sprite.get_rect(center=(self.car_x, self.car_y))


    def rotation(self):
        if self.direction == 1:
            self.angle -= self.rotating_speed
        elif self.direction == -1:
            self.angle += self.rotating_speed

        self.sprite = pygame.transform.rotozoom(self.original_sprite, self.angle, 1)

        self.rect = self.sprite.get_rect(center=(self.car_x, self.car_y))


    def update(self):
        self.rotation()
