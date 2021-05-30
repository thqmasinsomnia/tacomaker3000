# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


import pygame
from player import Player
from boundries import Boundry
from cheese import Cheese
from setup import Setup
from Logic import Logic
from Scoreboard import Scoreboard
from Scoring import Scoring

import sys

screen_w = 1000
screen_h = 700

class Game:

    def run_game(self):
        pygame.init()
        su = Setup(screen_w, screen_h)
        su.create()
        log = Logic(su.screen, su.wall_list)
        log.newRound(su.player, su.all_sprite_list)


        su.all_sprite_list.add(log.all_sprite_list)


        # screen = pygame.display.set_mode((screen_w, screen_h))
        # pygame.display.set_caption('TACO HELL')
        # background_image = pygame.image.load("kitchen.jpg")
        # clock = pygame.time.Clock()
        #
        # pygame.display.flip()
        # all_sprite_list = pygame.sprite.Group()
        #
        # player = Player(100, 100)
        # wall_list = pygame.sprite.Group()
        #
        # #bottom boundry
        # boundry = Boundry(0, screen_h - 150, screen_w, 200)
        # wall_list.add(boundry)
        # all_sprite_list.add(boundry)
        #
        # count = 0
        # xloc = 100
        # totPlat = random.randint(6, 7)
        #
        # while(count < totPlat):
        #     platsize = random.randint(50, 100)
        #     yloc = random.randint(100, 500)
        #     boundry = Boundry(xloc, yloc, platsize, 10)
        #     wall_list.add(boundry)
        #     all_sprite_list.add(boundry)
        #     count += 1
        #     xloc += random.randint(100, 150)
        #     boundry.isMoving = True
        #     boundry.movingSpeed = random.randint(1, 5)
        #     if platsize % 2 == 0:
        #         boundry.movingDown = True
        #
        # cheese = Cheese(100, 100, screen, wall_list, player)
        # all_sprite_list.add(cheese)
        #
        #
        #
        #
        # player.walls = wall_list
        # all_sprite_list.add(player)
        #
        # running = True
        # while running:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             running = False
        #
        #
        #     all_sprite_list.update()
        #     screen.blit(background_image, [0, 0])
        #     all_sprite_list.draw(screen)
        #     pygame.display.flip()
        #     clock.tick(60)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            su.update(log.wantedList, log.round)

            print(su.player.playerList)
            log.checkEndRound(su.player, su.sb, su.all_sprite_list)




g = Game()
g.run_game()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
