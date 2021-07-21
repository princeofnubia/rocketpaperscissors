from .util import clear
from time import sleep
from .computer import Computer
from .human import Human
from .rockpaperscissors import RockPaperScissors
from .lizardspock import LizardSpock

class Engine:


    # Game Context
    _COMPUTER_VERSUS_HUMAN: int = 1
    _COMPUTER_VERSUS_COMPUTER: int = 2
    _OPPONENT_OPTION = {_COMPUTER_VERSUS_HUMAN: "Computer Vs Human", _COMPUTER_VERSUS_COMPUTER: "Computer Vs Computer"}
    _game_context = None

    # End Game Options
    _REPLAY: int = 1
    _MENU: int = 2
    _STAT: int = 3
    _EXIT: int = 4
    _END_GAME_OPTION = {_REPLAY: 'Replay', _MENU: 'Menu', _STAT: 'Stat', _EXIT: 'Exit'}
    
    #Game Variant
    _ROCKPAPERSCISSORS = 1
    _LIZARDSPOCK = 2
    _game_variant = None
    _GAME_VARIANT = {_ROCKPAPERSCISSORS: 'Rock Paper Scissors', _LIZARDSPOCK: 'Rock Paper Scissors Lizard Spock'}


    def start(self):
        clear()
        self._game_header("CHOOSE YOUR OPPONENT")
        self._game_context = self._option_prompter(self._OPPONENT_OPTION)
        self._get_game_variants()
        if self._game_context == self._COMPUTER_VERSUS_HUMAN:
            clear()
            self._game_header("Game Profile")
            self._player_name = input('Provide your name: ')
            self._human_player = Human(name=self._player_name)
            self._computer = Computer()
           
            return self._start_game_computer_vs_human()
        self._computer_1 = Computer(name="Computer1")
        self._computer_2 = Computer(name="Computer2")
        return self._start_game_computer_vs_computer()

    def _start_game_computer_vs_human(self):
        clear()
        print(self._game_variant)
        self._game_header("ENTER YOUR MOVE {}".format(self._player_name))
        game = RockPaperScissors(player = self._human_player, opponent= self._computer)
        if (self._game_variant == LizardSpock):
            print(self._game_variant)
            game = LizardSpock(game)
        self.game_loop(game)

    def _start_game_computer_vs_computer(self):
            computer1 = self._computer_1
            computer2 = self._computer_2
            clear()
            self._game_header("{} Vs {}".format(computer1, computer2))
            print('{} making move..'.format(computer1))
            sleep(1)
            print('{} making move..'.format(computer2))
            sleep(1)
            clear()
            game = RockPaperScissors(player= computer1, opponent=computer2)
            if (self._game_variant == LizardSpock):
                game = LizardSpock(game)
            self.game_loop(game)
    def _replay_game(self):
        if self._game_context == self._COMPUTER_VERSUS_HUMAN:
            return self._start_game_computer_vs_human()
        return self._start_game_computer_vs_computer()

    def _option_prompter(self, args):
        try:
            options_string = ""
            for option in args:
                options_string += "{} {} \n".format(option, args[option])
            options_string += "Enter your option: "
            option = int(input(options_string))
            return option
        except ValueError:
            self._option_prompter(args)
                

    def announce_winner(self):
        self._show_stat()
        if self._stat['status'] == "tie":
            print("TIE GAME! What a competition! {}".format(self._stat['tie_choice']))
            sleep(2)
            return
        winner_selection = self._stat['winner_selection']
        winner = self._stat['winner']
        loser = self._stat['loser']
        loser_selection = self._stat['loser_selection']
        if(self._game_context == self._COMPUTER_VERSUS_COMPUTER):
            print("{} WIN!".format(winner))
        else:
            if(isinstance(self._stat['winner'], Human)):
                print("{}(You) WIN!".format(self._stat['winner'] ))
            else:
                print("{}(You) lose".format(self._stat['loser'],))
        print("{} picked {}, {} picked {}".format(winner, winner_selection, loser, loser_selection))
        sleep(2)

    
    def _get_game_variants(self):
        clear()
        self._game_header("GAME OPTIONS")
        print("Which game do you want to play? ")
        options = self._GAME_VARIANT
        playchoice = self._option_prompter(options)
        if playchoice == self._ROCKPAPERSCISSORS:
            self._game_variant = RockPaperScissors
            return
        elif playchoice == self._LIZARDSPOCK:
            self._game_variant = LizardSpock
            return
        else:
            return self._get_game_variants()
    
    def game_loop(self, game):
        while(game.play()):
            self._stat = game.game_stat()
            self.announce_winner()
            sleep(1)
            clear()
            self._game_header('GAME OVER')
            choice = self._option_prompter(self._END_GAME_OPTION)
            if(choice == self._EXIT):
                return self._game_end()
            elif(choice == self._REPLAY):
                return self._replay_game()
            elif(choice == self._STAT):
                self._show_stat()
                key = input("Press any Key to Continue")
                if(key):
                    return self.start()
            elif(choice == self._MENU):
                return self.start()
            else:
                print("Wrong input enter")
    
    def _show_stat(self):
        clear()
        player = self._stat['player']
        opponent = self._stat['opponent']
        self._game_header("SCORE STAT {}(You) {}:{} {}".format(player.getName(), player.getScore(),  opponent.getScore(), opponent.getName()))

    def _game_header(self, game_state):
        print("--------------------------------------")
        print("\tGAMBA GAME STUDIO")
        print("--------------------------------------")
        print("{}".format(game_state))
        print("--------------------------------------")
    
    def _game_end(self):
        self = None
        print("Bye!")
        exit()