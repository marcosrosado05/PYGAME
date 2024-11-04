import pygame
from constantes import *
from funcoes import *



window, state, assets = inicializa()

while state["estado"]:
    desenha(window, state, assets)

    if state['tela_atual'] == TELA_DE_PLAY:
        desenha_p1 (window, assets, posicao_inicial_x_p1, posicao_inicial_y_p1)
    if state['tela_atual'] == TELA_DE_PLAY:
        desenha_p2 (window, assets, posicao_inicial_x_p2, posicao_inicial_y_p2)
    
    # Atualiza a tela
    pygame.display.flip()
    

pygame.quit()

