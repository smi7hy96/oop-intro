import unittest
from dog_class import Dog


class DogTest(unittest.TestCase):
    def setUp(self):
        self.dog = Dog('Scooby', 'Great Dane', 'BIG')

    def test_bark(self):
        self.assertEqual(self.dog.bark(), f'{self.dog.size} bark')

    def test_eat(self):
        self.assertEqual(self.dog.eat('Scooby Snax'), 'oooh, scooby snax')

    def test_sleep(self):
        self.assertEqual((self.dog.sleep()), '*snore*')

    def test_fetch(self):
        self.assertEqual(self.dog.fetch('ball'), 'CHAAAASE')
        self.assertEqual(self.dog.fetch('stick'), 'GET THA STICK')
        self.assertEqual(self.dog.fetch('leaf'), "*yawn* i'll sit back down")

if __name__ == '__main__':
    unittest.main()
