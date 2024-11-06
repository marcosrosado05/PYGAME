import pygame
from constantes import *
from funcoes import *


window, state, assets = inicializa()
direcao_p1= (0, velocidade_motos)
direcao_p2= (0, -velocidade_motos)

posicao_atual_P1 = [posicao_inicial_x_p1, posicao_inicial_y_p1]
posicao_atual_P2 = [posicao_inicial_x_p2, posicao_inicial_y_p2]


while state["estado"]:
    desenha(window, state, assets)
    update_state(state)

    if state['tela_atual'] == TELA_DE_PLAY:

        moto_atual_P1, moto_atual_P1_rect = gira_moto_P1(direcao_p1, moto_P1, posicao_atual_P1)
        moto_atual_P2, moto_atual_P2_rect = gira_moto_P2(direcao_p2, moto_P2, posicao_atual_P2)

        desenha_p1 (window, assets, posicao_atual_P1[0], posicao_atual_P1[1], moto_atual_P1)
        desenha_p2 (window, assets, posicao_atual_P2[0], posicao_atual_P2[1], moto_atual_P2)

        # Verifique quais teclas estão pressionadas para alterar a direção do P1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:   # Esquerda
            direcao_p1 = (-velocidade_motos, 0)
        elif keys[pygame.K_d]:  # Direita
            direcao_p1 = (velocidade_motos, 0)
        elif keys[pygame.K_w]:    # Cima
            direcao_p1 = (0, -velocidade_motos)
        elif keys[pygame.K_s]:  # Baixo
            direcao_p1 = (0, velocidade_motos)
        
        # Verifique quais teclas estão pressionadas para alterar a direção do P2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:   # Esquerda
            direcao_p2 = (-velocidade_motos, 0)
        elif keys[pygame.K_RIGHT]:  # Direita
            direcao_p2 = (velocidade_motos, 0)
        elif keys[pygame.K_UP]:    # Cima
            direcao_p2 = (0, -velocidade_motos)
        elif keys[pygame.K_DOWN]:  # Baixo
            direcao_p2 = (0, velocidade_motos)

        # Chame a função para mover as duas motos e verificar se está dentro do tabuleiro
        print(direcao_p1)
        posicao_atual_P1_2= move_moto_P1 (posicao_atual_P1[0], posicao_atual_P1[1], direcao_p1, WIDTH, HEIGHT, window, state)
        posicao_atual_P1 = posicao_atual_P1_2
        posicao_atual_P2_2= move_moto_P2 (posicao_atual_P2[0], posicao_atual_P2[1], direcao_p2, WIDTH, HEIGHT, window, state)
        posicao_atual_P2 = posicao_atual_P2_2
        

    # Atualiza a tela
    pygame.display.update()
    
