#
# 2_pg.py
# @author bulbasaur
# @description 绘制多边形
# @created 2019-07-30T17:53:36.028Z+08:00
# @last-modified 2019-07-30T17:58:18.419Z+08:00
#

import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

points = [(200, 75), (300, 25), (400, 75), \
    (450, 25), (450, 125), (400, 75), (300, 125)]

width, height = 640, 200
size = width, height

screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill(WHITE)

    pygame.draw.polygon(screen, GREEN, points, 0)

    pygame.display.flip()

    clock.tick(10)
