import pygame
from scoreSprites import ScoreSprites


class Scoreboard():
    def __init__(self, screen):
        self.score = 0
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.screen = screen
        self.screen_rect = screen.get_rect()


    def update(self, wl, pl, round):
        items = [
            pygame.image.load('items/cheese.png'),
            pygame.image.load('items/beef.png'),
            pygame.image.load('items/lettuce.png'),
            pygame.image.load('items/tomato.png'),
            pygame.image.load('items/taco-shell.png')
        ]

        txt = "Score: " + str(self.score)
        text = self.font.render(txt, True, self.text_color)
        textRect = text.get_rect()
        textRect.center = (100, 600)

        images = []

        for item in wl:
            if item == 'c':
                images.append(items[0])
            if item == 'b':
                images.append(items[1])
            if item == 'l':
                images.append(items[2])
            if item == 't':
                images.append(items[3])
            if item == 's':
                images.append(items[4])

        move = 650
        for x in images:
            self.screen.blit(x, [move, 580])
            move += 50


        wantedText = self.font.render("WANTED ITEMS: ", True, self.text_color)
        wantedTextRect = wantedText.get_rect()
        wantedTextRect.center = (500, 600)

        err = ""
        for item in pl:
            err += item + " "

            images2 = []

            for item2 in pl:
                if item2 == 'c':
                    images2.append(items[0])
                if item2 == 'b':
                    images2.append(items[1])
                if item2 == 'l':
                    images2.append(items[2])
                if item2 == 't':
                    images2.append(items[3])
                if item2 == 's':
                    images2.append(items[4])

            move = 650
            for x in images2:
                self.screen.blit(x, [move, 635])
                move += 50

        playerText = self.font.render("CURRENT ITEMS: ", True, self.text_color)
        playerTextRect = playerText.get_rect()

        playerTextRect.center = (500, 650)

        roundText = self.font.render("ORDER: " + str(round), True, self.text_color)
        roundTextRect = roundText.get_rect()
        roundTextRect.center = (200, 650)

        self.screen.blit(text, textRect)
        self.screen.blit(wantedText, wantedTextRect)
        self.screen.blit(playerText, playerTextRect)
        self.screen.blit(roundText, roundTextRect)
        pygame.display.update()

