import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (217, 217, 217), (0, 0, 400, 400))

circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 101, 1)
rect(screen, (0, 0, 0), (150, 250, 100, 20))
circle(screen, (255, 0, 0), (150, 180), 20)
circle(screen, (0, 0, 0), (150, 180), 10)
circle(screen, (0, 0, 0), (150, 180), 21, 1)
circle(screen, (255, 0, 0), (250, 180), 15)
circle(screen, (0, 0, 0), (250, 180), 7)
circle(screen, (0, 0, 0), (250, 180), 16, 1)
polygon(screen, (0, 0, 0), [(220,166), (298,136), (301,144), (224,173)])
polygon(screen, (0, 0, 0), [(182,166), (178,173), (99,125), (104,117)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
