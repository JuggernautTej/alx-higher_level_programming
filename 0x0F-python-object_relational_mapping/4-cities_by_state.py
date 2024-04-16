#!/usr/bin/python3
"""A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                             passwd=mysql_password, db=db_name, charset="utf8")
    except MySQLdb.Error as err:
        print("Error connecting to database: {}".format(err))
        sys.exit(1)

    cur = db.cursor()
    try:
        cur.execute(
            "SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.id = states.id\
            ORDER BY cities.id ASC")
        rows = cur.fetchall()
        if rows is not None:
            for line in rows:
                print(line)
    except MySQLdb.Error as err:
        print("Error executing query: {}".format(err))
        sys.exit(1)
    finally:
        cur.close()
        db.close()
