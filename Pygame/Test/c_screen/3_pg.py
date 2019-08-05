#
# 3_pg.py
# @author bulbasaur
# @description 实现通过键盘放大/缩小图像
# =/-：放大/缩小图像；空格键恢复原始尺寸
# @created 2019-07-29T18:23:25.261Z+08:00
# @last-modified 2019-07-29T23:43:25.668Z+08:00
#

import pygame
import sys
from pygame.locals import *
from math import sqrt

# 初始化 Pygame
pygame.init()

width, height = 576, 324
size = width, height
speed = [1, 1]
l_sp = sqrt(2)
print(l_sp)
bg = (255, 255, 255)    # RGB

# 创建指定大小的窗口  返回一个 Surface 对象
screen = pygame.display.set_mode(size, RESIZABLE)
# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

# 设置放大缩小的比率

ratio = 1.0

# 加载图片
# turtle = pygame.image.load("images/turtle.png")
original = pygame.image.load("Pygame/Test/c_screen/images/turtle.png")
oturtle = turtle = original

# 获得图像的位置矩形
oturtle_rect = turtle.get_rect()
position = oturtle_rect

# 按左右方向键改变图像运动方向时改变图像方向
r_head = turtle
l_head = pygame.transform.flip(turtle, True, False)

fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-l_sp, 0]
                turtle = l_head
                oturtle = pygame.transform.flip(original, True, False)
            if event.key == K_RIGHT:
                speed = [l_sp, 0]
                turtle = r_head
                oturtle = original
            if event.key == K_UP:
                speed = [0, -l_sp]
            if event.key == K_DOWN:
                speed = [0, l_sp]
            if event.key == K_w:
                speed = [-1, -1]
                turtle = l_head
                oturtle = pygame.transform.flip(original, True, False)
            if event.key == K_e:
                speed = [1, -1]
                turtle = r_head
                oturtle = original
            if event.key == K_s:
                speed = [-1, 1]
                turtle = l_head
                oturtle = pygame.transform.flip(original, True, False)
            if event.key == K_d:
                speed = [1, 1]
                turtle = r_head
                oturtle = original

            # 全屏
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    width, height = 1920, 1080
                    size = width, height
                    screen = pygame.display.set_mode((1920, 1080), \
                        FULLSCREEN | HWSURFACE)
                else:
                    width, height = 576, 324
                    size = width, height
                    screen = pygame.display.set_mode(size)
                
            # 放大、缩小小乌龟（=、-），空格键恢复原始尺寸
            if event.key == K_EQUALS or event.key == K_MINUS \
                or event.key == K_SPACE:
                # 最大只能放大一倍、缩小一半
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0

                turtle = pygame.transform.smoothscale(oturtle, (\
                    int(oturtle_rect.width * ratio), \
                    int(oturtle_rect.height * ratio)))
                    
                # 更新 position 中长宽值，并将改变前
                # 的位置记录下来，赋给新的 position
                p_l, p_t = position.left, position.top
                position = turtle.get_rect()
                position.left, position.top = p_l, p_t

                r_head = pygame.transform.smoothscale(original, (\
                    int(oturtle_rect.width * ratio), \
                    int(oturtle_rect.height * ratio)))
                l_head = pygame.transform.flip(r_head, True, False)

        # 用户调整窗口尺寸
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            screen = pygame.display.set_mode(size, RESIZABLE)

    # 移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 翻转图像，第一个 True 设置水平翻转，第二个设置垂直翻转
        turtle = pygame.transform.flip(turtle, True, False)
        oturtle = pygame.transform.flip(oturtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        # 反方向移动
        speed[1] = -speed[1]

    # 判断是否超出边界
    if position.right > width:
        position.right = width
    if position.bottom > height:
        position.bottom = height
    if position.left < 0:
        position.left = 0
    if position.top < 0:
        position.top = 0
        
    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 时间延迟
    pygame.time.delay(6)
