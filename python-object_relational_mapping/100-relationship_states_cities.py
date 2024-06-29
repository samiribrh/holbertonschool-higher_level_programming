#!/usr/bin/python3
"""Module for creating State California and City San Francisco"""

from relationship_city import City, Base
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

# Run only when executed
if __name__ == "__main__":
    # Creating the engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Binding the database
    Base.metadata.create_all(engine)

    # Creating the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Adding new city and state
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_state)
    session.add(new_city)

    # Commiting changes
    session.commit()

    # Closing the session
    if session:
        session.close()