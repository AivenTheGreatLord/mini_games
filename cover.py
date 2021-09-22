import pygame
import random


pygame.init()
#pygame.mixer.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Cover")



run = True; x = 150; y = 150; v_x = random.randint(-10,10); v_y = random.randint(-10,10)

while run == True:
    pygame.time.delay(5)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x += v_x; y += v_y

    if y <=30 or y >= 570:
        v_y *= -1
    if x <=30 or x >= 570:
        v_x *= -1

    screen.fill((0,0,0))

    pygame.draw.circle(screen,(0,255,0),(x,y),30)

    pygame.display.update()


pygame.QUIT()
