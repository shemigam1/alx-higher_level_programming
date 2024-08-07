#!/usr/bin/python3
"""
post search api param
"""

import requests
import sys
import json

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    try:
        q = sys.argv[1]
    except:
        q = ''
    payload = {'q': q}
    r = requests.post(url, params=payload)
    try:
        res = r.json()
        if res == {}:
            print('No result')
        else:
            print('[{}] {}'.format(res.get('id'), res.get('name')))
    except ValueError:
        print('Not a valid JSON')
