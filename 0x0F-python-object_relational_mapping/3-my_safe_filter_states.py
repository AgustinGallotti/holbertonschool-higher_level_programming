#!/usr/bin/python3
"""
    module
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT id, name FROM states WHERE name=%s "
              "ORDER BY id", (argv[4],))
    for row in c.fetchall():
        print("({}, '{}'".format(row[0], row[1]))
    c.close()
    db.close()

