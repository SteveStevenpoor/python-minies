import unittest

from task1.count_weight import count_weight


class CountWeightTest(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(count_weight(7), 3)
        self.assertEqual(count_weight(2935), 9)
        self.assertEqual(count_weight(128753924), 11)
        self.assertEqual(count_weight(9375), 8)
        self.assertEqual(count_weight(932756230598), 19)


    def test_negative(self):
        self.assertEqual(count_weight(-123), 3)
        self.assertEqual(count_weight(-9273561), 16)
        self.assertEqual(count_weight(-1), 1)
        self.assertEqual(count_weight(-2), 1)
        self.assertEqual(count_weight(-1111), 7)


if __name__ == "__main__":
    unittest.main()


