from settings import *


def import_image(*path, image_type='.png'):
    full_path = join(*path) + f'{image_type}'
    return pygame.image.load(full_path).convert_alpha() if image_type == '.png' else pygame.image.load(full_path).convert()

def import_subfolders(*path):
    animation_list = []

    for folder_path, _, file_names in walk(join(*path)):

        car_animation = []
        for file in sorted(file_names, key=lambda x: int(x.split('.')[0])):
            full_path = join(folder_path, file)
            surf = pygame.image.load(full_path).convert_alpha()
            car_animation.append(surf)

        if car_animation:
            animation_list.append(car_animation)

    return animation_list

def import_folder(*path):
    animation_list = []

    for folder_path, _, files in walk(join(*path)):
        for file in sorted(files, key=lambda x: int(x.split('.')[0])):
            full_path = join(folder_path, file)
            surf = pygame.image.load(full_path).convert_alpha()
            animation_list.append(surf)

    return animation_list
