#
# 2_pg.py
# @author bulbasaur
# @description 将所有事件输出到屏幕上
# @created 2019-07-29T12:21:55.713Z+08:00
# @last-modified 2019-07-29T12:42:42.890Z+08:00
#

import pygame
import sys

pygame.init()

width, height = 600, 400
size = width, height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")

# None：设置字体样式（空）；20：字体大小
font = pygame.font.Font(None, 20)

position = 0
line_height = font.get_linesize()   # 获取行高

bg = (0, 0, 0)
screen.fill(bg)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        
        # True：消除锯齿；(0, 255, 0)：设置颜色为绿色；(0, position)：显示位置
        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
        position += line_height

        if position > height:
            position = 0
            screen.fill(bg)

    pygame.display.flip()

