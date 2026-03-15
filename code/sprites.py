from settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)

        self.image = surf
        self.rect = self.image.get_frect(center=pos)


class AminationSprite(Sprite):
    def __init__(self, frames, pos, groups):
        self.frames = frames
        self.frame_index = 0

        super().__init__(self.frames[self.frame_index], pos, groups)

    def update(self, delta_time):
        self.frame_index += 1 * delta_time
        self.image = self.frames[self.frame_index] % len(self.frames)