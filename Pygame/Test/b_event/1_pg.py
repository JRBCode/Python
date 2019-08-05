#
# pg.py
# @author bulbasaur
# @description 将所有事件写入文本中
# @created 2019-07-29T12:10:30.949Z+08:00
# @last-modified 2019-07-29T16:24:33.998Z+08:00
#

import pygame
import sys

# 初始化 Pygame
pygame.init()

width, height = 600, 400
size = width, height

# 创建指定大小的窗口  返回一个 Surface 对象
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

f = open("Pygame/Test/b_event/1_record.txt", 'w')

while True:
    for event in pygame.event.get():
        f.write(str(event) + '\n')

        if event.type == pygame.QUIT:
            f.close()
            sys.exit()
