#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Class Square """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Defines a square.
    """
    def __init__(self, size):
        """
        Initialize and validates square data.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Square area.
        """
        return (self.__size ** 2)
