from sqlmodel import Session, create_engine, SQLModel

from .models import *

database_url = "postgresql+psycopg2://user:password@localhost:5432/graphql_sample_db"
engine = create_engine(database_url, echo=True)
SQLModel.metadata.create_all(engine)


def initialize_db():
    SQLModel.metadata.create_all(engine)


def create_heros():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit()

    # session = Session(engine)
    # session.add(hero_1)
    # session.add(hero_2)
    # session.add(hero_3)

    # session.commit()

    # session.close()
