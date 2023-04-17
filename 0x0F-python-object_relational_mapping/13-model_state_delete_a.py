#!/usr/bin/python3
"""Delete state object"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).filter(State.name.ilike('%a%')).all()
    if all_states:
        for state in all_states:
            session.delete(state)

        session.commit()

    session.close()
