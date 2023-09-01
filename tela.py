import pygame
import time
from objeto import Objeto
from carro_jogador import CarroJogador
from carro_bot import CarroBot
import random
import pygame_menu
import init
from tipo_objeto import TipoObjeto


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
            posicaoY=600, posicaoX=670, imagemObj="./imagens/carro_vermelho.png", largura=0, altura=0, screen=self)
        self.objetos = []
        self.imagem_fundo = "./imagens/background_menu.png"

        self.adicionar_objeto(self.carro)

    def adicionar_objeto(self, objeto):
        self.objetos.append(objeto)

    def remover_objeto(self, objeto):
        self.objetos.remove(objeto)

    def processamento_fisica(self, dt):
        self.carro.movimentarCarrinho(dt)

        for obj in self.objetos:
            if obj.vivo:
                obj.processarFisica(dt)

    def renderizar_tela(self, dt):
        self.renderizar_pista(dt)

        for obj in self.objetos:
            if obj.vivo:
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
        self.colisao()
        self.carro.atualizar_timer(self.tempo_decorrido)

        pygame.display.update()

        t = time.time()
        self.tempo_decorrido = t - self.tempo_ultimo
        self.tempo_ultimo = t

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
        if obj.vivo == False or obj_2.vivo == False:
            return False
        else:
            return (abs((obj.posicaoX + obj.largura/2.0) - (obj_2.posicaoX + obj_2.largura/2.0)) < ((obj.largura + obj_2.largura) / 2.0) and abs((obj.posicaoY + obj.altura/2.0) - (obj_2.posicaoY + obj_2.altura/2.0)) < ((obj.altura + obj_2.altura) / 2.0))

    def tratar_colisao_bot(self, player, bot):
        init.mostrar_menu(self.imagem_fundo, False)

    def tratar_explosao(self, tiro, bot):
        som_explosao = pygame.mixer.Sound('./audios/explosao.ogg')
        som_explosao.set_volume(0.3)
        som_explosao.play()

        bot.vivo = False
        
    def objectos_colididos(self, obj: Objeto, obj_2: Objeto):
        if (obj.tipo == TipoObjeto.JOGADOR and obj_2.tipo == TipoObjeto.BOT):
            self.tratar_colisao_bot(obj, obj_2)
        elif (obj.tipo == TipoObjeto.BOT and obj_2.tipo == TipoObjeto.JOGADOR):
            self.tratar_colisao_bot(obj_2, obj)
        elif (obj.tipo == TipoObjeto.BOT and obj_2.tipo == TipoObjeto.TIRO):
            self.tratar_explosao(obj_2, obj)
        elif (obj.tipo == TipoObjeto.TIRO and obj_2.tipo == TipoObjeto.BOT):
            self.tratar_explosao(obj, obj_2)

    def colisao(self):
        for i in range(0, len(self.objetos) - 1):
            for j in range(i+1, len(self.objetos)):
                if (self.objetos_em_colisao(self.objetos[j], self.objetos[i])):
                    self.objectos_colididos(
                        self.objetos[j], self.objetos[i])
