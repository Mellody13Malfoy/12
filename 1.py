import os 
import pygame
import copy
import sys

pygame.init()
# размеры окна: 
size = width, height = 700, 500
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
FPS = 50
step = 50
clock = pygame.time.Clock()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

def terminate():
    pygame.quit()
    sys.exit()
terminate()