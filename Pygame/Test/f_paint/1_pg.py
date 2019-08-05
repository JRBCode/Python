#
# 1_pg.py
# @author bulbasaur
# @description 绘制矩形
# @created 2019-07-30T17:05:19.047Z+08:00
# @last-modified 2019-08-05T09:48:59.398Z+08:00
#

import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
    
    # 最后一个参数，设置边框大小，边框为 0 时，颜色填充整个图形
    pygame.draw.rect(screen, BLACK, (50, 50, 150, 50), 0)
    pygame.draw.rect(screen, BLACK, (250, 50, 150, 50), 1)
    pygame.draw.rect(screen, BLACK, (450, 50, 150, 50), 10)

    pygame.display.flip()

    clock.tick(10)
