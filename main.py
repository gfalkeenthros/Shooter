import pygame as pg
import sys
import esper

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 720

MAP_WIDTH = 50
MAP_HEIGHT = 50

screen = pg.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

while True:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
    pg.display.update()
    