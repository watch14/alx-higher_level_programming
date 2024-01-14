#!/usr/bin/python3
"""SQLAlch"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]} \
                    @localhost:3306/{sys.argv[3]}")

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in to_delete:
        session.delete(state)

    session.commit()

    session.close()
