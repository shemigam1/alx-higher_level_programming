#!/usr/bin/python3
"""
Script that lists the State objects with corresponding City objects
from the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """Creating the SQLAlchemy engine"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    """Creating a session """
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).outerjoin(City).order_by(State.id, City.id).all()
    for state in query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("     {}: {}".format(city.id, city.name))
