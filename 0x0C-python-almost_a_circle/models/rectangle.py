#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Class Rectangle  """

from models.base import Base


class Rectangle(Base):
    """ Class for rectangle definition """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle initialization """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Rectangle area"""
        return self.__height * self.__width

    def display(self):
        """
        Display rectangle in # pattern
        given an (x, y) position.
        """
        pattern = (("\n" * self.__y) +
                   "\n".join(((" " * self.__x) + ("#" * self.__width))
                             for j in range(self.__height)))
        print(pattern)

    def __str__(self):
        """ Rectangle string representation """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}" +
                f" - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute

        Parameters
        ----------
        args: list
            parameters to update Rectangle class
        kwargs: dict
            parameters to update Rectangle class
        """
        if len(args) != 0:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                elif num == 1:
                    self.width = arg
                elif num == 2:
                    self.height = arg
                elif num == 3:
                    self.x = arg
                elif num == 4:
                    self.y = arg
        elif len(kwargs) != 0:
            for (key, val) in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """ Dictionary representation of Rectangle """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
