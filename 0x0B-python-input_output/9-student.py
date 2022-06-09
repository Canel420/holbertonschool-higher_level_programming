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

    def to_json(self):
        """ Return instances method dictionary"""
        return self.__dict__
