#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
      sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    sstr = 'a'
    states = session.query(State).order_by(State.id).filter(
      State.name.contains(sstr)).all()
    for state in states:
        print("{0}: {1}".format(state.id, state.name))
