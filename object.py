import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, x,y,speed, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.dx = 0;self.dy=0
        self.is_jump = False
        self.walk = False
        self.frame = 0

    def update(self, *args) -> None:
        self.rect.x += self.dx
        if not (self.is_jump):
            self.dy+=1
        self.rect.y+=self.dy
        self.is_jump = False

        if self.rect.y>args[0]:
            self.rect.y = args[0]
            self.dy = 0
            self.is_jump = True
        if self.walk:
            self.frame+=0.5
            if self.frame>9:
                self.frame-=9
            pers = ['Run__000.png','Run__001.png','Run__002.png','Run__003.png','Run__004.png','Run__005.png','Run__006.png','Run__007.png','Run__008.png','Run__009.png',]
            self.image = pygame.image.load('hero/hero_go_right/'+ pers[int(self.frame)]).convert_alpha()




        self.dx = 0
