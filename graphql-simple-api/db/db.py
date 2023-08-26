from sqlmodel import Session, col, create_engine, SQLModel, select, or_

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


def select_heros():
    with Session(engine) as session:
        heros = session.exec(
            select(Hero)
            .where(col(Hero.age) >= 35)
            .limit(1)
            # .where(Hero.secret_name == "Dive Wilson")
        ).all()
        print(heros)


def update_heros():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        results = session.exec(statement)
        hero = results.one()
        print("Hero:", hero)

        hero.age = 17
        session.add(hero)
        session.commit()
        session.refresh(hero)
        print("Updated hero:", hero)


def delete_heros():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        results = session.exec(statement)
        hero = results.one()
        print("Hero:", hero)

        session.delete(hero)
        session.commit()

        print("Deleted hero:", hero)

        statement = select(Hero).where(Hero.name == "Spider-Boy")
        results = session.exec(statement)
        hero = results.first()

        if hero is None:
            print("There's no hero named Spider-Boy")
