import pygame
from constantes import *



# INICIA O JOGO

def inicializa():
    pygame.init()

    # DIMENSIONA A TELA
    window = pygame.display.set_mode((WIDTH, HEIGHT)) 

    pygame.display.set_caption("TRON LEGACY")

    #DICIONARIO DE STATE DO JOGO
    state = {'tela_atual': TELA_INICIAL, 'estado': True}

    # dicionario com todos os itens assets
    assets = {
        "tela_de_play" : pygame.image.load("image/TELA_PLAY_TRON.png"),
        "titulo" : 'TRON LEGACY' ,
        "logo_titulo" : pygame.image.load("image/logo.png"),
        "tabuleiro1": pygame.image.load("image/tabuleiro1.png"),
        "tabuleiro2": pygame.image.load("image/tabuleiro2.png"),
        "Moto_P1": pygame.image.load("image/moto-azul.png"),
        "Moto_P2": pygame.image.load("image/moto-laranja.png"),
        "Blue_wins" : pygame.image.load("image/blue_wins.webp"),
        "Orange_wins" : pygame.image.load("image/Orange_wins.webp")
    }

    # Imprime instruções
    print('*' * len(assets['titulo']))
    print(assets['titulo'].upper())
    print('*' * len(assets['titulo']))
    print('Utilize as teclas "W", "A", "S", "D" e "↑", "←", "→", "↓" PARA MOVER OS PERSONAGENS.')

    return window, state, assets

assets = {
    "tela_de_play" : pygame.image.load("image/TELA_PLAY_TRON.png"),
    "titulo" : 'TRON LEGACY' ,
    "logo_titulo" : pygame.image.load("image/logo.png"),
    "tabuleiro1": pygame.image.load("image/tabuleiro1.png"),
    "tabuleiro2": pygame.image.load("image/tabuleiro2.png"),
    "Moto_P1": pygame.image.load("image/moto-azul.png"),
    "Moto_P2": pygame.image.load("image/moto-laranja.png")
}

moto_P1= assets['Moto_P1']
moto_P1 = pygame.transform.scale(moto_P1, (MOTO_WIDTH, MOTO_HEIGHT))
moto_P1_rect= moto_P1.get_rect(topleft=(posicao_inicial_x_P1, posicao_inicial_y_P1))

moto_P2=  assets['Moto_P2']
moto_P2 = pygame.transform.scale(moto_P2, (MOTO_WIDTH, MOTO_HEIGHT))
moto_P2_rect= moto_P2.get_rect(topleft=(posicao_inicial_x_P2, posicao_inicial_y_P2))
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
        window.blit(assets['logo_titulo'], (WIDTH/2 - assets['logo_titulo'].get_width()/2,HEIGHT/3 - 100))

    #DESENHANDO TELA DE PLAY
    if state['tela_atual'] == TELA_DE_PLAY:
        window.fill(BLACK)
        window.blit(assets['tabuleiro1'], (WIDTH / 2 - assets['tabuleiro1'].get_width() / 2, HEIGHT / 2 - assets['tabuleiro1'].get_height() / 2))

    # pygame.display.flip() #ATUALIZANDO FRAME
    

def desenha_p1(window,assets, posicao_inicial_x_p1, posicao_inicial_y_p1, moto_atual_P1):
    
    moto_P1= assets['Moto_P1']
    moto_P1 = pygame.transform.scale(moto_P1, (MOTO_WIDTH, MOTO_HEIGHT))
    moto_P1_rect= moto_P1.get_rect(center=(posicao_inicial_x_p1, posicao_inicial_y_p1))
    # Desenha a imagem na tela
    window.blit(moto_atual_P1, moto_P1_rect)

def desenha_p2(window, assets, posicao_inicial_x_p2, posicao_inicial_y_p2, moto_atual_P2):
    
    moto_P2=  assets['Moto_P2']
    moto_P2 = pygame.transform.scale(moto_P2, (MOTO_WIDTH, MOTO_HEIGHT))
    moto_P2_rect= moto_P2.get_rect(center=(posicao_inicial_x_p2, posicao_inicial_y_p2))
    # Desenha a imagem na tela
    window.blit(moto_atual_P2, moto_P2_rect)

#função pra mover a moto do P1
def move_moto_P1(posicao_atual_x_P1, posicao_atual_y_P1, direcao_P1, WIDTH, HEIGHT, window, state):
    posicao_atual_x_P1 += direcao_P1[0]
    posicao_atual_y_P1 += direcao_P1[1]

    # Verifique se a sprite bateu na borda da tela
    if posicao_atual_x_P1 < 0 or posicao_atual_x_P1 > WIDTH or posicao_atual_y_P1 < 0 or posicao_atual_y_P1 > HEIGHT:
        state["estado"]= False  # Retorna False se bater na borda e acaba o jogo
        return
    if posicao_atual_x_P1 < WIDTH / 2 - assets['tabuleiro1'].get_width() // 2 or posicao_atual_x_P1 > WIDTH / 2 + assets['tabuleiro1'].get_width() // 2 - 65:
        posicao_atual_x_P1 -= direcao_P1[0]

    if posicao_atual_y_P1 < 100 or posicao_atual_y_P1 > assets['tabuleiro1'].get_height() + 31:
        posicao_atual_y_P1 -= direcao_P1[1]

    posicao_atual_P1= [posicao_atual_x_P1, posicao_atual_y_P1]
    return posicao_atual_P1
    

#função pra mover a moto do P2
def move_moto_P2(posicao_atual_x_P2, posicao_atual_y_P2, direcao_P2, WIDTH, HEIGHT, window, state):
    
    posicao_atual_x_P2 += direcao_P2[0]
    posicao_atual_y_P2 += direcao_P2[1]

    # Verifique se a sprite bateu na borda da tela
    if posicao_atual_x_P2 < 0 or posicao_atual_x_P2 > WIDTH or posicao_atual_y_P2 < 0 or posicao_atual_y_P2 > HEIGHT:
        state["estado"]= False  # Retorna False se bater na borda e acaba o jogo
        return
    if posicao_atual_x_P2 < WIDTH / 2 - assets['tabuleiro1'].get_width() // 2 or posicao_atual_x_P2 > WIDTH / 2 + assets['tabuleiro1'].get_width() // 2 - 65:
        posicao_atual_x_P2 -= direcao_P2[0]

    if posicao_atual_y_P2 < 100 or posicao_atual_y_P2 > assets['tabuleiro1'].get_height() + 31:
        posicao_atual_y_P2 -= direcao_P2[1]

    posicao_atual_P2= [posicao_atual_x_P2, posicao_atual_y_P2]
    return posicao_atual_P2
    
#função para girar a moto do P1
def gira_moto_P1(direcao_P1, moto_P1, posicao_atual_P1):
    # Gira a imagem da moto e cria o rect correspondente
    moto_P1_baixo = pygame.transform.rotate(moto_P1, 90)
    moto_P1_cima = pygame.transform.rotate(moto_P1, -90)
    moto_P1_esquerda = pygame.transform.rotate(moto_P1, 0)
    moto_P1_direita = pygame.transform.rotate(moto_P1, 180)
    
    # Seleciona a imagem e o rect com base na direção
    if direcao_P1 == (0, velocidade_motos):
        moto_atual_P1 = moto_P1_baixo
    elif direcao_P1 == (0, -velocidade_motos):
        moto_atual_P1 = moto_P1_cima
    elif direcao_P1 == (velocidade_motos, 0):
        moto_atual_P1 = moto_P1_direita
    elif direcao_P1 == (-velocidade_motos, 0):
        moto_atual_P1 = moto_P1_esquerda

    # Cria o rect e centraliza-o na posição atual da moto 1
    moto_atual_P1_rect = moto_atual_P1.get_rect(center=posicao_atual_P1)

    return moto_atual_P1, moto_atual_P1_rect


#função para girar a moto do P2
def gira_moto_P2(direcao_P2, moto_P2, posicao_atual_P2):
    # Gira a imagem da moto e cria o rect correspondente
    moto_P2_baixo = pygame.transform.rotate(moto_P2, 90)
    moto_P2_cima = pygame.transform.rotate(moto_P2, -90)
    moto_P2_esquerda = pygame.transform.rotate(moto_P2, 0)
    moto_P2_direita = pygame.transform.rotate(moto_P2, 180)
    
    # Seleciona a imagem e o rect com base na direção
    if direcao_P2 == (0, velocidade_motos):
        moto_atual_P2 = moto_P2_baixo
    elif direcao_P2 == (0, -velocidade_motos):
        moto_atual_P2 = moto_P2_cima
    elif direcao_P2 == (velocidade_motos, 0):
        moto_atual_P2 = moto_P2_direita
    elif direcao_P2 == (-velocidade_motos, 0):
        moto_atual_P2 = moto_P2_esquerda

    # Cria o rect e centraliza-o na posição atual da moto 2
    moto_atual_P2_rect = moto_atual_P2.get_rect(center=posicao_atual_P2)

    return moto_atual_P2, moto_atual_P2_rect

def update_rastro_P1(posicao_atual_P1, direcao_P1, rastro_list_P1):
    '''if direcao_P1 == (0, velocidade_motos): #Direção para baixo
        pos_pixel_rastro1 = (posicao_atual_P1[0], posicao_atual_P1[1])
    elif direcao_P1 == (0, -velocidade_motos): #Direção para cima
        pos_pixel_rastro1 = (posicao_atual_P1[0], posicao_atual_P1[1])
    elif direcao_P1 == (velocidade_motos, 0): #Direção para direita
        pos_pixel_rastro1 = (posicao_atual_P1[0], posicao_atual_P1[1]+14)
    elif direcao_P1 == (-velocidade_motos, 0): #Direção para esquerda
        pos_pixel_rastro1 = (posicao_atual_P1[0] + MOTO_WIDTH, posicao_atual_P1[1]+20)'''

    rastro_list_P1.append(posicao_atual_P1)
    if len(rastro_list_P1) > TAMANHO_RASTRO:
        rastro_list_P1.pop(0)

    return rastro_list_P1

def update_rastro_P2 (posicao_atual_P2, direcao_P2, rastro_list_P2):

    pos_pixel_rastro2 = posicao_atual_P2

    rastro_list_P2.append(pos_pixel_rastro2)
    if len(rastro_list_P2) > TAMANHO_RASTRO:
        rastro_list_P2.pop(0)

    return rastro_list_P2

pygame.quit()