import pygame
from objeto import Objeto


class Carro(Objeto):
    def __init__(self, posicaoX, posicaoY, largura, altura, imagemObj, screen):
        super().__init__(posicaoX, posicaoY, largura, altura, imagemObj, screen)
        carro = pygame.image.load(imagemObj)
        self.imagem = carro
        self.configAceleracaoY = 50

    def movimentarCarrinho(self, dt):
        pass

    def renderizar(self, dt, tela):
        tela.blit(self.imagem, (self.posicaoX, self.posicaoY))
