#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                             passwd=mysql_password, db=db_name, charset="utf8")
    except MySQLdb.Error as err:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
        .format(state_name))
    rows = cur.fetchall()

    for line in rows:
        print(line)

    cur.close()
    db.close()
