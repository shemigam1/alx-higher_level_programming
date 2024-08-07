#!/usr/bin/python3
"""
post search api param
"""

import requests
import sys

if __name__ == '__main__':
    name = sys.argv[1]
    pwd = "Bearer {}".format(sys.argv[2])
    url = 'https://api.github.com/user'
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": pwd, "X-GitHub-Api-Version": "2022-11-28"}
    r = requests.get(url, headers=headers)
    res = r.json()
    # print(res)
    print('{}'.format(res.get('id')))
