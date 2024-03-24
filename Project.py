import pygame
from object import Object
pygame.init()
W, H = 1200, 840
screen = pygame.display.set_mode((W, H))  # flags = pygame.NOFRAME - убрать рамку у окна
clock = pygame.time.Clock()
fps = 60
hero = Object(30,700,3,'hero/hero_go_right/Run__000.png')
# pygame.display.set_caption('#') # задать название для окна
background = pygame.image.load('background/Background.png')
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type ==pygame.KEYUP:
            hero.walk = False

    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        hero.rect.x +=5
        hero.walk = True
    if key[pygame.K_a]:
        hero.rect.x-=5
        hero.walk = True
    if key[pygame.K_w]:
        if hero.is_jump:
            hero.dy-=10
            hero.is_jump = False
    screen.blit(background,(0,0))
    hero.update(H-hero.rect.h)
    screen.blit(hero.image,hero.rect)
    pygame.display.update()
    clock.tick(fps)
    # screen.blit(background,(bg_x,0))
    # screen.blit(background, (bg_x+1200, 0)) # здесь мы циклически ставим один задний фон за другим

