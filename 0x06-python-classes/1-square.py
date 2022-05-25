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
    def __init__(self, size):
        """
        Parameters
        ----------
        size: int
           the side size of the square
        """
        self.__size = size
