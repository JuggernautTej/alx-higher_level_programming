#!/usr/bin/python3
"""This script that prints the State object with
the name passed as argument from the database
hbtn_0e_6_usa"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Test documentation"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    with_a = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for entry in with_a:
        print(f"{entry.id}: {entry.name}")

    session.close()
