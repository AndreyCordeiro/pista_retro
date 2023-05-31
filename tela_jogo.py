import pygame, time
from tela import Tela

objTela = Tela(1440, 800, [0, 100, 200, 300, 400, 500, 600, 700, 800], [500, 700, 900])

icone = pygame.image.load("./imagens/icone.jpg")
pygame.display.set_icon(icone)

tela = pygame.display.set_mode(
    (objTela.largura, objTela.altura), pygame.RESIZABLE)
pygame.display.set_caption("Pista Retro")
fps = 60
velocidade = 1
tempo_inicial = time.time()
def renderizar_tela():
    tela.fill((0, 128, 0))

    pygame.draw.rect(tela, (0, 128, 0), (1, 0, 340, 880))
    pygame.draw.rect(tela, (105, 105, 105), (300, 0, 800, 840))
    pygame.draw.rect(tela, (0, 128, 0), (1100, 0, 340, 840))

    tempo_atual = time.time() - tempo_inicial
    deslocamento = velocidade * tempo_atual * fps
    
    for x in objTela.posicoes_x:
        for y in objTela.posicoes_y:
            pygame.draw.rect(tela, (255, 255, 255), (x, y, 5, 50))

    for i, y in enumerate(objTela.posicoes_y):
        if y >= objTela.altura:
            objTela.posicoes_y[i] = 0
        objTela.posicoes_y[i] += deslocamento

    pygame.display.update()
