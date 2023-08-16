import pygame
from carro import Carro


class CarroJogador(Carro):
    def __init__(self, posicaoX, posicaoY, largura, altura, imagemObj, screen):
        super().__init__(posicaoX, posicaoY, largura, altura, imagemObj, screen)

    def movimentarCarrinho(self, dt):
        comando = pygame.key.get_pressed()

        if comando[pygame.K_RIGHT] or comando[pygame.K_d]:
            self.velocidadeX = 700
            if (self.posicaoX > 1010):
                self.posicaoX = 1010
        elif comando[pygame.K_LEFT] or comando[pygame.K_a]:
            self.velocidadeX = -700
            if (self.posicaoX < 280):
                self.posicaoX = 280
        else:
            self.velocidadeX = 0

        if comando[pygame.K_UP] or comando[pygame.K_w]:
            self.aceleracaoY = 500
        elif comando[pygame.K_DOWN] or comando[pygame.K_s]:
            self.aceleracaoY = -600
            if self.velocidadeYReal < 0:
                self.velocidadeYReal = 0
        else:
            self.aceleracaoY = 0