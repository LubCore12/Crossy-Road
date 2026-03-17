from settings import *


def import_animation_folders(*path):
    animation_list = []
    for folder_path, _, file_names in walk(join(*path)):
        car_animations = []
        for file in sorted(file_names, key=lambda x: int(x.split('.')[0])):
            path = join(folder_path, file)
            surf = pygame.image.load(path).convert_alpha()
            car_animations.append(surf)
            animation_list.append(car_animations)

    return animation_list


def import_folder(*path):
    animation_list = []
    for folder_path, _, file_name in walk(join(*path)):
        path = join(folder_path, file_name[0])
        surf = pygame.image.load(path).convert_alpha()
        animation_list.append(surf)

    return animation_list
