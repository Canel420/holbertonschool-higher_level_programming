#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Class Student """


class Student:
    """
    Describes a student basic characteristics.
    """
    def __init__(self, first_name, last_name, age):
        """ Initialize class student with public instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return all attributes dictionary
        if no specific attribute list is given.
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """
        Set instance attributes given
        in json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
