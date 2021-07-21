from .absplayer import Player

class Human(Player):
    """Concrete human player class"""
    def __init__(self, name='You', score=0):
        self._name = name
        self._score = score

    def getChoice(self, choices):
        choice_strings = ''
        for choice in choices:
            choice_strings += '{} {} \n'.format(choice, choices[choice])
        self._choice = int(input("{}Enter your move: ".format(choice_strings)))
        return self._choice

    def getName(self):
        return self._name
    
    def __str__(self):
        if(self._name == None):
            return 'You'
        return self._name

    def getScore(self):
        return self._score

    def setScore(self, score):
        self._score += score
