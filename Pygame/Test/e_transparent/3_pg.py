#
# 3_pg.py
# @author bulbasaur
# @description 优化透明度设置
# @created 2019-07-30T15:52:22.738Z+08:00
# @last-modified 2019-07-30T16:57:03.125Z+08:00
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
def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    # 新建 temp（空白），与 turtle 的大小一致，
    # 不是 alpha 格式的，以便调整整个图像的透明度
    temp = pygame.Surface((source.get_width(), \
        source.get_height())).convert()
    # 将背景中相对应位置图像绘制到 temp 中，
    # 从 temp 的（-x, -y）位置开始绘制，
    # 因此 temp 中草就是背景正中间位置的草
    temp.blit(target, (-x, -y))
    # 将已除去白色背景的乌龟图像覆盖到 temp 中
    temp.blit(source, (0, 0))
    # 设置透明度
    temp.set_alpha(opacity)
    # 将 temp 添加到 screen 中，
    # temp中的草和 screen 中的
    # 草重合，因此看起来是透明的
    target.blit(temp, location)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    screen.blit(background, (0, 0))
    blit_alpha(screen, turtle, position, 200)

    pygame.display.flip()

    clock.tick(30)
