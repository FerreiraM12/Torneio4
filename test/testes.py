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

    def test_projeto_3(self):
        m = [[5, 2, 4, 1, 6, 3, 8, 9, 7],
             [7, 9, 1, 8, 5, 4, 2, 6, 3],
             [6, 8, 3, 7, None, None, 1, 5, 4],
             [4, 1, 2, 9, None, None, 3, 8, 5],
             [8, 5, 7, 3, None, None, 9, 2, 6],
             [3, 6, 9, 5, 8, 2, 7, 4, 1],
             [9, 7, None, None, 3, 5, 4, 1, 8],
             [2, 4, None, None, 1, 7, 5, 3, 9],
             [1, 3, 5, 4, 9, 8, 6, 7, 2]]
        v = ([4, 2, 3, 3, 4, 3, 2, 1, 3], [3, 5, 3, 3, 1, 2, 3, 3, 2], [4, 2, 3, 2, 2, 3, 1, 4, 4],
             [2, 4, 3, 3, 2, 5, 2, 1, 4])
        self.assertEqual(projeto(m, *v), [[5, 2, 4, 1, 6, 3, 8, 9, 7],
                                          [7, 9, 1, 8, 5, 4, 2, 6, 3],
                                          [6, 8, 3, 7, 2, 9, 1, 5, 4],
                                          [4, 1, 2, 9, 7, 6, 3, 8, 5],
                                          [8, 5, 7, 3, 4, 1, 9, 2, 6],
                                          [3, 6, 9, 5, 8, 2, 7, 4, 1],
                                          [9, 7, 6, 2, 3, 5, 4, 1, 8],
                                          [2, 4, 8, 6, 1, 7, 5, 3, 9],
                                          [1, 3, 5, 4, 9, 8, 6, 7, 2]])


if __name__ == '__main__':
    unittest.main()
