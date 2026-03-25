import random
import pygame
import sys

pygame.init()
class Cores:
    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
class Config:
    LARGURA = 800
    ALTURA = 600
    FPS = 60
class JogoConfig:
    RAQUETE_LARGURA = 10
    RAQUETE_ALTURA = 60
    TAMANHO_BOLA = 7
    VELOCIDADE_RAQUETE = 5

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, direcao):
        self.y += direcao * JogoConfig.VELOCIDADE_RAQUETE

        if self.y < 0:
            self.y = 0
        elif self.y > Config.ALTURA - JogoConfig.RAQUETE_ALTURA:
            self.y = Config.ALTURA - JogoConfig.RAQUETE_ALTURA

    def ia(self, bola_y):
        if self.y + JogoConfig.RAQUETE_ALTURA//2 < bola_y:
            self.mover(1)
        elif self.y + JogoConfig.RAQUETE_ALTURA//2 > bola_y:
            self.mover(-1)

    def desenhar(self, tela):
        pygame.draw.rect(
            tela,
            Cores.BRANCO,
            (self.x, self.y, JogoConfig.RAQUETE_LARGURA, JogoConfig.RAQUETE_ALTURA)
        )

    def get_rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            JogoConfig.RAQUETE_LARGURA,
            JogoConfig.RAQUETE_ALTURA
        )

class Bola:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = Config.LARGURA//2 - JogoConfig.TAMANHO_BOLA//2
        self.y = Config.ALTURA//2 - JogoConfig.TAMANHO_BOLA//2
        self.vel_x = random.choice([-5, 5])
        self.vel_y = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y

        if self.y <= 0 or self.y >= Config.ALTURA - JogoConfig.TAMANHO_BOLA:
            self.vel_y = -self.vel_y

    def colisao(self, player1, player2):
        if self.get_rect().colliderect(player1.get_rect()) or self.get_rect().colliderect(player2.get_rect()):
            self.vel_x = -self.vel_x

    def desenhar(self, tela):
        pygame.draw.circle(tela, Cores.BRANCO, (self.x, self.y), JogoConfig.TAMANHO_BOLA)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, JogoConfig.TAMANHO_BOLA, JogoConfig.TAMANHO_BOLA)

tela = pygame.display.set_mode((Config.LARGURA, Config.ALTURA))
pygame.display.set_caption("Pong")

def menu_principal():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    return True

        tela.fill(Cores.PRETO)

        fonte = pygame.font.SysFont(None, 50)
        texto = fonte.render("Pong", True, Cores.BRANCO)
        rect = texto.get_rect(center=(Config.LARGURA//2, Config.ALTURA//2))
        tela.blit(texto, rect)

        font_blynk = pygame.font.SysFont(None, 26)
        tempo = pygame.time.get_ticks()

        if tempo % 2000 < 1000:
            texto_blynk = font_blynk.render("Pressione ESPACO para jogar", True, Cores.BRANCO)
            rect_blynk = texto_blynk.get_rect(center=(Config.LARGURA//2, Config.ALTURA//2 + 50))
            tela.blit(texto_blynk, rect_blynk)

        pygame.display.flip()

def game():
    clock = pygame.time.Clock()

    player1 = Player(15, Config.ALTURA//2 - JogoConfig.RAQUETE_ALTURA//2)
    player2 = Player(Config.LARGURA - 15 - JogoConfig.RAQUETE_LARGURA,
                     Config.ALTURA//2 - JogoConfig.RAQUETE_ALTURA//2)

    bola = Bola()

    score_player1 = 0
    score_player2 = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return True

        tela.fill(Cores.PRETO)

        bola.mover()
        bola.colisao(player1, player2)

        if bola.x <= 0:
            score_player2 += 1
            bola.reset()
            if score_player2 >= 2:
                return True

        if bola.x >= Config.LARGURA - JogoConfig.TAMANHO_BOLA:
            score_player1 += 1
            bola.reset()
            if score_player1 >= 10:
                return True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player1.mover(-1)
        if keys[pygame.K_DOWN]:
            player1.mover(1)

        player2.ia(bola.y)

        player1.desenhar(tela)
        player2.desenhar(tela)
        bola.desenhar(tela)

        font_score = pygame.font.SysFont(None, 36)
        score_text = font_score.render(f"{score_player1} - {score_player2}", True, Cores.BRANCO)
        tela.blit(score_text, score_text.get_rect(center=(Config.LARGURA//2, 30)))

        pygame.display.flip()
        clock.tick(Config.FPS)

def main():
    while True:
        if not menu_principal():
            break
        if not game():
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()