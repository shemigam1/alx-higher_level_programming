#!/usr/bin/python3

"""
script takes 3 args
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    list asll states that start with 'N'
    """
    db = MySQLdb.connect(
            host="localhost", user=argv[1],
            passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                    ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
