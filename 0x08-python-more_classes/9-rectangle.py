#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Class that defines a rectangle width and heigth """


class Rectangle:
    """
    Rectangle Class
    """

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """
        Defines a square
        """
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Determines the biggest rectangle
        based on area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

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
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        Desctructor for class instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
        Rectangle drawed with symbols.
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string = "\n".join(str(self.print_symbol) * self.__width
                               for j in range(self.__height))
        return string

    def __repr__(self):
        """
        Official representation of the rectangle.

        Returns
        -------
        Rectangle official representation, name + measures.

        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))