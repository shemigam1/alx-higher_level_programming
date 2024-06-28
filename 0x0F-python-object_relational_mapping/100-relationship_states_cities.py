#!/usr/bin/python3

"""
 add the State object 'Louisiana' to the
 database hbtn_0e_6_usa
"""
from relationship_state import Base, State
from relationship_city import City
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cali = State(name="California")
    san_fran = City(name="San Francisco")
    cali.cities.append(san_fran)
    session.add(cali)
    session.commit()

    session.close()
