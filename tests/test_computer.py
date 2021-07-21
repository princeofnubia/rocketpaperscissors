from src.pkg.computer import Computer
from unittest import TestCase

class ComputerTest(TestCase):
    
    def test_choice_must_be_in_range(self):
        computer = Computer()
        choices = ["a", "b", "c"]
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