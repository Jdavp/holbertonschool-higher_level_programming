#!/usr/bin/python3
'prints the State object with the name passed as argument'
from sys import argv
import sys
from sqlalchemy.orm import relationship
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    s = Session()
    db = s.query(State).order_by(State.id)

    for data in db:
        print('{}: {}'.format(data.id, data.name))
        for datacity in data.cities:
            print('    {}: {}'.format(datacity.id, datacity.name))
    s.close()
