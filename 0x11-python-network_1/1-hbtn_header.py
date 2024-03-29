#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id variable.
"""

from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        header = response.getheader("X-Request-Id")
        print(header)
        response.close()
