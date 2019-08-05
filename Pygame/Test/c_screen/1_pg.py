#
# i_pg.py
# @author bulbasaur
# @description 增加 F11 键全屏功能
# @created 2019-07-29T16:02:50.634Z+08:00
# @last-modified 2019-07-29T22:33:16.997Z+08:00
#

import pygame
import sys
from pygame.locals import *

# 初始化 Pygame
pygame.init()

width, height = 576, 324
size = width, height
speed = [1, 1]
bg = (255, 255, 255)    # RGB

# 创建指定大小的窗口  返回一个 Surface 对象
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

# 加载图片
# turtle = pygame.image.load("images/turtle.png")
turtle = pygame.image.load("Pygame/Test/c_screen/images/turtle.png")

# 获得图像的位置矩形
position = turtle.get_rect()

r_head = turtle
l_head = pygame.transform.flip(turtle, True, False)

fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-1, 0]
                turtle = l_head
            if event.key == K_RIGHT:
                speed = [1, 0]
                turtle = r_head
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]

            # 全屏
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    width, height = 1920, 1080
                    size = width, height
                    screen = pygame.display.set_mode((1920, 1080), FULLSCREEN | HWSURFACE)
                else:
                    width, height = 576, 324
                    size = width, height
                    screen = pygame.display.set_mode(size)

    # 移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 翻转图像，第一个 True 设置水平翻转，第二个设置垂直翻转
        turtle = pygame.transform.flip(turtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    if position.bottom > height:
        position.bottom = height
        
    if position.right > width:
        position.right = width

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 时间延迟
    pygame.time.delay(10)
