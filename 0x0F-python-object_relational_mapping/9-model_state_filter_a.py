#!/usr/bin/python3
"""
    module
    func is a specialobj instance wich generate SQL functions based on name,
    attr., any name can be give to func.

"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy import func
from sys import argv


if __name__ == '__main__':
    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                       argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(db)
    Session = sessionmaker(bind=db)
    sn = Session()
    """row = sn.query(State).filter(State.name.contains(func.found("a")))
    if row:
        print("{}: {}".format(row.id, row.name))"""
    for row in sn.query(State).filter(State.name.contains("a")):
        print("{}: {}".format(row.id, row.name))
