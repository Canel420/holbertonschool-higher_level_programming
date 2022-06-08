#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Function to_json_string """

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of 
    an object.
    """
    return json.dumps(my_obj)
