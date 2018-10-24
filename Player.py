import Config as cfg
from Block import Block

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 100


class Player(object):
    def __init__(self):
        self.block = Block(
                        initial_position=(cfg.SCREEN_WIDTH/5,
                                          100),
                        size=(PLAYER_WIDTH, PLAYER_HEIGHT),
                        color=cfg.COLOR_BLACK
                        )

    def draw(self, screen):
        self.block.draw(screen)
