#!/usr/bin/python3
"""
response header value
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    code = r.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(r.text)
