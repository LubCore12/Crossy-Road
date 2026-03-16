import pygame

from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Crossy Road")
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = AllSprites()
        self.car_sprites = pygame.sprite.Group()
        self.load_assets()

        self.player = Player(pygame.image.load(join('images', 'chicken', '1.png')), (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), self.all_sprites)

        self.car_timer = Timer(500, repeat=True, autorun=True, func=self.create_cars)

    def create_cars(self):
        Car(choice(self.car_images), (choice((-500, WINDOW_WIDTH + 500)), randint(0, WINDOW_HEIGHT)), (self.all_sprites, self.car_sprites))

    def load_assets(self):
        self.car_images = import_animation_folders('images', 'cars')

    def player_collisions(self):
         if pygame.sprite.spritecollide(self.player, self.car_sprites, dokill=False):
             self.player.rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 100)

    def run_game(self):
        while self.running:
            delta_time = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.car_timer.update()
            self.player_collisions()

            self.all_sprites.update(delta_time)
            self.display_surface.fill((0, 0, 0))
            self.all_sprites.draw(self.player.rect.center)

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run_game()

