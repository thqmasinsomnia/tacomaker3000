import pygame
from boundries import Boundry
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width

        self.walking_frames_r = [
            pygame.image.load('player/running_animation_0.png'),
            pygame.image.load('player/running_animation_1.png'),
            pygame.image.load('player/running_animation_2.png'),
            pygame.image.load('player/running_animation_3.png'),
            pygame.image.load('player/running_animation_4.png'),
            pygame.image.load('player/running_animation_5.png'),
            pygame.image.load('player/running_animation_6.png'),
            pygame.image.load('player/running_animation_7.png')
        ]
        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x / 2, y / 2)
        self.pos = vec(x / 2, y / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.canJump = True
        self.walls = None
        self.playerList = []
        self.isLeft = False
        self.isRight = False
        self.rightCount = 0
        self.frame = 0
        self.leftCount = 0






        # Set speed vector

        self.pos = (x/2, y/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        if self.canJump:
            self.vel.y += -10
            self.canJump = False

    def update(self):

        self.acc = vec(0, 0.5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -0.5
            self.isRight = False
            self.isLeft = True
            self.leftCount += 1
        if keys[pygame.K_RIGHT]:
            self.acc.x = 0.5
            self.isRight = True
            self.isLeft = False
            self.rightCount +=1
        if keys[pygame.K_SPACE]:
            self.jump()

        if self.rightCount == 5:
            self.frame += 1
            self.rightCount = 0
        if self.frame == 7:
            self.frame = 0
        if self.isRight:
            self.image = self.walking_frames_r[self.frame]

        if self.leftCount == 5:
            self.frame += 1
            self.leftCount = 0
        if self.frame == 7:
            self.frame = 0
        if self.isLeft:
            self.image = pygame.transform.flip(self.walking_frames_r[self.frame], True, False)





        self.acc.x += self.vel.x * -0.12
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > 1000:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = 1000
        if self.pos.y < 0:
            self.vel.y = 0
            self.pos.y = 30


        self.rect.midbottom = self.pos
        hits = pygame.sprite.spritecollide(self, self.walls, False)

        if hits:

            self.pos.y = hits[0].rect.top
            self.vel.y = 0
            self.canJump = True