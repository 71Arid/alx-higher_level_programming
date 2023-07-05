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
    L_state = State(name="Louisiana")
    session.add(L_state)
    session.commit()
    states = session.query(State).filter(State.name == "Louisiana").first()
    if states is not None:
        print(states.id)
    session.close()
