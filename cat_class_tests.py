import unittest
from cat_class import Cat


class CatTest(unittest.TestCase):
    def SetUp(self):
        self.cat = Cat()


if __name__ == '__main__':
    unittest.main()
