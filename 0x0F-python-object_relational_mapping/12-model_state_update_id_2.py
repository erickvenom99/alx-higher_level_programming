#!/usr/bin/python3
"""
script that changes the name of a State object
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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

    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
