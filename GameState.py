import Config as cfg
import pygame as pg
import sys

from Block import Block
from Camera import Camera
from Player import Player
from State import State, FINISH_STATE


FLOOR_HEIGHT = 50
OBSTACLE_HEIGHT = 60
FPS = 60


class GameState(object):
    def __init__(self, screen):
        self.state = State(self.input_handler, self.update,
                           self.draw, self.on_delete, screen)
        self.cam = Camera()
        self.floor = Block(
                      name='floor',
                      starting_position=(0, cfg.SCREEN_HEIGHT - FLOOR_HEIGHT),
                      size=(cfg.SCREEN_WIDTH, FLOOR_HEIGHT),
                      color=cfg.COLOR_BLACK, camera=self.cam)

        self.obstacle = Block(
                         name='obstacle',
                         starting_position=(500, cfg.SCREEN_HEIGHT -
                                            FLOOR_HEIGHT - OBSTACLE_HEIGHT),
                         size=(40, OBSTACLE_HEIGHT),
                         color=cfg.COLOR_BROWN, camera=self.cam
                         )
        self.player = Player()
        self.block_list = [self.floor, self.obstacle]
        self.clock = pg.time.Clock()

    def input_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.player.xvel = -2
                elif event.key == pg.K_RIGHT:
                    self.player.xvel = 2
                elif event.key == pg.K_SPACE:
                    self.player.jump()
                elif event.key == pg.K_ESCAPE:
                    return FINISH_STATE
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.player.xvel = 0
                elif event.key == pg.K_RIGHT:
                    self.player.xvel = 0

    def update(self):
        self.player.update()
        self.player.test_collision(self.block_list)
        pg.display.flip()
        self.clock.tick(FPS)

    def draw(self):
        self.state.screen.fill(cfg.COLOR_WHITE)
        for block in self.block_list:
            block.draw(self.state.screen)
        self.player.draw(self.state.screen)

    def on_delete(self):
        pass
