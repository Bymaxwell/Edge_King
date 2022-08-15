import pygame
pygame.init()
from main import game_edge

timer = pygame.time.Clock()

largura = 800
altura = 600
windows_size = (largura, altura)
screen = pygame.display.set_mode(windows_size)
pygame.display.set_caption('Edge King')


back_ground = pygame.sprite.Sprite()
back_ground.image = pygame.image.load('data/sprites/back_ground_menu.png')
back_ground.rect = pygame.Rect(0,0,1,1)

begin = pygame.mixer.Sound('data/sounds/efects/Win.wav')


def menu():
    icone = pygame.image.load('data/sprites/icone.png')
    pygame.display.set_icon(icone)
    loop = True
    rodando = 0
    pygame.mixer.music.unload()
    pygame.mixer.music.load('data/sounds/music/Awake.wav')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)
    
    while loop:
        
          
        screen.fill([255,255,255])
        screen.blit(back_ground.image, [0,0])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    begin.play()
                    rodando, segundos, minutos, horas, kill = game_edge()
                   
        if rodando == 1:
            loop = False
        if rodando == 30:
            rodando = creditos(segundos, minutos, horas, kill)
        if rodando == 2:
            pygame.mixer.music.unload()
            pygame.mixer.music.load('data/sounds/music/Awake.wav')
            pygame.mixer.music.set_volume(0.25)
            pygame.mixer.music.play(-1)
            rodando = 3
            

        timer.tick(60)

def creditos(segundos, minutos, horas, kill):
    pygame.mixer.music.unload()
    pygame.mixer.music.load('data/sounds/music/Awake.wav')
    pygame.mixer.music.play(-1)
    #Fontes
    fonte = pygame.font.SysFont('Impact', 31, False, False)
    fonte_data = pygame.font.SysFont('Impact', 25, False, True)
    fonte_insp = pygame.font.SysFont('Impact', 31, False, True)
    fonte_final = pygame.font.SysFont('Segoe Script',31, False, False)
    #Textos
    agradecimentos_text = fonte.render('Agradeço por jogar Edge King', True, [255,255,255])
    autor_text = fonte_final.render('By Max', True, [255,255,255])
    inspiracao_text = fonte_insp.render('Inspirado em On The Edge', True, [255,255,255])
    cronometro_text = fonte.render(f'Tempo total  |{horas}:{minutos}:{segundos:.2f}|', True, [255,255,255])
    kill_text = fonte.render(f'{kill} Mortes', True, [255,255,255])
    data = fonte_data.render('14/07/2022', True, [255,255,255])
    
    loop = True
    while loop:
        screen.fill([0,0,0])
        screen.blit(agradecimentos_text, [225,75])
        screen.blit(autor_text, [325, 525])
        screen.blit(inspiracao_text,[235, 450])
        screen.blit(cronometro_text,  [275,200])
        screen.blit(kill_text, [350, 300])
        screen.blit(data, [650, 550])
        pygame.display.update()
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                return 2 
                             
menu()            