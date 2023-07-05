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
    stname = sys.argv[4]
    states = session.query(State).filter(State.name == stname).all()
    if (states):
        for state in states:
            print(state.id)
    else:
        print('Not found')
