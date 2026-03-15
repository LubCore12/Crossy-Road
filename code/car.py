from settings import *


class Car(AminationSprite):
    def __init__(self, surf, pos, groups):
        super().__init__(surf, pos, groups)

        self.speed = 300

    def move(self, delta_time):
        self.rect.x += delta_time * self.speed

    def update(self, delta_time):
        self.move(delta_time)
