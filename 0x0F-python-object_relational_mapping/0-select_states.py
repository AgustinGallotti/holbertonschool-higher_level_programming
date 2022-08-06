#!/usr/bin/python3
"""
    module
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    c.execute("SELECT * FROM states")
    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()
    db.close()
