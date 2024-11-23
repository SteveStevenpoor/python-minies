import unittest

from task11.my_itertools import cycle, chain


def take(generator, n: int) -> list:
    it = iter(generator)
    out = list()
    for i in range(n):
        out.append(next(it))
    return out


class ItertoolsTest(unittest.TestCase):
    def test_cycle(self):
        self.assertEqual([1, 2, 3, 1, 2, 3, 1, 2, 3, 1], take(cycle([1, 2, 3]), 10))

    def test_chain(self):
        self.assertEqual([1, 2, 3, 'a', 'b', 'c'], take(chain([1, 2, 3], ['a', 'b', 'c']), 6))


if __name__ == '__main__':
    unittest.main()
