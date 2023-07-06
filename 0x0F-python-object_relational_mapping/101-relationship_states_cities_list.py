#!/usr/bin/python3
"""Start link class to table in database
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
      sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    stc = session.query(State, City).select_from(State).order_by(
       State.id, City.id).join(State.cities).all()
    printed_states = set()
    for state, city in stc:
        if state not in printed_states:  # Print the state if it hasn't been printed yet
            print("{}: {}".format(state.id, state.name))
            printed_states.add(state)
        print("    {}: {}".format(city.id, city.name))
