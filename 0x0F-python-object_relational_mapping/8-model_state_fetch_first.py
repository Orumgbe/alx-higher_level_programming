#!/usr/bin/python3
"""Gets first state object stored in hbtn_0e_6_usa"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()
    if (first_state):
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
