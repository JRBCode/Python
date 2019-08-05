#
# 2_main.py
# @author bulbasaur
# @description 添加碰撞检测（自定义函数）
# @created 2019-07-30T20:29:43.410Z+08:00
# @last-modified 2019-07-31T20:07:08.678Z+08:00
#

import pygame
import sys
import math
from pygame.locals import *
from random import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]

    # 小球移动函数
    def move(self):
        self.rect = self.rect.move(self.speed)

        if self.rect.right < 0:
            self.rect.left = self.width

        if self.rect.left > self.width:
            self.rect.right = 0

        if self.rect.bottom < 0:
            self.rect.top = self.height

        if self.rect.top > self.height:
            self.rect.bottom = 0


# 小球碰撞检测函数
def collide_check(item, target):
    col_balls = []
    for each in target:
        distance = math.sqrt(\
            math.pow((item.rect.center[0] - each.rect.center[0]), 2) + \
            math.pow((item.rect.center[1] - each.rect.center[1]), 2))
        if distance <= (item.rect.width + each.rect.width) / 2:
            col_balls.append(each)

    return col_balls


def main():
    pygame.init()

    ball_image = "Pygame/Test/g_playBall/images/gray_ball.png"
    bg_image = "Pygame/Test/g_playBall/images/background.png"

    runing = True

    width, height = 1024, 681
    bg_size = width, height
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball - FishC Demo")

    background = pygame.image.load(bg_image).convert_alpha()

    balls = []
    
    BALL_NUM = 5

    # 创建 5 个球
    for i in range(BALL_NUM):
        position = randint(0, width-100), randint(0, height-100)
        speed = [randint(-5, 5), randint(-5, 5)]
        ball = Ball(ball_image, position, speed, bg_size)
        
        # 检测小球的初始位置是否冲突
        while collide_check(ball, balls):
            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, height-100)

        balls.append(ball)

    clock = pygame.time.Clock()

    while runing:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background, (0, 0))

        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)

        # 碰撞检测
        for i in range(BALL_NUM):
            item = balls.pop(i)

            if  collide_check(item, balls):
                item.speed[0] = -item.speed[0]
                item.speed[1] = -item.speed[1]

            balls.insert(i, item)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
