import pygame as pg
import Config as cfg


class Block(object):
    def __init__(self, name='', starting_position=(0, 0), size=(60, 60),
                 color=cfg.COLOR_BLACK, gravity=True, camera=None):
        self.name = name
        self.color = color
        self.rect = pg.Rect(starting_position, size)
        self.camera = camera

    def draw(self, surface):
        xpos, ypos = self.x, self.y
        if self.camera is not None:
            xpos += self.camera.x
            ypos += self.camera.y
        if cfg.is_in_screen((xpos, ypos), (self.width, self.height)):
            pg.draw.rect(surface, self.color,
                         pg.Rect(xpos, ypos, self.width, self.height))
    
    def move(self, distance):
        self.rect.move_ip(*distance)

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height
