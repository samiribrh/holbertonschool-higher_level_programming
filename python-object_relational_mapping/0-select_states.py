#!/usr/bin/python3
"""Module for Selecting states"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states')
    print(cursor.fetchall())
