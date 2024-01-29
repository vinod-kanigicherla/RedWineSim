#import pygame
import pygame
from sys import exit
import math

#variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 494.4
TITLE_FONT = "oldenglishtext"

#initialize
pygame.init
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((165,42,42))
pygame.font.init()

#set header
pygame.display.set_caption("Red Wine Simulator")

#create clock
clock = pygame.time.Clock()

#background
background = pygame.image.load("background.jpeg")

#barrel
barrelImage = pygame.image.load('barrel.png')
barrelImage = pygame.transform.smoothscale(barrelImage, (240, 180))

#title
title1 = pygame.font.SysFont(TITLE_FONT, 50)
textSurface = title1.render('Wine Making', True, 'white')
title2 = pygame.font.SysFont(TITLE_FONT, 50)
textSurface2 = title2.render('Simulator', True, 'white')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0, 0))
    screen.blit(barrelImage, (30, 30))
    screen.blit(textSurface, (30, 300))
    screen.blit(textSurface2, (30, 350))
    #update elements
    pygame.display.update()
    clock.tick(60)
