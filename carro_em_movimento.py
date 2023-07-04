import pygame


class CarroEmMovimento:

    def __init__(self, x, y):
        carro = pygame.image.load("./imagens/carro_vermelho.png")
        self.imagem = carro
        self.x = x
        self.y = y
        self.v = 5

    def movimentarCarrinho(self):
        comando = pygame.key.get_pressed()

        if comando[pygame.K_RIGHT] or comando[pygame.K_d]:
            self.x += self.v
            if (self.x > 1010):
                self.x = 1010

        if comando[pygame.K_LEFT] or comando[pygame.K_a]:
            self.x -= self.v
            if (self.x < 280):
                self.x = 280
