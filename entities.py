import pygame

class Cube(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/sprites/red_cube.png')
        self.rect = pygame.Rect(400, 21, 12, 12)
       

class PisoBranco(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/sprites/white_floor.png')
        self.rect = pygame.Rect(400, 30, 2, 2)
       
            
class PisoPreto(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/sprites/black_floor.png')
        self.rect = pygame.Rect(400, 30, 2, 2)
       

class PisoAzul(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('data/sprites/blue_floor.png')
        self.rect = pygame.Rect(400, 30, 2, 2)
      

class PisoVermelho(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/sprites/red_floor.png')
        self.rect = pygame.Rect(400, 30, 2, 2)
     
