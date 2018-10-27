import Config as cfg
import pygame as pg

from State import StateStack
from GameState import GameState


pg.init()
screen = pg.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
state_stack = StateStack()
state_stack.push(GameState(screen))

# Game Loop
while not state_stack.is_empty():
    state_stack.run_current_state()
