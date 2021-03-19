import pygame
from pygame import gfxdraw
import math
import random
import time
import copy


WHITE = (255, 255, 255)
BLACK = ( 0 ,  0 ,  0 )

vector2D = pygame.math.Vector2


class wall():
    def __init__(self, win, x1, y1, x2, y2):
        self.win = win
        self.A = vector2D(x1, y1)
        self.B = vector2D(x2, y2)

    def show(self):
        pygame.draw.aaline(self.win, WHITE, self.A, self.B, 10)
