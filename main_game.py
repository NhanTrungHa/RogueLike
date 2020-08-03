import pygame
import tcod as libtcod

# game files
import constants


#      _______.___________..______       __    __    ______ .___________.
#     /       |           ||   _  \     |  |  |  |  /      ||           |
#    |   (----`---|  |----`|  |_)  |    |  |  |  | |  ,----'`---|  |----`
#     \   \       |  |     |      /     |  |  |  | |  |         |  |
# .----)   |      |  |     |  |\  \----.|  `--'  | |  `----.    |  |
# |_______/       |__|     | _| `._____| \______/   \______|    |__|

class struc_Tile:
    def __init__(self, block_path):
        self.block_path = block_path


#   ______   .______          __   _______   ______ .___________.    _______.
#  /  __  \  |   _  \        |  | |   ____| /      ||           |   /       |
# |  |  |  | |  |_)  |       |  | |  |__   |  ,----'`---|  |----`  |   (----`
# |  |  |  | |   _  <  .--.  |  | |   __|  |  |         |  |        \   \
# |  `--'  | |  |_)  | |  `--'  | |  |____ |  `----.    |  |    .----)   |
#  \______/  |______/   \______/  |_______| \______|    |__|    |_______/

class obj_Actor:
    def __init__(self, x, y, name_object, sprite, creature=None):
        self.x = x  # map address
        self.y = y
        self.sprite = sprite

        if creature:
            self.creature = creature
            creature.owner = self

    def draw(self):
        SURFACE_MAIN.blit(self.sprite, (self.x * constants.CELL_WIDTH, self.y * constants.CELL_HEIGHT))

    def move(self, dx, dy):
        if not GAME_MAP[self.x + dx][self.y + dy].block_path:
            self.x += dx
            self.y += dy


#   ____ ___  __  __ ____   ___  _   _ _____ _   _ _____ ____
#  / ___/ _ \|  \/  |  _ \ / _ \| \ | | ____| \ | |_   _/ ___|
# | |  | | | | |\/| | |_) | | | |  \| |  _| |  \| | | | \___ \
# | |__| |_| | |  | |  __/| |_| | |\  | |___| |\  | | |  ___) |
#  \____\___/|_|  |_|_|    \___/|_| \_|_____|_| \_| |_| |____/

class com_Creature:
    """
    Creatures have health, can damage other objects by attacking them. Can also die.
    """

    def __init__(self, name_instance, hp=10):
        self.name_instance = name_instance
        self.hp = hp


# class com_Item:

# class com_Container:


# .___  ___.      ___      .______
# |   \/   |     /   \     |   _  \
# |  \  /  |    /  ^  \    |  |_)  |
# |  |\/|  |   /  /_\  \   |   ___/
# |  |  |  |  /  _____  \  |  |
# |__|  |__| /__/     \__\ | _|

def map_create():
    new_map = [[struc_Tile(False) for y in range(0, constants.MAP_HEIGHT)] for x in range(0, constants.MAP_WIDTH)]

    new_map[10][10].block_path = True
    new_map[10][15].block_path = True

    return new_map


#  _______  .______          ___   ____    __    ____  __  .__   __.   _______
# |       \ |   _  \        /   \  \   \  /  \  /   / |  | |  \ |  |  /  _____|
# |  .--.  ||  |_)  |      /  ^  \  \   \/    \/   /  |  | |   \|  | |  |  __
# |  |  |  ||      /      /  /_\  \  \            /   |  | |  . `  | |  | |_ |
# |  '--'  ||  |\  \----./  _____  \  \    /\    /    |  | |  |\   | |  |__| |
# |_______/ | _| `._____/__/     \__\  \__/  \__/     |__| |__| \__|  \______|

def draw_game():
    global SURFACE_MAIN

    #  clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    #  draw the map
    draw_map(GAME_MAP)

    ENEMY.draw()

    #  draw the character
    PLAYER.draw()

    #  update the display
    pygame.display.flip()


def draw_map(map_to_draw):
    for x in range(0, constants.MAP_WIDTH):
        for y in range(0, constants.MAP_HEIGHT):
            if map_to_draw[x][y].block_path:
                # draw wall
                SURFACE_MAIN.blit(constants.S_WALL, (x * constants.CELL_WIDTH, y * constants.CELL_HEIGHT))
            else:
                # draw floor
                SURFACE_MAIN.blit(constants.S_FLOOR, (x * constants.CELL_WIDTH, y * constants.CELL_HEIGHT))


#   _______      ___      .___  ___.  _______
#  /  _____|    /   \     |   \/   | |   ____|
# |  |  __     /  ^  \    |  \  /  | |  |__
# |  | |_ |   /  /_\  \   |  |\/|  | |   __|
# |  |__| |  /  _____  \  |  |  |  | |  |____
#  \______| /__/     \__\ |__|  |__| |_______|

def game_main_loop():
    """In this function, we loop the main game"""
    game_quit = False

    while not game_quit:
        #  get player input
        events_list = pygame.event.get()
        #  process input
        for event in events_list:
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    PLAYER.move(0, -1)
                if event.key == pygame.K_j:
                    PLAYER.move(0, 1)
                if event.key == pygame.K_h:
                    PLAYER.move(-1, 0)
                if event.key == pygame.K_l:
                    PLAYER.move(1, 0)

        #  draw the game
        draw_game()
    #  quit the game
    pygame.quit()
    exit()


def game_initialize():
    """This function initializes the main window, and pygame"""

    global SURFACE_MAIN, GAME_MAP, PLAYER, ENEMY

    # initialize pygame
    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))

    GAME_MAP = map_create()

    creature_com1 = com_Creature("greg")
    PLAYER = obj_Actor(0, 0, "python", constants.S_PLAYER, creature=creature_com1)

    creature_com2 = com_Creature("jackie")
    ENEMY = obj_Actor(15, 15, "crab", constants.S_ENEMY, creature=creature_com2)


if __name__ == '__main__':
    game_initialize()
    game_main_loop()
