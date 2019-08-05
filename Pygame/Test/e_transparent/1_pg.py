#
# 1_pg.py
# @author bulbasaur
# @description 使小乌龟的白色背景变为透明
# @created 2019-07-30T13:49:56.030Z+08:00
# @last-modified 2019-07-30T16:57:54.885Z+08:00
#

import pygame
import sys
from pygame.locals import *

pygame.init()

width, height = 640, 480
size = width, height
bg = (0, 0, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")

turtle = pygame.image.load\
    ("Pygame/Test/e_transparent/images/turtle.jpg")\
    .convert()
background = pygame.image.load\
    ("Pygame/Test/e_transparent/images/background.jpg")\
    .convert()
position = turtle.get_rect()
position.center = width // 2, height // 2

# 裁剪掉小乌龟的白色背景
turtle.set_colorkey((255, 255, 255))
# 设置小乌龟整个图像的透明度
# 值越小越透明（0~255）
turtle.set_alpha(200)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    screen.blit(background, (0, 0))
    screen.blit(turtle, position)

    pygame.display.flip()

    clock.tick(30)
