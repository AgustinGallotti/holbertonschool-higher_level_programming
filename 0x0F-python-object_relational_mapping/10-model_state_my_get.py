#!/usr/bin/python3
"""
    module
"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sys import argv


if __name__ == '__main__':
    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                       argv[2], argv[3]), pool_pre_ping=True)
    arg = argv[4]
    Base.metadata.create_all(db)
    Session = sessionmaker(bind=db)
    sn = Session()
    rows = sn.query(State).filter(State.name == arg)
    if len(rows.all()) == 0:
        print("Not found")
    else:
        for row in rows:
            print("{}".format(row.id))
