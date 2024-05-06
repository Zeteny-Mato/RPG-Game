import pygame

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("My RPG Game")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.display.flip()

pygame.quit()