import pygame
import time
from objeto import Objeto
from carro_jogador import CarroJogador
from carro_bot import CarroBot
import random
import pygame_menu
import init

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
        self.tela = pygame.display.set_mode(
            (self.largura, self.altura), pygame.RESIZABLE)
        self.icone = pygame.image.load("./imagens/icone.jpg")
        self.tela.fill((0, 128, 0))
        pygame.display.set_icon(self.icone)

        pygame.display.set_caption("Pista Retro")
        self.carro = CarroJogador(
            posicaoY=600, posicaoX=40, imagemObj="./imagens/carro_vermelho.png", largura=0, altura=0, screen=self)
        self.objetos = []

        self.adicionar_objeto(self.carro)

    def adicionar_objeto(self, objeto):
        self.objetos.append(objeto)

    def processamento_fisica(self, dt):
        self.carro.movimentarCarrinho(dt)

        for obj in self.objetos:
            obj.processarFisica(dt)

    def renderizar_tela(self, dt):
        self.renderizar_pista(dt)

        for obj in self.objetos:
            obj.renderizar(dt, self.tela)

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

    def laco_principal(self):
        self.processamento_fisica(self.tempo_decorrido)
        self.renderizar_tela(self.tempo_decorrido)
        self.spawn_carrinhos(self.tempo_decorrido)
        self.collision()

        pygame.display.update()

        t = time.time()
        self.tempo_decorrido = t - self.tempo_ultimo
        self.tempo_ultimo = t

    def iniciar_jogo():
        init.init()

    def spawn_carrinhos(self, dt):
        caminho = "./imagens/"
        posicoes_spawn = [350, 550, 750, 950]
        sprites = [f"{caminho}carro_azul.png", f"{caminho}carro_amarelo.png", f"{caminho}carro_preto.png",
                   f"{caminho}carro_verde.png", f"{caminho}carro_roxo.png"]

        if random.randint(0, 100) < 1:
            posicao_spawn = random.choice(posicoes_spawn)
            sprite_carrinho = random.choice(sprites)

            novo_carrinho = CarroBot(
                posicaoY=0, posicaoX=posicao_spawn, imagemObj=sprite_carrinho, largura=0, altura=0, screen=self)

            self.adicionar_objeto(novo_carrinho)

    def objetos_em_colisao(self, obj: Objeto, obj_2: Objeto):
        return (abs((obj.posicaoX + obj.largura/2.0) - (obj_2.posicaoX + obj_2.largura/2.0)) < ((obj.largura + obj_2.largura) / 2.0) and abs((obj.posicaoY + obj.altura/2.0) - (obj_2.posicaoY + obj_2.altura/2.0)) < ((obj.altura + obj_2.altura) / 2.0))

    def objectos_colididos(self, obj: Objeto, obj_2: Objeto):
        if (obj == self.carro or obj_2 == self.carro):
            surface = pygame.display.set_mode((1440, 800))
            menu = pygame_menu.Menu('Pista Retro', 1440, 800,
                                    theme=pygame_menu.themes.THEME_DEFAULT)
            
            menu.add.button('Jogar', self.iniciar_jogo)
            menu.add.button('Sair', pygame_menu.events.EXIT)

            menu.mainloop(surface)

    def collision(self):
        for i in range(0, len(self.objetos) - 1):
            for j in range(i+1, len(self.objetos)):
                if (self.objetos_em_colisao(self.objetos[j], self.objetos[i])):
                    self.objectos_colididos(
                        self.objetos[j], self.objetos[i])