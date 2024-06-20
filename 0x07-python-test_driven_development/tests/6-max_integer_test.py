#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test case for max integer"""

    def test_regular(self):
        """test basic usage"""
        li = [6, 4, 3, 2, 88]
        result = max_integer(li)
        self.assertEqual(result, 88)

    def test_type_int(self):
        """test type of arg int"""
        self.assertRaises(TypeError, max_integer, 8)

    def test_list_not_int(self):
        """test mixed list"""
        l = ['damn', 9, 3]
        self.assertRaises(TypeError, max_integer, l)

    def test_negative(self):
        """lets negative numbers"""
        l = [-3, -5, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_float(self):
        """test float"""
        l = [4.5, 2, 4]
        result = max_integer(l)
        self.assertEqual(result, 4.5)

    def test_empty(self):
        """test empty list"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_unique(self):
        """test one item in list"""
        l = [9]
        result = max_integer(l)
        self.assertEqual(result, 9)

    def test_duplicate(self):
        """test duplicate"""
        l = [3, 3, 3, 3]
        result = max_integer(l)
        self.assertEqual(result, 3)

    def test_none(self):
        """test none argument"""
        self.assertRaises(TypeError, max_integer, None)
