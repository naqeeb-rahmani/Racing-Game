
class Car:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, sprite):
        self.car_x = SCREEN_WIDTH / 2
        self.car_y = SCREEN_HEIGHT / 2

        self.speed = 10

        self.sprite = sprite

