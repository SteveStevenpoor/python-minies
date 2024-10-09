import unittest

from task3.stomat import stomat


class StomatTest(unittest.TestCase):
    def test_ordinary(self):
        s = '1 2 | 3 4'
        mat = [[1.0, 2.0], [3.0, 4.0]]
        self.assertEqual(stomat(s), mat)
        s = '1 2 3 | 3 4 5'
        mat = [[1.0, 2.0, 3.0], [3.0, 4.0, 5.0]]
        self.assertEqual(stomat(s), mat)
        s = '1.1 2.2 | 3.3 4.4'
        mat = [[1.1, 2.2], [3.3, 4.4]]
        self.assertEqual(stomat(s), mat)


    def test_weird(self):
        s = 'inf inf | inf inf'
        mat = [[float('inf'), float('inf')], [float('inf'), float('inf')]]
        self.assertEqual(stomat(s), mat)


if __name__ == '__main__':
    unittest.main()
