#!/usr/bin/python3
"""SQLAlch"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]} 
            @localhost:3306/{sys.argv[3]}")

    Session = sessionmaker(bind=engine)

    session = Session()

    first = session.query(State).order_by(State.id).first()

    print(f"{first.id}: {first.name}")

    session.close()
