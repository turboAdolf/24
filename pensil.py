from pygame import *
from random import randint

font1 = font.init()

font1 = font.Font(None, 40)

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('galaxy.jpg'), (700,500))

lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,speed_player):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100,100))
        self.speed_player = speed_player
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed_player
        global lost
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(50,win_width - 50)
            lost = lost + 1
    mixer.init()
    mixer.music.load('alahah.ogg')
    mixer.music.play()
    kick = mixer.Sound('alahah.ogg')
    kick.play()

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed_player
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed_player
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_player
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed_player

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx-50, self.rect.top, 15)
        bullets.add(bullet)




bon=Player('rocket.png', 30, 100, 8)
enemy = Enemy('ufo.png', 30, 100, 1)
enemy1 = Enemy('ufo.png', 30, 100, 2)
enemy2 = Enemy('ufo.png', 30, 100, 2)
enemy3 = Enemy('ufo.png', 30, 100, 3)
enemy4 = Enemy('ufo.png', 30, 100, 2)
steroid = Enemy('asteroid.png', 70, 200, 6)
steroid2 = Enemy('asteroid.png', 70, 200, 6)
steroid3 = Enemy('asteroid.png', 70, 200, 6)


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed_player
        if self.rect.y < 0:
            self.kill()



asteroids = sprite.Group()
monsters = sprite.Group()
bullets = sprite.Group()
monsters.add(enemy, enemy3, enemy1, enemy2, enemy4)
asteroids.add(steroid, steroid2, steroid3)


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

count_kill = 0

run = True

clock = time.Clock()
FPS = 60
finish = False


ggg = font1.render('Колчество убитых:' +str(count_kill), True, (14, 88, 52))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                #fire_sound.play('badabim-badabum.ogg')
                bon.fire()


    if finish != True:
        window.blit(background, (0, 0))
        ggg = font1.render('Колчество убитых:' + str(count_kill), True, (14, 88, 52))
        window.blit(ggg, (40, 55))
        bebrun = font1.render('Кличество пропущенных:' + str(lost), True, (14, 88, 52))
        window.blit(bebrun, (40, 80))
        bon.update()
        bon.reset()
        monsters.draw(window)
        monsters.update()
        asteroids.draw(window)
        asteroids.update()
        bullets.draw(window)
        bullets.update()
        pisun = sprite.groupcollide(monsters, bullets, True , True)
        for i in pisun:
            count_kill += 1
            ufo = Enemy('ufo.png', randint(1, 7), randint (50,600) , 8)
            monsters.add(ufo)
        if count_kill > 10:
            finish = True
            bebr = font1.render('Winner' , True, (0, 188, 52))
            window.blit(bebr, (250, 300))
        if lost > 15:
            finish = True
            bebca = font1.render('Lose' , True, (0, 200, 52))
            window.blit(bebca, (250, 300))
        sprites_list = sprite.spritecollide(bon, asteroids,True)
        for i in sprites_list:
            steroid4 =  Enemy('asteroid.png', 70, 200, 6)
            asteroids.add(steroid4)




    display.update()

    clock.tick(FPS)