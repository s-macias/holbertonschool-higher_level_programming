#!/usr/bin/python3
""" script that lists all states with a name starting with N """
import MySQLdb
import sys


if __name__ == "__main__":
    h = "localhost"
    us = sys.argv[1]
    pas = sys.argv[2]
    dbn = sys.argv[3]
    db = MySQLdb.connect(host=h, user=us, passwd=pas, db=dbn, port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    print(cur)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
