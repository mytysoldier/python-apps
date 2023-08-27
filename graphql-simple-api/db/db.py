from sqlmodel import Session, col, create_engine, SQLModel, select, or_

from .models import *

database_url = "postgresql+psycopg2://user:password@localhost:5432/graphql_sample_db"
engine = create_engine(database_url, echo=True)
SQLModel.metadata.create_all(engine)


def initialize_db():
    SQLModel.metadata.create_all(engine)


def create_heros():
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret’s Bar")
        session.add(team_preventers)
        session.add(team_z_force)
        session.commit()

        hero_deadpond = Hero(
            name="Deadpond", secret_name="Dive Wilson", team_id=team_z_force.id
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            team_id=team_preventers.id,
        )
        hero_spider_boy = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()


def update_heros():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        hero_spider_boy = session.exec(statement).one()
        hero_spider_boy.team_id = 1
        session.add(hero_spider_boy)
        session.commit()
        session.refresh(hero_spider_boy)
        print("Updated hero:", hero_spider_boy)


def remove_team_connection():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        hero_spider_boy = session.exec(statement).one()
        hero_spider_boy.team_id = None
        session.add(hero_spider_boy)
        session.commit()
        session.refresh(hero_spider_boy)
        print("No longer Preventer:", hero_spider_boy)


def select_heros():
    with Session(engine) as session:
        statement = select(Hero, Team).where(Hero.team_id == Team.id)
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero, "Team:", team)


def select_join_heros():
    with Session(engine) as session:
        statement = select(Hero, Team).join(Team, isouter=True)
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero, "Team:", team)


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
