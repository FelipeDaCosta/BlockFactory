import Config as cfg
import pygame as pg

from State import StateStack
from GameState import MenuState


pg.init()
pg.font.init()
screen = pg.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
state_stack = StateStack()
state_stack.push(MenuState(screen, state_stack))

# Game Loop
while not state_stack.is_empty():
    state_stack.run_current_state()
