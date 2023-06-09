import pygame
import time
from objeto import objeto
from carro_em_movimento import CarroEmMovimento

#carro = CarroEmMovimento(y= 600, x= 400)

class Tela: 
    def __init__(self, largura, altura, posicoes_y, posicoes_x, tempo_inicial):
        self.largura = largura                                
        self.altura = altura
        self.posicoes_y = posicoes_y
        self.posicoes_x = posicoes_x
        self.tempo_inicial = tempo_inicial
        self.tempo_ultimo = self.tempo_inicial
        self.tempo_decorrido = 0.0
        self.posicao_pista = 0
        self.deslocamento_pista = 0
        self.tela = pygame.display.set_mode((self.largura, self.altura), pygame.RESIZABLE)
        self.icone = pygame.image.load("./imagens/icone.jpg")
        self.tela.fill((0, 128, 0))
        pygame.display.set_icon(self.icone)

        pygame.display.set_caption("Pista Retro")
        self.carro = CarroEmMovimento(posicaoY=600, posicaoX=40, imagemObj="./imagens/carro_vermelho.png", largura=0, altura=0,screen=self)
        self.objetos = []

        self.adicionarObjeto(self.carro)

    def adicionarObjeto(self, objeto):
        self.objetos.append(objeto)

    def processamentoFisica(self, dt):
        self.carro.movimentarCarrinho(dt)
        for obj in self.objetos:
            obj.processarFisica(dt)

  
        

    def renderizar_tela(self, dt):
        self.renderizar_pista(dt)
        self.carro.renderizar(dt, self.tela)
        

    def renderizar_pista(self, dt):
        pygame.draw.rect(self.tela, (0, 128, 0), (1, 0, 340, 880))
        pygame.draw.rect(self.tela, (105, 105, 105), (300, 0, 800, 840))
        pygame.draw.rect(self.tela, (0, 128, 0), (1100, 0, 340, 840))

        velocidade_pista = self.carro.velocidadeYReal

        self.deslocamento_pista = velocidade_pista * self.tempo_decorrido
        self.posicao_pista += self.deslocamento_pista

        for x in self.posicoes_x:
            for y in self.posicoes_y:
                pygame.draw.rect(self.tela, (255, 255, 255), (x, y, 5, 50))

        for i, y in enumerate(self.posicoes_y):
            if y >= self.altura:
                self.posicoes_y[i] = 0
            self.posicoes_y[i] += self.deslocamento_pista

    def lacoPrincipal(self):
        #arbusto = objeto(self.largura/64  , 400, 150, 150, 'imagens/arbusto.png',0)
        #print(self.tempo_decorrido)
        #print(velocidade_pista)
        #self.tela.blit(arbusto.imagem, (arbusto.posicaoX, arbusto.posicaoY))

        self.processamentoFisica(self.tempo_decorrido)
        self.renderizar_tela(self.tempo_decorrido)
        pygame.display.update()
        t = time.time()
        self.tempo_decorrido = t - self.tempo_ultimo
        self.tempo_ultimo = t
     

                