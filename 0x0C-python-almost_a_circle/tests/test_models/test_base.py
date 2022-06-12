#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for base.py module
"""

import unittest
from models import base
Base = base.Base


class baseTest(unittest.TestCase):
    """ Tests for Base class """
    def test1(self):
        """ Test for no args passed"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test2(self):
        """ Test for 1 arg passed """
        b = Base(12)
        self.assertEqual(b.id, 12)
