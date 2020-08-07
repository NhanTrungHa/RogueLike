import pygame
import tcod as libtcod

pygame.init()

# Game Sizes
GAME_WIDTH = 800
GAME_HEIGHT = 600
CELL_WIDTH = 32
CELL_HEIGHT = 32

# MAP VARS
MAP_WIDTH = 20
MAP_HEIGHT = 20

# color definitions
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)

# Game colors
COLOR_DEFAULT_BG = COLOR_GREY

# SPRITES
S_PLAYER = pygame.image.load("data/snake.png")
S_ENEMY = pygame.image.load("data/enemy1.png")

S_WALL = pygame.image.load("data/wall.png")
S_WALLEXPLORED = pygame.image.load("data/wallunseen.png")

S_FLOOR = pygame.image.load("data/floor.png")
S_FLOOREXPLORED = pygame.image.load("data/floorunseen.png")




# FOV SETTINGS
FOV_ALGO = libtcod.FOV_BASIC
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10