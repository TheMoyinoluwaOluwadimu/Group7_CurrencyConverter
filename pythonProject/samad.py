import pygame

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
GRAY = (170,170,170)

background = GREEN
screen = pygame.display.set_mode((700, 450))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            if event.key == pygame.K_b:
                background = BLUE

            screen.fill(background)
    pygame.display.update()
pygame.quit()
