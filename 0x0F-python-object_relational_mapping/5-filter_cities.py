#!/usr/bin/python3
"""a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name \
    FROM cities INNER JOIN states ON cities.state_id = states.id\
    WHERE states.name LIKE BINARY %s ORDER BY cities.id ASC",
                {state_name})
    rows = cur.fetchall()
    city_names = ', '.join(row[0] for row in rows)
    print(city_names)

    cur.close()
    db.close()
