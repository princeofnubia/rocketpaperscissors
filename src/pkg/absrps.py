from abc import ABCMeta, abstractmethod

class AbsRPS(metaclass = ABCMeta):
    """Rock Paper Scissors Interface implemented by RockPaperScissor concrete interface as well as its Decorators"""

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