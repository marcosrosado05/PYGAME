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
    state = {'tela_atual': TELA_INICIAL}

    # dicionario com todos os itens assets
    assets = {
    "tela_de_play" : pygame.image.load("image/TELA PLAY TRON.png"),
    "titulo" : 'TRON LEGACY' ,
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
            return False #QUEBRA O LOOP DO JOGO
        
        #EVENTOS DA TELA INICIAL
        if state['tela_atual'] == TELA_INICIAL:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False #QUEBRA O LOOP DO JOGO
                
                if event.key == pygame.K_SPACE:
                    state['tela_atual'] = TELA_DE_PLAY

        #EVENTOS TELA DE PLAY          
        elif state['tela_atual'] == TELA_DE_PLAY:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:   # .key todo evento tem uma chave (key) e essa chave é uma série de números da biblio do pygame, cada tecla é um número distinto 
                    state['tela_atual'] = TELA_INICIAL


    return True #MANTÉM O LOOP DO JOGO

def desenha(window, state, assets):

    #DESENHANDO TELA INICIAL
    if state['tela_atual'] == TELA_INICIAL:
        window.fill(BLACK)
        window.blit(assets['tela_de_play'], (WIDTH/2 - assets['tela_de_play'].get_width()/2,0))

    #DESENHANDO TELA DE PLAY
    if state['tela_atual'] == TELA_DE_PLAY:
        window.fill(BLACK)
    pygame.display.flip() #ATUALIZANDO FRAME


def game_loop(window, state, assets): #LOOP PRINCIPAL DO JOGO
    while True:
        if not update_state(state):
            break
        desenha(window, state, assets) #DESENHANDO A CADA NOVO FRAME