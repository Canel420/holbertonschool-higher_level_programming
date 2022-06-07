#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Class MyList """


class MyList(list):
    def __init__(self):
        """ Initialize with base class method """
        super().__init__

    def print_sorted(self):
        """ Print a list in ascending order """
        print(sorted(self))
