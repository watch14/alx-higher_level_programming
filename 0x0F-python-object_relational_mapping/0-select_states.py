#!/usr/bin/python3
""" import form table """
import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(
            host='localhost',
            username=sys.args[1],
            password=sys.args[2],
            db=sys.argv[3],
            port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM 'states' BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
