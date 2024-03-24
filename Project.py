import pygame
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((768, 416)) # flags = pygame.NOFRAME - убрать рамку у окна
pygame.display.set_caption('Game') # задать название для окна
background = pygame.image.load('background/Map.png') # задаем задний фон

hero_stay = [pygame.image.load('hero/Движение/На месте/Idle__000.png'),
pygame.image.load('hero/Движение/На месте/Idle__000.png'),
pygame.image.load('hero/Движение/На месте/Idle__000.png'),
pygame.image.load('hero/Движение/На месте/Idle__001.png'),
pygame.image.load('hero/Движение/На месте/Idle__001.png'),
pygame.image.load('hero/Движение/На месте/Idle__001.png'),
pygame.image.load('hero/Движение/На месте/Idle__002.png'),
pygame.image.load('hero/Движение/На месте/Idle__002.png'),
pygame.image.load('hero/Движение/На месте/Idle__002.png'),
pygame.image.load('hero/Движение/На месте/Idle__003.png'),
pygame.image.load('hero/Движение/На месте/Idle__003.png'),
pygame.image.load('hero/Движение/На месте/Idle__003.png'),
pygame.image.load('hero/Движение/На месте/Idle__004.png'),
pygame.image.load('hero/Движение/На месте/Idle__004.png'),
pygame.image.load('hero/Движение/На месте/Idle__004.png'),
pygame.image.load('hero/Движение/На месте/Idle__005.png'),
pygame.image.load('hero/Движение/На месте/Idle__005.png'),
pygame.image.load('hero/Движение/На месте/Idle__005.png'),
pygame.image.load('hero/Движение/На месте/Idle__006.png'),
pygame.image.load('hero/Движение/На месте/Idle__006.png'),
pygame.image.load('hero/Движение/На месте/Idle__006.png'),
pygame.image.load('hero/Движение/На месте/Idle__007.png'),
pygame.image.load('hero/Движение/На месте/Idle__007.png'),
pygame.image.load('hero/Движение/На месте/Idle__007.png'),
pygame.image.load('hero/Движение/На месте/Idle__008.png'),
pygame.image.load('hero/Движение/На месте/Idle__008.png'),
pygame.image.load('hero/Движение/На месте/Idle__008.png'),
]
hero_run_right = [pygame.image.load('hero/Движение/Бег вправо/Run__000.png'), # все картинки для анимации героя(идет вправо)
pygame.image.load('hero/Движение/Бег вправо/Run__001.png'),
pygame.image.load('hero/Движение/Бег вправо/Run__002.png'),
pygame.image.load('hero/Движение/Бег вправо/Run__003.png'),
pygame.image.load('hero/Движение/Бег вправо/Run__004.png'),
pygame.image.load('hero/Движение/Бег вправо/Run__005.png'),
pygame.image.load('hero/Движение/Бег вправо/Run__006.png'),
pygame.image.load('hero/Движение/Бег вправо/Run__007.png'),
pygame.image.load('hero/Движение/Бег вправо/Run__008.png'),
pygame.image.load('hero/Движение/Бег вправо/Run__009.png'),
]
hero_run_left = [pygame.image.load('hero/Движение/Бег влево/Run__000.png'), # все картинки для анимации героя(идет вправо)
pygame.image.load('hero/Движение/Бег влево/Run__001.png'),
pygame.image.load('hero/Движение/Бег влево/Run__002.png'),
pygame.image.load('hero/Движение/Бег влево/Run__003.png'),
pygame.image.load('hero/Движение/Бег влево/Run__004.png'),
pygame.image.load('hero/Движение/Бег влево/Run__005.png'),
pygame.image.load('hero/Движение/Бег влево/Run__006.png'),
pygame.image.load('hero/Движение/Бег влево/Run__007.png'),
pygame.image.load('hero/Движение/Бег влево/Run__008.png'),
pygame.image.load('hero/Движение/Бег влево/Run__009.png'),
]
hero_jump = [pygame.image.load('hero/hero_go_right/Jump__000.png'),
pygame.image.load('hero/hero_go_right/Jump__001.png'),
pygame.image.load('hero/hero_go_right/Jump__002.png'),
pygame.image.load('hero/hero_go_right/Jump__003.png'),
pygame.image.load('hero/hero_go_right/Jump__004.png'),
pygame.image.load('hero/hero_go_right/Jump__005.png'),
pygame.image.load('hero/hero_go_right/Jump__006.png'),
pygame.image.load('hero/hero_go_right/Jump__007.png'),
pygame.image.load('hero/hero_go_right/Jump__008.png'),
pygame.image.load('hero/hero_go_right/Jump__009.png'),
]
walk_right = [
pygame.image.load('hero/hero_go_right/Slide__000.png'),
pygame.image.load('hero/hero_go_right/Slide__001.png'),
pygame.image.load('hero/hero_go_right/Slide__002.png'),
pygame.image.load('hero/hero_go_right/Slide__003.png'),
pygame.image.load('hero/hero_go_right/Slide__004.png'),
pygame.image.load('hero/hero_go_right/Slide__004.png'),
pygame.image.load('hero/hero_go_right/Slide__005.png'),
pygame.image.load('hero/hero_go_right/Slide__006.png'),
pygame.image.load('hero/hero_go_right/Slide__007.png'),
pygame.image.load('hero/hero_go_right/Slide__008.png'),
pygame.image.load('hero/hero_go_right/Slide__009.png'),
pygame.image.load('hero/hero_go_right/Dead__000.png'),
pygame.image.load('hero/hero_go_right/Dead__001.png'),
pygame.image.load('hero/hero_go_right/Dead__002.png'),
pygame.image.load('hero/hero_go_right/Dead__003.png'),
pygame.image.load('hero/hero_go_right/Dead__004.png'),
pygame.image.load('hero/hero_go_right/Dead__005.png'),
pygame.image.load('hero/hero_go_right/Dead__006.png'),
pygame.image.load('hero/hero_go_right/Dead__007.png'),
pygame.image.load('hero/hero_go_right/Dead__008.png'),
pygame.image.load('hero/hero_go_right/Dead__009.png'),


pygame.image.load('hero/hero_go_right/Attack__000.png'),
pygame.image.load('hero/hero_go_right/Attack__001.png'),
pygame.image.load('hero/hero_go_right/Attack__002.png'),
pygame.image.load('hero/hero_go_right/Attack__003.png'),
pygame.image.load('hero/hero_go_right/Attack__004.png'),
pygame.image.load('hero/hero_go_right/Attack__005.png'),
pygame.image.load('hero/hero_go_right/Attack__006.png'),
pygame.image.load('hero/hero_go_right/Attack__007.png'),
pygame.image.load('hero/hero_go_right/Attack__008.png'),
pygame.image.load('hero/hero_go_right/Attack__009.png'),
pygame.image.load('hero/hero_go_right/Jump_Attack__000.png'),
pygame.image.load('hero/hero_go_right/Jump_Attack__001.png'),
pygame.image.load('hero/hero_go_right/Jump_Attack__002.png'),
pygame.image.load('hero/hero_go_right/Jump_Attack__003.png'),
pygame.image.load('hero/hero_go_right/Jump_Attack__004.png'),
pygame.image.load('hero/hero_go_right/Jump_Attack__005.png'),
pygame.image.load('hero/hero_go_right/Jump_Attack__006.png'),
pygame.image.load('hero/hero_go_right/Jump_Attack__007.png'),
pygame.image.load('hero/hero_go_right/Jump_Attack__008.png'),
pygame.image.load('hero/hero_go_right/Jump_Attack__009.png'),
pygame.image.load('hero/hero_go_right/Jump_Throw__000.png'),
pygame.image.load('hero/hero_go_right/Jump_Throw__001.png'),
pygame.image.load('hero/hero_go_right/Jump_Throw__002.png'),
pygame.image.load('hero/hero_go_right/Jump_Throw__003.png'),
pygame.image.load('hero/hero_go_right/Jump_Throw__004.png'),
pygame.image.load('hero/hero_go_right/Jump_Throw__005.png'),
pygame.image.load('hero/hero_go_right/Jump_Throw__006.png'),
pygame.image.load('hero/hero_go_right/Jump_Throw__007.png'),
pygame.image.load('hero/hero_go_right/Jump_Throw__008.png'),
pygame.image.load('hero/hero_go_right/Jump_Throw__009.png'),
]
is_jump = False
jump = 10
jump_count = 0
hero_speed = 5
hero_pos_x = 20
hero_pos_y = 282
stay_count = 0
run_r_count = 0 # счетчик картинок
bg_x = 0 # начальное положение заднего фона по х
running = True # основной цикл игры
while running:
    clock.tick(30) # частота обновления (если задать значение больше все действия будут быстрее?)
    screen.blit(background,(bg_x,0)) #(этот код нам нужен, если у нас будет одна большая карта, а не зацикленная на одном месте картинка?)
    # screen.blit(background, (bg_x+768, 0)) # здесь мы циклически ставим один задний фон за другим
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        screen.blit(hero_run_left[run_r_count % 10], (hero_pos_x, hero_pos_y))
        run_r_count += 1
        hero_pos_x -= hero_speed
        bg_x +=2
    elif keys[pygame.K_d]:
        screen.blit(hero_run_right[run_r_count%10], (hero_pos_x, hero_pos_y))
        run_r_count += 1
        hero_pos_x +=hero_speed
        bg_x-=2
    else:
        screen.blit(hero_stay[stay_count%27], (hero_pos_x,hero_pos_y)) # перебираем картинки анимации
        stay_count += 1
    if not is_jump:
        if keys[pygame.K_w]:
            is_jump = True

    else:
        if jump>= -10:
            if jump>0:
                hero_pos_y-=(jump**2) / 2
            else:
                hero_pos_y += (jump ** 2) / 2
            jump-=1
        else:
            is_jump = False
            jump = 10
    if bg_x == -1200:
        bg_x = 0

    pygame.display.update()
    for event in pygame.event.get(): # перебрать все возможные ивент в pygame, если quit - закрыть окно, или проще если жмем красный крест на окне - закрыть окно
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
