#!/usr/bin/python3
"""
Module prints all City objects from database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    comm_args = sys.argv
    if len(comm_args) != 4:
        exit(1)

    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        comm_args[1],
        comm_args[2],
        comm_args[3]
    )
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state_name, city_id, city_name in session.query(
            State.name, City.id, City.name
    ).join(City, State.id == City.state_id):
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()
