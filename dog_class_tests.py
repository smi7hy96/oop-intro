from unittest import TestCase
from dog_class import Dog


class DogTest(TestCase):
    def setUp(self):
        self.dog = Dog('Scooby')

    def test_bark(self):

        self.assertEqual(self.dog.bark(), f'{self.dog.name}, bark')
