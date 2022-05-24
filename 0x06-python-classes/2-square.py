#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Class that defines a square of a given size """


class Square:
    """
    Class square

    Attributes
    ----------
    size: int
        the side size of the square
    """
    def __init__(self, size=0):
        """
        Parameters
        ----------
        size: int
           the side size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
