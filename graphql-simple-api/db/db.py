from sqlmodel import create_engine, SQLModel

from .models import *

database_url = "postgresql+psycopg2://user:password@localhost:5432/graphql_sample_db"
engine = create_engine(database_url, echo=True)
SQLModel.metadata.create_all(engine)


def initialize_db():
    SQLModel.metadata.create_all(engine)
