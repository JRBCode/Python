#
# main.py
# @author bulbasaur
# @description 添加五个移动的球
# @created 2019-07-30T19:27:17.155Z+08:00
# @last-modified 2019-07-30T20:29:25.469Z+08:00
#

import pygame
import sys
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

    for i in range(5):
        position = randint(0, width-100), randint(0, height-100)
        speed = [randint(-6, 6), randint(-6, 6)]
        ball = Ball(ball_image, position, speed, bg_size)
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

        pygame.display.flip()
        clock.tick(65)


if __name__ == "__main__":
    main()
