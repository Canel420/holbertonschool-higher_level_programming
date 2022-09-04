#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that fetches https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        decode_body = body.decode("utf-8")
        print('Body response:\n\t- type: {}\n\t- content: {}\n\t- \
utf8 content: {}'.format(type(body), body, decode_body))
        response.close()
