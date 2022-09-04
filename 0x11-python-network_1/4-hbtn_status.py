#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    page = requests.get(url)
    print('Body response:\n\t- type: {}\n\t- \
content: {}'.format(type(page.text), page.text))
