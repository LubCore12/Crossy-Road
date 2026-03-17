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

        self.map = load_pygame(join('data', 'maps', 'map.tmx'))

        self.car_timers = Timer(100, autorun=True)
        self.car_positions = []

        self.setup()

    def create_cars(self, x, y, speed=500, flip=False):
        Car(choice(self.car_images), (x, y), (self.all_sprites, self.car_sprites), speed, flip)

    def load_assets(self):
        self.car_images = import_animation_folders('images', 'cars')

    def setup(self):
        for x, y, image in self.map.get_layer_by_name('Ground').tiles():
            Sprite(image, (x * TILE_SIZE, y * TILE_SIZE), self.all_sprites)

        for entity in self.map.get_layer_by_name('Objects'):
            if entity.name == "Player":
                self.spawn_point = entity.x, entity.y
                self.player = Player(pygame.image.load(join('images', 'chicken', '1.png')), self.spawn_point, self.all_sprites)

            if entity.name == "Car":
                print(entity.x, entity.y)
                self.car_positions.append((randrange(int(entity.x), -200), entity.y))
            if entity.name == "Car reverse":
                self.car_positions.append((entity.x, entity.y, -500, True))

    def collisions(self):
         if pygame.sprite.spritecollide(self.player, self.car_sprites, dokill=False):
             self.player.rect.center = self.spawn_point
             self.player.have_to_jump = 0

    def run_game(self):
        while self.running:
            delta_time = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.collisions()
            self.car_timers.update()

            if not self.car_timers:
                self.create_cars(*choice(self.car_positions))
                self.car_timers.activate()

            self.all_sprites.update(delta_time)
            self.display_surface.fill((0, 0, 0))
            self.all_sprites.draw(self.player.rect.center)

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run_game()

