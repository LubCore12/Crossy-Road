from settings import *


class Car(AnimationSprite):
    def __init__(self, surf, pos, groups, speed, flip):
        super().__init__(surf, pos, groups)

        self.flip = flip
        self.image = pygame.transform.flip(self.image, self.flip, False)

        self.speed = speed
        self.frames = [pygame.transform.flip(frame, flip, False) for frame in self.frames]
        self.rect = self.rect.move(0, -20).inflate(0, -40)

    def move(self, delta_time):
        self.rect.x += delta_time * self.speed

    def destroy(self):
        if -1000 > self.rect.x or WINDOW_WIDTH + 1000 < self.rect.x:
            self.kill()

    def update(self, delta_time):
        self.destroy()
        self.move(delta_time)
