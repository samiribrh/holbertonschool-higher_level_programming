#!/usr/bin/python3
"""
Module for fetching all states from the database using SQLAlchemy ORM.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Run only executed
if __name__ == "__main__":
    # Defining argv inputs
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Creating the engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pwd, db_name))

    # Creating the classes
    Base.metadata.create_all(engine)

    # Opening the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Printing the result
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
