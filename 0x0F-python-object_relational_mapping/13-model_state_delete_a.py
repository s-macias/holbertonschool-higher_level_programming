#!/usr/bin/python3
""" script that deletes all State objects whose name contains the letter a """


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
    eng = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
          u, pas, h, p, db_n))

    Session = sessionmaker(bind=eng)
    session = Session()
    state_del = session.query(State).order_by(State.id).filter(
                State.name.like('%a%'))

    for i in state_del:
        session.delete(i)
    session.commit()
