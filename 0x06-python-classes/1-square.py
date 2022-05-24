#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Square:
    """
    Class that defines a square of a given size

    Attributes
    ----------
    size: int
        the side size of the square
    """
    def __init__(self, size):
        """
        Parameters
        ----------
        size: int
           the side size of the square
        """
        self.__size = size
