#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that adds all arguments from command line
to a Python list, and then save them to a file.
"""

import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    lst = load_from_json_file('add_item.json')
except ValueError:
    lst = []

for i in range(1, len(sys.argv)):
    lst.append(sys.argv[i])

save_to_json_file(lst, 'add_item.json')