import unittest

from src.projeto import projeto


class projetoTest(unittest.TestCase):

    def test_projeto_1(self):
        m = [[None, None, None, None],
             [None, 4, None, None],
             [None, None, None, None],
             [None, None, None, 3]]
        v = ([3, 2, 2, 1], [1, 3, 2, 2], [4, 2, 3, 1], [1, 2, 2, 2])
        self.assertEqual(projeto(m, *v), [[1, 2, 3, 4], [3, 4, 1, 2], [2, 3, 4, 1], [4, 1, 2, 3]])

    def test_projeto_2(self):
        m = [[None, None, 2],
             [None, 3, None],
             [None, None, None]]
        v = ([None, None, None], [None, None, None], [None, None, None], [None, None, None])
        self.assertEqual(projeto(m, *v), [[3, 1, 2], [2, 3, 1], [1, 2, 3]])


if __name__ == '__main__':
    unittest.main()

