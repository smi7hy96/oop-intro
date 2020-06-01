import unittest
from animal_class import Animal


class AnimalTest(unittest.TestCase):
    def setUp(self):
        self.animal = Animal('Ginger', 'Mufasa', 'Tabby', False)

    def test_eat(self):
        self.assertEqual(self.animal.eat('tuna'), 'ugh, Tuna')

    def test_sleep(self):
        self.assertEqual(self.animal.sleep(), 'I wanna play!')
        self.animal.sleepy = True
        self.assertEqual((self.animal.sleep()), '*snore*')


if __name__ == '__main__':
    unittest.main()
