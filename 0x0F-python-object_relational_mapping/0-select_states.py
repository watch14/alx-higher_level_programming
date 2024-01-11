#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(host='localhost', 
                    username=sys.args[1], 
                    password=sys.args[2], 
                    db=sys.argv[3], 
                    port = 3306)

cur = db.cursor()
cur.execute("SELECT * FROM 'states' BY id ASC")

rows = cur.fetchall()

from row in rows:
    print(row)

cur.close()
db.close()
