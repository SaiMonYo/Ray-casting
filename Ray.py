import pygame
from pygame import gfxdraw
import math
import random
import time
import copy


WHITE = (255, 255, 255)
BLACK = ( 0 ,  0 ,  0 )

vector2D = pygame.math.Vector2


class ray():
    def __init__(self, win, pos, angle):
        self.win = win
        self.pos = pos
        self.direction = vector2D(math.cos(angle), math.sin(angle))
        self.endPos = vector2D(self.direction.x * 1000 + self.pos.x,  self.direction.y * 1000 + self.pos.y)

    def cast(self, wall):
        x1 = wall.A.x
        y1 = wall.A.y
        x2 = wall.B.x
        y2 = wall.B.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.endPos.x
        y4 = self.endPos.y

        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if denominator == 0:
            return

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator

        if 0 < t < 1 and u > 0:
            inter = vector2D(0, 0)
            inter.x = x1 + t * (x2 - x1)
            inter.y = y1 + t * (y2 - y1)

            return inter
        return

    def show(self):
        pygame.draw.aaline(self.win, WHITE, self.pos, self.endPos, 10)
