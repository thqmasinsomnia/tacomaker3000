import pygame
import random
from cheese import Cheese
from beef import Beef
from tomato import Tomato
from lettuce import Lettuce
from shell import Shell
from Scoring import Scoring

class Logic():
    def __init__(self,screen, boundries):
        self.round = 0
        self.playerList = []
        self.wantedList = []
        self.all_sprite_list = pygame.sprite.Group()
        self.screen = screen
        self.bound = boundries

        self.scoring = Scoring()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)


    def newRound(self, player, asl):

        for a in asl:
            if isinstance(a, Cheese):
                a.kill()
            if isinstance(a, Shell):
                a.kill()
            if isinstance(a, Tomato):
                a.kill()
            if isinstance(a, Beef):
                a.kill()
            if isinstance(a, Lettuce):
                a.kill()


        self.wantedList = []
        self.round += 1

        wantCount = 0
        wantAmount = random.randint(3, 5)
        while (wantCount < wantAmount):

            item = random.randint(1,5)

            if item == 1:
                self.wantedList.append('c')
            if item == 2:
                self.wantedList.append('b')
            if item == 3:
                self.wantedList.append('l')
            if item == 4:
                self.wantedList.append('t')
            if item == 5:
                self.wantedList.append('s')
            wantCount += 1

        print(len(self.wantedList))
        count = 0

        for item in self.wantedList:
            print("HELLO")
            xloc = random.randint(0, 1000)
            yloc = random.randint(100, 500)
            if item == 'c':
                add = Cheese(xloc, yloc, self.screen, self.bound, player)
            if item == 'b':
                add = Beef(xloc, yloc, self.screen, self.bound, player)
            if item == 'l':
                add = Lettuce(xloc, yloc, self.screen, self.bound, player)
            if item == 't':
                add = Tomato(xloc, yloc, self.screen, self.bound, player)
            if item == 's':
                add = Shell(xloc, yloc, self.screen, self.bound, player)
            asl.add(add)


        while (count < 10):
            xloc = random.randint(0, 1000)
            yloc = random.randint(100, 500)
            item = random.randint(1,5)
            if item == 1:
                add = Cheese(xloc, yloc, self.screen, self.bound, player)
            if item == 2:
                add = Beef(xloc, yloc, self.screen, self.bound, player)
            if item == 3:
                add = Lettuce(xloc, yloc, self.screen, self.bound, player)
            if item == 4:
                add = Tomato(xloc, yloc, self.screen, self.bound, player)
            if item == 5:
                add = Shell(xloc, yloc, self.screen, self.bound, player)
            asl.add(add)

            count += 1




    def checkEndRound(self, player, sb, asl):
        if len(player.playerList) == len(self.wantedList):
            print("yoooo")
            self.scoring.checkscore(player.playerList, self.wantedList, sb)
            player.playerList = []
            self.newRound(player, asl)



