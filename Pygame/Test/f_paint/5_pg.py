#
# 5_pg.py
# @author bulbasaur
# @description 绘制弧线
# @created 2019-07-30T18:28:40.695Z+08:00
# @last-modified 2019-07-30T18:33:57.810Z+08:00
#

import pygame
import sys
import math
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

    # 最后一个参数设置为 0 时，图形不显示
    pygame.draw.arc(screen, BLUE, (220, 50, 200, 200), math.pi, math.pi*2, 8)
    pygame.draw.arc(screen, BLACK, (100, 100, 440, 100), 0, math.pi, 5)

    pygame.display.flip()

    clock.tick(150)
