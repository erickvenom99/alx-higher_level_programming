#!/usr/bin/python3
"""
contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    MetaData
)
from sqlalchemy.ext.declarative import declarative_base

MyMeta = MetaData()
Base = declarative_base(metadata=MyMeta)


class State(Base):
    """definition of a State and an instance"""
    __tablename__ = 'states'
    id = Column(
        Integer,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(128), nullable=False)
