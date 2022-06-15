#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
from models.square import Square


class squareTest(unittest.TestCase):
    """ Class for testing Square class """
    def test_value_existence(self):
        """ Test for normal args """
        Base._Base__nb_objects = 0

        S0 = Square(1, )
        self.assertEqual((S0.size, S0.x, S0.y, S0.id), (1, 0, 0, 1))
        S1 = Square(1, 2)
        self.assertEqual((S1.size, S1.x, S1.y, S1.id), (1, 2, 0, 2))
        S2 = Square(1, 2, 3)
        self.assertEqual((S2.size, S2.x, S2.y, S2.id), (1, 2, 3, 3))
        S3 = Square(1, 2, 3, 4)
        self.assertEqual((S3.size, S3.x, S3.y, S3.id), (1, 2, 3, 4))

    def test_value_error(self):
        """ Test for not allowed args """
        with self.assertRaises(TypeError):
            S = Square()
        with self.assertRaises(TypeError):
            S = Square("1", "1")
        with self.assertRaises(ValueError):
            S = Square(-1, -1)
        with self.assertRaises(TypeError):
            S = Square(1, 1, "1", "1")
        with self.assertRaises(ValueError):
            S = Square(1, 1, -1, -1)
        with self.assertRaises(TypeError):
            S = Square(1, 1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            S = Square(1.2, 1.2, 1.2)
        with self.assertRaises(TypeError):
            S = Square([1, 2], 3)
        with self.assertRaises(TypeError):
            S = Square(1, 1, {'one': 1}, 1)
        with self.assertRaises(TypeError):
            S = Square(True)
        with self.assertRaises(TypeError):
            S = Square((1, 2))
        with self.assertRaises(TypeError):
            S = Square(float('inf'))

    def test_area(self):
        """ Tests for area """
        S = Square(1)
        self.assertEqual(S.area(), 1)

        with self.assertRaises(TypeError):
            a = S.area(1)

    def test_display(self):
        """
        Redirect print statement to
        a file for testing.
        """
        f = io.StringIO()
        S = Square(1)
        with redirect_stdout(f):
            S.display()
        self.assertEqual(f.getvalue(), (('#' * 1 + '\n') * 1))

        f = io.StringIO()
        S = Square(1, 2, 3)
        with redirect_stdout(f):
            S.display()
        self.assertEqual(f.getvalue(), (('\n' * 3) +
                                        (' ' * 2 + '#' * 1 + '\n') * 1))

    def test_str(self):
        """ Test for string output """
        S = Square(1, 2, 3, 4)
        self.assertEqual("[Square] (4) 2/3 - 1", str(S))
