#!/usr/bin/python3
"""
Module creates a script that adds the State object
"Louisiana" to the database hbtn_0e_6_usa
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
    louisiana_state = State(name="Louisiana")
    session.add(louisiana_state)
    session.commit()
    print(louisiana_state.id)

    session.close()
