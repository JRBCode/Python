#
# a_pg.py
# @author bulbasaur
# @description 小甲鱼图像移动
# @created 2019-07-29T10:15:30.415Z+08:00
# @last-modified 2019-07-29T13:10:03.320Z+08:00
#

import pygame
import sys

# 初始化 Pygame
pygame.init()

width, height = 600, 400
size = width, height
speed = [1, 1]
bg = (255, 255, 255)    # RGB

clock = pygame.time.Clock()

# 创建指定大小的窗口  返回一个 Surface 对象
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

# 加载图片
# turtle = pygame.image.load("images/turtle.png")
turtle = pygame.image.load("Pygame/Test/a_hello/images/turtle.png")
# 获得图像的位置矩形
position = turtle.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 翻转图像，第一个 True 设置水平翻转，第二个设置垂直翻转
        turtle = pygame.transform.flip(turtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟，值越大移动速度越快（帧率）
    clock.tick(150)
    # 也可以用下面的方法延迟 10毫秒
    # pygame.time.delay(10)
