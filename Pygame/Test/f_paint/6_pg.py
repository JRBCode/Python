#
# 6_pg.py
# @author bulbasaur
# @description 绘制一条/多条线段
# @created 2019-07-30T18:35:29.280Z+08:00
# @last-modified 2019-07-30T18:54:23.737Z+08:00
#

import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

points = [(200, 75), (300, 25), (400, 75), \
    (450, 25), (450, 125), (400, 75), (300, 125)]


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

    # 第三个参数设置线段是否闭合
    pygame.draw.lines(screen, BLUE, 1, points, 1)
    pygame.draw.line(screen, BLACK, (100, 200), (540, 250), 4)
    # 最后一个参数设置是否抗锯齿（羽化边缘），
    # 无 width 参数，只能画一个像素的线段
    pygame.draw.aaline(screen, BLACK, (100, 250), (540, 300), 1)
    pygame.draw.aaline(screen, BLACK, (100, 300), (540, 350), 0)

    pygame.display.flip()

    clock.tick(150)