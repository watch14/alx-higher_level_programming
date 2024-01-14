#!/usr/bin/python3
""" x """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    engine = create_engine(
            f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]} \
                    @localhost:3306/{sys.argv[3]}")

    Base.metadata.create_all(engine)

    session = Session(engine)

    content = session.query(State).order_by(State.id).all()

    for state in content:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
