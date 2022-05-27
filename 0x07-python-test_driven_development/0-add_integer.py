#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
0-add_integer.py module

"""


def add_integer(a, b=98):
    """
    Sum of two integers

    Parameters
    ----------
    a: First integer.
    b: Second integer (98 by default).

    Returns
    --------
    sum

    Raises
    ------
    TypeError if parameters type are not integers or floats.


    """
    if type(a) is not int:
        if type(a) is float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
