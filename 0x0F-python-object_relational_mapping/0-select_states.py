#!/usr/bin/python3

"""
this script takes 3 args from the cmd line
mysql username
mysql password
db name
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    access db to get states table
    """
    db = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
