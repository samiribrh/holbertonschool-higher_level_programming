#!/usr/bin/python3
"""Module for Selecting states"""

if __name__ == '__main__':
    from sys import argv
    import mysql.connector

    db = mysql.connector.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()

    cursor.execute('SELECT * FROM states')

    for state in cursor.fetchall():
        print(state)
