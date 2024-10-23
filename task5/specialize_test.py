import unittest

from task5.specialize import specialize


def my_sum(x, y, z):
    return x + y + z

class SpecializeTest(unittest.TestCase):
    def test_pos_args(self):
        specialized = specialize(my_sum, 1)
        self.assertEqual(specialized(2, 3), 6)
        specialized = specialize(my_sum, 1, 2)
        self.assertEqual(specialized(3), 6)
        specialized = specialize(my_sum, 1, 2, 3)
        self.assertEqual(specialized(), 6)


    def test_kw_args(self):
        specialized = specialize(my_sum, z = 1)
        self.assertEqual(specialized(2, 3), 6)
        specialized = specialize(my_sum, y = 1, z = 2)
        self.assertEqual(specialized(3), 6)
        specialized = specialize(my_sum, x = 1, y = 2, z = 3)
        self.assertEqual(specialized(), 6)


    def test_args(self):
        specialized = specialize(my_sum, 1, z = 3)
        self.assertEqual(specialized(2), 6)
        self.assertEqual(specialized(y = 2), 6)


if __name__ == '__main__':
    unittest.main()
