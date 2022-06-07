#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" is_same_class function """


def is_same_class(obj, a_class):
    """ 
    Function that returns True if 
    the object is exactly an instance 
    of the specified class """
    return (isinstance(obj, a_class))
