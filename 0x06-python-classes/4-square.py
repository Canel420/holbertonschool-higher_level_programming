#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Class that defines a square of a given size """


class Square:
    """
    Class square

    Parameters
    ----------
    size: int
          the side size of the square
    """
    def __init__(self, size=0):
        """
        Instansiation of the square

        """
        self.__size = size

    @property
    def size(self):
        """
        Getter of size parameter

        Returns
        -------
           Side size of square
        """
        return self.__size

    @size.setter
    def size(self, val):
        """
        Setter of size

        Parameters
        ----------
        value: int
               side size of square
        """

        if type(val) is not int:
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    def area(self):
        """
        Calculate square area

        Returns
        -------
        area

        """
        return self.__size ** 2
