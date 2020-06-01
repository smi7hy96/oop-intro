import unittest
from cat_class import Cat


class CatTest(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Aggressive', 'Ginger', 'Mufasa', True, 'Tabby', 5)

    def test_attack(self):
        self.assertEqual(self.cat.attack(), 'HISS')
        self.cat.sleepy = True
        self.assertEqual(self.cat.attack(), 'HISS')
        self.cat.behaviour = 'Not Aggressive'
        self.assertEqual(self.cat.attack(), '*snore*')

    def test_chase(self):
        self.assertEqual(self.cat.chase('mouse'), 'Come here Jerry')
        self.assertEqual(self.cat.chase('rabbit'), 'Not interested')

    def test_play(self):
        self.assertEqual(self.cat.play('box'), 'If I fits....')
        self.assertEqual(self.cat.play('new toy'), "Erm no. Where's the box?")

    def test_eat(self):
        self.assertEqual(self.cat.eat('tuna'), 'Really? Im trying to sleep here')
        self.cat.sleepy = False
        self.assertEqual(self.cat.eat('tuna'), f'OOOH, Tuna')


if __name__ == '__main__':
    unittest.main()
