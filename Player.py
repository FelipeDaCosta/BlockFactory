import Config as cfg
import pygame as pg
from Block import Block

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 100


class Player(object):
    def __init__(self):
        self.block = Block(name='Player',
                           starting_position=(cfg.SCREEN_WIDTH/5,
                                              100),
                           size=(PLAYER_WIDTH, PLAYER_HEIGHT),
                           color=cfg.COLOR_BLACK
                           )
        # Bottom Rect is used to know if the block is touching
        # the ground.
        self.bottom_rect = pg.Rect(self.block.x, self.block.y,
                                   self.block.width, 1)
        self.xvel, self.yvel = (0, 1)
        self.touching_ground = False
        self.can_jump = False

    def draw(self, screen):
        self.block.draw(screen)

    def move(self, distance):
        self.block.move(distance)
        self.bottom_rect.top = self.block.rect.bottom

    def update(self):
        self.move((self.xvel, self.yvel))

    def notiffy_collision(self, other_block):
        if self.yvel > 0:
            if self.block.rect.bottom >= other_block.rect.top and \
               self.block.rect.bottom <= other_block.rect.bottom:
                self.block.rect.bottom = other_block.rect.top
                self.touching_ground = True
                self.can_jump = True

    def test_collision(self, other_block):
        if self.block.rect.colliderect(other_block.rect):
            self.notiffy_collision(other_block)
