from sys import exit

import pygame
from pygame.locals import *

import tela_jogo


def init():
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        tela_jogo.renderizar_tela()
