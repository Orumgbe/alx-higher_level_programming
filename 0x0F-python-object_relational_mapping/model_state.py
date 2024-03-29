#!/usr/bin/python3
"""Contains states class definition that inherits from declarative_base()"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """Defines states table with columns 'id' and 'name'"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
