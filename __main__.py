from pygame import *
from random import randint

FPS = 240

win_width = 1080
win_height = 720
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('piper.jpg'), (1080,720))
window.fill((0,255,0))
clock = time.Clock()
FPS = 240

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,speed_player):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50,150))
        self.speed_player = speed_player
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()



        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed_player
        if keys[K_S] and self.rect.y < win_height - 80:
            self.rect.y += self.speed_player
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_player
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed_player

# player  = Player('adolfus.png', 30, 100, 4)
# player2 = Player('adolfus.png', 30, 100, 4)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(FPS)
    window.blit(background, (0, 0))