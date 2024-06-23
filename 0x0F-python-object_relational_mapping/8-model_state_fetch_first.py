#!/usr/bin/python3
"""
    Module creates script that prints
    the first State object from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

comm_args = sys.argv
if len(comm_args) != 4:
    exit(1)

connection_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
engine = create_engine(
    connection_string.format(
        comm_args[1],
        comm_args[2],
        comm_args[3]
    )
)

Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

session = Session()
states = session.query(State).order_by(State.id).first()

if states:
    print("{}: {}".format(states.id, states.name))
else:
    print("Nothing")

session.close()
