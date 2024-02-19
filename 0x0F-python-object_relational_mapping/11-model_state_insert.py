#!/usr/bin/python3

"""
 add the State object 'Louisiana' to the
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

    louis = State(name="Louisiana")
    session.add(louis)
    session.commit()
    print("{}".format(louis.id))

    session.close()
