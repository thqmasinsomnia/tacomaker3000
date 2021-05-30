import pygame
from pygame.sprite import Sprite

class Beef(Sprite):
    def __init__(self, x,y, screen, boundries, player):
        super(Beef, self).__init__()
        self.player = player

        self.screen_rect = screen.get_rect()
        self.bd = boundries
        self.screen = screen

        self.image = pygame.image.load('items/beef.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center = float(self.rect.centerx)


    def player_colide(self):
        col = pygame.sprite.collide_rect(self, self.player)

        if col:
            self.kill()
            self.player.playerList.append('b')
            coin = pygame.mixer.Sound('coin.ogg')
            coin.play()



    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.player_colide()

