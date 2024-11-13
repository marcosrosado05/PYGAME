# IMPORTS
import pygame
pygame.font.init()


# FPS
FPS = 120


# CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)


#fonte
fonte = pygame.font.Font(None, 50)


#TELAS
WIDTH, HEIGHT = 1920,1080
TELA_INICIAL = 0
TELA_DE_PLAY = 1
TELA_VENCEDOR_P1= 2
TELA_VENCEDOR_P2= 3

# Motos
MOTO_WIDTH = 90
MOTO_HEIGHT = 45


# Rasotros
RASTRO_WIDTH, RASTRO_HEIGHT = 10, 10
TAMANHO_RASTRO = 120


#JOGADORES
posicao_inicial_x_P1=560
posicao_inicial_y_P1=200
posicao_inicial_x_P2=1330  
posicao_inicial_y_P2=900 
posicao_inicial_P1= [posicao_inicial_x_P1, posicao_inicial_y_P1]
posicao_inicial_P2= [posicao_inicial_x_P2, posicao_inicial_y_P2]

velocidade_motos= 3

pontos_jogador_P1=0
pontos_jogador_P2=0

direcao_P1= (0, velocidade_motos)
direcao_P2= (0, -velocidade_motos)

posicao_atual_P1 = [posicao_inicial_x_P1, posicao_inicial_y_P1]
posicao_atual_P2 = [posicao_inicial_x_P2, posicao_inicial_y_P2]

rastro_skin_P1 = pygame.Surface((RASTRO_WIDTH, RASTRO_HEIGHT))
rastro_skin_P1.fill(BLUE)
rastro_list_P1 = []


# Variáveis do Timer e Scoreboard
tempo_inicial = pygame.time.get_ticks()
tempo_decorrido = 0
scoreboard = []

assets = {
    "tela_de_play" : pygame.image.load("image/TELA_PLAY_TRON.png"),
    "titulo" : 'TRON LEGACY' ,
    "tabuleiro1": pygame.image.load("image/tabuleiro1.png"),
    "tabuleiro2": pygame.image.load("image/tabuleiro2.png"),
    "Moto_P1": pygame.image.load("image/moto-azul.png"),
    "Moto_P2": pygame.image.load("image/moto-laranja.png"),
    "P1_vencedor" : pygame.image.load("image/blue_wins.webp"),
    "P2_vencedor" : pygame.image.load("image/orange_wins.webp")

} 

