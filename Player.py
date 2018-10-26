import Config as cfg
import pygame as pg
from Block import Block

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 100


def is_inside(point, lower, higher):
    return point >= lower and point <= higher


class Player(object):
    def __init__(self):
        self.block = Block(name='Player',
                           starting_position=(cfg.SCREEN_WIDTH/5,
                                              300),
                           size=(PLAYER_WIDTH, PLAYER_HEIGHT),
                           color=cfg.COLOR_BLACK
                           )
        # Bottom Rect is used to know if the block is touching
        # the ground.
        self.bottom_rect = pg.Rect(self.block.x, self.block.y,
                                   2, 2)
        self.xvel, self.yvel = (0, 1)
        self.touching_ground = False
        self.can_jump = False

    def draw(self, screen):
        self.block.draw(screen)

    def move(self, distance):
        self.block.move(distance)
        self.bottom_rect.top = self.block.rect.bottom

    def update(self):
        if not self.touching_ground:
            self.yvel += 0.5
        self.move((self.xvel, self.yvel))

    def jump(self):
        if self.touching_ground:
            self.yvel = -9
            self.touching_ground = False
        elif self.can_jump:
            self.yvel = -8

    def collision_stop_movement(self, other_block):
        """
        Reaction to collision with a floor or obstacle
        """
        if self.yvel > 0:
            if is_inside(self.block.rect.bottom, other_block.rect.top,
                         other_block.rect.bottom):
                self.block.rect.bottom = other_block.rect.top
                self.touching_ground = True
                self.can_jump = True
                self.yvel = 0
        elif self.yvel < 0:
            if is_inside(self.block.rect.top, other_block.rect.top,
                         other_block.rect.bottom):
                self.block.rect.top = other_block.rect.bottom
                self.yvel = 0
        else:  # Focus on vertical collision
            if self.xvel > 0:
                if is_inside(self.block.rect.right, other_block.rect.left,
                             other_block.rect.right):
                    self.block.rect.right = other_block.rect.left
                    self.xvel = 0
            elif self.xvel < 0:
                if is_inside(self.block.rect.left, other_block.rect.left,
                             other_block.rect.right):
                    self.block.rect.left = other_block.rect.right
                    self.xvel = 0

    def notiffy_collision(self, other_block):
        self.collision_stop_movement(other_block)

    def test_collision(self, block_list):
        if self.bottom_rect.collidelist([rect for rect in block_list]) == -1:
            self.touching_ground = False
        for block in block_list:
            if self.block.rect.colliderect(block.rect):
                self.notiffy_collision(block)
