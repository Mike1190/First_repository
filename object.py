import pygame


class Object(pygame.sprite.Sprite):
    def init(self, x,y,speed, filename):
        pygame.sprite.Sprite.init(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.dx = 0;self.dy=0
        self.on_ground = False  #0
        self.jump = False   #0
        self.slide = False  #0
        self.walk = False   #0
        self.right = False  #0
        self.left = False   #0
        self.frame = 0

    def update(self, *args) -> None:
        self.rect.x += self.dx
        if not (self.on_ground):
            self.dy+=1
        self.rect.y+=self.dy
        self.on_ground = False  #0



        if self.rect.y>args[0]:
            self.rect.y = args[0]
            self.dy = 0
            self.on_ground = True   #1



        pers = ['000.png', '001.png', '002.png', '003.png', '004.png', '005.png',
                '006.png', '007.png', '008.png', '009.png', ]

        if self.walk:
            self.frame += 0.5
            if self.frame > 9:
                self.frame -= 9
            if self.right:
                self.image = pygame.image.load(f'hero/hero_go_right/Run__'+ pers[int(self.frame)]).convert_alpha()
            if self.left:
                self.image = pygame.image.load('hero/hero_go_left/Run__'+ pers[int(self.frame)]).convert_alpha()
        elif self.jump:
            self.frame += 0.18
            if self.frame > 9:
                self.frame -= 9
            self.image = pygame.image.load('hero/hero_go_right/Jump__' + pers[int(self.frame)]).convert_alpha()
        elif self.slide:
            self.image = pygame.image.load('hero/hero_go_right/Slide__' + pers[int(self.frame)]).convert_alpha()


        else:
            self.frame += 0.1
            if self.frame > 9:
                self.frame -= 9
            self.image = pygame.image.load('hero/hero_go_right/Idle__' + pers[int(self.frame)]).convert_alpha()








        self.dx = 0