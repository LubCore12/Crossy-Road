from settings import *

from timer import Timer
from support import import_folder, import_image, import_subfolders
from sprites import Sprite, DeathSprite, Car, Tree
from player import Player
from groups import AllSprites


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Crossy Road")
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = AllSprites()
        self.car_sprites = pygame.sprite.Group()
        self.tree_sprites = pygame.sprite.Group()

        self.load_assets()

        self.map = load_pygame(join('data', 'maps', 'map.tmx'))

        self.car_timer = Timer(100, autorun=True)
        self.car_positions = []

        self.tree_timer = Timer(5000, autorun=True)
        self.tree_positions = []

        self.tree_surf = import_image('graphics', 'tree')

        self.setup()

    def create_cars(self, x, y, speed=450, flip=False):
        Car(choice(self.car_images), (x, y), (self.all_sprites, self.car_sprites), speed, flip)

    def create_trees(self, pos, speed):
        Tree([self.tree_surf], pos, (self.all_sprites, self.tree_sprites), -speed, self.player)

    def load_assets(self):
        self.car_images = import_subfolders('graphics', 'cars')
        self.player_images = import_folder('graphics', 'chicken')

    def setup(self):
        for entity in self.map.get_layer_by_name('Objects'):
            if entity.name == "Player":
                self.spawn_point = entity.x, entity.y
                self.player = Player(self.player_images, self.spawn_point, self.all_sprites, self.tree_sprites)
            if entity.name == "Car":
                self.car_positions.append((randrange(int(entity.x), int(entity.x) + 400), entity.y))
            if entity.name == "Car reverse":
                self.car_positions.append((randrange(int(entity.x), int(entity.x) + 400), entity.y , -450, True))
            if entity.name == "Floating tree":
                self.tree_positions.append(((entity.x, entity.y), randint(150, 220)))

        for x, y, image in self.map.get_layer_by_name('Ground').tiles():
            Sprite(image, (x * TILE_SIZE, y * TILE_SIZE), self.all_sprites)
        for x, y, image in self.map.get_layer_by_name('Death Objects').tiles():
            DeathSprite(image, (x * TILE_SIZE, y * TILE_SIZE), self.all_sprites, self.player, self.spawn_point)

    def collisions(self):
        if pygame.sprite.spritecollide(self.player, self.car_sprites, dokill=False):
            self.player.reset_player(self.spawn_point)

        cars = list(self.car_sprites)
        for index, first_sprite in enumerate(cars):
            for second_sprite in cars[index + 1:]:
                if first_sprite.flip == second_sprite.flip and first_sprite.rect.colliderect(second_sprite.rect):
                    first_sprite.kill()
                    second_sprite.kill()

    def run_game(self):
        while self.running:
            delta_time = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.car_timer.update()
            self.tree_timer.update()

            if not self.car_timer:
                self.create_cars(*choice(self.car_positions))
                self.car_timer.activate()

            if not self.tree_timer:
                for tree in self.tree_positions:
                    self.create_trees(*tree)
                self.tree_positions = [(i[0], randint(150, 220)) for i in self.tree_positions]
                self.tree_timer.activate()

            self.all_sprites.update(delta_time)
            self.display_surface.fill((0, 0, 0))
            self.all_sprites.draw(self.player.rect.center)
            self.collisions()

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run_game()
