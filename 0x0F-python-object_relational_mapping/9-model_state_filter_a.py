#!/usr/bin/python3
"""a script that lists State containing a"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    for state in session.query(State)\
            .filter(State.name.contains('a')).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
