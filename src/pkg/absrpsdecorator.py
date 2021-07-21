from abc import ABCMeta, abstractmethod
from .absrps import AbsRPS
class AbsRPSDecorator(AbsRPS):
    """Abstract Decorator implementing The Abstract RockPaperLizard Interface"""
    _choices: dict = {}
    _game_rules: dict = {}
    
    def __init__(self,decorated_rps):
        self.decorated_rps = decorated_rps
    
    def _update_game_stat(self, status=None, **kwargs):
        return self.decorated_rps._update_game_stat(status=None, **kwargs)

    def play(self):
        return self.decorated_rps.play()

    def restart(self):
        return self.decorated_rps.restart()

    def game_stat(self):
        return self.decorated_rps.game_stat()
    
    def instruction(self):
        return self.decorated_rps.instruction()