from sys import exit
import pygame
from pygame.locals import *
from tela import Tela
import time
import pygame_menu

def iniciar(imagem_fundo, menu_game_over):
    pygame.init()

    pygame.mixer.music.load('./audios/musica_tema.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # loop infinito (-1)

    mostrar_menu(imagem_fundo, menu_game_over)


def iniciar_jogo():
    objTela = Tela(1440, 800, [-100, 100, 200, 300, 400, 500, 600, 700, 800], [500, 700, 900],
                   time.time())

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        objTela.laco_principal()

def mostrar_menu(imagem_fundo, menu_game_over):
    surface = pygame.display.set_mode((1440, 800))
    meu_tema = pygame_menu.themes.Theme(background_color=(20, 139, 34),
                                        widget_margin=( 0 , 10 ),
                                        widget_padding=(10, 40),
                                        selection_color=(0, 0, 0),
                                        title_font_size=50,
                                        title_font_color=(255, 255, 255),
                                        widget_font_size=40,
                                        widget_font_color=(255, 255, 255),
                                        widget_background_color=(0, 0, 0, 0),
                                        widget_offset=(20, 20))
    banner_game_over = "./imagens/banner_game_over.png"

    menu = pygame_menu.Menu('Pista Retro', 1440, 800,
                            theme=meu_tema)
    if menu_game_over:
        menu.add.image(banner_game_over, angle=0, scale=(1.5, 0.75), align=pygame_menu.locals.ALIGN_CENTER)
    menu.add.button('Jogar', iniciar_jogo, align=pygame_menu.locals.ALIGN_CENTER)
    menu.add.button('Sair', pygame_menu.events.EXIT, align=pygame_menu.locals.ALIGN_CENTER)
    menu.add.image(imagem_fundo, angle=0, scale=(1.8, 1.5), align=pygame_menu.locals.ALIGN_CENTER)
    
    menu.mainloop(surface)
