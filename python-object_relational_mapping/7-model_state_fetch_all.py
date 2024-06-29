#!/usr/bin/python3
"""Module for fetching all states from the database using SQLAlchemy ORM."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

from model_state import State

# Run only executed
if __name__ == "__main__":

    # Engine creation with mysql and mysqldb DBAPI
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creating Session and its instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Printing the result
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
