import pygame
from pygame.locals import *


def criar_tela():
    pygame.init()

    largura = 1440
    altura = 800
    x = [500, 700, 900]
    y = [0, 100, 200, 300, 400, 500, 600, 700, 800]

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Pista Retro")
    relogio = pygame.time.Clock()

    while True:
        relogio.tick(60)
        tela.fill((0, 128, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        desenhar_tela(tela, x, y, largura, altura)

        pygame.display.update()


def desenhar_tela(tela, x, y, largura, altura):
    tela.fill((0, 128, 0))

    pygame.draw.rect(tela, (0, 128, 0), (1, 0, 340, altura))
    pygame.draw.rect(tela, (105, 105, 105), (300, 0, largura - 600, altura))

    for i in range(len(x)):
        for j in range(len(y)):
            pygame.draw.rect(tela, (255, 255, 255), (x[i], y[j], 5, 50))
            if y[j] >= altura:
                y[j] = 0
            y[j] += 5

    pygame.draw.rect(tela, (0, 128, 0), (largura - 340, 0, 340, altura))
