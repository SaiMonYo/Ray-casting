import pygame
from pygame import gfxdraw
import math
import random
import time
import copy

from Ray import ray

WHITE = (255, 255, 255)
BLACK = ( 0 ,  0 ,  0 )

vector2D = pygame.math.Vector2


class caster():
    def __init__(self, win, pos):
        self.win = win
        self.pos = vector2D(pos)
        self.rays = []
        self.moveDist = 0.5
        self.fov = 90
        self.offset = 0

        for angle in range(-self.fov // 2, self.fov // 2):
            self.rays.append(ray(self.win, self.pos, math.radians(angle)))

    def move_left(self):
        self.pos.x -= self.moveDist

    def move_right(self):
        self.pos.x += self.moveDist

    def move_up(self):
        self.pos.y -= self.moveDist

    def move_down(self):
        self.pos.y += self.moveDist

    def rotate(self, angle):
        self.offset += angle
        for ray in self.rays:
            ray.angle += self.offset

    def look(self, walls):
        window = []
        for ray in self.rays:
            closest = None
            lowest = math.inf
            for wall in walls:
                inter = ray.cast(wall)
                if inter != None:
                    dist = vector2D(self.pos - inter).length()
                    if dist < lowest:
                        lowest = dist
                        closest = inter

            if closest != None:
                pygame.draw.line(self.win, WHITE, self.pos, closest, 1)
            window.append(lowest)

        return window
        

    
            
