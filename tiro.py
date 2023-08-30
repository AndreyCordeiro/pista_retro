import pygame
from objeto import Objeto
from tipo_objeto import TipoObjeto


class Tiro(Objeto):
    def __init__(self, posicaoX, posicaoY, largura, altura, imagemObj, screen):
        super().__init__(posicaoX, posicaoY, largura, altura, imagemObj, screen)
        tiro = pygame.image.load(imagemObj)
        self.imagem = tiro
        self.configAceleracaoY = 50
        self.largura = self.imagem.get_width()
        self.altura = self.imagem.get_height()
        self.tipo = TipoObjeto.TIRO

    def renderizar(self, dt, tela):
        tela.blit(self.imagem, (self.posicaoX, self.posicaoY))
