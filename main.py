from pygame import *
from random import choice
window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('fon.jpg'), (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    

    def collidepoint(self, x,y):
        return self.rect.collidepoint(x,y)

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y>10:
            self.rect.y-=self.speed
        if keys[K_RIGHT] and self.rect.y<500 -10- self.rect.width:
            self.rect.y+=self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>10:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<500 -10- self.rect.width:
            self.rect.y+=self.speed

class Ball(GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, speed)
        self.direct = [0,0]

    def update(self):
        global score_l, score_r
        self.rect.x += self.speed*self.direct[0]
        self.rect.y += self.speed*self.direct[1]
        if self.rect.y<=0 or self.rect.y>=500-self.rect.height:
            self.direct[1] *= -1
        if self.rect.colliderect(pl_l) or self.rect.colliderect(pl_r):
            self.direct[0] *= -1
        if self.rect.x<=0:
            score_r += 1
            self.start()
        if self.rect.x>=700-self.rect.width:
            score_l += 1
            self.start()

    def start(self):
        self.rect.x = 325
        self.rect.y = 225
        ball.direct[0] = choice([-1,1])
        ball.direct[1] = choice([-1,1])

ball = Ball('ball.jpg', 350-25, 250-25, 50,50,5)
ball.direct[0] = choice([-1,1])
ball.direct[1] = choice([-1,1])

pl_l = Player('ball.jpg', 10, 200, 50,50,5)
pl_r = Player('ball.jpg', 650, 200, 50,50,5)

btn = GameSprite('btn.png',(700-137)/2, (500-72)/2, 137, 72, 0)

font.init()
font_1 = font.SysFont('Arial', 36)
win = ''

game = True
finish = True
menu = True
score_r = 0
score_l = 0
rule = 3
clock = time.Clock()
fps = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if menu:
        window.blit(background, (0,0))
        btn.reset()
        pressed = mouse.get_pressed()
        pos = mouse.get_pos()
        if pressed[0]:
            if btn.rect.collidepoint(pos[0], pos[1]):
                menu = False
                finish = False
                win = ''
                score_l = 0
                score_r = 0
        if win != '':
            winner = font_1.render('Победил '+win+'!', 1, (255,255,255))
            window.blit(winner, (150,350))
            scr = font_1.render('со счетом '+str(max(score_l, score_r))+':'+str(min(score_l, score_r)), 1, (255,255,255))
            window.blit(scr, (250,400))
    if not finish:
        window.blit(background, (0,0))
        ball.update()
        ball.reset()
        pl_l.update_l()
        pl_l.reset()
        pl_r.update_r()
        pl_r.reset()
        scr_left = font_1.render(
            str(score_l), 1, (255, 255, 255))
        window.blit(scr_left, (10,10))
        if score_l>=3:
            win = 'левый игрок'
            menu = True
            finish = True
        if score_r>=3:
            win = 'правый игрок'
            menu = True
            finish = True

    clock.tick(fps)
    display.update()