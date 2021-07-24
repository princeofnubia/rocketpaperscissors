from src.pkg.computer import Computer
from src.pkg.absplayer import Player
from unittest import TestCase

class ComputerTest(TestCase):
    
    def test_choice_must_be_in_range(self):
        computer = Computer()
        choices = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        choice = computer.getChoice(choices)
        self.assertTrue(choice <= len(choices))
        self.assertTrue(choice >= 1)

    def test_should_provide_default_name(self):
        computer = Computer()
        self.assertTrue(computer.getName() == 'Computer')

    def test_should_be_instance_of_computer(self):
        computer = Computer()
        self.assertTrue(isinstance(computer, Computer))
    
    def test_should_provide_expected_name(self):
        computer = Computer('Ade')
        self.assertTrue(computer.getName() == 'Ade')
        self.assertTrue(computer.__str__() == 'Ade')

    def test_should_produce_exact_score(self):
        computer = Computer('Ade')
        self.assertTrue(computer.getScore() == 0)
        self.assertTrue(computer.setScore(1) == None)
        self.assertTrue(computer.getScore() == 1)
        computer = Computer('Seun')

    def test_should_produce_increment_score(self):
        computer = Computer('Seun')
        self.assertTrue(computer.getScore() == 0)
        self.assertTrue(computer.setScore(4) == None)
        self.assertTrue(computer.getScore() == 4)
        self.assertTrue(computer.setScore(4) == None)
        self.assertTrue(computer.getScore() == 8) 

    def test_should_be_player(self):
        computer = Computer('Seun')
        self.assertTrue(isinstance(computer, Player))