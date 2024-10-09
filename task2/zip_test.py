import unittest

from task2.zip import my_zip


class MyZipTest(unittest.TestCase):
    def test_primitive(self):
        a = [1, 2, 3]
        b = ['a', 'b']
        self.assertEqual(list(zip(a, b)), my_zip(a, b))
        a = [1, 2, 3]
        b = [1, 2, 3, 4, 5]
        self.assertEqual(list(zip(a, b)), my_zip(a, b))
        a = ['a', 'b', 'c']
        b = [1.1, 2.2]
        self.assertEqual(list(zip(a, b)), my_zip(a, b))
        a = ['a', 'b', 'c']
        b = ['a', 'b', 'c']
        self.assertEqual(list(zip(a, b)), my_zip(a, b))


    def test_complex(self):
        a = [1, 2, 3]
        b = [['a', 'b'], 'c']
        self.assertEqual(list(zip(a, b)), my_zip(a, b))
        a = [1, 2, 3]
        b = [1, 'aboba', 3.1, ('a', 'b'), 5]
        self.assertEqual(list(zip(a, b)), my_zip(a, b))
        a = ['a', 'b', 'c']
        b = [[1.1, 2.2]]
        self.assertEqual(list(zip(a, b)), my_zip(a, b))
        a = ['a', 'b', 'c']
        b = ['a', -7, 2]
        self.assertEqual(list(zip(a, b)), my_zip(a, b))


if __name__ == "__main__":
    unittest.main()