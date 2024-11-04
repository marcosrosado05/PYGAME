import pygame
from constantes import *


# INICIA O JOGO

def inicializa():
    pygame.init()

    # DIMENSIONA A TELA
    window = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.init()
    pygame.display.set_caption("TRON LEGACY")

    #DICIONARIO DE STATE DO JOGO
    state = {'tela_atual': TELA_INICIAL, 'estado': True}

    # dicionario com todos os itens assets
    assets = {
        "tela_de_play" : pygame.image.load("image/TELA_PLAY_TRON.png"),
        "titulo" : 'TRON LEGACY' ,
        "logo_titulo" : pygame.image.load("image/logo_nome.png"),
        "tabuleiro1": pygame.image.load("image/tabuleiro1.png"),
        "tabuleiro2": pygame.image.load("image/tabuleiro2.png"),
    }

    # Imprime instruções
    print('*' * len(assets['titulo']))
    print(assets['titulo'].upper())
    print('*' * len(assets['titulo']))
    print('Utilize as teclas "W", "A", "S", "D" e "↑", "←", "→", "↓" PARA MOVER OS PERSONAGENS.')

    return window, state, assets


def update_state(state):

    #TRATAMENTO DE EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state['estado'] = False #QUEBRA O LOOP DO JOGO
            return
        
        #EVENTOS DA TELA INICIAL
        if state['tela_atual'] == TELA_INICIAL:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state['estado'] = False #QUEBRA O LOOP DO JOGO
                    return
                
                if event.key == pygame.K_SPACE:
                    state['tela_atual'] = TELA_DE_PLAY

        #EVENTOS TELA DE PLAY          
        elif state['tela_atual'] == TELA_DE_PLAY:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:   # .key todo evento tem uma chave (key) e essa chave é uma série de números da biblio do pygame, cada tecla é um número distinto 
                    state['tela_atual'] = TELA_INICIAL
                if event.key == pygame.K_ESCAPE:
                    state['estado'] = False #QUEBRA O LOOP DO JOGO
                    return

    # return True #MANTÉM O LOOP DO JOGO

def desenha(window, state, assets):

    #DESENHANDO TELA INICIAL
    if state['tela_atual'] == TELA_INICIAL:
        window.fill(BLACK)
        window.blit(assets['tela_de_play'], (WIDTH/2 - assets['tela_de_play'].get_width()/2,0))

    #DESENHANDO TELA DE PLAY
    if state['tela_atual'] == TELA_DE_PLAY:
        window.fill(BLACK)
        window.blit(assets['tabuleiro1'], (WIDTH / 2 - assets['tabuleiro1'].get_width() / 2, HEIGHT / 2 - assets['tabuleiro1'].get_height() / 2))

    pygame.display.flip() #ATUALIZANDO FRAME
    update_state(state)
