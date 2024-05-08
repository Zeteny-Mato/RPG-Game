import pygame

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("My RPG Game")

player_image = pygame.image.load("Smaller_black_circle.png")
player_rect = player_image.get_rect()
player_rect.center = (width // 2, height // 2)

player_speed = 1

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_rect.move_ip(-player_speed, 0)
    if keys[pygame.K_RIGHT]:
        player_rect.move_ip(player_speed, 0)
    if keys[pygame.K_UP]:
        player_rect.move_ip(0, -player_speed)
    if keys[pygame.K_DOWN]:
        player_rect.move_ip(0, player_speed)

    screen.fill((255, 255, 255))

    screen.blit(player_image, player_rect)

    pygame.display.flip()

pygame.quit()