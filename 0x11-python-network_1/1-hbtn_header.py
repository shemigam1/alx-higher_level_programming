#!/usr/bin/python3
"""
displays value of X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        req_id = headers.get('X-Request-Id')
    print(req_id)
