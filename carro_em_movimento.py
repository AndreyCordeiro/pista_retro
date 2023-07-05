import pygame
from objeto import objeto


class CarroEmMovimento(objeto):
  
    def __init__(self, posicaoX, posicaoY, largura, altura, imagemObj,screen):
        super().__init__(posicaoX, posicaoY, largura, altura, imagemObj, screen)
        carro = pygame.image.load(imagemObj)
        self.imagem = carro
        self.configAceleracaoY = 50
        

    def movimentarCarrinho(self, dt):
        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_RIGHT]:
            self.velocidadeX = 300
            if(self.posicaoX > 1010):
                self.posicaoX = 1010
        elif comandos[pygame.K_LEFT]:
            self.velocidadeX = -300
            if(self.posicaoX < 280):
                self.posicaoX = 280
        else:
            self.velocidadeX = 0

        if comandos[pygame.K_UP]:
            self.aceleracaoY = 250
        elif comandos[pygame.K_DOWN]:
            self.aceleracaoY = -100
            if self.velocidadeYReal < 0:
                self.velocidadeYReal = 0
        else:
            self.aceleracaoY = 0

    def renderizar(self, dt, tela):
        tela.blit(self.imagem, (self.posicaoX, self.posicaoY))
