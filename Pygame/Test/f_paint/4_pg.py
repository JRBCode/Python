#
# 4_pg.py
# @author bulbasaur
# @description 绘制椭圆
# @created 2019-07-30T18:20:16.669Z+08:00
# @last-modified 2019-07-30T18:25:44.353Z+08:00
#

import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

width, height = 640, 400
size = width, height

screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill(WHITE)

    pygame.draw.ellipse(screen, BLUE, (220, 50, 200, 200), 0)
    pygame.draw.ellipse(screen, BLACK, (100, 100, 440, 100), 1)

    pygame.display.flip()

    clock.tick(150)
