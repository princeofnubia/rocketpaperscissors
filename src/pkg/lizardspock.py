from .absrpsdecorator import AbsRPSDecorator
class LizardSpock(AbsRPSDecorator):
    """Lizard Spock Decorator Class to extend Rock Paper Scissor Game"""
    """Just provide the game rules and choices and the Extending class will handle the remaining logic"""
    """I had to rewrite the constants for readability """
    _ROCK = 1
    _PAPER = 2
    _SCISSORS = 3
    _LIZARD = 4
    _SPOCK = 5
    _TIE = -1

    def __init__(self,decorated_rps):
        AbsRPSDecorator.__init__(self,decorated_rps)
        decorated_rps._choices = {self._ROCK: 'Rock', self._PAPER: 'Paper', self._SCISSORS: 'SCISSORS', self._LIZARD: 'Lizard', self._SPOCK: 'Spock'}
        decorated_rps._game_rules = {
        self._ROCK: {self._ROCK: self._TIE, self._SCISSORS: self._ROCK, self._PAPER: self._PAPER, self._LIZARD:self._ROCK, self._SPOCK: self._SPOCK},
        self._SCISSORS: {self._ROCK: self._ROCK, self._SCISSORS: self._TIE, self._PAPER:self._SCISSORS, self._LIZARD:self._SCISSORS, self._SPOCK: self._SPOCK},
        self._PAPER: {self._ROCK: self._PAPER, self._SCISSORS: self._SCISSORS, self._PAPER: self._TIE, self._LIZARD:self._LIZARD, self._SPOCK: self._PAPER},
        self._LIZARD: {self._ROCK: self._ROCK, self._SCISSORS: self._SCISSORS, self._PAPER:self._LIZARD, self._LIZARD:self._TIE, self._SPOCK: self._LIZARD},
        self._SPOCK: {self._ROCK: self._SPOCK, self._PAPER: self._PAPER, self._SCISSORS: self._SPOCK, self._LIZARD:self._LIZARD, self._SPOCK: self._TIE}
        }
    
    def _update_game_stat(self, status=None, **kwargs):
        return self.decorated_rps._update_game_stat(status=None, **kwargs)

    def play(self):
        return self.decorated_rps.play()

    def game_stat(self):
        return self.decorated_rps.game_stat()