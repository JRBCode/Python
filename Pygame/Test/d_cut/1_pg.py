#
# 1_pg.py
# @author bulbasaur
# @description 裁剪图像
# @created 2019-07-29T22:38:59.155Z+08:00
# @last-modified 2019-07-29T23:36:09.782Z+08:00
#

import pygame
import sys
from pygame.locals import *

pygame.init()

width, height = 640, 480
size = width, height
bg = (255, 255, 255)    # RGB

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

pygame.display.set_caption("FishC Demo")

oturtle = pygame.image.load("Pygame/Test/d_cut/images/turtle.png")
turtle = pygame.transform.chop(oturtle, (250, 200, 60, 60))
# turtle = oturtle

position = turtle.get_rect()
position.center = width //2, height //2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(bg)
    screen.blit(turtle, position)
    pygame.draw.rect(screen, (0, 0, 0), position, 1)

    pygame.display.flip()
    
    pygame.time.delay(10)
