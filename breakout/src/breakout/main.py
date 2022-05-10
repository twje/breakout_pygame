# from core.application import Application
# from .breakout import Breakout


# def main():
#     application = Application(
#         listener=Breakout(),
#         caption="Hello World",
#         width=600,
#         height=400
#     )
#     application.run()


from pygame.locals import *
import pygame
import sys

import time;
import random;

clock = pygame.time.Clock()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((530, 212))

while True:
    t = random.random()
    t *= 255
    for event in pygame.event.get():        
        if event.type == QUIT:
            pygame.quit()
        print (event)

    DISPLAYSURF.fill((int(t) % 255, int(t) % 255, int(t) % 255))
    pygame.display.update()

    print(clock.tick(60))