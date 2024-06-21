#!/usr/bin/python3


"""
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    dont execute on import
    """
    db = MySQLdb.connect(
            host="localhost", user=argv[1],
            passwd=argv[2], db=argv[3], port=3306)
    with db.cursor() as db_cursor:
        db_cursor.execute("""
        SELECT cities.id, cities.name
        FROM states JOIN cities
        ON states.id = cities.state_id
        WHERE states.name LIKE BINARY %(states_name)s
        ORDER BY cities.id ASC""", {'states_name': argv[4]})
        rows = db_cursor.fetchall()
    if rows is not None:
        print(", ".join([row[1] for row in rows]))
