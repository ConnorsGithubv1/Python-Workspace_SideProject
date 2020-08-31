import pygame, sys, os

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()  # initiates pygame

pygame.display.set_caption('Pygame Platformer')

display_width = 300
display_height = 200
WINDOW_SIZE = (display_width, display_height)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate the window

display = pygame.Surface((100, 80))  # used as the surface for rendering, which is scaled

current_frame = 0

grey = (12,12,12)

idle_animation = []
idle_animation.append(pygame.image.load('player/idle/0.png'))
idle_animation.append(pygame.image.load('player/idle/1.png'))
idle_animation.append(pygame.image.load('player/idle/2.png'))
idle_animation.append(pygame.image.load('player/idle/3.png'))

run_animation = []
run_animation.append(pygame.image.load('player/run/0.png'))
run_animation.append(pygame.image.load('player/run/1.png'))
run_animation.append(pygame.image.load('player/run/2.png'))
run_animation.append(pygame.image.load('player/run/3.png'))
run_animation.append(pygame.image.load('player/run/4.png'))
run_animation.append(pygame.image.load('player/run/5.png'))

image = idle_animation[current_frame]
player_rect = image.get_rect()
player_rect2 = pygame.draw.rect(display, grey, (0,0,61,59))
print(player_rect)
player_rect.topleft = [0,0]

moving_right = False
current_animation = idle_animation



while True:  # game loop

    for event in pygame.event.get():  # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                moving_right = True
        if event.type == KEYUP:
            if event.key == K_d:
                moving_right = False

    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))

    display.fill(grey)

    current_frame += 0.15

    if moving_right == False:
        image = idle_animation[int(current_frame)]
        current_animation = idle_animation

    if moving_right == True:
        image = run_animation[int(current_frame)]
        current_animation = run_animation

    pygame.draw.rect(display, grey, (0, 0, 61, 59))
    display.blit(image, (0,0))
    if current_frame >= len(current_animation) - 0.15:
        current_frame = 0

    pygame.display.update()
    clock.tick(60)
