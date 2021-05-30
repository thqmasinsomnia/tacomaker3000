import pygame
from pygame.sprite import Sprite

class Cheese(Sprite):
    def __init__(self, x,y, screen, boundries, player):
        super(Cheese, self).__init__()
        self.player = player

        self.screen_rect = screen.get_rect()
        self.bd = boundries
        self.screen = screen

        self.image = pygame.image.load('items/cheese.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center = float(self.rect.centerx)


    def player_colide(self):
        col = pygame.sprite.collide_rect(self, self.player)

        if col:
            coin = pygame.mixer.Sound('coin.ogg')
            coin.play()

            self.kill()
            self.player.playerList.append('c')



    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.player_colide()

