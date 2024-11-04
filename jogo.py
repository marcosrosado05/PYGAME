import pygame
from constantes import *
from funcoes import *

# Comando para evitar travamentos.
try:
    window, state, assets = inicializa()
    game_loop(window, state, assets)
finally:
    pygame.quit()