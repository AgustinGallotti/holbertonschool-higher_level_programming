#!/usr/bin/python3
"""
    module
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = '%s'" % (argv[4]))
    rows = c.fetchall()
    for row in rows:
        print (row)
    c.close()
    db.close()
