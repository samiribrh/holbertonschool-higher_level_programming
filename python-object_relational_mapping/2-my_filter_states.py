#!/usr/bin/python3
"""Module for Selecting states where name equals argument"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    name = argv[4]

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id".format(name))

    for state in cursor.fetchall():
        print(state)

    if cursor:
        cursor.close()
    if db:
        db.close()
