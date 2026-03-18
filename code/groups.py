from settings import *
from sprites import AnimationSprite, Tree


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()

    def draw(self, target):
        target_x, target_y = target

        self.offset.y = -(target_y - WINDOW_HEIGHT / 2) if target_y < 200 * TILE_SIZE - 400 else -(LEVEL_HEIGHT - 400 - WINDOW_HEIGHT / 2)

        for sprite in sorted(self, key=lambda sprite: self.sort_sprite_key(sprite)):
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)

    def sort_sprite_key(self, sprite):
        return (
            isinstance(sprite, AnimationSprite),
            isinstance(sprite, Tree),
            sprite.rect.y
        )
