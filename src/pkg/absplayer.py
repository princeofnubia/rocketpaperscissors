from abc import ABCMeta, abstractmethod

class Player(metaclass = ABCMeta):
    

    @abstractmethod
    def getChoice(self, choices):
        pass

    @abstractmethod
    def getName(self):
        pass
    
    @abstractmethod
    def getScore(self):
        pass
    
    @abstractmethod
    def setScore(self, score):
        pass