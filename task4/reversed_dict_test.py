import unittest

from task4.reversed_dict import give_reversed_dict


class ReverseDictTest(unittest.TestCase):
    def test_hashable(self):
        orig_dict = {}
        rev_dict = {}
        self.assertEqual(give_reversed_dict(orig_dict), rev_dict)
        orig_dict = {'Ivanov': 97832, 'Petrov': 55521, 'Kuznecov': 97832}
        rev_dict = {97832: ('Ivanov', 'Kuznecov'), 55521: 'Petrov'}
        self.assertEqual(give_reversed_dict(orig_dict), rev_dict)
        orig_dict = {'Ivanov': 97832, 'Petrov': 55521, 'Kuznecov': 97832, 'Pivov': 97832}
        rev_dict = {97832: ('Ivanov', 'Kuznecov', 'Pivov'), 55521: 'Petrov'}
        self.assertEqual(give_reversed_dict(orig_dict), rev_dict)
        orig_dict = {'Ivanov': 97832, 'Petrov': 55521, 'Kuznecov': 11111}
        rev_dict = {97832: 'Ivanov', 55521: 'Petrov', 11111: 'Kuznecov'}
        self.assertEqual(give_reversed_dict(orig_dict), rev_dict)


    def test_unhashable(self):
        orig_dict = {'Ivanov': 97832, 'Petrov': 55521, 'Kuznecov': [97832]}
        self.assertRaises(TypeError, give_reversed_dict, orig_dict)
        orig_dict = {'Ivanov': {1: 2}}
        self.assertRaises(TypeError, give_reversed_dict, orig_dict)


if __name__ == '__main__':
    unittest.main()
