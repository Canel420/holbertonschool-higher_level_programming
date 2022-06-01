#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Class that defines a rectangle width and heigth """


class Rectangle:
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
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """ Getter for the private attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Settter for the private attribute height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ Getter for the private attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the private attribute width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
