import unittest

from task9.lru import LRUCache


class LruTest(unittest.TestCase):
    def test_init(self):
        c = LRUCache()
        self.assertEqual(c.capacity, 16)
        c = LRUCache(5)
        self.assertEqual(c.capacity, 5)

    def test_put(self):
        c = LRUCache(5)
        c.put(1, 'a')
        c.put(2, 'b')
        c.put(3, 'c')
        c.put(4, 'd')
        c.put(5, 'e')

        self.assertEqual(list(c._lru), [1, 2, 3, 4, 5])

        c.put(1, 'a')
        self.assertEqual(list(c._lru), [2, 3, 4, 5, 1])

        c.put(6, 'f')
        self.assertEqual(list(c._lru), [3, 4, 5, 1, 6])


    def test_get(self):
        c = LRUCache(5)
        c.put(1, 'a')
        c.put(2, 'b')
        c.put(3, 'c')
        c.put(4, 'd')
        c.put(5, 'e')

        self.assertEqual(c.get(1), 'a')
        self.assertEqual(list(c._lru), [2, 3, 4, 5, 1])

        self.assertEqual(c.get(3), 'c')
        self.assertEqual(list(c._lru), [2, 4, 5, 1, 3])

        self.assertEqual(c.get(6), None)


if __name__ == '__main__':
    unittest.main()
