import pygame


class CarroEmMovimento:
  

    def __init__(self, x, y):
        carro = pygame.image.load("./imagens/carro_vermelho.png")
        self.imagem = carro
        self.x = x
        self.y = y
        self.v = 5

    def movimentarCarrinho(self):
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]:
            self.x += self.v
        if comandos[pygame.K_LEFT]:
            self.x -= self.v