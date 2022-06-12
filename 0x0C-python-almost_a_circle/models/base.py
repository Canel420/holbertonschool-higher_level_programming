#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Base class  """


class Base:
    """
    This base class of all
    other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__class__.__nb_objects
