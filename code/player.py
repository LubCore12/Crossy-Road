from settings import *
from sprites import AnimationSprite


class Player(AnimationSprite):
    def __init__(self, surf, pos, groups, tree_group):
        super().__init__(surf, pos, groups)

        self.position = pos
        self.direction = pygame.Vector2()

        self.jump_length = TILE_SIZE
        self.have_to_jump = 0
        self.can_jump = True

        self.tree_group = tree_group

    @property
    def on_tree(self):
        return pygame.sprite.spritecollide(self, self.tree_group, dokill=False)

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
            self.rect.center += self.direction * self.have_to_jump
            self.direction = pygame.Vector2()
            self.have_to_jump = 0
            self.can_jump = True

    def wall_collisions(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

    def reset_player(self, pos):
        self.rect.topleft = pos
        self.direction = pygame.Vector2()
        self.have_to_jump = 0
        self.can_jump = True

    def update(self, delta_time):
        self.move(delta_time)
        self.wall_collisions()