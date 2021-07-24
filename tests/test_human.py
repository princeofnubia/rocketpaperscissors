from src.pkg.human import Human
from src.pkg.absplayer import Player
from unittest import TestCase
from unittest.mock import MagicMock
from .test_stud_base import get_display_output, set_keyboard_input
from .util import clear
import random
import pytest

class HumanTest(TestCase):

    
    def test_choice_must_be_correct(self):
        set_keyboard_input(['1'])
        inputs = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        human = Human()
        user_input = human.getChoice(inputs)
        get_display_output()
        assert 1 == user_input
        clear()

    def test_should_provide_default_name(self):
        human = Human()
        self.assertTrue(human.getName() == 'You')
        self.assertTrue(human.__str__() == 'You')

    def test_should_be_instance_of_human(self):
        human = Human()
        self.assertTrue(isinstance(human, Human))
    
    def test_should_be_provide_given_name(self):
        human = Human('Chan')
        self.assertTrue(human.getName() == 'Chan')

    def test_should_produce_exact_score(self):
        player = Human('Ade')
        self.assertTrue(player.getScore() == 0)
        self.assertTrue(player.setScore(1) == None)
        self.assertTrue(player.getScore() == 1)

    def test_should_produce_increment_score(self):
        player = Human('Seun')
        self.assertTrue(player.getScore() == 0)
        self.assertTrue(player.setScore(4) == None)
        self.assertTrue(player.getScore() == 4)
        self.assertTrue(player.setScore(4) == None)
        self.assertTrue(player.getScore() == 8) 

    def test_should_be_player(self):
        player = Human('Seun')
        self.assertTrue(isinstance(player, Player))