#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
3-say_my_name.py module

"""


def say_my_name(first_name, last_name=""):
    """
    Prints complete name

    Parameters
    ----------
    first_name: Some first name
    last_name: Some last name

    Returns
    -------
    My name is <first name> <last name>

    Raises
    ------
    TypeError: if names are not string types

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
