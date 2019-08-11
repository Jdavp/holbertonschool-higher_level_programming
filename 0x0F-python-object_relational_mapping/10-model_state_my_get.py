#!/usr/bin/python3
'prints the State object with the name passed as argument'
from sys import argv
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    search = states.filter(State.name == sys.argv[4]).first()
    if search:
        print(search.id)
    else:
        print("Not found")
    session.close()
