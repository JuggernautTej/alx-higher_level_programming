#!/usr/bin/python3
"""This script that lists all State objects from the database hbtn_0e_6_usa"""


import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Test documentation"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
db = "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, db_name)
engine = create_engine(db, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
# Query to retrieve all State objects from database
for objects in session.query(State).order_by(State.id):
    print('{}: {}'.format(objects.id, objects.name))
