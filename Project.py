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
bg_x = 0
bg_y = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYUP:
            hero.walk = False   #0
            hero.jump = False   #0
            hero.slide = False
            hero.stay = True    #1

    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        hero.rect.x +=1
        hero.walk = True    #1
        hero.right = True   #1
        hero.left = False   #0
        bg_x -= 2
    if key[pygame.K_a]:
        hero.rect.x-=1
        hero.walk = True    #1
        hero.left = True    #1
        hero.right = False  #0
        bg_x += 2
    if key[pygame.K_w]:
        hero.walk = False   #0
        hero.left = False   #0
        hero.right = False  #0
        hero.jump = True    #1
        if hero.on_ground:
            hero.dy-=20
            hero.on_ground = False  #0
    if key[pygame.K_s]:
        hero.slide = True
        hero.rect.x += 7
        hero.dy = 5


    screen.blit(background,(bg_x,0))
    screen.blit(background, (bg_x + 1200, 0))
    hero.update(H-hero.rect.h)
    screen.blit(hero.image,hero.rect)
      # передвигать каждую итерацию главного цикла задний фон на 2 пикселя?
    if bg_x == -1200:
        bg_x = 0
    pygame.display.update()
    clock.tick(fps)
    # screen.blit(background,(bg_x,0))
    # screen.blit(background, (bg_x+1200, 0)) # здесь мы циклически ставим один задний фон за другим

