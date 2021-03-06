#!/usr/bin/python3
""" script that lists all states where name matches the argument """
import MySQLdb
import sys


if __name__ == "__main__":
    h = "localhost"
    us = sys.argv[1]
    pas = sys.argv[2]
    dbn = sys.argv[3]
    search = sys.argv[4]
    db = MySQLdb.connect(host=h, user=us, passwd=pas, db=dbn, port=3306)
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id".
        format(search))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
