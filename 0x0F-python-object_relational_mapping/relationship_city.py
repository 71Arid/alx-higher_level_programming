#!/usr/bin/python3
""" relationship update """

from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer
from relationship_state import Base


class City(Base):
    """module representation of table city"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
