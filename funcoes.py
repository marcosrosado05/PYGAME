import pygame
from constantes import *



# INICIA O JOGO

def inicializa():
    pygame.init()
    pygame.font.init()

    # DIMENSIONA A TELA
    window = pygame.display.set_mode((WIDTH, HEIGHT)) 

    pygame.display.set_caption("TRON LEGACY")

    #DICIONARIO DE STATE DO JOGO
    state = {'tela_atual': TELA_INICIAL, 'estado': True}

    # dicionario com todos os itens assets

    # Imprime instruções
    print('*' * len(assets['titulo']))
    print(assets['titulo'].upper())
    print('*' * len(assets['titulo']))
    print('Utilize as teclas "W", "A", "S", "D" e "↑", "←", "→", "↓" PARA MOVER OS PERSONAGENS.')

    if state == {'tela_atual': TELA_INICIAL, 'estado': True}:
        pygame.mixer.music.load("sons/Encom Part II.mp3")
        pygame.mixer.music.set_volume(2)
        pygame.mixer.music.play(-1)

    return window, state, assets

moto_P1= assets['Moto_P1']
moto_P1 = pygame.transform.scale(moto_P1, (MOTO_WIDTH, MOTO_HEIGHT))
moto_P1_rect= moto_P1.get_rect(center=(posicao_inicial_x_P1, posicao_inicial_y_P1))

moto_P2=  assets['Moto_P2']
moto_P2 = pygame.transform.scale(moto_P2, (MOTO_WIDTH, MOTO_HEIGHT))
moto_P2_rect= moto_P2.get_rect(center=(posicao_inicial_x_P2, posicao_inicial_y_P2))
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
                    if state["estado"] == True:
                        pygame.mixer.music.load("sons/Daft Punk - Derezzed (Lunar Lightcycle Remix).mp3")
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-4)
        #EVENTOS TELA DE PLAY          
        elif state['tela_atual'] == TELA_DE_PLAY:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:   # .key todo evento tem uma chave (key) e essa chave é uma série de números da biblio do pygame, cada tecla é um número distinto 
                    state['tela_atual'] = TELA_INICIAL
                if event.key == pygame.K_ESCAPE:
                    state['estado'] = False #QUEBRA O LOOP DO JOGO
                    return
                
        #EVENTOS DA TELA DOS VENCEDORES
        if state['tela_atual'] == TELA_VENCEDOR_P1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state['estado'] = False #QUEBRA O LOOP DO JOGO
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state['tela_atual'] = TELA_INICIAL
                    return
        if state['tela_atual'] == TELA_VENCEDOR_P2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state['estado'] = False #QUEBRA O LOOP DO JOGO
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state['tela_atual'] = TELA_INICIAL
                    return
                
    return True #MANTÉM O LOOP DO JOGO

def desenha(window, state, assets):

    #DESENHANDO TELA INICIAL
    if state['tela_atual'] == TELA_INICIAL:
        window.fill(BLACK)
        window.blit(assets['tela_de_play'], (WIDTH/2 - assets['tela_de_play'].get_width()/2,0))

    #DESENHANDO TELA DE PLAY
    if state['tela_atual'] == TELA_DE_PLAY:
        window.fill(BLACK)
        window.blit(assets['tabuleiro1'], (WIDTH / 2 - assets['tabuleiro1'].get_width() / 2, HEIGHT / 2 - assets['tabuleiro1'].get_height() / 2))

    #DESENHANDO TELA DO VENCEDOR 1
    if state['tela_atual'] == TELA_VENCEDOR_P1:
        window.fill(BLACK)
        window.blit(assets['P1_vencedor'], (WIDTH/2- assets['P1_vencedor'].get_width()/2,0))

    #DESENHANDO TELA DO VENCEDOR 2
    if state['tela_atual'] == TELA_VENCEDOR_P2:
        window.fill(BLACK)
        window.blit(assets['P2_vencedor'], (WIDTH/2 - assets['P2_vencedor'].get_width()/2,0))

    

def desenha_p1(window,assets, posicao_inicial_x_p1, posicao_inicial_y_p1, moto_atual_P1):
    
    moto_P1= assets['Moto_P1']
    moto_P1 = pygame.transform.scale(moto_P1, (MOTO_WIDTH, MOTO_HEIGHT))
    moto_P1_rect= moto_P1.get_rect(center=(posicao_inicial_x_p1 + 15, posicao_inicial_y_p1))
    # Desenha a imagem na tela
    window.blit(moto_atual_P1, moto_P1_rect)

def desenha_p2(window, assets, posicao_inicial_x_p2, posicao_inicial_y_p2, moto_atual_P2):
    
    moto_P2=  assets['Moto_P2']
    moto_P2 = pygame.transform.scale(moto_P2, (MOTO_WIDTH, MOTO_HEIGHT))
    moto_P2_rect= moto_P2.get_rect(center=(posicao_inicial_x_p2 + 15, posicao_inicial_y_p2))
    # Desenha a imagem na tela
    window.blit(moto_atual_P2, moto_P2_rect)

#função pra mover a moto
def move_moto(posicao_atual_x, posicao_atual_y, direcao, WIDTH, HEIGHT, window, state):
    posicao_atual_x += direcao[0]
    posicao_atual_y += direcao[1]

    # Verifique se a sprite bateu na borda da tela
    if posicao_atual_x < WIDTH / 2 - assets['tabuleiro1'].get_width() // 2 or posicao_atual_x > WIDTH / 2 + assets['tabuleiro1'].get_width() // 2 - 65:
        posicao_atual_x -= direcao[0]

    if posicao_atual_y < 100 or posicao_atual_y > assets['tabuleiro1'].get_height() + 31:
        posicao_atual_y -= direcao[1]

    posicao_atual= [posicao_atual_x, posicao_atual_y]
    return posicao_atual
    
#função para girar a moto
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

def update_rastro (posicao_atual, rastro_list):
    pos_pixel_rastro1 = posicao_atual

    rastro_list.append(pos_pixel_rastro1)
    if len(rastro_list) > TAMANHO_RASTRO:
        rastro_list.pop(0)

    return rastro_list


def colisao_rastro_P1(rastro_list, moto_rect, pontos_jogador_P1):
    pontos_jogador_P1+=1
    for posicao_rastro in rastro_list:
        rastro_rect = pygame.Rect(posicao_rastro[0], posicao_rastro[1], RASTRO_WIDTH, RASTRO_HEIGHT)
        if rastro_rect.colliderect(moto_rect):
            return True
    return False

def colisao_rastro_P2(rastro_list, moto_rect, pontos_jogador_P2):
    pontos_jogador_P2+=1
    for posicao_rastro in rastro_list:
        rastro_rect = pygame.Rect(posicao_rastro[0], posicao_rastro[1], RASTRO_WIDTH, RASTRO_HEIGHT)
        if rastro_rect.colliderect(moto_rect):
            return True
    return False

def reset_game(rastro_list_P1, rastro_list_P2, state):
    global posicao_atual_P1, posicao_atual_P2, direcao_P1, direcao_P2
    posicao_atual_P1 = [posicao_inicial_x_P1, posicao_inicial_y_P1]
    posicao_atual_P2 = [posicao_inicial_x_P2, posicao_inicial_y_P2]
    direcao_P1 = (0, velocidade_motos)
    direcao_P2 = (0, -velocidade_motos)
    rastro_list_P1.clear()
    rastro_list_P2.clear()
    state['tela_atual'] = TELA_DE_PLAY

pygame.quit()