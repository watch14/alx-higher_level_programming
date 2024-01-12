#!/usr/bin/python3
""" start with N """
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

