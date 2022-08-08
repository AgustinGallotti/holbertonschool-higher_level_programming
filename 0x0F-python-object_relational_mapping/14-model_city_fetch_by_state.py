#!/usr/bin/python3
"""
    module
"""


if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        argv[1], argv[2], argv[3], pool_pre_ping=True))
    Base.metadata.create_all(db)
    Session = sessionmaker(bind=db)
    sn = Session()
    for i, j in sn.query(City, State).filter(City.state_id == State.id):
        print("{}: ({}) {}".format(j.name, i.id, i.name))
