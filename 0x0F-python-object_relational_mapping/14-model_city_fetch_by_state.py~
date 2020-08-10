#!/usr/bin/python3
""" script that adds the State object "Louisiana" to a database """


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

    new_s = State(name='Louisiana')
    r.add(new_s)
    r.commit()
    print(new_s.id)
