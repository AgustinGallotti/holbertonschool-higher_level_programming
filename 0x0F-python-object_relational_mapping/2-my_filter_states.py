#!/usr/bin/python3
"""
    module
"WHERE name LIKE BINARY 'N%' """


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3])

    c = db.cursor()
    c.exectue("SELECT * FROM states WHERE name LIKE BINARY {} ORDER\
              \BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))
    c.close()
    db.close()
