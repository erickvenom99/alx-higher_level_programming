#!/usr/bin/python3
"""
Module creates a script that deletes all State objects
with a name containing the letter 'a' from
the database hbtn_0e_6_usa
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

    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()
