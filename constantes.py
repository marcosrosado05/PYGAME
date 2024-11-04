# IMPORTS

import pygame
import random 
from os import path



# INFORMAÇÕES DA TELA 
WIDTH, HEIGHT = 1920,1080


# FPS
FPS = 120

# CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#TELAS
TELA_INICIAL = 0
TELA_DE_PLAY = 1

#JOGADORES
velocidade_x_p1 = 0
velocidade_y_p1 = -10

velocidade_x_p2 = 0
velocidade_y_p2 = 10

velocidade =10
posicao_inicial_x_p1=650
posicao_inicial_y_p1=250
posicao_inicial_x_p2=1230  
posicao_inicial_y_p2=830 

MOTO_WIDTH = 350
MOTO_HEIGHT = 200