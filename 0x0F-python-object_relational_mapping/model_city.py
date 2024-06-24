#!/usr/bin/python3
"""
Module contains a script that contains
definition of class
"""

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

MyMeta = MetaData()
Base = declarative_base(metadata=MyMeta)


class City(Base):
    """
        city definition and attribues
    """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        unique=True,
        nullable=False,
        primary_key=True,
        autoincrement=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('state.id'),
        nullable=False
    )
