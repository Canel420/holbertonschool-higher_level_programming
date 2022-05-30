#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases class for 6-max_integer module
    """
    def test_max_integer(self):
        """
        Test case for a list of
        positive integers.
        """
        t_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(t_list), 4, "Should be 4")

    def test_max_neg_integer(self):
        """
        Test case for a list of
        negative integers.
        """
        t_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(t_list), -1, "Should be -1")

    def test_max_empty(self):
        """
        Test case for an empty
        list.
        """
        t_list = []
        self.assertEqual(max_integer(t_list), None, "Should be None")

    def test_max_str(self):
        """
        Test case for a list of
        strings.
        """
        t_list = ["a", "b", "c"]
        self.assertEqual(max_integer(t_list), "c", "Should be c")

    def test_max_float(self):
        """
        Test case for a list of
        floats.
        """
        t_list = [1.2, 2.3, 3.4]
        self.assertEqual(max_integer(t_list), 3.4, "Should be 3.4")

    def test_max_neg_float(self):
        """
        Test case for a list of
        negative floats.
        """
        t_list = [-1.2, -2.3, -3.4]
        self.assertEqual(max_integer(t_list), -1.2, "Should be -1.2")

    def test_max_equal(self):
        """
        Test case for a list of
        equal elements.
        """
        t_list = [3, 3, 3, 3]
        self.assertEqual(max_integer(t_list), 3, "Should be 3")

    def test_max_lists(self):
        """
        Test case for a list of
        lists.
        """
        t_list = [[11, 2], [7, 4], [5, 6]]
        self.assertEqual(max_integer(t_list), [11, 2], "Should be [11, 2]")

    def test_max_tuple(self):
        """
        Test case for a list of
        tuples.
        """
        t_list = [(3, 4), (-2, 11), (5, 7)]
        self.assertEqual(max_integer(t_list), (5, 7), "Should be (5, 7)")

    def test_max_mix(self):
        """
        Test case for a list of
        string and integer elements.
        """
        t_list = [4, 2, "420", 3]
        with self.assertRaises(TypeError):
            max_integer(t_list)

    def test_max_none(self):
        """
        Test case for a list with None
        as argument
        """
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
