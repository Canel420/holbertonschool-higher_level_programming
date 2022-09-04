#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that takes in a URL, sends a request
to the URL and displays the body of the response
(decoded in utf-8).
"""

from urllib.error import HTTPError
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code: {}'.format(error.status))
