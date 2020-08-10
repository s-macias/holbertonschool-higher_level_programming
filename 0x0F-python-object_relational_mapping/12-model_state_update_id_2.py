#!/usr/bin/python3
""" script that changes the name of a State object """


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
    r = Session()
    r.query(State).filter(State.id == 2).update({State.name: 'New Mexico'})
    r.commit()
