import pygame
from constantes import *


class Jogador():

    def __init__(self, posicao_inicial, direcao, image_asset, rastro_skin):
        self.rastro_list = []
        self.posicao_atual = posicao_inicial
        self.posicao_inicial = posicao_inicial  # para resetar
        self.direcao = direcao
        self.image_asset = image_asset
        self.pontos = 0
        self.rastro_skin = rastro_skin

    def reseta_posicao(self):
        self.posicao_atual = self.posicao_inicial

    def reseta_rastro(self):
        self.rastro_list = []

    def desenha(self, window, moto_atual):
        moto = self.image_asset
        moto = pygame.transform.scale(moto, (MOTO_WIDTH, MOTO_HEIGHT))
        moto_rect = moto.get_rect(center=(self.posicao_atual[0] + 15, self.posicao_atual[1]))
        # Desenha a imagem na tela
        window.blit(moto_atual, moto_rect)

    #função pra mover a moto
    def move_moto(self):
        posicao_atual_x, posicao_atual_y = self.posicao_atual
        posicao_atual_x += self.direcao[0]
        posicao_atual_y += self.direcao[1]

        # Verifique se a sprite bateu na borda da tela
        if posicao_atual_x < WIDTH / 2 - assets['tabuleiro1'].get_width() // 2 or posicao_atual_x > WIDTH / 2 + assets['tabuleiro1'].get_width() // 2 - 65:
            posicao_atual_x -= self.direcao[0]

        if posicao_atual_y < 100 or posicao_atual_y > assets['tabuleiro1'].get_height() + 31:
            posicao_atual_y -= self.direcao[1]

        self.posicao_atual = [posicao_atual_x, posicao_atual_y]

    #função para girar a moto
    def gira_moto(self, moto):
        # Gira a imagem da moto e cria o rect correspondente
        moto_baixo = pygame.transform.rotate(moto, 90)
        moto_cima = pygame.transform.rotate(moto, -90)
        moto_esquerda = pygame.transform.rotate(moto, 0)
        moto_direita = pygame.transform.rotate(moto, 180)
        
        # Seleciona a imagem e o rect com base na direção
        if self.direcao == (0, velocidade_motos):
            moto_atual = moto_baixo
        elif self.direcao == (0, -velocidade_motos):
            moto_atual = moto_cima
        elif self.direcao == (velocidade_motos, 0):
            moto_atual = moto_direita
        elif self.direcao == (-velocidade_motos, 0):
            moto_atual = moto_esquerda

        # Cria o rect e centraliza-o na posição atual da moto 1
        moto_atual_rect = moto_atual.get_rect(center=self.posicao_atual)

        return moto_atual, moto_atual_rect
        
    def update_rastro(self):
        self.rastro_list.append(self.posicao_atual)
        if len(self.rastro_list) > TAMANHO_RASTRO:
            self.rastro_list.pop(0)
        return self.rastro_list
    
    def desenha_rastro(self, window):
        for pos in self.rastro_list:
            window.blit(self.rastro_skin, [pos[0] - 13, pos[1] - 5])

    def detectar_colisao_rastro(self, moto_rect):
        for posicao_rastro in self.rastro_list:
            rastro_rect = pygame.Rect(posicao_rastro[0], posicao_rastro[1], RASTRO_WIDTH, RASTRO_HEIGHT)
            if rastro_rect.colliderect(moto_rect):
                return True
        return False
