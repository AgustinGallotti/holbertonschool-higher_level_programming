#!/usr/bin/python3
"""
    module
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT id, name FROM states "
              "WHERE name='" + argv[4] + "' ORDER BY id")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
