#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
4-print_square module

"""


def print_square(size):
    """
    Print a square pattern of a given size.

    Parameters
    ----------
    size: side size of the square.

    Raises
    ------
    TypeError: if size is not integer.
    ValueError: if size is less than zero.

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size <= 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for i in range(size):
            print('#', end='')
        print()
