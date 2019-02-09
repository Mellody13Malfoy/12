import os 
import pygame.key
import pygame
import random
import sys

pygame.init()
# размеры окна: 
size = width, height = 800, 600
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
screen.fill((135, 206, 250))
FPS = 50
step = 50
n = 0
clock = pygame.time.Clock()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

def terminate():
    pygame.quit()
    sys.exit()

def inst():
    pygame.init()
    # размеры окна: 
    size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    screen.fill((135, 206, 250))
    font = pygame.font.Font(None, 60)
    text = font.render("Инструкция", True, (255, 99, 17))
    font1 = pygame.font.Font(None, 30)
    text1 = font1.render("Привет!",True, (255, 99, 17))
    text_1 = font1.render("Назад(нажми backspase)", True, (255, 99, 17))
    text2 = font1.render("Что это?",True, (255, 99, 17))
    text3 = font1.render(' Это обучающая игра "Math Drive" для развития твоих ',True, (255, 99, 17))
    text4 = font1.render('интеллектуальных способностей.Она поможет тебе быстрее вычислять ',True, (255, 99, 17))
    text5 = font1.render('различные примеры из таблицы умножения что очень пригодится тебе ',True, (255, 99, 17))
    text6 = font1.render('в дальнейшем на уроках математики.',True, (255, 99, 17))
    
    text7 = font1.render("Как играть?",True, (255, 99, 17))
    text8 = font1.render('Передвигай машинку вверх и вниз, используя кнопки, чтобы перейти ', True, (255, 99, 17))
    text9 = font1.render('на ряд с нужным ответом на пример в облачке наверху, чтобы потом ', True, (255, 99, 17))
    text11 = font1.render('получить мидаль.Чтобы выйти из игры нажми backspase.', True, (255, 99, 17))
    text10 = font1.render('Думай быстрои у тебя всё получится!', True, (255, 99, 17))
    #Рисуем изображение текста на экран в точке (250, 250)
    screen.blit(text, [200, 50] )
    screen.blit(text_1, [530, 50] )
    screen.blit(text1, [50, 150] )
    screen.blit(text2, [50, 180] )
    screen.blit(text3, [50, 210] )
    screen.blit(text4, [50, 240] )
    screen.blit(text5, [50, 270] )
    screen.blit(text6, [50, 300] )
    screen.blit(text7, [50, 400] )
    screen.blit(text8, [50, 450] )
    screen.blit(text9, [50, 480] )
    screen.blit(text11, [50, 510] )
    screen.blit(text10, [50, 540] )
    # ожидание закрытия окна:
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_BACKSPACE:          
                    start_screen()
    pygame.quit()
    sys.exit()

def rez():
    global n 
    pygame.init()
    # размеры окна: 
    size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    screen.fill((135, 206, 250))
    d = [6000, 3000, 2000, 500, 100,]
    for i in range(len(d)):
        if int(n) > d[i]:
            d.append(int(n))
            d.sort(reverse = True)
            del d [-1]
            break
    for i in range(len(d)):
        font1 = pygame.font.Font(None, 50)
        text10 = font1.render(str(d[i]),True, (255, 99, 17))
        screen.blit(text10, [200, 200 + (70 * i)])
    font = pygame.font.Font(None, 60)
    text = font.render("Результаты", True, (255, 99, 17))
    font1 = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 30)
    text1 = font1.render("1",True, (255, 99, 17))
    text_1 = font2.render("Назад(нажми backspase)", True, (255, 99, 17))
    text2 = font1.render("2",True, (255, 99, 17))
    text3 = font1.render('3',True, (255, 99, 17))
    text4 = font1.render('4',True, (255, 99, 17))
    text5 = font1.render('5',True, (255, 99, 17))
    text6 = font1.render('Место',True, (255, 99, 17))
    #Рисуем изображение текста на экран в точке (250, 250)
    screen.blit(text, [200, 50] )
    screen.blit(text_1, [530, 50] )
    screen.blit(text1, [50, 200] )
    screen.blit(text2, [50, 270] )
    screen.blit(text3, [50, 340] )
    screen.blit(text4, [50, 410] )
    screen.blit(text5, [50, 480] )
    screen.blit(text6, [50, 140] )
    # ожидание закрытия окна:
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_BACKSPACE:          
                    start_screen()
    pygame.quit()
    sys.exit()

def car():
    global n
    pygame.init()
    # размеры окна: 
    size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    screen.fill((135, 206, 250))
    flag = False
    v = ['2*2', '2*3', '2*4', '2*5', '2*6', '2*7', '2*8', '2*9', '3*3', '3*4',
         '3*5', '3*6', '3*7', '3*8', '3*9', '4*4', '4*5', '4*6', '4*7', '4*8',
         '4*9', '5*5', '5*6', '5*7', '5*8', '5*9', '6*6', '6*7', '6*8', '6*9',
         '7*7', '7*8', '7*9', '8*8', '8*9', '9*9']
    o = ['4', '6', '8', '10', '12', '14', '16', '18', '9', '12', '15', '18',
         '21', '24', '27', '16', '20', '24', '28', '32', '36', '25', '30', '35',
         '40', '45', '36', '42', '48', '54', '49', '56', '63', '64', '72', '81']
    o1= ['0', '7', '5', '12', '16', '10', '12', '12', '3', '11', '12', '19',
         '25', '22', '24', '14', '25', '28', '14', '24', '32', '30', '35', '25',
         '37', '39', '26', '32', '42', '52', '39', '58', '53', '54', '62', '71']
    o2= ['5', '3', '6', '17', '18', '11', '66', '15', '8', '17', '18', '14',
         '27', '28', '21', '12', '16', '20', '21', '40', '40', '20', '25', '15',
         '24', '27', '37', '41', '28', '51', '41', '47', '62', '62', '71', '57']
    pygame.draw.line(screen, (34, 139, 34), (0, 210), (800, 210), 30)
    pygame.draw.line(screen, (255, 255, 255), (0, 230), (800, 230), 9)
    pygame.draw.line(screen, (128, 128, 128), (0, 414), (800, 414), 360)
    pygame.draw.line(screen, (255, 255, 255), (0, 360), (800, 360), 9)
    pygame.draw.line(screen, (255, 255, 255), (0, 480), (800, 480), 9)
    pygame.draw.line(screen, (255, 255, 255), (0, 595), (800, 595), 9)
    pygame.draw.circle(screen, (255, 255, 255), (85, 60), 30, 0)
    pygame.draw.circle(screen, (255, 255, 255), (120, 55), 40, 0)
    pygame.draw.circle(screen, (255, 255, 255), (150, 60), 30, 0)
    pygame.draw.circle(screen, (255, 255, 255), (600, 60), 30, 0)
    pygame.draw.circle(screen, (255, 255, 255), (630, 55), 40, 0)
    pygame.draw.circle(screen, (255, 255, 255), (680, 60), 30, 0)
    pygame.draw.circle(screen, (255, 255, 255), (350, 90), 55, 0)
    pygame.draw.circle(screen, (255, 255, 255), (400, 85), 67, 0)
    pygame.draw.circle(screen, (255, 255, 255), (450, 90), 55, 0)

    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)
        image = image.convert_alpha()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        return image


    class Bomb(pygame.sprite.Sprite):
        image3 = load_image("poloska.png")
        
        image = pygame.transform.scale(image3, (100, 10))
        
        def __init__(self, group):
                # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
                # Это очень важно!!!
                super().__init__(group)
                self.image = Bomb.image
                self.rect = self.image.get_rect()
                self.rect.x = 800
                self.rect.y = random.choice([300, 425, 550])
        
        def update(self):

            if self.rect.x >= 0:
                self.rect = self.rect.move(random.randrange(2) - 200, 0)
            else:
                self.rect.x =  800
                self.rect.y = random.choice([300, 425, 550])
                
        def get_event(self, event):
                
                if self.rect.collidepoint(event.pos):
                    self.image = self.image_boom 
       
    all_sprites = pygame.sprite.Group()
    x1 = 750
    y1 = 230  
    for i in range(20):
        Bomb(all_sprites)

    def load_image1(name1, colorkey=None):
        fullname1 = os.path.join('data', name1)
        try:
            image1 = pygame.image.load(fullname1)
        except pygame.error as message:
            print('Cannot load image1:', name1)
            raise SystemExit(message)
        image1 = image1.convert_alpha()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image1.set_colorkey(colorkey)
        return image1
    image2 = load_image1("2.png")
    image = pygame.transform.scale(image2, (220, 220))
    pygame.draw.circle(screen, (255, 255, 255), (x1, y1), 30, 0)
    x = 0
    t = 0
    m = 0
    w = 3
    w1 = str(3)
    n = str(0)
    y = 290
    x1 = 750
    screen.blit(image, [x, y] )
    b = 20
    running = True
    while running:
        if x1 == 0:
            x1 == 800
        else:
            x1 -= 10
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False            
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_UP:
                    if y == 290 or y == 420:
                        y -= 130
                if event.key ==  pygame.K_DOWN:
                    if y == 160 or y == 290:
                        y += 130
                if event.key ==  pygame.K_BACKSPACE:
                    start_screen()            
        screen.fill((135, 206, 250))   
        pygame.draw.line(screen, (34, 139, 34), (0, 210), (800, 210), 30)
        pygame.draw.line(screen, (255, 255, 255), (0, 230), (800, 230), 9)
        pygame.draw.line(screen, (128, 128, 128), (0, 414), (800, 414), 360)
        pygame.draw.line(screen, (255, 255, 255), (0, 360), (800, 360), 9)
        pygame.draw.line(screen, (255, 255, 255), (0, 480), (800, 480), 9)
        pygame.draw.line(screen, (255, 255, 255), (0, 595), (800, 595), 9)
        pygame.draw.circle(screen, (255, 255, 255), (85, 60), 30, 0)
        pygame.draw.circle(screen, (255, 255, 255), (120, 55), 40, 0)
        pygame.draw.circle(screen, (255, 255, 255), (150, 60), 30, 0)
        pygame.draw.circle(screen, (255, 255, 255), (600, 60), 30, 0)
        pygame.draw.circle(screen, (255, 255, 255), (630, 55), 40, 0)
        pygame.draw.circle(screen, (255, 255, 255), (680, 60), 30, 0)
        if b == 20:
            b -= 20
            font = pygame.font.Font(None, 60)
            t = v.index(random.choice(v))
            text = font.render(v[t], True, (255, 99, 17))
            screen.blit(text, [590, 40])
            ot = [o[t], o1[t], o2[t]]
            q = random.choice(ot)
            ind = ot.index(q)
            del ot[ind]
            q1 = random.choice(ot)
            ind = ot.index(q1)
            del ot[ind]
            q2 = ''.join(ot)        
        else:
            b += 1
            screen.blit(text, [590, 40])
            if x1 >= 0:
                x1 -= 30
            else:
                x1 = 750
        pygame.draw.circle(screen, (178, 34, 34), (x1, 210), 30, 0)
        pygame.draw.circle(screen, (178, 34, 34), (x1, 380), 30, 0)
        pygame.draw.circle(screen, (178, 34, 34), (x1, 500), 30, 0)
        font_03 = pygame.font.Font(None, 30)
        text_03 = font_03.render("пример:", True, (255, 99, 17))
        screen.blit(text_03, [590, 20] )
        font1 = pygame.font.Font(None, 60)
        text1 = font1.render(q, True, (255, 99, 17))
        screen.blit(text1, [x1 - 23, y1-30])
        font2 = pygame.font.Font(None, 60)
        text2 = font2.render(q1, True, (255, 99, 17))
        screen.blit(text2, [x1 - 25, 364])
        font3 = pygame.font.Font(None, 60)
        text3 = font3.render(q2, True, (255, 99, 17))
        screen.blit(text3, [x1 - 27, 490])     
        pygame.draw.circle(screen, (255, 255, 255), (350, 90), 55, 0)
        pygame.draw.circle(screen, (255, 255, 255), (380, 85), 67, 0)
        pygame.draw.circle(screen, (255, 255, 255), (450, 90), 55, 0)
        all_sprites.draw(screen)
        image2 = load_image1("2.png")
        image = pygame.transform.scale(image2, (220, 220))
        screen.blit(image, [x, y] )
        if q == o[t] and y == 160 and x1 == 100:
            m += 100
            n = str(m)
            font_02 = pygame.font.Font(None, 30)
            text_02 = font_02.render("Очки:", True, (255, 99, 17))
            screen.blit(text_02, [350, 30] )
            font4 = pygame.font.Font(None, 60)
            text4 = font4.render(n, True, (255, 99, 17))
            screen.blit(text4, [350, 70])        
        elif q1 == o[t] and y == 290 and x1 == 100:
            m += 100
            n = str(m)
            font_02 = pygame.font.Font(None, 30)
            text_02 = font_02.render("Очки:", True, (255, 99, 17))
            screen.blit(text_02, [350, 30] )
            font4 = pygame.font.Font(None, 60)
            text4 = font4.render(n, True, (255, 99, 17))
            screen.blit(text4, [350, 70])         
        elif q2 == o[t] and y == 420 and x1 == 100:
            m += 100
            n = str(m)
            font_02 = pygame.font.Font(None, 30)
            text_02 = font_02.render("Очки:", True, (255, 99, 17))
            screen.blit(text_02, [350, 30] )
            font4 = pygame.font.Font(None, 60)
            text4 = font4.render(n, True, (255, 99, 17))
            screen.blit(text4, [350, 70])
        elif (y == 420 or y == 160 or y == 290) and x1 == 100 and q2 != o[t]:
            w -= 1
            w1 = str(w)
            font_01 = pygame.font.Font(None, 20)
            text_01 = font_01.render("Жизни:", True, (255, 99, 17))
            screen.blit(text_01, [80, 20] ) 
            font5 = pygame.font.Font(None, 60)
            text5 = font5.render(w1, True, (255, 99, 17))
            screen.blit(text5, [100, 40])
        font_01 = pygame.font.Font(None, 20)
        text_01 = font_01.render("Жизни:", True, (255, 99, 17))
        screen.blit(text_01, [80, 20] )
        font_02 = pygame.font.Font(None, 30)
        text_02 = font_02.render("Очки:", True, (255, 99, 17))
        screen.blit(text_02, [350, 30] )
        font5 = pygame.font.Font(None, 60)
        text5 = font5.render(w1, True, (255, 99, 17))  
        font4 = pygame.font.Font(None, 60)
        text4 = font4.render(n, True, (255, 99, 17))
        screen.blit(text4, [350, 70])
        screen.blit(text5, [100, 40])
        if int(w1) == 0:
            game()
        if int(n) >= 500 and int(n) <= 900:
            font_04 = pygame.font.Font(None, 30)
            text_04 = font_04.render("награда:", True, (255, 99, 17))
            screen.blit(text_04, [710, 90] )
            fon = pygame.transform.scale(load_image('20190120_122441.png'), (width, height))
            fon1 = pygame.transform.scale(fon, (80, 80))
            screen.blit(fon1, (720, 10))
        elif int(n) >= 1000 and int(n) <= 1900:
            font_04 = pygame.font.Font(None, 30)
            text_04 = font_04.render("награда:", True, (255, 99, 17))
            screen.blit(text_04, [710, 90] )
            fon = pygame.transform.scale(load_image('20190120_122347.png'), (width, height))
            fon1 = pygame.transform.scale(fon, (80, 80))
            screen.blit(fon1, (720, 10))
        elif int(n) >= 2000 and int(n) <= 4900:
            font_04 = pygame.font.Font(None, 30)
            text_04 = font_04.render("награда:", True, (255, 99, 17))
            screen.blit(text_04, [710, 90] )
            fon = pygame.transform.scale(load_image('20190120_122241.png'), (width, height))
            fon1 = pygame.transform.scale(fon, (80, 80))
            screen.blit(fon1, (720, 10))
        elif int(n) >= 5000:
            font_04 = pygame.font.Font(None, 30)
            text_04 = font_04.render("награда:", True, (255, 99, 17))
            screen.blit(text_04, [710, 90] )
            fon = pygame.transform.scale(load_image('20190120_121120.png'), (width, height))
            fon1 = pygame.transform.scale(fon, (80, 80))
            screen.blit(fon1, (720, 10))        
        all_sprites.update()    
        pygame.display.flip()
        # завершение работы:
    pygame.quit()
    sys.exit()

'''def mus():
    pygame.init()
    song = pygame.mixer.Sound('Jack & Jack - Beg.mp3')
    clock = pygame.time.Clock()
    song.play()
    while True:
        clock.tick(60)
    pygame.quit()'''

def game():
    pygame.init()
    # размеры окна: 
    size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    screen.fill((135, 206, 250))
    clock = pygame.time.Clock()
    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)
        image = image.convert_alpha()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        return image
    
    all_sprites = pygame.sprite.Group()
    
    
    class GAME(pygame.sprite.Sprite):
        image1 = load_image("maxresdefault.jpg")
        image = pygame.transform.scale(image1, (800, 600))
        
        def __init__(self, group):
                # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
                # Это очень важно!!!
                super().__init__(group)
                self.image = GAME.image
                self.rect = self.image.get_rect()
                self.rect.x = 700
                self.rect.y = 0
        def update(self):
            if self.rect.x != 0:
                self.rect.x -= 10
                
            else:
                self.rect.x = 0
                self.rect.y = 0
    all_sprites = pygame.sprite.Group()
    GAME(all_sprites)
    #mus()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_BACKSPACE:
                    start_screen()
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        screen.fill((135, 206, 250))
        clock.tick(200)
    pygame.quit()   

def start_screen():
    global n
    screen.fill((135, 206, 250))
    intro_text = ["",
                  "                                                  Привет!",
                  "",
                  "                                   чтобы начать играть нажми 'p'",
                  "                             чтобы прочитать правила нажми пробел",
                  "                         что бы прейти на таблицу результатов нажми 'r'",
                  "                                                   удачи вам "]
 
    fon = pygame.transform.scale(load_image('1547976103654.png'), (width, height))
    fon1 = pygame.transform.scale(fon, (220, 220))
    screen.blit(fon1, (270, 50))
    font = pygame.font.Font(None, 30)
    text_coord = 300
    if int(n) >= 500 and int(n) <= 900:
        font_04 = pygame.font.Font(None, 30)
        text_04 = font_04.render("награда:", True, (255, 99, 17))
        screen.blit(text_04, [670, 130] )
        fon = pygame.transform.scale(load_image('20190120_122441.png'), (width, height))
        fon1 = pygame.transform.scale(fon, (120, 120))
        screen.blit(fon1, (680, 10))
    elif int(n) >= 1000 and int(n) <= 1900:
        font_04 = pygame.font.Font(None, 30)
        text_04 = font_04.render("награда:", True, (255, 99, 17))
        screen.blit(text_04, [710, 90] )
        fon = pygame.transform.scale(load_image('20190120_122347.png'), (width, height))
        fon1 = pygame.transform.scale(fon, (80, 80))
        screen.blit(fon1, (720, 10))
    elif int(n) >= 2000 and int(n) <= 4900:
        font_04 = pygame.font.Font(None, 30)
        text_04 = font_04.render("награда:", True, (255, 99, 17))
        screen.blit(text_04, [710, 90] )
        fon = pygame.transform.scale(load_image('20190120_122241.png'), (width, height))
        fon1 = pygame.transform.scale(fon, (80, 80))
        screen.blit(fon1, (720, 10))
    elif int(n) >= 5000:
        font_04 = pygame.font.Font(None, 30)
        text_04 = font_04.render("награда:", True, (255, 99, 17))
        screen.blit(text_04, [710, 90] )
        fon = pygame.transform.scale(load_image('20190120_121120.png'), (width, height))
        fon1 = pygame.transform.scale(fon, (80, 80))
        screen.blit(fon1, (720, 10))
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color(0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_SPACE:
                    inst()
                if event.key ==  pygame.K_p:
                    car()
                if event.key ==  pygame.K_r:
                    rez()
        pygame.display.flip()
        clock.tick(FPS)
start_screen()
