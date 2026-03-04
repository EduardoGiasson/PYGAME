import pygame
import sys

PRETO=(0, 0, 0)
BRANCO=(255, 255, 255)

LARGURA=800
ALTURA=600

tela=pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong")

clock=pygame.time.Clock()

raquete_largura = 10
raquete_altura = 60
tamanho_bola = 10

player1_x = 15
player1_y = ALTURA // 2 - raquete_altura // 2

player2_x = LARGURA - 30 - raquete_largura
player2_y = ALTURA // 2 - raquete_altura // 2

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill(PRETO)

    pygame.draw.rect(tela, BRANCO, (player1_x, player1_y, raquete_largura, raquete_altura))
    pygame.draw.rect(tela, BRANCO, (player2_x, player2_y, raquete_largura, raquete_altura))
    pygame.display.flip()
    clock.tick(60)
import pygame
import sys

PRETO=(0, 0, 0)
BRANCO=(255, 255, 255)

LARGURA=800
ALTURA=600

tela=pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong")

clock=pygame.time.Clock()

raquete_largura = 10
raquete_altura = 60
tamanho_bola = 10

player1_x = 15
player1_y = ALTURA // 2 - raquete_altura // 2

player2_x = LARGURA - 15- raquete_largura
player2_y = ALTURA // 2 - raquete_altura // 2

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill(PRETO)

    pygame.draw.rect(tela, BRANCO, (player1_x, player1_y, raquete_largura, raquete_altura))
    pygame.draw.rect(tela, BRANCO, (player2_x, player2_y, raquete_largura, raquete_altura))
    pygame.display.flip()
    clock.tick(60)