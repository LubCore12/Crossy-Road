import pygame

from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Crossy Road")
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.load_assets()

        Car(self.car_sprites[0], (100, 100), self.all_sprites)

        surf = pygame.Surface((100, 100))
        surf.fill('yellow')

        Player(surf, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), self.all_sprites)

    def load_assets(self):
        self.car_sprites = import_animation_folders('images', 'cars')

    def run_game(self):
        while self.running:
            delta_time = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.all_sprites.update(delta_time)
            self.display_surface.fill((0, 0, 0))
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run_game()

