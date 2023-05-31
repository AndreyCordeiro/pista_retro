# pylint: disable=missing-class-docstring
import pygame


class Objeto(pygame.sprite.Sprite):
    def __init__(self, posicaoX, posicaoY, largura, altura, imagemObj, velocidade):
        pygame.sprite.Sprite.__init__(self)
        imagemArbusto = pygame.image.load(imagemObj)
        objeto_imagem = pygame.transform.scale(imagemArbusto, (largura, altura))

        self.altura = altura
        self.largura = largura
        self.posicaoX = posicaoX
        self.posicaoY = posicaoY
        self.image = objeto_imagem
        self.rect = self.image.get_rect()
        self.velocidade = velocidade

    def update(self):
        self.rect.x += self.velocidade
