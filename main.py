
import pygame
import entities 
#from floors import*
from maps import*
timer = pygame.time.Clock()
pygame.init()

largura = 800
altura = 600
windows_size = (largura, altura)
screen = pygame.display.set_mode(windows_size)
pygame.display.set_caption('Edge King')

#Grupos onde serão contidos os sprites

objectGroup = pygame.sprite.Group()
red_cubeGroup = pygame.sprite.Group()
white_floorGroup = pygame.sprite.Group()
black_floorGroup = pygame.sprite.Group()
blue_floorGroup = pygame.sprite.Group()
red_floorGroup = pygame.sprite.Group()

#Plano de Fundo
back_ground = pygame.sprite.Sprite()
back_ground.image = pygame.image.load('data/sprites/back_ground.png')
back_ground.rect = pygame.Rect(0, 0, largura, altura)
back_ground.image = pygame.transform.scale(back_ground.image, [largura, altura])

#Música e Efeitos
def playlist(musics, stop):
    if stop == True:
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.unload()
        pygame.mixer.music.load(f'data/sounds/music/{musics}')
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(-1) 
    if  musics == 'F2.wav':
        pygame.mixer.music.set_volume(0.18)
    if musics == 'Sentimental.wav':
        pygame.mixer.music.set_volume(0.2)
        
step = pygame.mixer.Sound('data/sounds/efects/Step.wav')
teleport = pygame.mixer.Sound('data/sounds/efects/Teleport.wav')
die = pygame.mixer.Sound('data/sounds/efects/FX292.mp3')
win = pygame.mixer.Sound('data/sounds/efects/Win.wav')
teleport.set_volume(0.18)
step.set_volume(0.18)
die.set_volume(0.36)


#Playlist
musics = ['Space.mp3','Elvis.wav','Enemy.wav','I_need_some_sleep.wav','Another_love.wav','Radioactive.wav','The_scientist.wav','Sentimental.wav','Rick_Morty.wav','F2.wav','Touch_Daft_Punk.wav']


list_white = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
list_blue = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
list_black = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
list_red = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

#Criação de todas as variaveis dos pisos e armazenando em suas respectivas matrizes.

for i in range(18):
    for j in range(15):
        piso_branco = entities.PisoBranco()
        list_white[i].append(piso_branco)
for i in range(18):
    for j in range(15):
        piso_preto = entities.PisoPreto()
        list_black[i].append(piso_preto)
for i in range(18):
    for j in range(15):
        piso_azul = entities.PisoAzul()
        list_blue[i].append(piso_azul)

for i in range(18):
    for j in range(15):
        piso_vermelho = entities.PisoVermelho()
        list_red[i].append(piso_vermelho)

#Cubo vermelho
cube = entities.Cube(red_cubeGroup)


#Função responsável por desenhar o mapa com base na lista dos niveis.
def drawmap(mapa):
    pisos_totais = 0
    pisos = 0
    count_blue_alive = 0
    list_blue_alive = []  

    i = 0
    for row in mapa:
        j = 0
        for tile in row:
            list_white[i][j].kill()
            list_black[i][j].kill()
            list_blue[i][j].kill()
            list_red[i][j].kill()
            j += 1
        i += 1
    
    y = 0
    for linha in mapa:
        x = 0
        for celula in linha:
            if celula == '1' or celula == '5' or celula == '2':
                list_white[y][x].add(objectGroup, white_floorGroup)  
                list_white[y][x].rect.x = 405 + 22*x - 22*y
                list_white[y][x].rect.y = 90 + 11*x + 11*y
                pisos_totais += 1
                            
            if celula == '2':
                list_black[y][x].add(objectGroup, black_floorGroup)      
                list_black[y][x].rect.x = 405 + 22*x - 22*y
                list_black[y][x].rect.y = 90 + 11*x + 11*y
           
            if celula == '3':
                list_blue[y][x].add(objectGroup, blue_floorGroup)    
                list_blue[y][x].rect.x = 405 + 22*x - 22*y
                list_blue[y][x].rect.y = 90 + 11*x + 11*y
                list_blue_alive.append(list_blue[y][x])
                count_blue_alive += 1
                pisos_totais += 1

            if celula == '4':
                list_red[y][x].add(objectGroup, red_floorGroup)      
                list_red[y][x].rect.x = 405 + 22*x - 22*y
                list_red[y][x].rect.y = 90 + 11*x + 11*y

            if celula == '5':
                cube.rect.x = 405 + 22*x - 22*y
                cube.rect.y =  81 + 11*x + 11*y        
            x += 1
        y += 1
    return pisos_totais, count_blue_alive, list_blue_alive, pisos



#Vetor com todos os níveis/matrizes
levels = [level01, level02, level03, level04, level05, level06,
          level07, level08, level09, level10, level11, level12,
          level13, level14, level15, level16, level17, level18,
          level19, level20, level21, level22, level23, level24,
          level25, level26, level27, level28, level29, level30]   

#Função do jogo, para ser chamada no menu()
def game_edge():

    #Lista com os dois pisos azuis que podem existir em uma fase. Necessário para a mecânica de teleporte.
    list_blue_alive_f = []
    segundos = 0.0
    minutos = 0
    horas = 0
    l = 1
    m = 1
    kill = 0

    fonte = pygame.font.SysFont('Impact',31,False,False)

    pisos_totais, count_blue_alive, list_blue_alive_f, pisos = drawmap(levels[l-1])
    playlist(musics[0],False)

    hadjkvdnjv = True
    ksnvuvnrun = False
    
    gameloop = True
    while gameloop:
        #Cronômetro
        segundos  += 1/60
        if segundos > 60:
            minutos  +=1
            segundos = 0.00
        if minutos == 60:
            horas +=1
            minutos = 00

        cronometro_text = fonte.render(f'{horas}:{minutos}:{segundos:.2f}', True, [255,255,255])

        #Mortes e Nivel - Texto
        mortes_nivel_text = fonte.render(f'{kill}/{l}', True, [255,255,255])
        kill_level_text = fonte.render(f'Mortes/Nível', True, [255,255,255])

        #Pisos restantes - Texto
        pisos_andamento = fonte.render('Pisos', True, [255,255,255])
        pisos_text = fonte.render(f'{pisos}/{pisos_totais}', True, [255,255,255])

        #Música - Texto
        music_text = fonte.render('Música : Parar|P| - Próxima|L| - Anterior|K|', True, [255,255,255])
        
        #Tela e atualizações
        screen.fill([255, 255, 255])
        screen.blit(back_ground.image,[0,0])
        screen.blit(cronometro_text,  [50,10])
        screen.blit(mortes_nivel_text,[350,50])
        screen.blit(kill_level_text,  [300,10])
        screen.blit(pisos_text,       [680,50])
        screen.blit(pisos_andamento,  [680, 10])
        screen.blit(music_text, [10,550])
        objectGroup.draw(screen)
        red_cubeGroup.draw(screen)

        #Teste de colisões, retornando uma lista com os sprites que colidiram. 
        colision_white = pygame.sprite.spritecollide(cube, white_floorGroup, False)
        colision_black = pygame.sprite.spritecollide(cube, black_floorGroup, False)
        colision_blue = pygame.sprite.spritecollide(cube, blue_floorGroup, False)
        colision_red = pygame.sprite.spritecollide(cube, red_floorGroup, False)

    
        #Lista de eventos e e suas aplicações
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:    
                gameloop = False
                return 1, segundos, minutos, horas, kill
               
            if event.type == pygame.KEYDOWN:

                #Mecânica dos pisos adicionada a partir da lista retornada nas colisões
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    if colision_white:
                        if colision_black:
                            pass
                        else:
                            pisos +=1
                            colision_white[0].kill()
                            print('Saiu do bloco branco!')
                        
                    if colision_black:
                        colision_black[0].kill()
                        print('Saiu do bloco preto!')
                    
                    if colision_blue:
                        pisos += 1
                        colision_blue[0].kill()
                        print( 'Saiu do bloco azul!')

                #Movimento do cubo.Funciona desde que o cubo inicie a fase alinhado com algum piso.         
            
                if event.key == pygame.K_UP:
                    cube.rect.x -= 22 
                    cube.rect.y -= 11
                    step.play()
                    
                if event.key == pygame.K_DOWN:
                    cube.rect.x += 22
                    cube.rect.y += 11
                    step.play()
                    
                if event.key == pygame.K_LEFT:
                    cube.rect.x -= 22
                    cube.rect.y += 11
                    step.play()
                
                if event.key == pygame.K_RIGHT:
                    cube.rect.x += 22
                    cube.rect.y -= 11
                    step.play()

                #Controle da Playlist 
                if event.key == pygame.K_l:
                    if m == len(musics) or m == len(musics)+1:
                        m = 0
                    playlist(musics[m], False)
                    m+=1
                    
                if event.key == pygame.K_k:
                    m -= 1
                    if m == 0:
                        m = len(musics)
                    playlist(musics[m-1], False)
    
                if event.key == pygame.K_p:
                    if m == len(musics):
                        playlist(musics[m-1], True)
                    else:
                        playlist(musics[m], True)
                

                                       
        #Game Over, Teleporte e Win
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT]:
    
            if colision_blue:
                if count_blue_alive == 2:
                    if colision_blue[0] == list_blue_alive_f[0]:
                        pisos += 1
                        count_blue_alive -= 1 
                        cube.rect.x = list_blue_alive_f[1].rect.x
                        cube.rect.y = list_blue_alive_f[1].rect.y - 9
                        colision_blue[0].kill()
                        teleport.play()
                        
                    if colision_blue[0] == list_blue_alive_f[1]:
                        pisos += 1
                        count_blue_alive -= 1
                        cube.rect.x = list_blue_alive_f[0].rect.x
                        cube.rect.y = list_blue_alive_f[0].rect.y - 9
                        colision_blue[0].kill()
                        teleport.play()
                    
                    print( 'Saiu do bloco azul!')

            if colision_red:
                
                if pisos == pisos_totais:
                    print('PASSOU DE FASE! :)')
                    win.play()
                    if l < len(levels):
                        pisos_totais, count_blue_alive, list_blue_alive_f, pisos= drawmap(levels[l])
                        l+=1
                    else:
                        gameloop = False
                        return l, segundos, minutos, horas, kill
                
            if not(colision_white or colision_black or colision_blue or colision_red):
                print('GAME OVER!')
                die.play()
                pisos_totais, count_blue_alive, list_blue_alive_f, pisos = drawmap(levels[l-1])
                kill += 1
   
            if kill == 7 and l == 11 and musics[m-1]=='Sentimental.wav':
                while hadjkvdnjv == True:
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load('data/sounds/music/Ressurections.wav')
                    pygame.mixer.music.set_volume(0.18)
                    pygame.mixer.music.play(-1)
                    drawmap(levelmx) 
                    ksnvuvnrun = True
                    hadjkvdnjv = False
            else:
                ksnvuvnrun = False

        if ksnvuvnrun:    
            hdvudusnakf = fonte.render('Legal ver você por aqui!', True, [255,255,255])
            screen.blit(hdvudusnakf, [490, 500])   
            
        pygame.display.update()
        timer.tick(60)












