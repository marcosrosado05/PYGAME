import pygame
from constantes import *
from funcoes import *


window, state, assets = inicializa()
direcao_p1= (0, velocidade_motos)
direcao_p2= (0, -velocidade_motos)

posicao_atual_P1 = [posicao_inicial_x_P1, posicao_inicial_y_P1]
posicao_atual_P2 = [posicao_inicial_x_P2, posicao_inicial_y_P2]

moto_P1_baixo = pygame.transform.rotate(moto_P1, 90)
moto_P2_cima = pygame.transform.rotate(moto_P2, -90)

rastro_skin_P1 = pygame.Surface((RASTRO_WIDTH, RASTRO_HEIGHT))
rastro_skin_P1.fill(BLUE)
rastro_P1_list = []

rastro_skin_P2 = pygame.Surface((RASTRO_WIDTH, RASTRO_HEIGHT))
rastro_skin_P2.fill(ORANGE)
rastro_P2_list = []

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
        posicao_atual_P1_2= move_moto_P1 (posicao_atual_P1[0], posicao_atual_P1[1], direcao_p1, WIDTH, HEIGHT, window, state)
        posicao_atual_P1 = posicao_atual_P1_2
        posicao_atual_P2_2= move_moto_P2 (posicao_atual_P2[0], posicao_atual_P2[1], direcao_p2, WIDTH, HEIGHT, window, state)
        posicao_atual_P2 = posicao_atual_P2_2

        # Verifique se as motos bateram uma na outra
        bate_motos= moto_atual_P1_rect.colliderect(moto_atual_P2_rect)
        if bate_motos:
            posicao_atual_P1 = posicao_inicial_P1
            posicao_atual_P2 = posicao_inicial_P2
            moto_atual_P1= moto_P1_baixo
            moto_atual_P2= moto_P2_cima
            moto_atual_P1_rect = moto_atual_P1.get_rect(center=posicao_atual_P1)
            moto_atual_P2_rect = moto_atual_P2.get_rect(center=posicao_atual_P2)
            moto_atual_P1_rect.center = posicao_inicial_P1
            moto_atual_P2_rect.center = posicao_inicial_P2


            rastro_list_P1 = update_rastro_P1()
            rastro_lista_P2 = update_rastro_P2()

        for rastro_P1_pos in rastro_list_P1:
            window.blit(rastro_skin_P1, rastro_P1_pos)

        for rastro_P1_pos in rastro_list_P1:
            window.blit(rastro_skin_P1, rastro_P1_pos)
        

    # Atualiza a tela
    pygame.display.update()
    
