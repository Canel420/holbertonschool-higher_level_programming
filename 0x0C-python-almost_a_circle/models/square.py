#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Class Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square representation """
    def __init__(self, size, x=0, y=0, id=None):
        """ Square initialization """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Set size """
        self.width = value
        self.height = value

    def __str__(self):
        """
        String representation of square.

        Return
        ------
        [Class name] (<id>) <x>/<y> - <size>
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """
        Assigns attributes

        Parameters
        ----------
        args: list
            undefined number of attributes.
        kwargs: dict
            undefined number of attributes.
        """
        if len(args) != 0 and args is not None:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                elif num == 1:
                    self.size = arg
                elif num == 2:
                    self.x = arg
                elif num == 3:
                    self.y = arg
        elif len(kwargs) != 0:
            for (key, val) in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """ Dictionary representation of square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
