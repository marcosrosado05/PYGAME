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
        "Moto_P1": pygame.image.load("image/Moto_P1.png"),
        "Moto_P2": pygame.image.load("image/Moto_P2.png")
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


def movimentacao(state):
    for event in pygame.event.get():
        if state['tela_atual'] == TELA_DE_PLAY:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocidade_x_p1= -velocidade
                if event.key == pygame.K_RIGHT:
                    velocidade_x_p1= velocidade
                if event.key == pygame.K_UP:
                    velocidade_y_p1= -velocidade
                if event.key == pygame.K_DOWN:
                    velocidade_y_p1= velocidade
                if event.key == pygame.K_a:
                    velocidade_x_p2= -velocidade
                if event.key == pygame.K_d:
                    velocidade_x_p2= velocidade
                if event.key == pygame.K_w:
                    velocidade_y_p2= -velocidade
                if event.key == pygame.K_s:
                    velocidade_y_p2= velocidade


def desenha_p1(window,assets, posicao_inicial_x_p1, posicao_inicial_y_p1):
    
    moto_P1= assets['Moto_P1']
    moto_P1 = pygame.transform.scale(moto_P1, (MOTO_WIDTH, MOTO_HEIGHT))
    moto_P1_rect= moto_P1.get_rect(topleft=(posicao_inicial_x_p1, posicao_inicial_y_p1))
    # Desenha a imagem na tela
    window.blit(moto_P1, moto_P1_rect)

def desenha_p2(window, assets, posicao_inicial_x_p2, posicao_inicial_y_p2):
    
    moto_P2=  assets['Moto_P2']
    moto_P2 = pygame.transform.scale(moto_P2, (MOTO_WIDTH, MOTO_HEIGHT))
    moto_P2_rect= moto_P2.get_rect(topleft=(posicao_inicial_x_p2, posicao_inicial_y_p2))
    # Desenha a imagem na tela
    window.blit(moto_P2, moto_P2_rect)


def desenha_sprite(tela, imagem, x, y):
    # Obtenha o retângulo da imagem para definir a posição
    sprite_rect = imagem.get_rect(topleft=(x, y))
    # Desenha a imagem na tela
    tela.blit(imagem, sprite_rect)