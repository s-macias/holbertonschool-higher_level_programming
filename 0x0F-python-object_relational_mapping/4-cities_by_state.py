#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    h = "localhost"
    us = sys.argv[1]
    pas = sys.argv[2]
    dbn = sys.argv[3]
    db = MySQLdb.connect(host=h, user=us, passwd=pas, db=dbn, port=3306)
    cur = db.cursor()

    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON\
        cities.state_id = states.id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
