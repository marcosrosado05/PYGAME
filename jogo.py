import pygame
from constantes import *
from funcoes import *


window, state, assets = inicializa()
moto_P1_baixo = pygame.transform.rotate(moto_P1, 90)
moto_P2_cima = pygame.transform.rotate(moto_P2, -90)

rastro_skin_P2 = pygame.Surface((RASTRO_WIDTH, RASTRO_HEIGHT))
rastro_skin_P2.fill(ORANGE)
rastro_list_P2 = []

while state["estado"]:
    desenha(window, state, assets)
    update_state(state)

    if state['tela_atual'] == TELA_DE_PLAY:
        
        rastro_list_P1 = update_rastro(posicao_atual_P1, rastro_list_P1)
        rastro_list_P2 = update_rastro(posicao_atual_P2, rastro_list_P2)

        for rastro_P1_pos in rastro_list_P1:
            window.blit(rastro_skin_P1, [rastro_P1_pos[0]-13, rastro_P1_pos[1]-5])
        
        for rastro_P2_pos in rastro_list_P2:
            window.blit(rastro_skin_P2, [rastro_P2_pos[0]-13, rastro_P2_pos[1]-5])

        moto_atual_P1, moto_atual_P1_rect = gira_moto_P1(direcao_P1, moto_P1, posicao_atual_P1)
        moto_atual_P2, moto_atual_P2_rect = gira_moto_P2(direcao_P2, moto_P2, posicao_atual_P2)

        desenha_p1 (window, assets, posicao_atual_P1[0], posicao_atual_P1[1], moto_atual_P1)
        desenha_p2 (window, assets, posicao_atual_P2[0], posicao_atual_P2[1], moto_atual_P2)

        
        # Verifique quais teclas estão pressionadas para alterar a direção do P1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:   # Esquerda
            direcao_P1 = (-velocidade_motos, 0)
        elif keys[pygame.K_d]:  # Direita
            direcao_P1 = (velocidade_motos, 0)
        elif keys[pygame.K_w]:    # Cima
            direcao_P1 = (0, -velocidade_motos)
        elif keys[pygame.K_s]:  # Baixo
            direcao_P1 = (0, velocidade_motos)
        
        # Verifique quais teclas estão pressionadas para alterar a direção do P2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:   # Esquerda
            direcao_P2 = (-velocidade_motos, 0)
        elif keys[pygame.K_RIGHT]:  # Direita
            direcao_P2 = (velocidade_motos, 0)
        elif keys[pygame.K_UP]:    # Cima
            direcao_P2 = (0, -velocidade_motos)
        elif keys[pygame.K_DOWN]:  # Baixo
            direcao_P2 = (0, velocidade_motos)

        # Chame a função para mover as duas motos e verificar se está dentro do tabuleiro
        posicao_atual_P1_2= move_moto (posicao_atual_P1[0], posicao_atual_P1[1], direcao_P1, WIDTH, HEIGHT, window, state)
        posicao_atual_P1 = posicao_atual_P1_2
        posicao_atual_P2_2= move_moto (posicao_atual_P2[0], posicao_atual_P2[1], direcao_P2, WIDTH, HEIGHT, window, state)
        posicao_atual_P2 = posicao_atual_P2_2

        # Verifica se as motos bateram uma na outra
        bate_motos = moto_atual_P1_rect.colliderect(moto_atual_P2_rect)
        if bate_motos:
            # Reseta as posições, direção e rastros ao colidirem
            posicao_atual_P1 = posicao_inicial_P1
            posicao_atual_P2 = posicao_inicial_P2
            moto_atual_P1 = moto_P1_baixo
            moto_atual_P2 = moto_P2_cima
            moto_atual_P1_rect = moto_atual_P1.get_rect(center=posicao_atual_P1)
            moto_atual_P2_rect = moto_atual_P2.get_rect(center=posicao_atual_P2)
            rastro_list_P1 = []
            rastro_list_P2 = []

        # Verifica colisão do rastro e pontuação
        if colisao_rastro(rastro_list_P1, moto_atual_P2_rect):
            pontos_jogador_P1 += 1
        if colisao_rastro(rastro_list_P2, moto_atual_P1_rect):
            pontos_jogador_P2 += 1

        # Altera para a tela de vencedor apenas se um jogador atingir 2 pontos
        if pontos_jogador_P1 == 2:
            state['tela_atual'] = TELA_VENCEDOR_P1
        elif pontos_jogador_P2 == 2:
            state['tela_atual'] = TELA_VENCEDOR_P2

            # Atualiza a tela
            pygame.display.update()
    pygame.display.update()
"""
    #ESSA PARTE ESTÁ DANDO ERRO, O JOGO TRAVA E FECHA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Lógica da tela de vencedor
    if state['tela_atual'] == TELA_VENCEDOR_P1:
        texto_reiniciar = fonte.render("PRESSIONE ENTER PARA JOGAR NOVAMENTE", True, WHITE)
        window.blit(texto_reiniciar, (WIDTH / 2 - texto_reiniciar.get_width() / 2, HEIGHT - 100))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            reset_game()

    elif state['tela_atual'] == TELA_VENCEDOR_P2:
        texto_reiniciar = fonte.render("PRESSIONE ENTER PARA JOGAR NOVAMENTE", True, WHITE)
        window.blit(texto_reiniciar, (WIDTH / 2 - texto_reiniciar.get_width() / 2, HEIGHT - 100))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            reset_game()"""

