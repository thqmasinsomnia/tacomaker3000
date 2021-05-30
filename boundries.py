import pygame

screen_w = 1000
screen_h = 700

class Boundry(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill((128,8,200))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.isMoving = False
        self.movingDown = False
        self.movingSpeed = 1


    def update(self):
        if self.isMoving == True:
            if not self.movingDown:
                if self.rect.y > 0:
                    self.rect.y -= self.movingSpeed
                if self.rect.y <= 0:
                    self.movingDown = True
            if self.movingDown:
                if self.rect.y < screen_h - 200:
                    self.rect.y += self.movingSpeed
                    if self.rect.y >= screen_h - 200:
                        self.movingDown = False


