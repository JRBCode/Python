#
# 2_pg.py
# @author bulbasaur
# @description 用 png 格式图片先将图片背景裁减
# 掉（ PPT），再载入图片，最后调整图片的透明度
# @created 2019-07-30T14:10:40.573Z+08:00
# @last-modified 2019-07-30T16:57:34.942Z+08:00
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
    ("Pygame/Test/e_transparent/images/turtle.png")\
    .convert_alpha()
background = pygame.image.load\
    ("Pygame/Test/e_transparent/images/background.jpg")\
    .convert()
position = turtle.get_rect()
position.center = width // 2, height // 2

# 设置透明度
for i in range(position.width):
    for j in range(position.height):
        # 获得单个像素（i, j）的颜色
        temp = turtle.get_at((i, j))
        # 设置图片不是白色的部分的透明度
        if temp[3] != 0:
            temp[3] = 200
        turtle.set_at((i, j), temp)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    screen.blit(background, (0, 0))
    screen.blit(turtle, position)

    pygame.display.flip()

    clock.tick(30)
