#!/usr/bin/python3
""" script that lists all State object with the name passed as argument """


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == '__main__':
    h = 'localhost'
    u = sys.argv[1]
    pas = sys.argv[2]
    db_n = sys.argv[3]
    p = 3306
    st_n = sys.argv[4]
    eng = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
          u, pas, h, p, db_n))

    Session = sessionmaker(bind=eng)
    r = Session().query(State).order_by(State.id).filter(
        State.name.like(st_n))
    for state in r:
        if state.id:
            print("{}".format(state.id))
    else:
        print("Not found")
