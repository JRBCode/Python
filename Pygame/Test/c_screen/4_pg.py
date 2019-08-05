#
# 4_pg.py
# @author bulbasaur
# @description 小甲鱼图像旋转，沿着窗口边缘转圈
# @created 2019-07-29T21:56:06.263Z+08:00
# @last-modified 2019-07-29T22:39:59.083Z+08:00
#

import pygame
import sys
from pygame.locals import *

# 初始化 Pygame
pygame.init()

width, height = 576, 324
size = width, height
speed = [5, 0]
bg = (255, 255, 255)    # RGB

# 创建指定大小的窗口
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("Pygame")

# 加载图片
# turtle = pygame.image.load("images/turtle.png")
turtle = pygame.image.load("Pygame/Test/c_screen/images/turtle.png")

turtle_bottom = pygame.transform.flip(turtle, True, False)
turtle_right = pygame.transform.rotate(turtle_bottom, 90)
turtle_top = pygame.transform.rotate(turtle_bottom, 180)
turtle_left = pygame.transform.rotate(turtle_bottom, 270)
turtle = turtle_top

# 获得图像的位置矩形
position = turtle.get_rect()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 用户调整窗口尺寸
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            print(size)
            screen = pygame.display.set_mode(size, RESIZABLE)

    # 移动图像
    position = position.move(speed)

    if position.right > width:
        turtle = turtle_right
        position = turtle.get_rect()
        position.right = width
        speed[0] = 0
        speed[1] = 5

    if position.bottom > height:
        turtle = turtle_bottom
        position = turtle.get_rect()
        position.bottom = height
        position.right = width
        speed[0] = -5
        speed[1] = 0
    if position.left < 0:
        turtle = turtle_left
        position = turtle.get_rect()
        position.bottom = height
        speed[0] = 0
        speed[1] = -5
        
    if position.top < 0:
        turtle = turtle_top
        position = turtle.get_rect()
        speed[0] = 5
        speed[1] = 0

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 时间延迟
    pygame.time.delay(10)
