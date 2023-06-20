import pygame
import time

class Tela: 
    def __init__(self, largura, altura, posicoes_y, posicoes_x, tempo_inicial):
        self.largura = largura                                
        self.altura = altura
        self.posicoes_y = posicoes_y
        self.posicoes_x = posicoes_x
        self.tempo_inicial = tempo_inicial
        self.tempo_ultimo = self.tempo_inicial
        self.tempo_decorrido = 0.0
        self.posicao_pista = 0
        self.deslocamento_pista = 0
        self.tela = pygame.display.set_mode((self.largura, self.altura), pygame.RESIZABLE)
        self.icone = pygame.image.load("./imagens/icone.jpg")
        self.tela.fill((0, 128, 0))
        pygame.display.set_icon(self.icone)

        pygame.display.set_caption("Pista Retro")


    def renderizar_tela(self, velocidade_pista):

        pygame.draw.rect(self.tela, (0, 128, 0), (1, 0, 340, 880))
        pygame.draw.rect(self.tela, (105, 105, 105), (300, 0, 800, 840))
        pygame.draw.rect(self.tela, (0, 128, 0), (1100, 0, 340, 840))

        self.deslocamento_pista = velocidade_pista * self.tempo_decorrido
        self.posicao_pista += self.deslocamento_pista

        print(self.tempo_decorrido)
        print(velocidade_pista)

        for x in self.posicoes_x:
            for y in self.posicoes_y:
                pygame.draw.rect(self.tela, (255, 255, 255), (x, y, 5, 50))

        for i, y in enumerate(self.posicoes_y):
            if y >= self.altura:
                self.posicoes_y[i] = 0
            self.posicoes_y[i] += self.deslocamento_pista

        pygame.display.update()
        t = time.time()
        self.tempo_decorrido = t - self.tempo_ultimo
        self.tempo_ultimo = t
