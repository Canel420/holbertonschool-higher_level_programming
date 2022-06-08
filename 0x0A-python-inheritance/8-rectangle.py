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
