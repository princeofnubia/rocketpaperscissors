from src.pkg.human import Human
from unittest import TestCase
from unittest.mock import MagicMock
from .test_stud_base import get_display_output, set_keyboard_input
from .util import clear
import random
import pytest

class HumanTest(TestCase):

    def choice_from_input(self):
        inputs = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        selection = random.randint(1, len(inputs))
        return selection
    
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