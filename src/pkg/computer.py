import random
from .absplayer import Player

class Computer(Player):

    def __init__(self, name='Computer', score=0):
        self._name = name
        self._score = score


    def getChoice(self, choices):
        self._choice = random.randint(1, len(choices))
        return self._choice
    
    def __str__(self):
        return self._name

    def getName(self):
        return self._name

    def getScore(self):
        return self._score

    def setScore(self, score):
        self._score += score