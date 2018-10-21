import pygame as pg
from Block import Block

pg.init()
screen = pg.display.set_mode((400, 300))
done = False

block = Block()

clock = pg.time.Clock()

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT]:
        block.move(-1, 0)
    elif pressed[pg.K_RIGHT]:
        block.move(1, 0)

    screen.fill((255, 255, 255))
    block.draw(screen)
    
    pg.display.flip()
    clock.tick(60)

        