import random 
import pygame
from renderer import Renderer
from camera import Camera
import sys
from pathlib import Path

pygame.init()

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 640

base_path = Path(__file__).parent
print(base_path)

TEXTURES = {
    'floor': pygame.image.load(str((base_path / 'textures' / 'floor.png').resolve())),
    'ceiling': pygame.image.load(str((base_path / 'textures' / 'ceiling.png').resolve())),
    '0': pygame.image.load(str((base_path / 'textures' / 'greystone.png').resolve())),
    '1': pygame.image.load(str((base_path / 'textures' / 'mossy.png').resolve())),
    '2': pygame.image.load(str((base_path / 'textures' / 'wood.png').resolve())),
}
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
renderer = Renderer(SCREEN_WIDTH, SCREEN_HEIGHT, TEXTURES)
camera = Camera([2,3], [1,1], 66)

grid = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,0,1,0,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1]
]

clock = pygame.time.Clock()

while True:
    screen.fill((255, 255, 255))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_w:
                camera.pos[0] += camera.dir[0] * 0.1
                camera.pos[1] += camera.dir[1] * 0.1

    renderer.render(camera, grid, screen)
    pygame.display.update()
    clock.tick(60)
