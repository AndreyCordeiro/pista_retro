import pygame
from tipo_objeto import TipoObjeto

class Objeto(pygame.sprite.Sprite):
    def __init__(self, posicaoX, posicaoY, largura, altura, imagemObj, screen):
        pygame.sprite.Sprite.__init__(self)
        imagemArbusto = pygame.image.load(imagemObj)
        objeto_imagem = pygame.transform.scale(
            imagemArbusto, (largura, altura))

        self.altura = altura
        self.largura = largura
        self.posicaoX = posicaoX
        self.posicaoY = posicaoY
        self.imagem = objeto_imagem
        self.rect = self.imagem.get_rect()
        self.velocidadeX = 0
        self.velocidadeYReal = 0
        self.velocidadeYVirtual = 0
        self.screen = screen
        self.aceleracaoY = 0
        self.tipo = TipoObjeto.GENERICO
        self.vivo = True

    def processarFisica(self, dt):
        self.velocidadeYVirtual = (self.velocidadeYReal - self.screen.carro.velocidadeYReal) * -1
        self.velocidadeYReal = self.velocidadeYReal + (self.aceleracaoY * dt)
        self.posicaoX = self.posicaoX + (self.velocidadeX * dt)
        self.posicaoY = self.posicaoY + (self.velocidadeYVirtual * dt)
