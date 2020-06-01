import unittest
from animal_class import Animal


class AnimalTest(unittest.TestCase):
    def setUp(self):
        self.animal = Animal('Ginger', 'Mufasa', 'Tabby', False, 5)

    def test_eat(self):
        self.assertEqual(self.animal.eat('tuna'), 'OOOH, Tuna')

    def test_sleep(self):
        self.assertEqual(self.animal.sleep(), 'No! I wanna play!')
        self.animal.sleepy = True
        self.assertEqual((self.animal.sleep()), '*snore*')

    def test_happy_birthday(self):
        self.assertEqual(self.animal.happy_birthday(), "Happy Birthday Mufasa!! You are 6!")


if __name__ == '__main__':
    unittest.main()
