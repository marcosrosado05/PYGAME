import pygame
from constantes import *
from funcoes import *

from tela import *
from jogador import Jogador


window, state, assets = inicializa()
moto_P1_baixo = pygame.transform.rotate(moto_P1, 90)
moto_P2_cima = pygame.transform.rotate(moto_P2, -90)

clock = pygame.time.Clock()
tela = TelaInicial()

# definir jogadores
jogador_1 = Jogador(
    posicao_inicial=[posicao_inicial_x_P1, posicao_inicial_y_P1],
    direcao=(0, velocidade_motos),
    image_asset=assets['Moto_P1'],
    rastro_skin=rastro_skin_P1
)
jogador_2 = Jogador(
    posicao_inicial=[posicao_inicial_x_P2, posicao_inicial_y_P2],
    direcao=(0, -velocidade_motos),
    image_asset=assets['Moto_P2'],
    rastro_skin=rastro_skin_P2
)

while state["estado"]:
    tela.desenha_tela(window, assets)
    # tela = update_state(state, tela)

     #TRATAMENTO DE EVENTOS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state['estado'] = False #QUEBRA O LOOP DO JOGO
            break
        
        # extraido dos ifs, pois sempre queremos testar esse caso
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            state['estado'] = False #QUEBRA O LOOP DO JOGO
            break
        
        #EVENTOS DA TELA INICIAL
        if tela.nome == "tela_inicial":
            if event.type == pygame.KEYDOWN:
        
                if event.key == pygame.K_SPACE:
                    tela = TelaPlay()
                    if state["estado"] == True:
                        pygame.mixer.music.load("sons/Daft Punk - Derezzed (Lunar Lightcycle Remix).mp3")
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-4)

        #EVENTOS TELA DE PLAY          
        elif tela.nome == "tela_play":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:   # .key todo evento tem uma chave (key) e essa chave é uma série de números da biblio do pygame, cada tecla é um número distinto 
                    tela = TelaInicial()

        #EVENTOS DA TELA DOS VENCEDORES
        if tela.nome == "tela_vencedor_p1":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    tela = TelaInicial()
        if tela.nome == "tela_vencedor_p2":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    tela = TelaInicial()

    clock.tick(FPS)

    if tela.jogo_em_andamento:

        fonte = pygame.font.Font(None, 48)
        texto_P1 = fonte.render(f"Jogador 1: {jogador_1.pontos}", True, BLUE)
        window.blit(texto_P1, [300, 200])
        texto_P2 = fonte.render(f"Jogador 2: {jogador_2.pontos}", True, ORANGE)
        window.blit(texto_P2, [(1400), (800)])

        jogador_1.update_rastro()
        jogador_2.update_rastro()

        jogador_1.desenha_rastro(window)
        jogador_2.desenha_rastro(window)

        moto_atual_P1, moto_atual_P1_rect = jogador_1.gira_moto(moto_P1)
        moto_atual_P2, moto_atual_P2_rect = jogador_2.gira_moto(moto_P2)

        jogador_1.desenha(window, moto_atual_P1)
        jogador_2.desenha(window, moto_atual_P2)

        # Verifique quais teclas estão pressionadas para alterar a direção do P1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:   # Esquerda
            jogador_1.direcao = (-velocidade_motos, 0)
        elif keys[pygame.K_d]:  # Direita
            jogador_1.direcao = (velocidade_motos, 0)
        elif keys[pygame.K_w]:    # Cima
            jogador_1.direcao = (0, -velocidade_motos)
        elif keys[pygame.K_s]:  # Baixo
            jogador_1.direcao = (0, velocidade_motos)
        
        # Verifique quais teclas estão pressionadas para alterar a direção do P2
        if keys[pygame.K_LEFT]:   # Esquerda
            jogador_2.direcao = (-velocidade_motos, 0)
        elif keys[pygame.K_RIGHT]:  # Direita
            jogador_2.direcao = (velocidade_motos, 0)
        elif keys[pygame.K_UP]:    # Cima
            jogador_2.direcao = (0, -velocidade_motos)
        elif keys[pygame.K_DOWN]:  # Baixo
            jogador_2.direcao = (0, velocidade_motos)

        # Chame a função para mover as duas motos e verificar se está dentro do tabuleiro
        jogador_1.move_moto()
        jogador_2.move_moto()

        # Verifica se as motos bateram uma na outra
        bate_motos = moto_atual_P1_rect.colliderect(moto_atual_P2_rect)
        if bate_motos:
            # Reseta as posições, direção e rastros ao colidirem
            jogador_1.reseta_posicao()
            jogador_2.reseta_posicao()
            moto_atual_P1 = moto_P1_baixo
            moto_atual_P2 = moto_P2_cima
            moto_atual_P1_rect = moto_atual_P1.get_rect(center=jogador_1.posicao_atual)
            moto_atual_P2_rect = moto_atual_P2.get_rect(center=jogador_2.posicao_atual)
            jogador_1.reseta_rastro()
            jogador_2.reseta_rastro()
        # Verifica colisão do rastro e pontuação
        if jogador_1.detectar_colisao_rastro(moto_atual_P2_rect):
            # Reseta o jogo pra proxima rodada
            assets['boom_sound'].play()
            jogador_1.pontos += 1
            jogador_1.reseta_posicao()
            jogador_2.reseta_posicao()
            moto_atual_P1_rect = moto_atual_P1.get_rect(center=jogador_1.posicao_atual)
            moto_atual_P2_rect = moto_atual_P2.get_rect(center=jogador_2.posicao_atual)
            jogador_1.reseta_rastro()
            jogador_2.reseta_rastro()

        elif jogador_2.detectar_colisao_rastro(moto_atual_P1_rect):
            # Reseta o jogo pra proxima rodada
            assets['boom_sound'].play()
            jogador_2.pontos += 1
            jogador_1.reseta_posicao()
            jogador_2.reseta_posicao()
            moto_atual_P1_rect = moto_atual_P1.get_rect(center=jogador_1.posicao_atual)
            moto_atual_P2_rect = moto_atual_P2.get_rect(center=jogador_2.posicao_atual)
            jogador_1.reseta_rastro()
            jogador_2.reseta_rastro()
        
        # Altera para a tela de vencedor apenas se um jogador atingir 2 pontos
        if jogador_1.pontos == 2:
            tela = TelaVencedorP1()
            jogador_1.pontos = 0
            jogador_2.pontos = 0
            pygame.display.update()
        elif jogador_2.pontos == 2:
            tela = TelaVencedorP2()
            jogador_1.pontos = 0
            jogador_2.pontos = 0
            pygame.display.update()

    # Atualiza a tela
    pygame.display.update()
