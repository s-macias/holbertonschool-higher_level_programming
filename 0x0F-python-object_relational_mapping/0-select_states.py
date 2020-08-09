#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    us = sys.argv[1]
    pas = sys.argv[2]
    dbn = sys.argv[3]
    h = "localhost"
    db = MySQLdb.connect(host=h, user=us, passwd=pas, db=dbn, port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    print(cur)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()