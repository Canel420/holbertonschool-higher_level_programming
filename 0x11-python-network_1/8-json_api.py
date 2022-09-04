#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ''}
    response = requests.post(url, data)
    try:
        json_body = response.json()
        if len(json_body) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(json_body['id'], json_body['name']))
    except:
        print('Not a valid JSON')
