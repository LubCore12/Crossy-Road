import pygame
from os.path import join
from os import walk
from random import randint, choice, randrange
from pytmx import load_pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
TILE_SIZE = 64
JUMP_SPEED = 300

from timer import *
from support import *
from sprites import *
from player import *
from car import *
from groups import *