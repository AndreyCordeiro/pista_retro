from sys import exit

import pygame
from pygame.locals import *

import menu


def init():
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        menu.criar_menu()
