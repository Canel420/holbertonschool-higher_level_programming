#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Rectangle class inherited from BaseGeometry """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle constructor
    """
    def __init__(self, width, height):
        """
        Rectangle measure initialization
        and validation.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Rectangle Area.
        """
        return(self.__height * self.__width)

    def __str__(self):
        """
        String rectangle representation
        """
        return (f"[Rectangle] {self.__init__}/{self.__height}")
