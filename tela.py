from abc import ABC, abstractmethod
from constantes import *
from funcoes import *
import pygame

class Tela(ABC):

    nome: str
    jogo_em_andamento = False

    @abstractmethod
    def desenha_tela(self, window, assets):
        pass


class TelaInicial(Tela):

    nome = "tela_inicial"

    def desenha_tela(self, window, assets):
        window.fill(BLACK)
        tela_incial_escala = pygame.transform.scale(assets['tela_de_play'], (WIDTH_TAB, HEIGHT_TAB))
        window.blit(tela_incial_escala, (WIDTH/2 - WIDTH_TAB/2, 106))

class TelaPlay(Tela):

    nome = "tela_play"
    jogo_em_andamento = True

    def desenha_tela(self, window, assets):
        window.fill(BLACK)
        window.blit(assets['tabuleiro1'], (WIDTH / 2 - assets['tabuleiro1'].get_width() / 2, HEIGHT / 2 - assets['tabuleiro1'].get_height() / 2))

class TelaVencedorP1(Tela):

    nome = "tela_vencedor_p1"

    def desenha_tela(self, window, assets):
        window.fill(BLACK)
        vencedor_p1 = pygame.transform.scale(assets['P1_vencedor'], (WIDTH_TAB, HEIGHT_TAB))
        window.blit(vencedor_p1, (WIDTH/2 - WIDTH_TAB/2,100))

class TelaVencedorP2(Tela):

    nome = "tela_vencedor_p2"

    def desenha_tela(self, window, assets):
        window.fill(BLACK)
        vencedor_p2 = pygame.transform.scale(assets['P2_vencedor'], (WIDTH_TAB, HEIGHT_TAB))
        window.blit(vencedor_p2, (WIDTH/2 - WIDTH_TAB/2,100))
