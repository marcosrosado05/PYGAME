import pygame
from constantes import *
from funcoes import *


window, state, assets = inicializa()

while state["estado"]:
    update_state(state)
    desenha(window, state, assets)

pygame.quit()
