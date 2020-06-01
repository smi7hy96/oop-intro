import unittest
from cat_class import Cat


class CatTest(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Aggressive', 'Ginger', 'Mufasa', False, 'Tabby')

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


if __name__ == '__main__':
    unittest.main()
