import Config as cfg
import pygame as pg
from Block import Block
from Camera import Camera
from Player import Player


FPS = 60
FLOOR_HEIGHT = 50
OBSTACLE_HEIGHT = 60

pg.init()
screen = pg.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
clock = pg.time.Clock()
done = False
block_list = []
cam = Camera()
floor = Block(name='floor', starting_position=(0, cfg.SCREEN_HEIGHT - FLOOR_HEIGHT),
              size=(cfg.SCREEN_WIDTH, FLOOR_HEIGHT), color=cfg.COLOR_BLACK,
              camera=cam)

obstacle = Block(name='obstacle', starting_position=(500, cfg.SCREEN_HEIGHT - FLOOR_HEIGHT -
                 OBSTACLE_HEIGHT), size=(40, OBSTACLE_HEIGHT),
                 color=cfg.COLOR_BROWN, camera=cam)
block_list.append(floor)
block_list.append(obstacle)
player = Player()

# Game Loop
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill(cfg.COLOR_WHITE)
    for block in block_list:
        block.draw(screen)
        player.test_collision(block)
    player.draw(screen)
    player.update()
    pg.display.flip()
    clock.tick(FPS)
