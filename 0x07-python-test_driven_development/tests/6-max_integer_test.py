#!/usr/bin/python3
"""module for test max integer in list"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """define my class"""

    def test_positive(self):
    """no duplicates"""
    list = [1, 2, 3, 0, 5]
    self.assertEqual(max_integer(list), 5)

    def duplicate(self):
    """test a list with duplicate non-max values"""
    list = [2, -7, 3, 2, -7]
    self.assertEqual(max_integer(list), 3)

    def duplicate_max(self):
    list = [2, -7, 3, 3, -7]
    self.assertEqual(max_integer(list), 3)

    def test_negative_result(self):
    """negative numbers largest number"""
    list = [-1, -2, 0, -6, -3]
    self.assertEqual(max_integer(list), -1)

    def test_negative(self):
    """test last element max"""
    list = [-1, -3, -5, -4, -6]
    self.assertEqual(max_integer(list), -1)

    def test_first(self):
    list = [10, 5, -6, 3, 2]
    self.assertEqual(max_integer(list), 10)

    def test_all_0(self):
    list = [0, 0, 0, 0, 0]
    self.assertEqual(max_integer(list), 0)

    def test_empty(self):
    list = []
    self.assertEqual(max_integer(list), None)

    def test_all_1(self):
    list = [1, 1, 1, 1, 1]
    self.assertEqual(max_integer(list), 1)

    def only_element(self):
    list = [1]
    self.assertEqual(max_integer(list), 1)

if __name__ == '__main__':
    unittest.main()
