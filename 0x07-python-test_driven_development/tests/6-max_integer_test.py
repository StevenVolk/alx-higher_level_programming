#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([4, 3, 2]), 4)
        self.assertEqual(max_integer([2, 4, 1]), 4)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([2, 3, -1, 5, 9]), 9)
        self.assertEqual(max_integer([-4, -1, -6, -8]), -1)
        self.assertEqual(max_integer([]), "\n")

if __name__ == '__main__':
    unittest.main()
