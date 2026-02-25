import pygame
import sys
import random

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Janela")

PRETO = (0, 0, 0)
fonte = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()

def cor_aleatoria():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def velocidade_aleatoria():
    while True:
        vx = random.randint(-3, 3)
        vy = random.randint(-3, 3)
        if vx != 0 or vy != 0:
            return vx, vy

cor1 = cor_aleatoria()
texto1 = fonte.render("Eduardo", True, cor1)
rect1 = texto1.get_rect(center=(200, 300))
vel_x1, vel_y1 = velocidade_aleatoria()

cor2 = cor_aleatoria()
texto2 = fonte.render("Python", True, cor2)
rect2 = texto2.get_rect(center=(600, 300))
vel_x2, vel_y2 = velocidade_aleatoria()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    rect1.x += vel_x1
    rect1.y += vel_y1

    rect2.x += vel_x2
    rect2.y += vel_y2

    for rect, vel in [(rect1, "1"), (rect2, "2")]:
        if rect.left <= 0 or rect.right >= largura:
            if vel == "1":
                vel_x1 *= -1
            else:
                vel_x2 *= -1

        if rect.top <= 0 or rect.bottom >= altura:
            if vel == "1":
                vel_y1 *= -1
            else:
                vel_y2 *= -1

    if rect1.colliderect(rect2):
        vel_x1 *= -1
        vel_y1 *= -1
        vel_x2 *= -1
        vel_y2 *= -1

        cor1 = cor_aleatoria()
        cor2 = cor_aleatoria()

        texto1 = fonte.render("Eduardo", True, cor1)
        texto2 = fonte.render("Python", True, cor2)

    tela.fill(PRETO)
    tela.blit(texto1, rect1)
    tela.blit(texto2, rect2)

    pygame.display.flip()
    clock.tick(500)

pygame.quit()
sys.exit()