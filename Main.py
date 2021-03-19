import pygame
from pygame import gfxdraw
import math
import random
import time
import copy

from Wall import wall
import Caster
from Ray import ray

WHITE = (255, 255, 255)
BLACK = ( 0 ,  0 ,  0 )

vector2D = pygame.math.Vector2


# screen pixel dimensions
WIDTH = 1000
HEIGHT = 1000

pygame.init()
# FPS used to make things move at same speed no matter FPS
FPS = 60
win = pygame.display.set_mode((WIDTH, HEIGHT))
# used to implement FPS and to time things and wait
clock = pygame.time.Clock()



walls = [wall(win, 0, 0, WIDTH, 0), wall(win, 0, 0, 0, HEIGHT), wall(win, 0, HEIGHT, WIDTH, HEIGHT), wall(win, WIDTH, HEIGHT, WIDTH, 0)]
#walls.append(wall(win, 500, 1000, 1000, 500))

for _ in range(10):
    w = wall(win, random.randint(0,1000), random.randint(0,1000), random.randint(0,1000), random.randint(0,1000))
    walls.append(w)
                                                                

caster = Caster.caster(win, (500, 500))

running = True
while running:
    win.fill(BLACK)
    for event in pygame.event.get():
        # user clicks the x
        if event.type == pygame.QUIT:
            running = False

    # keyboard input
    keys = pygame.key.get_pressed()
    # left arrow or 'a' key
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        caster.move_left()
    # right arrow or 'd' key
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        caster.move_right()

    # w key or up arrow starts the thrusters, any key not forward will stop thrusters
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        caster.move_up()

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        caster.move_down()
    
    for wall in walls:
        wall.show()

    caster.look(walls)
        

    pygame.display.update()


