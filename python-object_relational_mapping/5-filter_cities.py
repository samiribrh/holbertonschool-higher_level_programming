#!/usr/bin/python3
"""Module for Selecting cities"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()

    cursor.execute('SELECT c.name, s.name \
                    FROM cities AS c \
                    INNER JOIN states AS s ON s.id = c.state_id ')

    for state in cursor.fetchall():
        if state[1] == argv[4]:
            print(state[0])

    if cursor:
        cursor.close()
    if db:
        db.close()
