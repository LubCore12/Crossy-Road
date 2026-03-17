from settings import *


class Car(AminationSprite):
    def __init__(self, surf, pos, groups, speed, flip):
        super().__init__(surf, pos, groups)

        self.speed = speed
        self.frames = [pygame.transform.flip(frame, flip, False) for frame in self.frames]
        self.rect = self.frames[0].get_rect(bottomleft=pos - pygame.Vector2(0, -20)).inflate(0, -40)

    def move(self, delta_time):
        self.rect.x += delta_time * self.speed

    def update(self, delta_time):
        self.car_collisions()
        self.move(delta_time)
