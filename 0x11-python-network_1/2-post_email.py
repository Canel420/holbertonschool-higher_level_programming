#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response.
"""

from urllib import parse, request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        page = response.read().decode('utf-8')
        print(page)
        response.close()
