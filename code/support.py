from settings import *


def import_animation_folders(*path):
    animation_dict = []
    for folder_path, _, file_names in walk(join(*path)):
        car_animations = []
        for file in sorted(file_names, key=lambda x: int(x.split('.')[0])):
            path = join(folder_path, file)
            surf = pygame.image.load(path).convert_alpha()
            car_animations.append(surf)
            animation_dict.append(car_animations)

    return animation_dict
