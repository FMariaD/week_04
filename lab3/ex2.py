import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((750, 1060))

# фон
rect(screen, (85, 68, 0), (0, 0, 750, 479))
rect(screen, (141, 124, 56), (0, 479, 750, 2))
rect(screen, (128, 102, 0), (0, 481, 750, 580))
rect(screen, (0, 0, 0), (0, 0, 750, 1060), 3)

# окно
rect(screen, (213, 255, 230), (410, 30, 330, 430))
rect(screen, (135, 205, 222), (429, 45, 134, 110))
rect(screen, (135, 205, 222), (588, 45, 134, 110))
rect(screen, (135, 205, 222), (429, 170, 134, 275))
rect(screen, (135, 205, 222), (588, 170, 134, 275))

# хвост
serf1 = pygame.Surface((750, 1060), pygame.SRCALPHA)
#serf.fill((0, 0, 0))
ellipse(serf1, (200, 113, 55), (0, 0, 350, 100))
ellipse(serf1, (0, 0, 0), (0, 0, 350, 100), 3)
serf1 = pygame.transform.rotate(serf1, -30)
screen.blit(serf1, (0, 530))

# лапа1
serf2 = pygame.Surface((750, 1060), pygame.SRCALPHA)
#serf.fill((0, 0, 0))
ellipse(serf2, (0, 0, 0), (118, 698, 124, 69))
ellipse(serf2, (200, 113, 55), (120, 700, 120, 65))
serf2 = pygame.transform.rotate(serf2, -65)
screen.blit(serf2, (-290, 200))

# тело
ellipse(screen, (0, 0, 0), (133, 503, 444, 249))
ellipse(screen, (200, 113, 55), (135, 505, 440, 245))
ellipse(screen, (0, 0, 0), (18, 518, 204, 184))
ellipse(screen, (200, 113, 55), (20, 520, 200, 180))
circle(screen, (0, 0, 0), (510, 700), 80)
circle(screen, (200, 113, 55), (510, 700), 78)
ellipse(screen, (0, 0, 0), (123, 698, 124, 69))
ellipse(screen, (200, 113, 55), (125, 700, 120, 65))
ellipse(screen, (0, 0, 0), (558, 713, 59, 129))
ellipse(screen, (200, 113, 55), (560, 715, 55, 125))

# глаза
circle(screen, (136, 170, 0), (80, 620), 30)
circle(screen, (0, 0, 0), (80, 620), 31, 1)
circle(screen, (136, 170, 0), (170, 620), 30)
circle(screen, (0, 0, 0), (170, 620), 31, 1)
ellipse(screen, (0, 0, 0), (90, 593, 8, 53))
ellipse(screen, (0, 0, 0), (180, 593, 8, 53))

# рот
polygon(screen, (0, 0, 0), [[112, 651], [134, 651], [123, 664]])
polygon(screen, (255, 204, 170), [[114, 653], [132, 653], [123, 662]])
line(screen, (0, 0, 0), (123, 664), (123, 685), 2)
line(screen, (0, 0, 0), (110, 685), (136, 685), 2)
line(screen, (0, 0, 0), (100, 680), (0, 660), 1)
line(screen, (0, 0, 0), (100, 675), (0, 655), 1)
line(screen, (0, 0, 0), (100, 670), (0, 650), 1)
line(screen, (0, 0, 0), (146, 680), (246, 660), 1)
line(screen, (0, 0, 0), (146, 675), (246, 655), 1)
line(screen, (0, 0, 0), (146, 670), (246, 650), 1)

# уши
polygon(screen, (200, 113, 55), [[15, 515], [68, 542], [31, 582]])
polygon(screen, (0, 0, 0), [[15, 515], [68, 542], [31, 582]], 2)
polygon(screen, (222, 170, 135), [[24, 528], [60, 543], [34, 570]])
polygon(screen, (0, 0, 0), [[24, 528], [60, 543], [34, 570]], 2)
polygon(screen, (200, 113, 55), [[162, 539], [212, 509], [202, 577]])
polygon(screen, (0, 0, 0), [[162, 539], [212, 509], [202, 577]], 2)
polygon(screen, (222, 170, 135), [[171, 539], [204, 519], [198, 563]])
polygon(screen, (0, 0, 0), [[171, 539], [204, 519], [198, 563]], 2)

# клубок
circle(screen, (0, 0, 0), (455, 930), 87)
circle(screen, (153, 153, 153), (455, 930), 85)
arc(screen, (0, 0, 0), (455-50, 930-50, 100, 100), 0, 1.8, 3)
arc(screen, (0, 0, 0), (455-50, 930-50, 90, 90), 2.2, 3, 3)
arc(screen, (0, 0, 0), (455-70, 930-70, 120, 120), 1.2, 2.6, 3)
arc(screen, (0, 0, 0), (455-70, 930-50, 150, 120), 3, 0.3, 3)
aalines(screen, (0, 0, 0), False, [[370, 930], [340, 960], [300, 915], [260, 950], [200, 900], [180, 970], [160, 935]])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
