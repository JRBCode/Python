#
# 3_main.py
# @author bulbasaur
# @description 碰撞检测（预定义函数 spritecollide，
# 并增加参数 collide_circle，新增 Ball 的 radius
# 属性）; 添加背景音乐和音效
# @created 2019-07-30T22:16:06.728Z+08:00
# @last-modified 2019-08-05T09:49:23.902Z+08:00
#

import pygame
import sys
from pygame.locals import *
from random import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, grayball_image, greenball_image, \
        position, speed, bg_size, target):
        pygame.sprite.Sprite.__init__(self)

        # control 标记小球是否被玩家控制  side 小球运动方向
        # colllide 标记小球是否正在发生碰撞
        # target 参数为用来检测鼠标移动速度是否符合晓求得目标
        self.grayball_image = pygame.image.load(grayball_image).convert_alpha()
        self.greenball_image = pygame.image.load(greenball_image).convert_alpha()
        self.rect = self.grayball_image.get_rect()
        self.rect.left, self.rect.top = position
        self.side = [choice([-1, 1]), choice([-1, 1])]
        self.speed = speed
        self.collide = False
        self.target = target
        self.control = False
        self.width, self.height = bg_size[0], bg_size[1]
        self.radius = self.rect.width / 2

    def move(self):
        if self.control:
            self.rect = self.rect.move(self.speed)
        else:
            self.speed[0] = abs(self.speed[0])
            self.speed[1] = abs(self.speed[1])
            self.rect = self.rect.move((self.side[0] * self.speed[0], \
                self.side[1] * self.speed[1]))

        if self.rect.right < 0:
            self.rect.left = self.width

        if self.rect.left > self.width:
            self.rect.right = 0

        if self.rect.bottom < 0:
            self.rect.top = self.height

        if self.rect.top > self.height:
            self.rect.bottom = 0

    # 判断鼠标每秒钟产生的事件数量是否满足小球的目标
    def check(self, motion):
        if self.target < motion < self.target + 5:
            return True
        else:
            return False


# 鼠标移动处的背景
class Glass(pygame.sprite.Sprite):
    def __init__(self, glass_image, mouse_image, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.glass_image = pygame.image.load(glass_image).convert_alpha()
        self.glass_rect = self.glass_image.get_rect()
        self.glass_rect.left, self.glass_rect.top = \
            (bg_size[0] - self.glass_rect.width) // 2, \
            bg_size[1] - self.glass_rect.height

        # 添加自定义鼠标
        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect = self.mouse_image.get_rect()
        self.mouse_rect.left, self.mouse_rect.top = \
            self.glass_rect.left, self.glass_rect.top
        # 设置原来的鼠标为不可见
        pygame.mouse.set_visible(False)


def main():
    pygame.init()

    grayball_image = "Pygame/Test/g_playBall/images/gray_ball.png"
    greenball_image = "Pygame/Test/g_playBall/images/green_ball.png"
    bg_image = "Pygame/Test/g_playBall/images/background.png"
    glass_image = "Pygame/Test/g_playBall/images/glass.png"
    mouse_image = "Pygame/Test/g_playBall/images/hand.png"
    win_image = "Pygame/Test/g_playBall/images/win.png"
    gameover_image = "Pygame/Test/g_playBall/images/gameover.png"

    runing = True
    win = 0

    # 添加背景音乐
    pygame.mixer.music.load("Pygame/Test/g_playBall/sound/bg_music.ogg")
    pygame.mixer.music.play()

    # 添加音效
    loser_sound = pygame.mixer.Sound("Pygame/Test/g_playBall/sound/loser.wav")
    laugh_sound = pygame.mixer.Sound("Pygame/Test/g_playBall/sound/laugh.wav")
    winner_sound = pygame.mixer.Sound("Pygame/Test/g_playBall/sound/winner.wav")
    hole_sound = pygame.mixer.Sound("Pygame/Test/g_playBall/sound/hole.wav")

    # 音乐播放完时游戏结束
    # USEREVENT 自定义事件
    GAMEOVER = USEREVENT
    pygame.mixer.music.set_endevent(GAMEOVER)

    width, height = 1024, 681
    bg_size = width, height
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball - FishC Demo")

    background = pygame.image.load(bg_image).convert_alpha()

    # 五个球洞的坐标范围
    hole = [(116, 120, 198, 202), (224, 228, 389, 393), \
        (502, 506, 319, 323), (697, 701, 191, 195), (905, 909, 418, 422)]

    msgs = []

    balls = []
    BALL_NUM = 5
    group = pygame.sprite.Group()

    # 创建五个小球，位置随机
    for i in range(BALL_NUM):
        position = randint(0, width-100), randint(0, height-100)
        speed = [randint(1, 5), randint(1, 5)]
        ball = Ball(grayball_image, greenball_image, \
            position, speed, bg_size, 5 * (i+5))
        
        # 第三个参数为设置是否要将与 ball 碰撞的其他对象删除掉
        # 第四个参数为预定义函数，检测两个圆形是否发生碰撞
        while pygame.sprite.spritecollide(ball, group, False, \
            pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = \
                randint(0, width-100), randint(0, height-100)

        balls.append(ball)
        group.add(ball)

    glass = Glass(glass_image, mouse_image, bg_size)

    # 记录鼠标每秒钟产生事件数量
    motion = 0

    # 每隔一秒钟触发自定义事件 MYTIMER
    MYTIMER = USEREVENT + 1
    pygame.time.set_timer(MYTIMER, 1000)

    # 设置发送事件的延迟时间 set_repeat(delay, interval)
    # delay 参数指定第一次发送事件的延迟时间
    # interval 参数指定重复发送事件的时间间隔
    # 如果不带任何参数，表示取消重复发送事件
    # 此处设置按下键盘时重复发送 KEYDOWN 事件
    pygame.key.set_repeat(100, 100)

    clock = pygame.time.Clock()

    while runing:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            
            # 音乐结束，游戏结束
            elif event.type == GAMEOVER and win == 0:
                win = 1
                for each in group:
                    each.control = False
                    each.speed = [randint(1, 5), randint(1, 5)]
                loser_sound.play()
                msg = pygame.image.load(gameover_image).\
                    convert_alpha()
                msg_pos = (width - msg.get_width()) // 2, \
                    (height - msg.get_height()) // 2
                msgs.append((msg, msg_pos))
                # runing = False

            # 每隔一秒钟检测鼠标移动频率是否符合小球目标
            elif event.type == MYTIMER:
                if motion:
                    for each in group:
                        if each.check(motion):
                            if each.rect.left > 0 and \
                                    each.rect.right < width and \
                                    each.rect.top > 0 and \
                                    each.rect.bottom < height:
                                each.speed = [0, 0]
                                each.control = True
                    motion = 0

            elif event.type == MOUSEMOTION and win == 0:
                motion += 1

            elif event.type == KEYDOWN:
                if event.key == K_w:
                    for each in group:
                        if each.control:
                            each.speed[1] -= 1
                
                if event.key == K_s:
                    for each in group:
                        if each.control:
                            each.speed[1] += 1
                
                if event.key == K_a:
                    for each in group:
                        if each.control:
                            each.speed[0] -= 1
                if event.key == K_d:
                    for each in group:
                        if each.control:
                            each.speed[0] += 1

                # 玩家按下空格键判断是否有球进洞
                if event.key == K_SPACE:
                    for each in group:
                        if each.control:
                            for i in hole:
                                if i[0] <= each.rect.left <=i[1] and \
                                        i[2] <= each.rect.top <= i[3]:
                                    hole_sound.play()
                                    each.speed = [0, 0]
                                    group.remove(each)
                                    temp = balls.pop(balls.index(each))
                                    balls.insert(0, temp)
                                    hole.remove(i)
                            if not hole:
                                win = 2
                                pygame.mixer.music.stop()
                                winner_sound.play()
                                pygame.time.delay(6000)
                                msg = pygame.image.load(win_image).\
                                    convert_alpha()
                                msg_pos = (width - msg.get_width()) // 2, \
                                    (height - msg.get_height()) // 2
                                msgs.append((msg, msg_pos))

                    
        screen.blit(background, (0, 0))
        screen.blit(glass.glass_image, glass.glass_rect)

        # 将鼠标实时位置赋值给 glass.mouse_rect
        glass.mouse_rect.left, glass.mouse_rect.top = pygame.mouse.get_pos()

        # 限制自定义鼠标活动范围
        if glass.mouse_rect.left < glass.glass_rect.left:
            glass.mouse_rect.left = glass.glass_rect.left

        if glass.mouse_rect.right > glass.glass_rect.right:
            glass.mouse_rect.right = glass.glass_rect.right

        if glass.mouse_rect.top < glass.glass_rect.top:
            glass.mouse_rect.top = glass.glass_rect.top

        if glass.mouse_rect.bottom > glass.glass_rect.bottom:
            glass.mouse_rect.bottom = glass.glass_rect.bottom

        screen.blit(glass.mouse_image, glass.mouse_rect)

        for each in balls:
            each.move()
            # 碰撞后，小球速度变化
            if each.collide:
                each.speed = [randint(1, 5), randint(1, 5)]
                each.collide = False
            if each.control:
                # 画绿色的小球
                screen.blit(each.greenball_image, each.rect)
            else:
                screen.blit(each.grayball_image, each.rect)

        # 碰撞检测
        for each in group:
            group.remove(each)

            if pygame.sprite.spritecollide(each, group, False, \
                pygame.sprite.collide_circle):
                # 碰撞后，小球运动方向取反
                each.side[0] = -each.side[0]
                each.side[1] = -each.side[1]
                each.collide = True
                each.control = False

            group.add(each)

        for msg in msgs:
            screen.blit(msg[0], msg[1])

        pygame.display.flip()

        if win == 1 or win == 2:
            win = -1
            if win == 1:
                pygame.time.delay(2000)
            laugh_sound.play()

        clock.tick(60)


if __name__ == "__main__":
    main()
