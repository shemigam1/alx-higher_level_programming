#!/usr/bin/python3

"""
 prints the State object with that matches arg from the
 database hbtn_0e_6_usa
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    code should not be executed when imported
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
