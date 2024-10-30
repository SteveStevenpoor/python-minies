import unittest

from task6.flatten import flatten


class FlattenTest(unittest.TestCase):
    def test_no_depth(self):
        test_list = [1, 2, [3], [4, 5], [6, [7]], 8]
        target_list = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(flatten(test_list), target_list)

        test_list = [[1, [2, [3, [4, [5, [6, [7, [8]]]]]]]]]
        self.assertEqual(flatten(test_list), target_list)

        test_list = [1, 2, [3, 4, [5, 6]], 7, 8]
        self.assertEqual(flatten(test_list), target_list)

        test_list = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(flatten(test_list), target_list)

        test_list = [[1, 2], [3, 4], [5, 6, 7, [8]]]
        self.assertEqual(flatten(test_list), target_list)


    def test_with_depth(self):
        test_list = [1, 2, [3], [4, 5], [6, [7]], 8]
        target_list = [1, 2, 3, 4, 5, 6, [7], 8]
        self.assertEqual(flatten(test_list, 1), target_list)

        test_list = [[1, [2, [3, [4, [5, [6, [7, [8]]]]]]]]]
        target_list = [1, 2, 3, [4, [5, [6, [7, [8]]]]]]
        self.assertEqual(flatten(test_list, 3), target_list)

        test_list = [1, 2, [3, 4, [5, 6]], 7, 8]
        target_list = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(flatten(test_list, 10), target_list)

        test_list = [1, 2, 3, 4, 5, 6, 7, 8]
        target_list = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(flatten(test_list, 0), target_list)

        test_list = [[1, 2], [3, 4], [5, 6, 7, [8]]]
        target_list = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(flatten(test_list, 2), target_list)


if __name__ == '__main__':
    unittest.main()
