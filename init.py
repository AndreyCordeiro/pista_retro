from sys import exit

import pygame
from pygame.locals import *
from tela import Tela
import time


def init():
    pygame.init()

    objTela = Tela(1440, 800, [-100, 100, 200, 300, 400, 500, 600, 700, 800], [500, 700, 900], 
               time.time(), 60.0)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        objTela.renderizar_tela()
