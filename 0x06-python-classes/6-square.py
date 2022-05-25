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
    def __init__(self, size=0, position=(0, 0)):
        """
        Instansiation of the square

        """
        self.__size = size
        self.__position = position

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
    def size(self, value):
        """
        Setter of size

        Parameters
        ----------
        value: int
               side size of square
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter for position

        Parameters
        ----------
        value: tuple
               position to draw square

        Returns
        -------
        position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position

        Parameters
        ----------
        value: tuple
               position to draw square

        Raises
        ------
        TypeError: position must be a tuple of 2 positive integers
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculate square area

        Returns
        -------
        area

        """
        return self.__size ** 2

    def my_print(self):
        """
        Draw a square pattern using hastags
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ")
                for j in range(self.size):
                    print("#", end='')
                print()
