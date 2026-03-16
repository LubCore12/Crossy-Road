import pygame

from settings import *


class Player(Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(surf, pos, groups)

        self.position = pos
        self.direction = pygame.Vector2()

        self.jump_length = self.rect.width
        self.have_to_jump = 0
        self.can_jump = True

    def input(self):
        keys = pygame.key.get_just_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
        if not self.direction.x:
            self.direction.y = int(keys[pygame.K_DOWN] - keys[pygame.K_UP])

        if self.direction:
            self.have_to_jump = self.jump_length
            self.can_jump = False

    def move(self, delta_time):
        if self.can_jump:
            self.input()

        if self.have_to_jump > 0:
            self.rect.center += self.direction * delta_time * JUMP_SPEED
            self.have_to_jump -= abs(self.direction.x if self.direction.x else self.direction.y) * delta_time * JUMP_SPEED

        if self.have_to_jump <= 0:
            self.direction = pygame.Vector2()
            self.have_to_jump = 0
            self.can_jump = True

    def update(self, delta_time):
        self.move(delta_time)