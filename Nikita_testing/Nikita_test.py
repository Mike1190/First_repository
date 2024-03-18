import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 600))

pygame.display.set_caption("netonuya")
icon = pygame.image.load('Nikita_testing/nikita_icon.png')
pygame.display.set_icon(icon)

game_running = True
while game_running:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()