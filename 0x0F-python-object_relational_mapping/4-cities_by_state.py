#!/usr/bin/python3
"""Script to list cities from a MySQL database"""
import sys
import MySQLdb


if __name__ == "__main__":
    """Main execution block"""
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    cur = db.cursor()

    sql = """SELECT c.id, c.name, s.name FROM states s, cities c
          WHERE c.state_id = s.id ORDER BY c.id ASC"""

    cur.execute(sql)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()

    db.close()
