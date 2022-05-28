#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
5-text.py module

"""


def text_indentation(text):
    """
    Print a given text adding two new lines each
    time it encounters one of the following special symbols
    ['.', ':', '?'].

    Parameters
    ----------
    text: text to transform.

    Raises
    ------
    TypeError: if text is not string type.

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    str = text.replace('.', '.\n\n').replace(':', ':\n\n')\
        .replace('?', '?\n\n')
    for i in range(len(text)):
        str = str.replace('\n ', '\n')

    print(str, end='')
