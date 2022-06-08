#!/usr/bin/python3
# -*- coding: utf-8 -*-

from html.entities import name2codepoint


class BaseGeometry:
    """
    Class with public instance method.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
