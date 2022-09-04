#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    pwd = argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(username, pwd))
    print(response)
    try:
        json_body = response.json()
        print(json_body.get('id'))
    except ValueError:
        print(None)
