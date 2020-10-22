import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
scr = pygame.display.set_mode((750, 1060))

GREY = (153, 153, 153)
BLACK = (0, 0, 0)
BLUE = (135, 205, 222)
ORANGE = (200, 113, 55)
GREEN = (136, 170, 0)


def random_color():
    x = (randint(0, 250), randint(0, 250), randint(0, 250))
    return x


# фон
rect(scr, (85, 68, 0), (0, 0, 750, 479))
rect(scr, (141, 124, 56), (0, 479, 750, 2))
rect(scr, (128, 102, 0), (0, 481, 750, 580))
rect(scr, BLACK, (0, 0, 750, 1060), 3)


def draw_window(x0, y0, size):
    surf1 = pygame.Surface((750, 1060), pygame.SRCALPHA)
    rect(surf1, (213, 255, 230), (410, 30, 330, 430))
    rect(surf1, BLUE, (429, 45, 134, 110))
    rect(surf1, BLUE, (588, 45, 134, 110))
    rect(surf1, BLUE, (429, 170, 134, 275))
    rect(surf1, BLUE, (588, 170, 134, 275))
    surf1 = pygame.transform.scale(surf1, (int(750 * size), int(1060 * size)))
    x0 = int(x0 + 429 * size)
    y0 = int(y0 + 45 * size)
    scr.blit(surf1, (x0, y0))


def draw_cat(x0, y0, size, color):
    surf2 = pygame.Surface((1000, 1310), pygame.SRCALPHA)

    # arm & tail (angled ellipses)
    serf1 = pygame.Surface((750, 1060), pygame.SRCALPHA)
    ellipse(serf1, color, (0, 0, 350, 100))
    ellipse(serf1, BLACK, (0, 0, 350, 100), 3)
    serf1 = pygame.transform.rotate(serf1, -30)
    surf2.blit(serf1, (0, 530))
    serf2 = pygame.Surface((750, 1060), pygame.SRCALPHA)
    ellipse(serf2, BLACK, (118, 698, 124, 69))
    ellipse(serf2, color, (120, 700, 120, 65))
    serf2 = pygame.transform.rotate(serf2, -65)
    surf2.blit(serf2, (-290, 200))

    # body
    ellipse(surf2, BLACK, (133, 503, 444, 249))
    ellipse(surf2, color, (135, 505, 440, 245))
    ellipse(surf2, BLACK, (18, 518, 204, 184))
    ellipse(surf2, color, (20, 520, 200, 180))
    circle(surf2, BLACK, (510, 700), 80)
    circle(surf2, color, (510, 700), 78)
    ellipse(surf2, BLACK, (123, 698, 124, 69))
    ellipse(surf2, color, (125, 700, 120, 65))
    ellipse(surf2, BLACK, (558, 713, 59, 129))
    ellipse(surf2, color, (560, 715, 55, 125))

    # eyes
    circle(surf2, GREEN, (80, 620), 30)
    circle(surf2, BLACK, (80, 620), 31, 1)
    circle(surf2, GREEN, (170, 620), 30)
    circle(surf2, BLACK, (170, 620), 31, 1)
    ellipse(surf2, BLACK, (90, 593, 8, 53))
    ellipse(surf2, BLACK, (180, 593, 8, 53))

    # mouth
    polygon(surf2, BLACK, [[112, 651], [134, 651], [123, 664]])
    polygon(surf2, (255, 204, 170), [[114, 653], [132, 653], [123, 662]])
    line(surf2, BLACK, (123, 664), (123, 685), 2)
    line(surf2, BLACK, (110, 685), (136, 685), 2)
    line(surf2, BLACK, (100, 680), (0, 660), 1)
    line(surf2, BLACK, (100, 675), (0, 655), 1)
    line(surf2, BLACK, (100, 670), (0, 650), 1)
    line(surf2, BLACK, (146, 680), (246, 660), 1)
    line(surf2, BLACK, (146, 675), (246, 655), 1)
    line(surf2, BLACK, (146, 670), (246, 650), 1)

    # ears
    polygon(surf2, color, [[15, 515], [68, 542], [31, 582]])
    polygon(surf2, BLACK, [[15, 515], [68, 542], [31, 582]], 2)
    polygon(surf2, (222, 170, 135), [[24, 528], [60, 543], [34, 570]])
    polygon(surf2, BLACK, [[24, 528], [60, 543], [34, 570]], 2)
    polygon(surf2, color, [[162, 539], [212, 509], [202, 577]])
    polygon(surf2, BLACK, [[162, 539], [212, 509], [202, 577]], 2)
    polygon(surf2, (222, 170, 135), [[171, 539], [204, 519], [198, 563]])
    polygon(surf2, BLACK, [[171, 539], [204, 519], [198, 563]], 2)

    surf2 = pygame.transform.scale(surf2, (int(750 * size), int(1060 * size)))
    x0 = int(x0 + 429 - (429 - 250) * size)
    y0 = int(y0 + 620 - (620 - 250) * size)
    scr.blit(surf2, (x0, y0))


def draw_klubok(x0, y0, size, color):
    surf3 = pygame.Surface((1000, 1310), pygame.SRCALPHA)
    circle(surf3, BLACK, (455, 930), 87)
    circle(surf3, color, (455, 930), 85)
    arc(surf3, BLACK, (455 - 50, 930 - 50, 100, 100), 0, 1.8, 3)
    arc(surf3, BLACK, (455 - 50, 930 - 50, 90, 90), 2.2, 3, 3)
    arc(surf3, BLACK, (455 - 70, 930 - 70, 120, 120), 1.2, 2.6, 3)
    arc(surf3, BLACK, (455 - 70, 930 - 50, 150, 120), 3, 0.3, 3)
    aalines(surf3, BLACK, False, [[370, 930], [340, 960], [300, 915],
                                  [260, 950], [200, 900], [180, 970],
                                  [160, 935]])
    surf3 = pygame.transform.scale(surf3, (int(750 * size), int(1060 * size)))
    x0 = int(x0 + 350 - (350 - 250) * size)
    y0 = int(y0 + 930 - (930 - 250) * size)
    scr.blit(surf3, (x0, y0))


for x, y, z in [(0, 0, 0.7), (-350, 0, 0.7), (-700, 0, 0.7)]:
    draw_window(x, y, z)
for x, y, z in [(-120, 50, 1), (-300, -100, 0.6), (200, -20, 0.35)]:
    draw_cat(x, y, z, random_color())
for x, y, z in [(0, -400, 0.7), (-330, -20, 0.6), (200, 10, 0.5)]:
    draw_klubok(x, y, z, random_color())

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
