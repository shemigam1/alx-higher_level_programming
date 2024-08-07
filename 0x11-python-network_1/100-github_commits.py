#!/usr/bin/python3
"""
post search api param
"""

import requests
import sys

if __name__ == '__main__':
    name = sys.argv[1]
    repo = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(name, repo)
    r = requests.get(url)
    res = r.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                res[i].get("sha"),
                res[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
