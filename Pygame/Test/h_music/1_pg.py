#
# 1_pg.py
# @author bulbasaur
# @description 播放音效（左键、右键、空格）
# @created 2019-07-30T23:47:27.667Z+08:00
# @last-modified 2019-07-31T08:42:38.213Z+08:00
#

import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Pygame/Test/h_music/bg_music.ogg")
# 设置音量
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

cat_sound = pygame.mixer.Sound("Pygame/Test/h_music/cat.wav")
cat_sound.set_volume(0.2)
dog_sound = pygame.mixer.Sound("Pygame/Test/h_music/dog.wav")
dog_sound.set_volume(0.2)

width, height = 300, 200
bg_size = width, height
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("Music - FishC Demo")

pause = False

pause_image = pygame.image.load("Pygame/Test/h_music/pause.png").convert_alpha()
unpause_image = pygame.image.load("Pygame/Test/h_music/unpause.png").convert_alpha()
pause_rect = pause_image.get_rect()
pause_rect.left, pause_rect.top = (width - pause_rect.width) \
    // 2, (height - pause_rect.height) // 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                cat_sound.play()
            if event.button == 3:
                dog_sound.play()
            
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause = not pause
        
    screen.fill((255, 255, 255))

    if pause:
        screen.blit(pause_image, pause_rect)
        pygame.mixer.music.pause()
    else:
        screen.blit(unpause_image, pause_rect)
        pygame.mixer.music.unpause()

    pygame.display.flip()

    clock.tick(30)
