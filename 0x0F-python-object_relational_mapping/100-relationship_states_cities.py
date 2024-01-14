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

    Session = sessionmaker(bind=engine)

    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))

    session.commit()

    session.close()
