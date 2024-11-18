import pygame
from constantes import *
from funcoes import *


window, state, assets = inicializa()
moto_P1_baixo = pygame.transform.rotate(moto_P1, 90)
moto_P2_cima = pygame.transform.rotate(moto_P2, -90)

clock = pygame.time.Clock()

while state["estado"]:
    desenha(window, state, assets)
    update_state(state)

    clock.tick(FPS)

    if state['tela_atual'] == TELA_DE_PLAY:

        fonte = pygame.font.Font(None, 48)
        texto_P1 = fonte.render(f"Jogador 1: {pontos_jogador_P1}", True, BLUE)
        window.blit(texto_P1, [300, 200])
        texto_P2 = fonte.render(f"Jogador 2: {pontos_jogador_P2}", True, ORANGE)
        window.blit(texto_P2, [(1400), (800)])

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
        if colisao_rastro_P1(rastro_list_P1, moto_atual_P2_rect, pontos_jogador_P1):
            # Reseta o jogo pra proxima rodada
            assets['boom_sound'].play()
            pontos_jogador_P1 += 1
            posicao_atual_P1 = posicao_inicial_P1
            posicao_atual_P2 = posicao_inicial_P2
            moto_atual_P1_rect = moto_atual_P1.get_rect(center=posicao_atual_P1)
            moto_atual_P2_rect = moto_atual_P2.get_rect(center=posicao_atual_P2)
            rastro_list_P1 = []
            rastro_list_P2 = []

        elif colisao_rastro_P2(rastro_list_P2, moto_atual_P1_rect, pontos_jogador_P2):
            # Reseta o jogo pra proxima rodada
            assets['boom_sound'].play()
            pontos_jogador_P2 += 1
            posicao_atual_P1 = posicao_inicial_P1
            posicao_atual_P2 = posicao_inicial_P2
            moto_atual_P1_rect = moto_atual_P1.get_rect(center=posicao_atual_P1)
            moto_atual_P2_rect = moto_atual_P2.get_rect(center=posicao_atual_P2)
            rastro_list_P1 = []
            rastro_list_P2 = []

        
        
        
        # Altera para a tela de vencedor apenas se um jogador atingir 2 pontos
        if pontos_jogador_P1 == 2:
            state['tela_atual'] = TELA_VENCEDOR_P1
            pontos_jogador_P1=0
            pontos_jogador_P2=0
            pygame.display.update()
        elif pontos_jogador_P2 == 2:
            state['tela_atual'] = TELA_VENCEDOR_P2
            pontos_jogador_P1=0
            pontos_jogador_P2=0
            pygame.display.update()

    # Atualiza a tela
    pygame.display.update()
