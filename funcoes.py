import pygame
from constantes import *
from tela import *


# INICIA O JOGO

def inicializa():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    # DIMENSIONA A TELA
    window = pygame.display.set_mode((WIDTH, HEIGHT)) 

    pygame.display.set_caption("TRON LEGACY")

    #DICIONARIO DE STATE DO JOGO
    state = {'estado': True}

    # dicionario com todos os itens assets

    # Imprime instruções
    print('*' * len(assets['titulo']))
    print(assets['titulo'].upper())
    print('*' * len(assets['titulo']))
    print('Utilize as teclas "W", "A", "S", "D" e "↑", "←", "→", "↓" PARA MOVER OS PERSONAGENS.')

    pygame.mixer.music.load("sons/Encom Part II.mp3")
    pygame.mixer.music.set_volume(2)
    pygame.mixer.music.play(-1)

    return window, state, assets

moto_P1= assets['Moto_P1']
moto_P1 = pygame.transform.scale(moto_P1, (MOTO_WIDTH, MOTO_HEIGHT))
moto_P1_rect = moto_P1.get_rect(center=(posicao_inicial_x_P1, posicao_inicial_y_P1))

moto_P2=  assets['Moto_P2']
moto_P2 = pygame.transform.scale(moto_P2, (MOTO_WIDTH, MOTO_HEIGHT))
moto_P2_rect = moto_P2.get_rect(center=(posicao_inicial_x_P2, posicao_inicial_y_P2))

pygame.quit()