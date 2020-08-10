#!/usr/bin/python3
""" script that lists all cities in a state passed as an argument """
import MySQLdb
import sys


if __name__ == "__main__":
    h = "localhost"
    us = sys.argv[1]
    pas = sys.argv[2]
    dbn = sys.argv[3]
    state_n = sys.argv[4]
    db = MySQLdb.connect(host=h, user=us, passwd=pas, db=dbn, port=3306)
    cur = db.cursor()

    cur.execute(
        "SELECT cities.name FROM cities\
        JOIN states ON states.id = cities.state_id WHERE states.name = %s\
        ORDER BY cities.id", (state_n, ))
    rows = cur.fetchall()
    if rows:
        length = len(rows)
        for i in range(length):
            if i == length - 1:
                print(rows[i][0])
            else:
                print(rows[i][0], end=", ")
    else:
        print()
    cur.close()
    db.close()
