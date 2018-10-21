import pygame as pg


class Block():
    def __init__(self, initial_position=(0, 0), size=(60, 60), 
                 color=(0, 0, 0)):
        self.x = initial_position[0]
        self.y = initial_position[1]
        self.width = size[0]
        self.height = size[1]
        self.color = color

    def draw(self, surface):
        pg.draw.rect(surface, self.color, 
                     pg.Rect(self.x, self.y, self.width, self.height))

    def move(self, velX, velY):
        self.x += velX
        self.y += velY
        
