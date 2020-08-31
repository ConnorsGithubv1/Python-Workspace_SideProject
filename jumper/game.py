import warnings

from pygame.locals import *

import pygame, sys

clock = pygame.time.Clock()

# Python 3, Tkinter 8.6
# Centering Root Window on Screen

from tkinter import *

# initialization
pygame.init()

infoObject = pygame.display.Info()

display_width = 1280
display_height = 720
screensize = display_width, display_height

gameDisplay = pygame.display.set_mode((1280, 720))

# colors
black = (16, 16, 16)
white = (255, 255, 255)
red = (170, 0, 0, 128)
bright_red = (255, 100, 0)
blueviolet = (138, 43, 226)
purple = (147, 112, 219)

# image paths
stage = pygame.image.load("media/stage_01.png")
grass = pygame.image.load("media/grass.png")
dirt = pygame.image.load("media/dirt.png")

# scaling
scale_factor = 4
stage1 = pygame.transform.scale(stage, (1024 * scale_factor, 128 * scale_factor))
dirt = pygame.transform.scale(dirt, (16 * scale_factor, 16 * scale_factor))
grass = pygame.transform.scale(grass, (16 * scale_factor, 16 * scale_factor))

# map spacing
map_space = []

# gamemmap
game_map = [
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [-1, -1, -1, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, ],
    [-1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, 0, 0, 0,
     -1, -1, -1, -1, -1, -1, -1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ],
]

# player
player = pygame.image.load('media/sasuke_right.png')
playerlocation = [5, 64 * 2]
playerYmomentum = 0
playerX = player.get_width()
playerY = player.get_height()

# physics
gravity = 8
mass = -2

# movement
moving_right = False
moving_left = False
moving = False
jump = False
jumptimer = 0
currenttimer = 0


# camera
camera = False
xVal = 0


tilelocationlist = []

def creategamemap(gamemap):
    tilerects = []
    y = 0
    for layers in game_map:
        x = 0
        for tiles in layers:
            if tiles == -1:
                gameDisplay.blit(dirt, (xVal + x * 64, y * 64), )
                createrect(64, 64, xVal + x*64 , y *64 )
                tileloc = x, y
                tilelocationlist.append(tileloc)
            if tiles == 2:
                gameDisplay.blit(grass, (xVal + x * 64, y * 64))
            x = x + 1
        y = y + 1

#tile rectangle
def createrect(tileY, tileX, x, y):
    return pygame.draw.rect(gameDisplay, red, (x, y, tileX, tileY))

# player rectangle
def playerrect(playersizeX, playersizeY, playerlocation):
    return pygame.draw.rect(gameDisplay, 0, (playerlocation[0], playerlocation[1], playerX, playerY))


# hides the warnings
def hidewarnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)


# force
def force(gravity, mass):
    return mass * gravity




def game():
    global playerlocation, playerYmomentum, player, moving_left, moving_right, moving, camera, xVal, jumpcount, jump, jumptimer, game_map, jumptimer, currenttimer
    running = True
    # GameLoop
    while running:

        gameDisplay.fill(black)

        if playerlocation[1] > screensize[1] - player.get_height():
            playerYmomentum = 0
        else:
            playerYmomentum += 0.2
        playerlocation[1] += playerYmomentum

        if playerlocation[0] >= display_width / 2:
            camera = True

        if playerlocation[1] - 32 >= 600:
            jumpcount = 2
            jumptimer = 3

        if moving_right == True:
            playerlocation[0] += 4
            xVal -= 4
            player = pygame.image.load('media/sasuke_right.png')
        if moving_left == True:
            playerlocation[0] -= 4
            xVal += 4
            player = pygame.image.load('media/sasuke_left.png')
            
        if jump == True:
            jumptimer = pygame.time.get_ticks()

        if currenttimer - jumptimer < 2000:
            gameDisplay.fill(red)


        if camera == True:
            gameDisplay.blit(stage1, (xVal + display_width / 2, 104))
        else:
            gameDisplay.blit(stage1, (0, 104))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                if event.key == K_d:
                    moving = False
                    moving_right = True
                if event.key == K_a:
                    moving = False
                    moving_left = True
                if event.key == K_SPACE:
                    jump = True

            if event.type == KEYUP:
                if event.key == K_d:
                    moving = True
                    moving_right = False
                if event.key == K_a:
                    moving = True
                    moving_left = False
                if event.key == K_SPACE:
                    jump = False

        creategamemap(game_map)
        hidewarnings()
        gameDisplay.blit(player, playerlocation)
        currenttimer = pygame.time.get_ticks()
        #playerrect(playerX, playerY, playerlocation)
        pygame.display.update()
        clock.tick(60)


# Enter the mainloop----------------------------------------------------------
game()

pygame.quit()
sys.exit()
