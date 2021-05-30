import pygame

class Scoring():
    def __init__(self):
        print("hello")

    #compares collected items and sees if it matches the items needed then adjusts the score correctly
    def checkscore(self, pList, wList, sb):
        if len(pList) == len(wList):
            if pList == wList:
                sb.score += (len(pList) * 100)
            else:
                count = 0
                for item in pList:
                    if item == wList[count]:
                        sb.score += 100
                    else:
                        sb.score -= 100
                    count += 1




