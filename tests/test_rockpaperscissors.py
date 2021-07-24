from src.pkg.rockpaperscissors import RockPaperScissors
from src.pkg.computer import Computer
from src.pkg.human import Human
from src.pkg.absplayer import Player
from .test_stud_base import get_display_output, set_keyboard_input
from .util import clear
from unittest import TestCase

class RockPaperScissorsTest(TestCase):
    
    def test_ensure_that_game_is_played_for_computer_vs_computer(self):
        computer_1 = Computer(name="computer1")
        computer_2 = Computer(name="computer2")
        game = RockPaperScissors(computer_1, computer_2)
        game_play = game.play()
        self.assertTrue(game_play == True)

    def test_ensure_that_stat_is_well_defined_for_computer_vs_computer(self):
        computer = Computer(name="Chang")
        computer_2 = Computer(name="computer2")
        game = RockPaperScissors(computer_2, computer)
        game.play()
        game_stat = game.game_stat()
        self.assertTrue(type(game_stat) is dict)


    def test_ensure_that_game_is_played_for_computer_vs_human(self):
        computer_1 = Computer(name="computer1")
        computer_2 = Computer(name="computer2")
        game = RockPaperScissors(computer_1, computer_2)
        game_play = game.play()
        self.assertTrue(game_play == True)

    def test_ensure_that_stat_is_well_defined_for_computer_vs_human(self):
        computer = Computer(name="Chang")
        computer_2 = Computer(name="computer2")
        game = RockPaperScissors(computer_2, computer)
        game.play()
        game_stat = game.game_stat()
        self.assertTrue(type(game_stat) is dict)

    def test_ensure_that_game_is_played_computer_vs_human(self):
        set_keyboard_input(['3'])
        computer_1 = Computer(name="computer1")
        human = Human(name="Lon")
        game = RockPaperScissors(computer_1, human)
        game_play = game.play()
        clear()
        self.assertTrue(game_play == True)

    def test_ensure_that_game_stat_is_well_defined_computer_vs_human(self):
        set_keyboard_input(['1'])
        computer_1 = Computer(name="computer1")
        human = Human(name="Chi")
        game = RockPaperScissors(computer_1, human)
        game.play()
        get_display_output()
        clear()
        game_stat = game.game_stat()
        self.assertTrue(type(game_stat) is dict)