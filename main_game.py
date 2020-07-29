import pygame
import tcod as libtcod

# game files
import constants

def draw_game():

    global SURFACE_MAIN

    #TODO clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)
    #TODO draw the map

    #TODO draw the character
    SURFACE_MAIN.blit(constants.S_PLAYER, (200, 200))
    #TODO update the display
    pygame.display.flip()

def game_main_loop():
    """In this function, we loop the main game"""
    game_quit = False

    while not game_quit:
        # TODO get player input
        events_list = pygame.event.get()
        # TODO process input
        for event in events_list:
            if event.type == pygame.QUIT:
                game_quit = True

        # TODO draw the game
        draw_game()
    # TODO quit the game
    pygame.quit()
    exit()


def game_initialize():
    """This function initializes the main window, and pygame"""

    global SURFACE_MAIN

    # initialize pygame
    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))


if __name__ == '__main__':
    game_initialize()
    game_main_loop()
