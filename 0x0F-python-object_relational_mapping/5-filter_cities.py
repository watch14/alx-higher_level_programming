#!/usr/bin/python3
""" sql """
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

    query = """SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s ORDER BY cities.id ASC"""

    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()

    print(", ".join([city[0] for city in rows]))

    cur.close()
    db.close()
