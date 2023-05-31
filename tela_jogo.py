import pygame
from objeto import objeto

largura = 1440
altura = 800
posicoes_y = [0, 100, 200, 300, 400, 500, 600, 700, 800]
posicoes_x = [500, 700, 900]

icone = pygame.image.load("./imagens/icone.jpg")
pygame.display.set_icon(icone)

tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
pygame.display.set_caption("Pista Retro")


def criar_tela():
    tela.fill((0, 128, 0))
    arbusto = objeto(largura/4  , 400, 10, 20, 'imagens/arbusto.png')
    imagemArbusto = pygame.image.load(arbusto.imagemObj)

    pygame.draw.rect(tela, (0, 128, 0), (1, 0, 340, 880))
    pygame.draw.rect(tela, (105, 105, 105), (300, 0, 800, 840))
    pygame.draw.rect(tela, (0, 128, 0), (1100, 0, 340, 840))

    for x in posicoes_x:
        for y in posicoes_y:
            pygame.draw.rect(tela, (255, 255, 255), (x, y, 5, 50))

    for i, y in enumerate(posicoes_y):
        if y >= altura:
            posicoes_y[i] = 0
        posicoes_y[i] += 3  # velocidade do carro * tempo (frame)

    tela.blit(imagemArbusto, (arbusto.posicaoX, arbusto.posicaoY))

    pygame.display.update()

# Para ajustar o commit https://www.youtube.com/watch?v=k_7UZ1wlIxw
