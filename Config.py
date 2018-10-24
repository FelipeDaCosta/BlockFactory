GRAVITY = 0.5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BROWN = (139, 69, 19)


def is_in_screen(pos, dimensions):
    return (pos[0] >= -dimensions[0] and pos[0] <= SCREEN_WIDTH) and \
           (pos[1] >= -dimensions[1] and pos[1] <= SCREEN_HEIGHT)
