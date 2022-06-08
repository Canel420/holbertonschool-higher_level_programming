#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Function load_from_json_file """

import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”
    """
    with open(filename, 'r') as f:
        return json.load(f)
