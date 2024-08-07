#!/usr/bin/python3
"""
post search api param
"""

import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    try:
        q = sys.argv[1]
    except IndexError:
        q = ''
    payload = {'q': q}
    r = requests.post(url, data=payload)
    try:
        res = r.json()
        if res == {}:
            print('No result')
        else:
            print('[{}] {}'.format(res.get('id'), res.get('name')))
    except ValueError:
        print('Not a valid JSON')
