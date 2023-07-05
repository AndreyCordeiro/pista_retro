from sys import exit

import pygame
from pygame.locals import *
from tela import Tela
import time


def init():
    pygame.init()

    #velocidade = 60.0

    objTela = Tela(1440, 800, [-100, 100, 200, 300, 400, 500, 600, 700, 800], [500, 700, 900], 
               time.time())

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        objTela.lacoPrincipal()
       #velocidade += 1
