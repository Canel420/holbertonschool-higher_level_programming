#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Class MyInt """


class MyInt(int):
    """
    Inverts equal and not equal methods
    """
    def __eq__(self, other):
        """
        Equal is not equal.
        """
        return int(self) != other

    def __ne__(self, other):
        """
        Not equal is equal
        """
        return int(self) == other
