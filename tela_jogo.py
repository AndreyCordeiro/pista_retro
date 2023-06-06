import pygame, time
from tela import Tela

objTela = Tela(1440, 800, [0, 100, 200, 300, 400, 500, 600, 700, 800], [500, 700, 900], 
               time.time(), time.time(), 0.0, 60.0, 0, 0)

icone = pygame.image.load("./imagens/icone.jpg")
pygame.display.set_icon(icone)

tela = pygame.display.set_mode(
    (objTela.largura, objTela.altura), pygame.RESIZABLE)
pygame.display.set_caption("Pista Retro")

def renderizar_tela():
    tela.fill((0, 128, 0))

    pygame.draw.rect(tela, (0, 128, 0), (1, 0, 340, 880))
    pygame.draw.rect(tela, (105, 105, 105), (300, 0, 800, 840))
    pygame.draw.rect(tela, (0, 128, 0), (1100, 0, 340, 840))

    objTela.deslocamento_pista = objTela.velocidade_pista * objTela.tempo_decorrido
    objTela.posicao_pista = objTela.posicao_pista + objTela.deslocamento_pista
        

    for x in objTela.posicoes_x:
        for y in objTela.posicoes_y:
            pygame.draw.rect(tela, (255, 255, 255), (x, y, 5, 50))

    for i, y in enumerate(objTela.posicoes_y):
        if y >= objTela.altura:
            objTela.posicoes_y[i] = 0
        objTela.posicoes_y[i] += objTela.deslocamento_pista

    pygame.display.update()
    t = time.time()
    objTela.tempo_decorrido = t - objTela.tempo_ultimo
    objTela.tempo_ultimo = t

