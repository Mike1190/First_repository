import pygame
from object import Object
pygame.init()

pygame.mixer.music.load("sounds/background.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

jump_sound = pygame.mixer.Sound("sounds/jump.wav")
footsteps_sound = pygame.mixer.Sound("sounds/footsteps.wav")
slip_sound = pygame.mixer.Sound("sounds/slip.mp3")

W, H = 1200, 840
screen = pygame.display.set_mode((W, H))  # flags = pygame.NOFRAME - убрать рамку у окна
clock = pygame.time.Clock()
fps = 60
hero = Object(30,700,3,'hero/Movement/Staing/Idle__000.png')
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
            hero.walk = False  # 0
            hero.left = False  # 0
            hero.right = False
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        # footsteps_sound.play()
        hero.rect.x +=1
        hero.walk = True    #1
        hero.right = True   #1
        bg_x -= 2
    if key[pygame.K_a]:
        hero.rect.x-=1
        hero.walk = True    #1
        hero.left = True    #1

        bg_x += 2
    if key[pygame.K_w]:
        hero.jump = True #1
        jump_sound.play()
        if hero.on_ground:
            hero.dy -= 20
            hero.on_ground = False  #0
    if key[pygame.K_s]:
        slip_sound.play()
        hero.slide = True
        hero.rect.x += 5

    screen.blit(background,(bg_x,0))
    screen.blit(background, (bg_x + 1200, 0))
    hero.update(H-90)
    screen.blit(hero.image,hero.rect)
      # передвигать каждую итерацию главного цикла задний фон на 2 пикселя?
    if bg_x == -1200:
        bg_x = 0
    pygame.display.update()
    clock.tick(fps)
    # screen.blit(background,(bg_x,0))
    # screen.blit(background, (bg_x+1200, 0)) # здесь мы циклически ставим один задний фон за другим
    #

