#!/usr/bin/python3
# -*- coding: utf-8 -*-

class LockedClass:
    """
    Locked class that only lets create
    an instance if attribute is first_name.
    """
    __slots__ = ['first_name']
