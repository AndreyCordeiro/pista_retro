from sys import exit

import pygame
from pygame.locals import *
from tela import Tela
import time


def init():
    pygame.init()

    pygame.mixer.music.load('./audios/musica_tema.ogg')
    pygame.mixer.music.play(-1)  # loop infinito (-1)

    objTela = Tela(1440, 800, [-100, 100, 200, 300, 400, 500, 600, 700, 800], [500, 700, 900],
                   time.time())

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        objTela.laco_principal()
