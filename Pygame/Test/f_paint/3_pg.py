#
# 3_pg.py
# @author bulbasaur
# @description 绘制圆形，并且圆形会跟着鼠标移动
# @created 2019-07-30T17:58:38.985Z+08:00
# @last-modified 2019-07-30T18:16:47.330Z+08:00
#

import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

width, height = 640, 400
size = width, height

position = width // 2, height // 2
moving = False

screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                moving = True
        
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                moving = False

    if moving:
        position = pygame.mouse.get_pos()

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, position, 25, 1)
    pygame.draw.circle(screen, GREEN, position, 75, 1)
    pygame.draw.circle(screen, BLUE, position, 125, 1)

    pygame.display.flip()

    clock.tick(150)
