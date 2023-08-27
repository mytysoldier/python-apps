import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

from db.db import (
    create_heros,
    delete_heros,
    initialize_db,
    remove_team_connection,
    select_heros,
    select_join_heros,
    update_heros,
)

from schema.schema import schema


@strawberry.type
class Hero:
    id: int
    name: str
    secret_name: str
    age: int
    team_id: int


initialize_db()

# schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()

app.add_route("/graphql", graphql_app)


@app.get("/heros")
def heros():
    create_heros()
    return "sample data created"


@app.get("/select_heros")
def select():
    select_heros()
    return ""


@app.get("/select_join_heros")
def select_join():
    select_join_heros()
    return ""


@app.get("/update_heros")
def update():
    update_heros()
    return ""


@app.get("/remove_team_connection")
def remove_connection():
    remove_team_connection()
    return ""


@app.get("/delete_heros")
def delete():
    delete_heros()
    return ""
