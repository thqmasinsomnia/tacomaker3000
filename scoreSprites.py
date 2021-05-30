import pygame
from pygame.sprite import Sprite

class ScoreSprites(Sprite):
    def __init__(self, x, y, screen):
        super(ScoreSprites, self).__init__()

        self.items = [
            pygame.image.load('items/cheese.png'),
            pygame.image.load('items/beef.png'),
            pygame.image.load('items/tomato.png'),
            pygame.image.load('items/lettuce.png'),
            pygame.image.load('items/taco-shell.png')
        ]

        self.screen_rect = screen.get_rect()
        self.screen = screen
        self.image = pygame.image.load('items/cheese.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center = float(self.rect.centerx)

    def setImage(self, item):
        if item == 'c':
            self.image = self.items[0]
        if item == 'b':
            self.image = self.items[0]
        if item == 't':
            self.image = self.items[0]
        if item == 'l':
            self.image = self.items[0]
        if item == 's':
            self.image = self.items[0]


    def blitme(self):
        self.screen.blit(self.image, self.rect)

