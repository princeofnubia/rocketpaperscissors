from .absrpsdecorator import AbsRPSDecorator
class LizardSpock(AbsRPSDecorator):
    _ROCK = 1
    _PAPER = 2
    _SCISSORS = 3
    _LIZARD = 4
    _SPOCK = 5
    _TIE = -1
    _choices: {_ROCK: 'Rock', _PAPER: 'Paper', _SCISSORS: 'SCISSORS', _LIZARD: 'Lizard', _SPOCK: 'Spock'}
    _game_rules = {
        _ROCK: {_ROCK: _TIE, _SCISSORS: _ROCK, _PAPER: _PAPER, _LIZARD:_ROCK, _SPOCK: _SPOCK},
        _SCISSORS: {_ROCK: _ROCK, _SCISSORS: _TIE, _PAPER:_SCISSORS, _LIZARD:_SCISSORS, _SPOCK: _SPOCK},
        _PAPER: {_ROCK: _PAPER, _SCISSORS: _SCISSORS, _PAPER: _TIE, _LIZARD:_LIZARD, _SPOCK: _PAPER},
        _LIZARD: {_ROCK: _ROCK, _SCISSORS: _SCISSORS, _PAPER:_LIZARD, _LIZARD:_TIE, _SPOCK: _LIZARD},
        _SPOCK: {_ROCK: _SPOCK, _PAPER: _PAPER, _SCISSORS: _SPOCK, _LIZARD:_LIZARD, _SPOCK: _TIE}
    }
    def __init__(self,decorated_rps):
        AbsRPSDecorator.__init__(self,decorated_rps)

    
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