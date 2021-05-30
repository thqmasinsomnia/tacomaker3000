import pygame
from player import Player
from boundries import Boundry
from cheese import Cheese
import random
from Scoreboard import Scoreboard


class Setup():
    def __init__(self, screenw, screenh):
        self.screen_w = screenw
        self.screen_h = screenh
        self.screen =  pygame.display.set_mode((self.screen_w, self.screen_h))
        self.wall_list = None
        self.all_sprite_list = None
        self.background_image = None
        self.clock = None
        self.sb = Scoreboard(self.screen)

    def create(self):
        pygame.display.set_caption('TACO MAKER 3000')
        self.background_image = pygame.image.load("kitchen.jpg")
        self.clock = pygame.time.Clock()

        print("TACO MAKER 3000 BY THOMAS SMITH AND YUJI OSHIIRO")
        print("RESUME - CONTACT: thomas_smith_33@yahoo.com")
        print("MUSIC BY: windxws - ignorantwindows@gmail.com")

        pygame.display.flip()
        self.all_sprite_list = pygame.sprite.Group()

        self.player = Player(100, 1000)
        self.wall_list = pygame.sprite.Group()

        # bottom boundry
        boundry = Boundry(0, self.screen_h - 150, self.screen_w, 200)
        self.wall_list.add(boundry)
        self.all_sprite_list.add(boundry)

        count = 0
        xloc = 100
        totPlat = random.randint(6, 7)

        while (count < totPlat):
            platsize = random.randint(50, 100)
            yloc = random.randint(100, 500)
            boundry = Boundry(xloc, yloc, platsize, 10)
            self.wall_list.add(boundry)
            self.all_sprite_list.add(boundry)
            count += 1
            xloc += random.randint(100, 150)
            boundry.isMoving = True
            boundry.movingSpeed = random.randint(1, 5)
            if platsize % 2 == 0:
                boundry.movingDown = True

        cheese = Cheese(100, 100, self.screen, self.wall_list, self.player)
        self.all_sprite_list.add(cheese)

        self.player.walls = self.wall_list
        self.all_sprite_list.add(self.player)


    def update(self, wl, round):
        self.all_sprite_list.update()
        self.screen.blit(self.background_image, [0, 0])
        self.all_sprite_list.draw(self.screen)
        self.sb.update(wl, self.player.playerList, round)
        pygame.display.flip()
        self.clock.tick(60)