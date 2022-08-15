
import pygame
from entities import Cube
from floors import*
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

#Lista contendo todos os possíveis pisos brancos
list_white = [[fw11,  fw12,  fw13,  fw14,  fw15,  fw16,  fw17,  fw18,  fw19,  fw110,  fw111,  fw112,  fw113,  fw114,   fw115],
              [fw21,  fw22,  fw23,  fw24,  fw25,  fw26,  fw27,  fw28,  fw29,  fw210,  fw211,  fw212,  fw213,  fw214,   fw215],
              [fw31,  fw32,  fw33,  fw34,  fw35,  fw36,  fw37,  fw38,  fw39,  fw310,  fw311,  fw312,  fw313,  fw314,   fw315],
              [fw41,  fw42,  fw43,  fw44,  fw45,  fw46,  fw47,  fw48,  fw49,  fw410,  fw411,  fw412,  fw413,  fw414,   fw415],
              [fw51,  fw52,  fw53,  fw54,  fw55,  fw56,  fw57,  fw58,  fw59,  fw510,  fw511,  fw512,  fw513,  fw514,   fw515],
              [fw61,  fw62,  fw63,  fw64,  fw65,  fw66,  fw67,  fw68,  fw69,  fw610,  fw611,  fw612,  fw613,  fw614,   fw615],
              [fw71,  fw72,  fw73,  fw74,  fw75,  fw76,  fw77,  fw78,  fw79,  fw710,  fw711,  fw712,  fw713,  fw714,   fw715],
              [fw81,  fw82,  fw83,  fw84,  fw85,  fw86,  fw87,  fw88,  fw89,  fw810,  fw811,  fw812,  fw813,  fw814,   fw815],
              [fw91,  fw92,  fw93,  fw94,  fw95,  fw96,  fw97,  fw98,  fw99,  fw910,  fw911,  fw912,  fw913,  fw914,   fw915],
              [fw101, fw102, fw103, fw104, fw105, fw106, fw107, fw108, fw109, fw1010, fw1011, fw1012, fw1013, fw1014, fw1015],
              [fw1101,fw1102,fw1103,fw1104,fw1105,fw1106,fw1107,fw1108,fw1109,fw1110, fw1111, fw1112, fw1113, fw1114, fw1115],
              [fw1201,fw1202,fw1203,fw1204,fw1205,fw1206,fw1207,fw1208,fw1209,fw1210, fw1211, fw1212, fw1213, fw1214, fw1215],
              [fw1301,fw1302,fw1303,fw1304,fw1305,fw1306,fw1307,fw1308,fw1309,fw1310, fw1311, fw1312, fw1313, fw1314, fw1315],
              [fw1401,fw1402,fw1403,fw1404,fw1405,fw1406,fw1407,fw1408,fw1409,fw1410, fw1411, fw1412, fw1413, fw1414, fw1415],
              [fw1501,fw1502,fw1503,fw1504,fw1505,fw1506,fw1507,fw1508,fw1509,fw1510, fw1511, fw1512, fw1513, fw1514, fw1515],
              [fw1601,fw1602,fw1603,fw1604,fw1605,fw1606,fw1607,fw1608,fw1609,fw1610, fw1611, fw1612, fw1613, fw1614, fw1615],
              [fw1701,fw1702,fw1703,fw1704,fw1705,fw1706,fw1707,fw1708,fw1709,fw1710, fw1711, fw1712, fw1713, fw1714, fw1715],
              [fw1801,fw1802,fw1803,fw1804,fw1805,fw1806,fw1807,fw1808,fw1809,fw1810, fw1811, fw1812, fw1813, fw1814, fw1815]]


#Lista contendo todos os possíveis pisos pretos
list_black = [[fk11,  fk12,  fk13,  fk14,  fk15,  fk16,  fk17,  fk18,  fk19,  fk110,  fk111,  fk112,  fk113,  fk114,   fk115],
              [fk21,  fk22,  fk23,  fk24,  fk25,  fk26,  fk27,  fk28,  fk29,  fk210,  fk211,  fk212,  fk213,  fk214,   fk215],
              [fk31,  fk32,  fk33,  fk34,  fk35,  fk36,  fk37,  fk38,  fk39,  fk310,  fk311,  fk312,  fk313,  fk314,   fk315],
              [fk41,  fk42,  fk43,  fk44,  fk45,  fk46,  fk47,  fk48,  fk49,  fk410,  fk411,  fk412,  fk413,  fk414,   fk415],
              [fk51,  fk52,  fk53,  fk54,  fk55,  fk56,  fk57,  fk58,  fk59,  fk510,  fk511,  fk512,  fk513,  fk514,   fk515],
              [fk61,  fk62,  fk63,  fk64,  fk65,  fk66,  fk67,  fk68,  fk69,  fk610,  fk611,  fk612,  fk613,  fk614,   fk615],
              [fk71,  fk72,  fk73,  fk74,  fk75,  fk76,  fk77,  fk78,  fk79,  fk710,  fk711,  fk712,  fk713,  fk714,   fk715],
              [fk81,  fk82,  fk83,  fk84,  fk85,  fk86,  fk87,  fk88,  fk89,  fk810,  fk811,  fk812,  fk813,  fk814,   fk815],
              [fk91,  fk92,  fk93,  fk94,  fk95,  fk96,  fk97,  fk98,  fk99,  fk910,  fk911,  fk912,  fk913,  fk914,   fk915],
              [fk101, fk102, fk103, fk104, fk105, fk106, fk107, fk108, fk109, fk1010, fk1011, fk1012, fk1013, fk1014, fk1015],
              [fk1101,fk1102,fk1103,fk1104,fk1105,fk1106,fk1107,fk1108,fk1109,fk1110, fk1111, fk1112, fk1113, fk1114, fk1115],
              [fk1201,fk1202,fk1203,fk1204,fk1205,fk1206,fk1207,fk1208,fk1209,fk1210, fk1211, fk1212, fk1213, fk1214, fk1215],
              [fk1301,fk1302,fk1303,fk1304,fk1305,fk1306,fk1307,fk1308,fk1309,fk1310, fk1311, fk1312, fk1313, fk1314, fk1315],
              [fk1401,fk1402,fk1403,fk1404,fk1405,fk1406,fk1407,fk1408,fk1409,fk1410, fk1411, fk1412, fk1413, fk1414, fk1415],
              [fk1501,fk1502,fk1503,fk1504,fk1505,fk1506,fk1507,fk1508,fk1509,fk1510, fk1511, fk1512, fk1513, fk1514, fk1515],
              [fk1601,fk1602,fk1603,fk1604,fk1605,fk1606,fk1607,fk1608,fk1609,fk1610, fk1611, fk1612, fk1613, fk1614, fk1615],
              [fk1701,fk1702,fk1703,fk1704,fk1705,fk1706,fk1707,fk1708,fk1709,fk1710, fk1711, fk1712, fk1713, fk1714, fk1715],
              [fk1801,fk1802,fk1803,fk1804,fk1805,fk1806,fk1807,fk1808,fk1809,fk1810, fk1811, fk1812, fk1813, fk1814, fk1815]]

#Lista contendo todos os possíveis pisos azuis
list_blue  = [[fb11,  fb12,  fb13,  fb14,  fb15,  fb16,  fb17,  fb18,  fb19,  fb110,  fb111,  fb112,  fb113,  fb114,   fb115],
              [fb21,  fb22,  fb23,  fb24,  fb25,  fb26,  fb27,  fb28,  fb29,  fb210,  fb211,  fb212,  fb213,  fb214,   fb215],
              [fb31,  fb32,  fb33,  fb34,  fb35,  fb36,  fb37,  fb38,  fb39,  fb310,  fb311,  fb312,  fb313,  fb314,   fb315],
              [fb41,  fb42,  fb43,  fb44,  fb45,  fb46,  fb47,  fb48,  fb49,  fb410,  fb411,  fb412,  fb413,  fb414,   fb415],
              [fb51,  fb52,  fb53,  fb54,  fb55,  fb56,  fb57,  fb58,  fb59,  fb510,  fb511,  fb512,  fb513,  fb514,   fb515],
              [fb61,  fb62,  fb63,  fb64,  fb65,  fb66,  fb67,  fb68,  fb69,  fb610,  fb611,  fb612,  fb613,  fb614,   fb615],
              [fb71,  fb72,  fb73,  fb74,  fb75,  fb76,  fb77,  fb78,  fb79,  fb710,  fb711,  fb712,  fb713,  fb714,   fb715],
              [fb81,  fb82,  fb83,  fb84,  fb85,  fb86,  fb87,  fb88,  fb89,  fb810,  fb811,  fb812,  fb813,  fb814,   fb815],
              [fb91,  fb92,  fb93,  fb94,  fb95,  fb96,  fb97,  fb98,  fb99,  fb910,  fb911,  fb912,  fb913,  fb914,   fb915],
              [fb101, fb102, fb103, fb104, fb105, fb106, fb107, fb108, fb109, fb1010, fb1011, fb1012, fb1013, fb1014, fb1015],
              [fb1101,fb1102,fb1103,fb1104,fb1105,fb1106,fb1107,fb1108,fb1109,fb1110, fb1111, fb1112, fb1113, fb1114, fb1115],
              [fb1201,fb1202,fb1203,fb1204,fb1205,fb1206,fb1207,fb1208,fb1209,fb1210, fb1211, fb1212, fb1213, fb1214, fb1215],
              [fb1301,fb1302,fb1303,fb1304,fb1305,fb1306,fb1307,fb1308,fb1309,fb1310, fb1311, fb1312, fb1313, fb1314, fb1315],
              [fb1401,fb1402,fb1403,fb1404,fb1405,fb1406,fb1407,fb1408,fb1409,fb1410, fb1411, fb1412, fb1413, fb1414, fb1415],
              [fb1501,fb1502,fb1503,fb1504,fb1505,fb1506,fb1507,fb1508,fb1509,fb1510, fb1511, fb1512, fb1513, fb1514, fb1515],
              [fb1601,fb1602,fb1603,fb1604,fb1605,fb1606,fb1607,fb1608,fb1609,fb1610, fb1611, fb1612, fb1613, fb1614, fb1615],
              [fb1701,fb1702,fb1703,fb1704,fb1705,fb1706,fb1707,fb1708,fb1709,fb1710, fb1711, fb1712, fb1713, fb1714, fb1715],
              [fb1801,fb1802,fb1803,fb1804,fb1805,fb1806,fb1807,fb1808,fb1809,fb1810, fb1811, fb1812, fb1813, fb1814, fb1815]]

#Lista contendo todos os possíveis pisos vermelhos
list_red   = [[fr11,  fr12,  fr13,  fr14,  fr15,  fr16,  fr17,  fr18,  fr19,  fr110,  fr111,  fr112,  fr113,  fr114,   fr115],
              [fr21,  fr22,  fr23,  fr24,  fr25,  fr26,  fr27,  fr28,  fr29,  fr210,  fr211,  fr212,  fr213,  fr214,   fr215],
              [fr31,  fr32,  fr33,  fr34,  fr35,  fr36,  fr37,  fr38,  fr39,  fr310,  fr311,  fr312,  fr313,  fr314,   fr315],
              [fr41,  fr42,  fr43,  fr44,  fr45,  fr46,  fr47,  fr48,  fr49,  fr410,  fr411,  fr412,  fr413,  fr414,   fr415],
              [fr51,  fr52,  fr53,  fr54,  fr55,  fr56,  fr57,  fr58,  fr59,  fr510,  fr511,  fr512,  fr513,  fr514,   fr515],
              [fr61,  fr62,  fr63,  fr64,  fr65,  fr66,  fr67,  fr68,  fr69,  fr610,  fr611,  fr612,  fr613,  fr614,   fr615],
              [fr71,  fr72,  fr73,  fr74,  fr75,  fr76,  fr77,  fr78,  fr79,  fr710,  fr711,  fr712,  fr713,  fr714,   fr715],
              [fr81,  fr82,  fr83,  fr84,  fr85,  fr86,  fr87,  fr88,  fr89,  fr810,  fr811,  fr812,  fr813,  fr814,   fr815],
              [fr91,  fr92,  fr93,  fr94,  fr95,  fr96,  fr97,  fr98,  fr99,  fr910,  fr911,  fr912,  fr913,  fr914,   fr915],
              [fr101, fr102, fr103, fr104, fr105, fr106, fr107, fr108, fr109, fr1010, fr1011, fr1012, fr1013, fr1014, fr1015],
              [fr1101,fr1102,fr1103,fr1104,fr1105,fr1106,fr1107,fr1108,fr1109,fr1110, fr1111, fr1112, fr1113, fr1114, fr1115],
              [fr1201,fr1202,fr1203,fr1204,fr1205,fr1206,fr1207,fr1208,fr1209,fr1210, fr1211, fr1212, fr1213, fr1214, fr1215],
              [fr1301,fr1302,fr1303,fr1304,fr1305,fr1306,fr1307,fr1308,fr1309,fr1310, fr1311, fr1312, fr1313, fr1314, fr1315],
              [fr1401,fr1402,fr1403,fr1404,fr1405,fr1406,fr1407,fr1408,fr1409,fr1410, fr1411, fr1412, fr1413, fr1414, fr1415],
              [fr1501,fr1502,fr1503,fr1504,fr1505,fr1506,fr1507,fr1508,fr1509,fr1510, fr1511, fr1512, fr1513, fr1514, fr1515],
              [fr1601,fr1602,fr1603,fr1604,fr1605,fr1606,fr1607,fr1608,fr1609,fr1610, fr1611, fr1612, fr1613, fr1614, fr1615],
              [fr1701,fr1702,fr1703,fr1704,fr1705,fr1706,fr1707,fr1708,fr1709,fr1710, fr1711, fr1712, fr1713, fr1714, fr1715],
              [fr1801,fr1802,fr1803,fr1804,fr1805,fr1806,fr1807,fr1808,fr1809,fr1810, fr1811, fr1812, fr1813, fr1814, fr1815]]

#Cubo vermelho
cube = Cube(red_cubeGroup)


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












