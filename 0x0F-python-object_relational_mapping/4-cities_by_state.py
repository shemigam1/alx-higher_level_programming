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

    with db.cursor() as db_cursor:
        db_cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
        rows = db_cursor.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
