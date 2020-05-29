import unittest
from cat_class import Cat


class CatTest(unittest.TestCase):
    def SetUp(self):
        self.cat = Cat('Aggressive', 'Ginger', 'Mufasa', False)

    def test_eat(self):
        self.assertEqual(self.cat.eat('tuna'), 'ugh, tuna')

    def test_sleep(self):
        self.assertEqual((self.cat.sleep()), '*snore*')

    def test_attack(self):
        self.assertEqual(self.cat.attack(), 'HISS')
        self.assertEqual(self.cat.attack(), '*snore*')

    def test_chase(self):
        self.assertEqual(self.cat.chase('mouse'), 'Come here Jerry')
        self.assertEqual(self.cat.chase('rabbit'), 'Not interested')

    def test_play(self):
        self.assertEqual(self.cat.play('box'), 'If I fits....')
        self.assertEqual(self.cat.play('new toy'), "Erm no. Where's the box?")


if __name__ == '__main__':
    unittest.main()
