from settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)

        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)


class AnimationSprite(Sprite):
    def __init__(self, frames, pos, groups):
        self.frames = frames
        self.frame_index = 0

        super().__init__(self.frames[self.frame_index], pos, groups)

    def update(self, delta_time):
        self.frame_index = (self.frame_index + ANIMATION_SPEED * delta_time) % len(self.frames)
        self.image = self.frames[int(self.frame_index)]


class MoveableSprite(AnimationSprite):
    def __init__(self, frames, pos, groups):
        super().__init__(frames, pos, groups)

    def move(self, delta_time):
        self.rect.x += delta_time * self.speed

    def destroy(self):
        if -1000 > self.rect.x or WINDOW_WIDTH + 1000 < self.rect.x:
            self.kill()

    def update(self, delta_time):
        super().update(delta_time)
        self.destroy()
        self.move(delta_time)


class Car(MoveableSprite):
    def __init__(self, surf, pos, groups, speed, flip):
        super().__init__(surf, pos, groups)

        self.flip = flip
        self.image = pygame.transform.flip(self.image, self.flip, False)

        self.speed = speed
        self.frames = [pygame.transform.flip(frame, flip, False) for frame in self.frames]


class Tree(MoveableSprite):
    def __init__(self, frames, pos, groups, speed, target):
        super().__init__(frames, pos, groups)

        self.speed = speed
        self.target = target

    def target_move(self, delta_time):
        if self.target.rect.colliderect(self.rect) and (self.target.direction.y == 0):
            self.target.rect.x += delta_time * self.speed

    def update(self, delta_time):
        super().update(delta_time)
        self.target_move(delta_time)


class DeathSprite(Sprite):
    def __init__(self, surf, pos, groups, target, start_pos):
        super().__init__(surf, pos, groups)

        self.target = target
        self.start_pos = start_pos

    def respawn(self):
        if not self.target.on_tree:
            if self.rect.colliderect(self.target.rect):
                self.target.reset_player(self.start_pos)

    def update(self, delta_time):
        self.respawn()
