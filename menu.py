import pygame
import pygame_menu
import tela_jogo

largura = 1440
altura = 800


def criar_menu():
    pygame.init()

    pygame.mixer.music.load('./audios/main_menu.ogg')
    pygame.mixer.music.play(-1)  # loop infinito (-1)

    surface = pygame.display.set_mode((largura, altura))
    menu = pygame_menu.Menu('Pista Retro', largura, altura,
                            theme=pygame_menu.themes.THEME_DEFAULT)

    menu.add.selector(
        'Dificuldade :', [('Fácil', 1), ('Médio', 2), ('Difícil', 3)], onchange=set_difficulty)
    menu.add.button('Jogar', iniciar_jogo)
    menu.add.button('Sair', pygame_menu.events.EXIT)

    menu.mainloop(surface)


def set_difficulty(value, difficulty):
    pass


def iniciar_jogo():
    tela_jogo.criar_tela()
