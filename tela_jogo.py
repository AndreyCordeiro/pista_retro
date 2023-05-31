import pygame
pygame.font.init()

largura = 1440
altura = 800
posicoes_y = [0, 100, 200, 300, 400, 500, 600, 700, 800]
posicoes_x = [500, 700, 900]

icone = pygame.image.load("./imagens/icone.jpg")
pygame.display.set_icon(icone)

tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
pygame.display.set_caption("Pista Retro")

pontos = 0

def criar_tela():

    global pontos

    tela.fill((0, 128, 0))

    pygame.draw.rect(tela, (0, 128, 0), (1, 0, 340, 880))
    pygame.draw.rect(tela, (105, 105, 105), (300, 0, 800, 840))
    pygame.draw.rect(tela, (0, 128, 0), (1100, 0, 340, 840))

    for x in posicoes_x:
        for y in posicoes_y:
            pygame.draw.rect(tela, (255, 255, 255), (x, y, 5, 50))

    for i, y in enumerate(posicoes_y):
        if y >= altura:
            posicoes_y[i] = 0
            pontos += 1  # Incrementar o contador de pontos
        posicoes_y[i] += 3  # Velocidade do carro * tempo (frame)

    exibir_pontos()

    pygame.display.update()


def exibir_pontos():
    fonte = pygame.font.SysFont(None, 36)
    texto = fonte.render(str(pontos).zfill(6), True, (255, 255, 255))
    tela.blit(texto, (1300, 20))


while True:
    criar_tela()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
