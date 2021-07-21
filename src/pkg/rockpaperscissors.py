from .absrps import AbsRPS
from time import sleep

class RockPaperScissors(AbsRPS):
    _ROCK = 1
    _PAPER = 2
    _SCISSORS = 3
    _PAPER_COVERS_ROCK = "paper covers rock"
    _ROCK_SMASHES_SCISSORS = "rock smashes scissors"
    _SCISSORS_CUT_PAPER = "scissors cut paper"
    _choices = {_ROCK: 'Rock', _PAPER: 'Paper', _SCISSORS: 'Scissors'}
    _TIE= -1
    _ROCK_VS_SCISSORS = _ROCK
    _ROCK_VS_PAPER = _PAPER
    _game_rules = {
        _ROCK: {_ROCK: _TIE, _SCISSORS: _ROCK, _PAPER: _PAPER},
        _SCISSORS: {_ROCK: _ROCK, _SCISSORS: _TIE, _PAPER:_SCISSORS},
        _PAPER: {_ROCK: _PAPER, _SCISSORS: _SCISSORS, _PAPER: _TIE}
    }
    def __init__(self, player, opponent):
        self._player = player
        self._opponent = opponent
        self._score = {player: 0, opponent: 0}
        self._game_stat = {}
    
    def play(self):
        try:
            player = self._player
            opponent = self._opponent
            self._player_choice = self._player.getChoice(self._choices)
            self._opponent_choice = self._opponent.getChoice(self._choices)
            winner_choice = self._game_rules[self._player_choice][self._opponent_choice]
            if (self._player_choice == winner_choice):
                winner_selection = self._choices[self._player_choice]
                player.setScore(1)
                loser_selection = self._choices[self._opponent_choice]
                self._update_game_stat(player = player, opponent = opponent,winner=player, loser=opponent, winner_selection=winner_selection, loser_selection = loser_selection)
            elif (self._opponent_choice == winner_choice):
                winner_selection = self._choices[self._opponent_choice]
                loser_selection = self._choices[self._player_choice]
                opponent.setScore(1)
                self._update_game_stat(player = player, opponent = opponent,winner=opponent, loser=player, winner_selection=winner_selection, loser_selection = loser_selection)
            else:
                winner_selection = self._choices[self._player_choice]
                loser_selection = self._choices[self._opponent_choice]
                self._update_game_stat(player = player, opponent = opponent,winner=opponent, status='tie', tie_choice=winner_selection)
            return True
        except:
            print('Enter a proper input')
            return self.play()


    def restart(self):
        self.play()
    
    def _update_game_stat(self, status=None, **kwargs):
        self._game_stat = {**kwargs, 'status': status}

    def game_stat(self):
        return self._game_stat

    
    def instruction(self):
        print()
        print("Instructions for Rock-Paper-Scissors : ")
        print()
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
