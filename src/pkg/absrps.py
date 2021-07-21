from abc import ABCMeta, abstractmethod

class AbsRPS(metaclass = ABCMeta):
    

    _choices: dict = {}
    _game_rules: dict = {}

    def _update_game_stat(self, status=None, **kwargs):
        pass

    def play(self):
        pass

    def restart(self):
        pass

    def game_stat(self):
        pass
    
    def instruction(self):
        pass