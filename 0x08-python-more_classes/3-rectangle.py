#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Class that defines a rectangle width and heigth """


class Rectangle():
    """
    Rectangle Class

    Attributes
    ----------
    width: width of the rectangle.
    height: height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Constructs the necessary attributes
        for a rectangle object.

        Parameters
        ----------
        width : int
            width of the rectangle.
        heigth: int
            height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of a rectangle.

        Returns
        -------
        area.

        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate the perimeter of a rectangle.

        Returns
        -------
        0: if width of height is zero.
        perimeter value other way.

        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Reimplementation of str() method
        to print a rectangle.

        Returns
        -------
        Rectangle drawed with hastags.
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string = "\n".join("#" * self.__width for j in
                               range(self.__height))
        return string
