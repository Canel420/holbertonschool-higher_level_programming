#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for rectangle.py module
"""
import unittest
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

    def test_area(self):
        """ Tests for area """
        R = Rectangle(1, 2)
        self.assertEqual(R.area(), 2)

        with self.assertRaises(TypeError):
            a = R.area(12)

    def test_str(self):
        """ Test for string output """
        R = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(R))
