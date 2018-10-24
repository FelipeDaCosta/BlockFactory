import pygame as pg
import Config as cfg


class Block(object):
    def __init__(self, starting_position=(0, 0), size=(60, 60),
                 color=cfg.COLOR_BLACK, gravity=True, camera=None):
        self.x, self.y = starting_position
        self.width, self.height = size
        self.color = color
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.camera = camera

    def draw(self, surface):
        xpos, ypos = self.x, self.y
        if self.camera is not None:
            xpos += self.camera.x
            ypos += self.camera.y
        if cfg.is_in_screen((xpos, ypos), (self.width, self.height)):
            pg.draw.rect(surface, self.color,
                         pg.Rect(xpos, ypos, self.width, self.height))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height
