#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for rectangle.py module
"""

import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class rectangleTest(unittest.TestCase):
    """ Tests for Rectangle class """
    def test_value_existence(self):
        """ Test for Rectangle arguments """
        # This resets the Base class variable
        Base._Base__nb_objects = 0

        R1 = Rectangle(1, 1)
        self.assertEqual((R1.width, R1.height, R1.x, R1.y, R1.id),
                         (1, 1, 0, 0, 1))
        R2 = Rectangle(1, 1, 1)
        self.assertEqual((R2.width, R2.height, R2.x, R2.y, R2.id),
                         (1, 1, 1, 0, 2))
        R3 = Rectangle(1, 1, 1, 1)
        self.assertEqual((R3.width, R3.height, R3.x, R3.y, R3.id),
                         (1, 1, 1, 1, 3))
        R4 = Rectangle(1, 1, 1, 1, 42)
        self.assertEqual((R4.width, R4.height, R4.x, R4.y, R4.id),
                         (1, 1, 1, 1, 42))

    def test_value_error(self):
        """ Test for wrong args passsed """
        with self.assertRaises(TypeError):
            R = Rectangle()
        with self.assertRaises(TypeError):
            R = Rectangle(1, )
        with self.assertRaises(TypeError):
            R = Rectangle("1", "1")
        with self.assertRaises(ValueError):
            R = Rectangle(-1, -1)
        with self.assertRaises(TypeError):
            R = Rectangle(1, 1, "1", "1")
        with self.assertRaises(ValueError):
            R = Rectangle(1, 1, -1, -1)
        with self.assertRaises(TypeError):
            R = Rectangle(1, 1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            R = Rectangle(1.2, 1.2, 1.2, 1.2)
        with self.assertRaises(TypeError):
            R = Rectangle([1, 2], 3)
        with self.assertRaises(TypeError):
            R = Rectangle(1, 1, {'one': 1}, 1)
        with self.assertRaises(TypeError):
            R = Rectangle(True, 1)
        with self.assertRaises(TypeError):
            R = Rectangle(1, (1, 2))
        with self.assertRaises(TypeError):
            R = Rectangle(float('inf'), 1)

    def test_area(self):
        """ Tests for area """
        R = Rectangle(1, 2)
        self.assertEqual(R.area(), 2)

        with self.assertRaises(TypeError):
            a = R.area(14)

    def test_display(self):
        """
        Redirect print statement to
        a file for testing.
        """
        f = io.StringIO()
        R = Rectangle(1, 2)
        with redirect_stdout(f):
            R.display()
        self.assertEqual(f.getvalue(), (('#' * 1 + '\n') * 2))

        f = io.StringIO()
        R = Rectangle(1, 2, 1, 2)
        with redirect_stdout(f):
            R.display()
        self.assertEqual(f.getvalue(), (('\n' * 2) +
                                        (' ' * 1 + '#' * 1 + '\n') * 2))

    def test_str(self):
        """ Test for string output """
        R = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(R))

    def test_update_args(self):
        """ Test for ordered argument update """
        R = Rectangle(1, 1, 1, 1, 1)
        R.update(2)
        self.assertEqual(2, R.id)
        R.update(5, 4)
        self.assertEqual(4, R.width)
        R.update(3, 6, 7)
        self.assertEqual(7, R.height)
        R.update(2, 6, 8, 3)
        self.assertEqual(3, R.x)
        R.update(5, 3, 7, 8, 9)
        self.assertEqual(9, R.y)

    def test_update_kwargs(self):
        """ Test for unordered arguments update """
        R = Rectangle(1, 1, 1, 1, 1)
        R.update(id=2)
        self.assertEqual(2, R.id)
        R.update(x=3)
        self.assertEqual(3, R.x)
        R.update(width=5)
        self.assertEqual(5, R.width)
        R.update(y=7)
        self.assertEqual(7, R.y)
        R.update(height=9)
        self.assertEqual(9, R.height)

    def test_mix_args_kwargs(self):
        """ Testing for args and kwargs given """
        R = Rectangle(1, 1, 1, 1, 1)
        R.update(2, 2, 2, id=3, x=3, y=3)
        self.assertEqual(str(R), "[Rectangle] (2) 1/1 - 2/2")

    def test_dict_repr(self):
        """ Test for dictionary representation """
        Base._Base__nb_objects = 0

        R1 = Rectangle(1, 1, 1, 1, 1)
        D1 = R1.to_dictionary()
        self.assertEqual(D1, {'id': 1, 'width': 1,
                              'height': 1, 'x': 1, 'y': 1})
        R2 = Rectangle(2, 2)
        D2 = R2.to_dictionary()
        self.assertEqual(D2, {'id': 1, 'width': 2,
                              'height': 2, 'x': 0, 'y': 0})
        self.assertEqual(type(D1), dict)
