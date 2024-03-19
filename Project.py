import pygame
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1200,845)) # flags = pygame.NOFRAME - убрать рамку у окна
pygame.display.set_caption('#') # задать название для окна
background = pygame.image.load('background/background.png') # задаем задний фон

walk_right = [pygame.image.load('hero/hero_go_right/Run__000.png'), # все картинки для анимации героя(идет вправо)
pygame.image.load('hero/hero_go_right/Run__001.png'),
pygame.image.load('hero/hero_go_right/Run__002.png'),
pygame.image.load('hero/hero_go_right/Run__003.png'),
pygame.image.load('hero/hero_go_right/Run__004.png'),
pygame.image.load('hero/hero_go_right/Run__005.png'),
pygame.image.load('hero/hero_go_right/Run__006.png'),
pygame.image.load('hero/hero_go_right/Run__007.png'),
pygame.image.load('hero/hero_go_right/Run__008.png'),
pygame.image.load('hero/hero_go_right/Run__009.png'),
]
walk_right_count = 0 # счетчик картинок
bg_x = 0 # начальное положение заднего фона по х
running = True # основной цикл игры
while running:
    clock.tick(20) # частота обновления (если задать значение больше все действия будут быстрее?)
    screen.blit(background,(bg_x,0))
    screen.blit(background, (bg_x+1200, 0)) # здесь мы циклически ставим один задний фон за другим
    screen.blit(walk_right[walk_right_count], (110,520)) # перебираем картинки анимации
    if walk_right_count == 9: # если картинки в списке walk_right закончились , обнулить счетчик walk_right_count , начать заново
        walk_right_count = 0
    else:
        walk_right_count+=1
    bg_x-=2 # передвигать каждую итерацию главного цикла задний фон на 2 пикселя?
    if bg_x == -1200:
        bg_x = 0

    pygame.display.update()
    for event in pygame.event.get(): # перебрать все возможные ивент в pygame , если quit - закрыть окно, или проще если жмем красный крест на окне - закрыть окно
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
