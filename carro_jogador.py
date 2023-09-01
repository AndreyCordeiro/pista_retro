import pygame
from carro import Carro
from tiro import Tiro
from tipo_objeto import TipoObjeto


class CarroJogador(Carro):
    def __init__(self, posicaoX, posicaoY, largura, altura, imagemObj, screen):
        super().__init__(posicaoX, posicaoY, largura, altura, imagemObj, screen)

        self.tipo = TipoObjeto.JOGADOR
        self.cooldown_timer = 0
        self.cooldown_duration = 0.5

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

        if comando[pygame.K_SPACE]:
            self.atirar(dt)

    def atirar(self, dt):
        if self.cooldown_timer <= 0:
            sprite = "./imagens/bomba.png"

            tiro = Tiro(
                posicaoY=self.posicaoY, posicaoX=self.posicaoX, imagemObj=sprite, largura=0, altura=0, screen=self.screen)

            tiro.velocidadeX = 0
            tiro.velocidadeYReal = self.velocidadeYReal + 1600

            self.screen.adicionar_objeto(tiro)

            self.cooldown_timer = self.cooldown_duration
        #else:
           # print('Aguarde para atirar novamente.')

    def atualizar_timer(self, dt):
        self.cooldown_timer -= dt

        if self.cooldown_timer < 0:
            self.cooldown_timer = 0
