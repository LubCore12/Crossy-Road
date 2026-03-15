import pygame

from settings import *


class Player(Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(surf, pos, groups)

        self.position = pos
        self.direction = pygame.Vector2()
        self.jump_length = 100

        self.jump_timer = Timer(500, func=self.enable_jump, repeat=True, autorun=True)
        self.can_jump = False

    def enable_jump(self):
        self.can_jump = True

    def input(self):
        keys = pygame.key.get_just_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
        if not self.direction.x:
            self.direction.y = int(keys[pygame.K_DOWN] - keys[pygame.K_UP])

        if self.direction:
            self.can_jump = False

    def move(self, delta_time):
        if self.can_jump:
            self.input()

        self.rect.x += self.direction.x * self.jump_length
        self.rect.y += self.direction.y * self.jump_length

        if not self.can_jump:
            self.direction = pygame.Vector2()

    def update(self, delta_time):
        self.jump_timer.update()
        self.move(delta_time)