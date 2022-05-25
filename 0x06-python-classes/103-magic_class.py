#!/usr/bin/python3
import math
""" Defines MagicClass """


class MagicClass:
    """
    Measures a given circle attributes

    """
    def __init__(self, radius=0):
        """
        Instantiation of class MagicClass

        Parameter
        ---------
        radius: int
                radius of a given circle

        Raises
        ------
        TypeError: if radius is not and int type

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Measures circle area
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Measures circle circumference
        """
        return 2 * math.pi * self.__radius
