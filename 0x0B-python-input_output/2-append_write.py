#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Function append_write """


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and returns the number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
