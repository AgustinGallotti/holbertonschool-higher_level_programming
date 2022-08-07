#!/usr/bin/python3
"""
    module
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT cities.name FROM cities"
              " JOIN states ON states.id=cities.state_id "
			  "WHERE states.name=%s "
			  "ORDER BY cities.id", (argv[4],))
    rows = c.fetchall()
    print(", ".join([row[0] for row in rows]))
    c.close()
    db.close()
