import pygame
from carro import Carro
import random


class CarroBot(Carro):
    def __init__(self, posicaoX, posicaoY, largura, altura, imagemObj, screen):
        super().__init__(posicaoX, posicaoY, largura, altura, imagemObj, screen)

        self.velocidadeYReal = random.uniform(
            0, 0.7 * self.screen.carro.velocidadeYReal)

    def movimentarCarrinho(self, dt):
        a = 0