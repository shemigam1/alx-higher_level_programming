#!/usr/bin/python3

"""
this script takes 3 args from cmd line
argv[1] - mysql username
argv[2] - mysql password
argv[3] - database name
argv[4] - state name
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    connect to db
    """
    db = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' \
                    ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
