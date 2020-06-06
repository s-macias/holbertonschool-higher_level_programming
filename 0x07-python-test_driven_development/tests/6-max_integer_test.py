#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class to perform unittests
    """


    def test_empty_list(self):
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_one_item(self):
        test_list = [1]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_positive_integers(self):
        test_list = [1, 3, 50, 90, 100]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_positive_negative(self):
        test_list = [1, 3, 5, -1, 9, -5]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_floats(self):
        test_list = [1.5, 3.3, 5.3]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_negative(self):
        test_list = [-1, -3, -5]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_zero_positive(self):
        test_list = [1, 3, 5, 0, 6]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_zero_negative(self):
        test_list = [-1, -3, -5, 0]
        self.assertEqual(max_integer(test_list), max(test_list))
