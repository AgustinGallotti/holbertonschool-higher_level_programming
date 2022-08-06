#!/usr/bin/python3
"""
    module
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2], db=argv[3])
    c = db.cursor()

    c.execute("SELECT cities.id, cities.name, states.name FROM cities"
              " JOIN states ON states.id=cities.state_id ORDER BY cities.id")
    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()
    db.close()
