#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" add_attribute function """


def add_attribute(obj, name, value):
    """
    Defines if an attribute exist for a given
    object and set it

    Parameters
    ----------
    obj: Object for checking.
    name: name of attribute.
    value: value of attribute.

    Raise
    -----
    TypeError: if attribute doesn't exist
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
