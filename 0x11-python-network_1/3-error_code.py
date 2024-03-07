#!/usr/bin/python3
"""
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e.code)
