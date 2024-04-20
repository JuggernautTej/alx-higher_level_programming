#!/usr/bin/python3
"""This script that prints the first State
object from the database hbtn_0e_6_usa"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Test documentation"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    table_count = session.query(func.count(State.id)).scalar()
    if table_count == 0:
        print("Nothing")
    else:
        first_object = session.query(State).order_by(State.id).first()
        print(f"{first_object.id}: {first_object.name}")

    session.close()
