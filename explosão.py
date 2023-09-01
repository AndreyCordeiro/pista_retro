import pygame
from objeto import Objeto
from tipo_objeto import TipoObjeto


class Explosao(Objeto):
    def __init__(self, posicaoX, posicaoY, largura, altura, imagemObj, screen):
        super().__init__(posicaoX, posicaoY, largura, altura, imagemObj, screen)
        tiro = pygame.image.load(imagemObj)
        self.imagem = tiro
        self.configAceleracaoY = 50
        self.largura = 10
        self.altura = 10
        self.tipo = TipoObjeto.GENERICO
        self.tempo_de_vida = 5000 
        
    

    def renderizar(self, dt, tela):
        tela.blit(self.imagem, (self.posicaoX, self.posicaoY))


    def criar_explosão(self, obj: Objeto):
        explosao = Explosao(posicaoY=obj.posicaoY, posicaoX=obj.posicaoX, imagemObj="./imagens/explosao.png", largura=0, altura=0, screen=self)
        self.adicionar_objeto(explosao)
        
    def atualizar(self, dt):
        self.tempo_de_vida -= dt
        if self.tempo_de_vida <= 0:
            self.remover()
    
        
       
        

   